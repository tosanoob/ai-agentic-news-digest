from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
import digest_actions as digest

NOW = datetime(2026,11,26,1,tzinfo=timezone.utc)
URL = "https://example.com/announcement"
ROW = dict(story_id="test-event", update_id="initial",title="Test agent event", event_date="2026-11-25",
           category="agent_framework",canonical_url=URL,source_urls=[URL],change_summary="A verified test event.")
def bundle():
    return dict(digest_date="2026-11-26", digest_markdown="# Digest\n\n[Article](../articles/test-event/initial.md)",
                items=[dict(record=dict(ROW), article_markdown=f"# Test\n\nSource: {URL}")])

class DigestActionsTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        (self.root/"data").mkdir()
        self.ledger=self.root/"data/stories.jsonl"
        self.ledger.write_text("",encoding="utf-8")
    def apply_paths(self, paths):
        for path,body in paths.items():
            target=self.root/path
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_text(body,encoding="utf-8")
    def test_plan_and_retry_without_duplicate(self):
        paths,count=digest.plan(bundle(),self.root,NOW)
        self.assertEqual(count,1); self.assertEqual(len(paths),3)
        self.assertEqual(self.ledger.read_text(),"")
        self.apply_paths(paths)
        self.assertEqual(len(digest.ledger.load(self.ledger)),1)
        paths,count=digest.plan(bundle(),self.root,NOW+timedelta(minutes=5))
        self.assertEqual(count,0); self.assertNotIn("data/stories.jsonl",paths)
    def test_conflict_preserves_archive(self):
        paths,_=digest.plan(bundle(),self.root,NOW)
        self.apply_paths(paths)
        b=bundle(); b["digest_markdown"]+="\nextra"
        with self.assertRaisesRegex(ValueError,"refusing to overwrite"):
            digest.plan(b,self.root,NOW)
    def test_unsafe_key_and_missing_link(self):
        b=bundle(); b["items"][0]["record"]["story_id"]="../escape"
        with self.assertRaises(ValueError): digest.plan(b,self.root,NOW)
        b=bundle(); b["digest_markdown"]="# Digest"
        with self.assertRaisesRegex(ValueError,"missing digest link"): digest.plan(b,self.root,NOW)
    def test_zero_requires_explicit_confirmation(self):
        b=dict(digest_date="2026-11-26",digest_markdown="# No verified news",items=[])
        with self.assertRaises(ValueError): digest.plan(b,self.root,NOW)
        b["zero_verified_items"]=True
        paths,count=digest.plan(b,self.root,NOW)
        self.assertEqual(count,0); self.assertEqual(list(paths),["digests/2026-11-26.md"])
    def test_rss_recent_and_relevant(self):
        feed=b'<rss><channel><item><title>Agent release</title><link>https://example.com/new</link><pubDate>Wed, 25 Nov 2026 10:00:00 GMT</pubDate></item><item><title>Football</title><link>https://example.com/other</link><pubDate>Wed, 25 Nov 2026 10:00:00 GMT</pubDate></item></channel></rss>'
        total,items=digest.parse_feed(feed,"test",True,NOW-timedelta(days=2),NOW)
        self.assertEqual(total,2); self.assertEqual([i["title"] for i in items],["Agent release"])
