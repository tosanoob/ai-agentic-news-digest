"""Read news feeds and apply a reviewed editorial bundle; never sends notifications."""
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
import argparse
import json
from pathlib import Path
import re
from urllib.parse import urlsplit
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

def parse_feed(body, name, primary, cutoff, now):
    root = ET.fromstring(body)
    if root.tag not in ("rss", ATOM+"feed"):
        raise ValueError("expected RSS or Atom")
    nodes = root.findall("./channel/item") if root.tag == "rss" else root.findall(ATOM+"entry")
    items = []
    dated = 0
    for item in nodes:
        if root.tag == "rss":
            url = item.findtext("link", "")
            title = text(item.findtext("title", ""))
            summary = text(item.findtext("description", ""))
            dt = timestamp(item.findtext("pubDate", ""))
        else:
            url = next((l.get("href", "") for l in item.findall(ATOM+"link") if l.get("rel", "alternate") == "alternate"), "")
            title = text(item.findtext(ATOM+"title", ""))
            summary = text(item.findtext(ATOM+"summary", "") or item.findtext(ATOM+"content", ""))
            dt = timestamp(item.findtext(ATOM+"published", "") or item.findtext(ATOM+"updated", ""))
        if dt:
            dated += 1
        if not dt or not cutoff <= dt <= now or not title or not TOPIC.search(title+" "+summary[:1400]):
            continue
        if name=="arxiv-ai" and not STRONG_ARXIV.search(title+" "+summary[:1000]):
            continue
        try:
            if urlsplit(url).scheme != "https" or not urlsplit(url).hostname:
                continue
            ledger.normalize_url(url)
        except ValueError:
            continue
        items.append({"source":name, "primary_feed":primary, "title":title[:300], "url":url,
                      "feed_date":dt.isoformat()})
    if not nodes or not dated:
        raise ValueError("empty feed or no parseable dates")
    return len(nodes), items

def fetch(source, cutoff, now):
    name, url, primary = source
    try:
        request = Request(url, headers={"User-Agent":"AgenticDigestFeedReader/1.0",
                                       "Accept":"application/rss+xml, application/atom+xml, application/xml, text/xml"})
        with urlopen(request, timeout=20) as response:
            body = response.read(2_000_001)
            if len(body) > 2_000_000:
                raise ValueError("feed exceeds 2 MB")
        total, items = parse_feed(body, name, primary, cutoff, now)
        return {"source":name, "ok":True, "total":total, "matched":len(items)}, items
    except (OSError, ValueError, ET.ParseError) as error:
        return {"source":name, "ok":False, "error":str(error)[:200]}, []

def collect(output, days, now=None):
    now = now or datetime.now(timezone.utc)
    cutoff = now - timedelta(days=days)
    with ThreadPoolExecutor(max_workers=5) as pool:
        parts = list(pool.map(lambda s: fetch(s,cutoff,now), SOURCES))
    known = {ledger.normalize_url(r["canonical_url"]) for r in ledger.load()}
    unique = {}
    for _, items in parts:
        for item in sorted(items, key=lambda i:i["feed_date"], reverse=True)[:30 if items and items[0]["source"]=="arxiv-ai" else 20]:
            link = ledger.normalize_url(item["url"])
            if link not in known and (link not in unique or item["primary_feed"]):
                unique[link] = item
    out = {"as_of":now.isoformat(), "window_days":days, "sources":[status for status,_ in parts],
           "candidates":sorted(unique.values(), key=lambda i:(i["primary_feed"],i["feed_date"]), reverse=True)[:120]}
    output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"sources":out["sources"],"candidates":len(out["candidates"])},ensure_ascii=False))
    if not any(status["ok"] for status,_ in parts if status["source"]!="lobsters-ai"):
        raise ValueError("no primary source was retrieved")

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
    c=s.add_parser("collect"); c.add_argument("--output",type=Path,required=True); c.add_argument("--days",type=int,choices=range(1,8),default=3)
    a=s.add_parser("apply"); a.add_argument("bundle",type=Path); a.add_argument("--dry-run",action="store_true"); a.add_argument("--expected-date")
    args=p.parse_args()
    try:
        if args.cmd=="collect": collect(args.output,args.days)
        else: apply(args.bundle,dry_run=args.dry_run,expected_date=args.expected_date)
    except (OSError, ValueError, TypeError, KeyError) as error:
        p.exit(1,f"digest: {error}\n")
if __name__=="__main__":
    main()
