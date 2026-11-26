"""Read news feeds and apply a reviewed editorial bundle; never sends notifications."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from http.client import HTTPException
import argparse
import json
from pathlib import Path
import re
from urllib.parse import parse_qsl, urlsplit, urlunsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
import ledger

ROOT = Path(__file__).resolve().parents[1]
ATOM = "{http://www.w3.org/2005/Atom}"
SOURCES = (
    ("github-changelog", "https://github.blog/changelog/feed/", True),
    ("openai", "https://openai.com/news/rss.xml", True),
    ("arxiv-ai", "https://rss.arxiv.org/rss/cs.AI", True),
    ("huggingface", "https://huggingface.co/blog/feed.xml", True),
    ("lobsters-ai", "https://lobste.rs/t/ai.rss", False),
)
TOPIC = re.compile(r"\b(agent(?:s|ic)?|mcp|a2a|llms?|codex|copilot|gemini|claude|models?|inference|rag|benchmarks?|memory|tool.calling)\b", re.I)

STRONG_ARXIV = re.compile(r"\b(agentic|agents?|mcp|a2a|tool.calling|tool.use|multi.agent|language model orchestration)\b", re.I)

def text(raw):
    return " ".join(unescape(re.sub(r"<[^>]*>", " ", raw or "")).split())

def timestamp(value):
    for parser in (datetime.fromisoformat, parsedate_to_datetime):
        try:
            dt = parser(value)
            return dt.astimezone(timezone.utc) if dt.tzinfo else None
        except (ValueError, TypeError, OverflowError):
            pass
    return None

PRIVATE_QUERY = re.compile(r"^(?:.*token.*|.*signature.*|.*secret.*|.*password.*|.*credential.*|api[_-]?key|auth(?:orization)?|sig|key|code|session(?:id)?)$", re.I)

def public_url(raw):
    raw = raw.strip()
    try:
        parts = urlsplit(raw)
        if (len(raw) > 2048 or any(c.isspace() for c in raw) or parts.scheme != "https"
                or not parts.hostname or parts.username is not None or parts.password is not None
                or any(PRIVATE_QUERY.fullmatch(k) for k, _ in parse_qsl(parts.query, keep_blank_values=True))):
            return None
        ledger.normalize_url(raw)
        return urlunsplit(parts._replace(fragment=""))
    except ValueError:
        return None

def inspect_feed(body, name, primary, cutoff, now):
    # Bound XML input at the transport boundary and never expand declared entities.
    xml_probe = body.replace(b"\0", b"").upper()
    if b"<!DOCTYPE" in xml_probe or b"<!ENTITY" in xml_probe:
        raise ValueError("feed XML contains a declaration")
    root = ET.fromstring(body)
    if root.tag not in ("rss", ATOM+"feed"):
        raise ValueError("expected RSS or Atom")
    nodes = root.findall("./channel/item") if root.tag == "rss" else root.findall(ATOM+"entry")
    rows = []
    counts = Counter()
    for item in nodes:
        if root.tag == "rss":
            url = item.findtext("link", "")
            title = text(item.findtext("title", ""))
            summary = text(item.findtext("description", ""))
            dt = timestamp(item.findtext("pubDate", ""))
        else:
            url = next((l.get("href", "") for l in item.findall(ATOM+"link")
                        if l.get("rel", "alternate") == "alternate"), "")
            title = text(item.findtext(ATOM+"title", ""))
            summary = text(item.findtext(ATOM+"summary", "") or item.findtext(ATOM+"content", ""))
            dt = timestamp(item.findtext(ATOM+"published", "") or item.findtext(ATOM+"updated", ""))
        if dt:
            counts["dated"] += 1
        if dt and not cutoff <= dt <= now:
            counts["outside_window"] += 1
            continue
        url = public_url(url)
        flags = []
        if not dt:
            flags.append("missing_date")
        if not title:
            flags.append("missing_title")
        if not url:
            flags.append("missing_or_unsafe_url")
        if not TOPIC.search(title+" "+summary[:1400]):
            flags.append("topic_filter")
        if name == "arxiv-ai" and not STRONG_ARXIV.search(title+" "+summary[:1000]):
            flags.append("arxiv_topic_filter")
        counts.update(flags)
        if not flags:
            counts["matched"] += 1
        rows.append({"source":name, "primary_feed":primary, "title":title[:500] or None,
                     "url":url, "feed_date":dt.isoformat() if dt else None, "flags":flags})
    statistics = {"total":len(nodes), "dated":counts["dated"], "outside_window":counts["outside_window"],
                  "matched":counts["matched"], "raw_rows":len(rows)}
    return statistics, rows

def parse_feed(body, name, primary, cutoff, now):
    """Compatibility helper for the keyword/date screened list."""
    stats, rows = inspect_feed(body, name, primary, cutoff, now)
    if not stats["dated"]:
        raise ValueError("empty feed or no parseable dates")
    return stats["total"], [{k:v for k,v in r.items() if k != "flags"} for r in rows if not r["flags"]]

def fetch(source, cutoff, now):
    name, url, primary = source
    status = {"source":name, "feed_url":url, "primary_feed":primary}
    try:
        request = Request(url, headers={"User-Agent":"AgenticDigestFeedReader/1.0",
                                       "Accept":"application/rss+xml, application/atom+xml, application/xml, text/xml"})
        with urlopen(request, timeout=20) as response:
            body = response.read(2_000_001)
            if len(body) > 2_000_000:
                raise ValueError("feed exceeds 2 MB")
        stats, rows = inspect_feed(body, name, primary, cutoff, now)
        status.update(stats, ok=bool(stats["dated"]))
        if not status["ok"]:
            status["error"] = "empty_feed_or_no_parseable_dates"
        return status, rows
    except (OSError, ValueError, ET.ParseError, HTTPException) as error:
        # Exception messages can contain response locations; don't persist them.
        return dict(status, ok=False, error=type(error).__name__,
                    http_status=getattr(error, "code", None), total=0, dated=0,
                    matched=0, outside_window=0, raw_rows=0), []

def collect(output, days, now=None, raw_output=None):
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    with ThreadPoolExecutor(max_workers=5) as pool:
        parts = list(pool.map(lambda s: fetch(s,cutoff,now), SOURCES))
    try:
        known = {ledger.normalize_url(url) for r in ledger.load() for url in r["source_urls"]}
        ledger_ok = True
    except (OSError, ValueError, TypeError, KeyError):
        # Preserve the collection even when the ledger was unreadable.
        known, ledger_ok = set(), False
    unique = {}
    raw = []
    seen = set()
    for status, rows in parts:
        cap = 30 if status["source"] == "arxiv-ai" else 20
        status["shortlist_cap"] = cap
        status["primary_feed"] = next(x[2] for x in SOURCES if x[0]==status["source"])
        ordered = sorted(rows, key=lambda r:r["feed_date"] or "", reverse=True)
        ranked = 0
        for item in ordered:
            flags = item["flags"]
            matched = not flags
            key = ledger.normalize_url(item["url"]) if item["url"] else None
            if key:
                if key in known:
                    flags.append("seen_in_ledger")
                if key in seen:
                    flags.append("duplicate_url_in_scan")
                seen.add(key)
            if matched and key not in known and (key not in unique or (item["primary_feed"] and not unique[key]["primary_feed"])):
                ranked += 1
                if ranked > cap:
                    flags.append("source_shortlist_cap")
                else:
                    unique[key] = item
            raw.append(item)
    shortlist = sorted(unique.values(), key=lambda i:(i["primary_feed"],i["feed_date"]), reverse=True)
    for item in shortlist:
        item["shortlisted"] = True
    for item in raw:
        item.setdefault("shortlisted", False)
    for status, rows in parts:
        status["flags"] = dict(Counter(flag for row in rows for flag in row["flags"]))
        status["shortlisted"] = sum(row["shortlisted"] for row in rows)
    health = ("degraded" if not ledger_ok or not any(s["ok"] and s["primary_feed"] for s,_ in parts)
              else "ok" if all(s["ok"] for s,_ in parts) else "partial")
    out = {"schema_version":2, "as_of":now.isoformat(), "window_start":cutoff.isoformat(),
           "scan_date_ict":now.astimezone(ZoneInfo("Asia/Ho_Chi_Minh")).date().isoformat(),
           "window_days":days, "status":health,
           "ledger_ok":ledger_ok, "sources":[status for status,_ in parts], "raw_rows":len(raw),
           "candidate_count":len(shortlist), "candidates":shortlist}
    if raw_output:
        raw_output.write_text("".join(json.dumps(row,ensure_ascii=False,separators=(",",":"))+"\n" for row in raw),
                              encoding="utf-8")
    output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k!="candidates"},ensure_ascii=False))
    if health == "degraded":
        raise ValueError("no primary source retrieved or ledger unreadable; raw diagnostics are available")

def plan(bundle, root=ROOT, now=None):
    """Validate before staging any files; Git commit/push is outside this function."""
    now = now or datetime.now(timezone.utc)
    day = bundle["digest_date"]
    if date.fromisoformat(day).isoformat() != day or day > now.astimezone(ZoneInfo("Asia/Ho_Chi_Minh")).date().isoformat():
        raise ValueError("invalid or future digest date")
    digest = bundle.get("digest_markdown", "").strip()
    items = bundle["items"]
    if not isinstance(items,list) or len(items)>10 or not digest.startswith("# "):
        raise ValueError("bundle must include a Markdown heading and up to ten items")
    if not items and bundle.get("zero_verified_items") is not True:
        raise ValueError("empty bundle requires explicit verified zero-news status")
    if any(mark in digest for mark in ("<script", "<iframe", "", "<Cite ")):
        raise ValueError("digest contains unsupported markup")
    ledger_path = root/"data/stories.jsonl"
    rows = ledger.load(ledger_path)
    known = {(r["story_id"],r["update_id"]):r for r in rows}
    paths = {}
    additions = []
    for item in items:
        row = dict(item["record"], digest_date=day, recorded_at=now.isoformat().replace("+00:00","Z"))
        ledger.check_record(row)
        if date.fromisoformat(row["event_date"]) > date.fromisoformat(day):
            raise ValueError("event date after digest date")
        if any(urlsplit(url).scheme!="https" for url in row["source_urls"]):
            raise ValueError("expected HTTPS source URLs")
        key = (row["story_id"],row["update_id"])
        rel = f"articles/{key[0]}/{key[1]}.md"
        if rel in paths:
            raise ValueError(f"duplicate item: {key}")
        if f"../{rel}" not in digest:
            raise ValueError(f"missing digest link for {key}")
        article = item["article_markdown"].strip()
        if not article.startswith("# ") or row["canonical_url"] not in article or any(m in article for m in ("<script","<iframe","","<Cite ")):
            raise ValueError(f"malformed Markdown or missing primary link: {key}")
        if key in known:
            if any(row[k]!=known[key][k] for k in row if k!="recorded_at"):
                raise ValueError(f"conflicting ledger entry: {key}")
        else:
            canonical = ledger.normalize_url(row["canonical_url"])
            if any(ledger.normalize_url(r["canonical_url"])==canonical and r["story_id"]!=key[0] for r in rows+additions):
                raise ValueError(f"canonical URL already used: {canonical}")
            additions.append(row)
        paths[rel] = article+"\n"
    paths[f"digests/{day}.md"] = digest+"\n"
    for rel,content in paths.items():
        p=root/rel
        if p.exists() and p.read_text(encoding="utf-8")!=content:
            raise ValueError(f"refusing to overwrite {rel}")
    if additions:
        previous=ledger_path.read_text(encoding="utf-8")
        paths["data/stories.jsonl"]=(previous if previous.endswith("\n") or not previous else previous+"\n")+"".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in additions)
    return paths, len(additions)

def apply(bundlepath, root=ROOT, dry_run=False, expected_date=None):
    bundle=json.loads(bundlepath.read_text(encoding="utf-8"))
    if expected_date and bundle.get("digest_date") != expected_date:
        raise ValueError("editorial filename and bundle date differ")
    paths, count=plan(bundle,root)
    if not dry_run:
        for relative,content in paths.items():
            path=root/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content,encoding="utf-8")
        ledger.load(root/"data/stories.jsonl")
    print(json.dumps({"digest_date":bundle["digest_date"],"new_ledger_rows":count,"paths":sorted(paths),"dry_run":dry_run}))

def main():
    p=argparse.ArgumentParser()
    s=p.add_subparsers(dest="cmd",required=True)
    c=s.add_parser("collect"); c.add_argument("--output",type=Path,required=True); c.add_argument("--days",type=int,choices=range(1,8),default=3); c.add_argument("--raw-output",type=Path)
    a=s.add_parser("apply"); a.add_argument("bundle",type=Path); a.add_argument("--dry-run",action="store_true"); a.add_argument("--expected-date")
    args=p.parse_args()
    try:
        if args.cmd=="collect": collect(args.output,args.days,raw_output=args.raw_output)
        else: apply(args.bundle,dry_run=args.dry_run,expected_date=args.expected_date)
    except (OSError, ValueError, TypeError, KeyError) as error:
        p.exit(1,f"digest: {error}\n")
if __name__=="__main__":
    main()
