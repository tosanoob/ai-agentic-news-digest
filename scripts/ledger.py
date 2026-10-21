#!/usr/bin/env python3
"""Dependency-free validation and event-level duplicate checks for digest ledger.

A row is proof of inclusion in a GitHub-archived digest, NOT message delivery.
No network calls and no automatic semantic deduplication.
"""
import argparse
from collections import Counter
from datetime import date, datetime
from difflib import SequenceMatcher
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

DEFAULT_PATH = Path(__file__).resolve().parents[1] / "data" / "stories.jsonl"
CATEGORIES = {
    "breaking", "model_release", "agent_framework", "paper", "benchmark",
    "github_release", "security", "protocol", "enterprise", "policy", "other",
}
NEEDED = {
    "story_id", "update_id", "title", "event_date", "recorded_at",
    "digest_date", "category", "canonical_url", "source_urls", "change_summary",
}
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TRACKING = {"fbclid", "gclid", "mc_cid", "mc_eid", "ref_src", "utm_source",
            "utm_medium", "utm_campaign", "utm_term", "utm_content"}


def normalize_url(raw):
    """Remove tracking parameters without discarding meaningful URL parameters."""
    parsed = urlsplit(raw.strip())
    if parsed.scheme.lower() not in ("http", "https") or not parsed.netloc:
        raise ValueError("URL must use HTTP(S) and contain a host")
    host = parsed.hostname.lower()
    port = parsed.port
    netloc = host + (f":{port}" if port else "")
    path = parsed.path.rstrip("/") or "/"
    query = urlencode(
        sorted((k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True)
               if k.lower() not in TRACKING and not k.lower().startswith("utm_"))
    )
    return urlunsplit((parsed.scheme.lower(), netloc, path, query, ""))


def check_record(item):
    if not isinstance(item, dict):
        raise ValueError("record must be a JSON object")
    missing = NEEDED - item.keys()
    extra = item.keys() - NEEDED
    if missing or extra:
        raise ValueError(f"missing={sorted(missing)}, extra={sorted(extra)}")
    for key in ("story_id", "update_id"):
        if not isinstance(item[key], str) or not SLUG.fullmatch(item[key]):
            raise ValueError(f"{key} must be lowercase kebab-case")
    if item["category"] not in CATEGORIES:
        raise ValueError("unknown category")
    for key in ("title", "change_summary"):
        if not isinstance(item[key], str) or len(item[key].strip()) < (5 if key == "title" else 10):
            raise ValueError(f"{key} too short")
    for key in ("event_date", "digest_date"):
        if not isinstance(item[key], str):
            raise ValueError(f"{key} must be an ISO date")
        date.fromisoformat(item[key])
    if not isinstance(item["recorded_at"], str):
        raise ValueError("recorded_at must be a timestamp")
    recorded = datetime.fromisoformat(item["recorded_at"].replace("Z", "+00:00"))
    if recorded.tzinfo is None:
        raise ValueError("recorded_at needs a timezone")
    normalize_url(item["canonical_url"])
    urls = item["source_urls"]
    if not isinstance(urls, list) or not urls or len(set(urls)) != len(urls):
        raise ValueError("source_urls must be a unique, nonempty list")
    for url in urls:
        normalize_url(url)
    if normalize_url(item["canonical_url"]) not in {normalize_url(u) for u in urls}:
        raise ValueError("canonical_url must be in source_urls")


def load(path=DEFAULT_PATH):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"ledger missing: {path}")
    records = []
    seen = set()
    event_urls = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            check_record(item)
            key = item["story_id"], item["update_id"]
            if key in seen:
                raise ValueError(f"duplicate story/update key: {key}")
            seen.add(key)
            url = normalize_url(item["canonical_url"])
            existing_story = event_urls.get(url)
            if existing_story and existing_story != item["story_id"]:
                raise ValueError(f"same canonical URL used by story IDs {existing_story} and {item['story_id']}")
            event_urls[url] = item["story_id"]
            records.append(item)
        except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
            raise ValueError(f"{path}:{line_no}: {exc}") from exc
    return records


def classify(records, story_id, update_id, url=None, title=None):
    """Conservative decision: exact duplicate or candidate for human review."""
    if any((r["story_id"], r["update_id"]) == (story_id, update_id) for r in records):
        return {"status": "covered", "reason": "story_id + update_id already archived"}
    same_story = [r for r in records if r["story_id"] == story_id]
    if same_story and update_id != "initial":
        return {"status": "review", "reason": "new update to an existing story; verify material change"}
    if url:
        normalized = normalize_url(url)
        matches = [r["story_id"] for r in records
                   if normalized in {normalize_url(u) for u in r["source_urls"]}]
        if matches:
            return {"status": "review", "reason": "source URL already covered", "story_ids": sorted(set(matches))}
    if title:
        cleaned = lambda s: re.sub(r"\W+", " ", s.casefold()).strip()
        close = [(r["story_id"], round(SequenceMatcher(None, cleaned(title),
                  cleaned(r["title"])).ratio(), 3)) for r in records]
        candidates = sorted([(sid, score) for sid, score in close if score >= 0.86],
                            key=lambda p: -p[1])
        if candidates:
            return {"status": "review", "reason": "similar existing headlines, not automatically duplicate",
                    "candidates": candidates[:5]}
    return {"status": "new", "reason": "no exact match; editorial review still required"}


def append(path, item):
    check_record(item)
    records = load(path)
    key = (item["story_id"], item["update_id"])
    if any((r["story_id"], r["update_id"]) == key for r in records):
        raise ValueError("story/update pair already archived")
    new_url = normalize_url(item["canonical_url"])
    for r in records:
        if normalize_url(r["canonical_url"]) == new_url and r["story_id"] != item["story_id"]:
            raise ValueError("canonical URL belongs to another story_id")
    path = Path(path)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=".stories-", delete=False) as handle:
        temp_name = handle.name
        for row in [*records, item]:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
    try:
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_PATH)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    sub.add_parser("stats")
    checker = sub.add_parser("check")
    checker.add_argument("--story-id", required=True)
    checker.add_argument("--update-id", default="initial")
    checker.add_argument("--url")
    checker.add_argument("--title")
    writer = sub.add_parser("append")
    writer.add_argument("--json-file", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        rows = load(args.ledger)
        if args.command == "validate":
            print(f"OK: {len(rows)} ledger records")
        elif args.command == "stats":
            print(json.dumps({"records": len(rows),
                              "unique_stories": len({r["story_id"] for r in rows}),
                              "categories": dict(Counter(r["category"] for r in rows))}))
        elif args.command == "check":
            print(json.dumps(classify(rows, args.story_id, args.update_id, args.url, args.title),
                             ensure_ascii=False))
        else:
            item = json.loads(args.json_file.read_text(encoding="utf-8"))
            append(args.ledger, item)
            print("OK: record appended (archived, not confirmed delivered)")
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
