from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import archive_candidates
import digest_actions as digest


class CandidateArchiveTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.artifact = self.root / "artifact"
        self.artifact.mkdir()
        self.manifest = self.artifact / "digest-candidates.json"
        self.raw = self.artifact / "raw-candidates.jsonl"
        self.now = datetime.now(timezone.utc)

    def fixture(self, name, primary, cutoff, now):
        from email.utils import format_datetime
        from html import escape
        def entry(title,url,dt):
            return (f"<item><title>{title}</title><link>{escape(url)}</link>"
                    f"<pubDate>{format_datetime(dt) if dt else ''}</pubDate></item>")
        dt = now - timedelta(minutes=2)
        items = ("".join(entry(f"Agent release {i}", f"https://example.org/{i}", dt) for i in range(32))
                 + entry("Football news","https://example.org/football",dt)
                 + entry("Old agent","https://example.org/old",cutoff-timedelta(days=1))
                 + entry("Undated agent","https://example.org/undated",None)
                 + entry("Agent bad link","https://example.org/a?access_token=do-not-leak",dt)
                 + entry("Agent duplicate","https://example.org/1?utm_source=feed",dt))
        stats, rows = digest.inspect_feed(f"<rss><channel>{items}</channel></rss>".encode(),name,primary,cutoff,now)
        return dict(stats, source=name, primary_feed=primary, ok=True), rows

    def collect(self, now=None, all_fail=False):
        def fetch(source, cutoff, when):
            status, rows = self.fixture(*source[::2], cutoff, when)
            if all_fail:
                status["ok"] = False
            return status, rows
        with patch.object(digest,"SOURCES",(("github-test","https://example.org/feed",True),)), \
             patch.object(digest,"fetch",fetch), patch.object(digest.ledger,"load",return_value=[
                 {"canonical_url":"https://example.org/0","source_urls":["https://example.org/0"]}]):
            digest.collect(self.manifest,3,now or self.now,self.raw)

    def test_metadata_before_editor_filter(self):
        self.collect()
        d = json.loads(self.manifest.read_text())
        raw = self.raw.read_text()
        rows = [json.loads(line) for line in raw.splitlines()]
        self.assertEqual(36, d["raw_rows"])
        self.assertEqual(1, d["sources"][0]["outside_window"])
        self.assertEqual(20, d["candidate_count"])
        self.assertIn("Football news", raw)
        self.assertIn("missing_date", raw)
        self.assertIn("duplicate_url_in_scan", raw)
        self.assertIn("source_shortlist_cap", raw)
        self.assertIn("seen_in_ledger",raw)
        self.assertNotIn("do-not-leak",raw)
        self.assertFalse(next(r for r in rows if r["title"]=="Agent release 31")["shortlisted"])

    def test_degraded_results_still_archivable(self):
        with self.assertRaisesRegex(ValueError,"primary source"):
            self.collect(all_fail=True)
        day = archive_candidates.stage(self.artifact, self.root/"tree","45001","1")
        pointer = json.loads((self.root/"tree"/day/"latest.json").read_text())
        self.assertEqual("degraded",pointer["status"])

    def test_append_only_and_pointer_does_not_regress(self):
        self.collect()
        tree = self.root/"tree"
        day = archive_candidates.stage(self.artifact,tree,"45001","2")
        actual = (tree/day/"latest.json").read_bytes()
        archive_candidates.stage(self.artifact,tree,"45001","1")
        self.assertEqual(actual,(tree/day/"latest.json").read_bytes())
        self.assertTrue((tree/day/"45001-1"/"raw-candidates.jsonl").exists())
        self.collect(self.now + timedelta(microseconds=1))
        with self.assertRaisesRegex(ValueError,"immutable"):
            archive_candidates.stage(self.artifact,tree,"45001","2")

    def test_mismatched_artifact_and_invalid_run_are_rejected(self):
        self.collect()
        with self.assertRaisesRegex(ValueError,"identity"):
            archive_candidates.stage(self.artifact,self.root/"tree","../bad","1")
        self.raw.write_text("")
        with self.assertRaisesRegex(ValueError,"match"):
            archive_candidates.stage(self.artifact,self.root/"tree","1","1")

    def test_document_type_is_rejected(self):
        with self.assertRaisesRegex(ValueError,"declaration"):
            digest.inspect_feed(b"<!DOCTYPE rss><rss/>","feed",True,self.now,self.now)

    def test_html_doctype_inside_feed_cdata_is_not_xml_declaration(self):
        payload = b'<rss><channel><item><title>Agent news</title><description><![CDATA[<!DOCTYPE html>]]></description></item></channel></rss>'
        stats, metadata = digest.inspect_feed(payload,"feed",True,self.now,self.now)
        self.assertEqual((stats["total"], metadata[0]["title"]), (1, "Agent news"))

    def test_utf16_internal_entity_declaration_rejected(self):
        payload = ('<!DOCTYPE rss [<!ENTITY foo "test">]><rss>&foo;</rss>').encode("utf-16")
        with self.assertRaisesRegex(ValueError,"declaration"):
            digest.inspect_feed(payload,"feed",True,self.now,self.now)
