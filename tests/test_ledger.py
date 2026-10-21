import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("ledger", ROOT / "scripts" / "ledger.py")
ledger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ledger)


def sample(story="model-launch", update="initial"):
    return {
        "story_id": story, "update_id": update, "title": "Major model announcement",
        "event_date": "2026-10-21", "recorded_at": "2026-10-21T08:00:00Z",
        "digest_date": "2026-10-22", "category": "model_release",
        "canonical_url": "https://example.com/model-launch",
        "source_urls": ["https://example.com/model-launch"],
        "change_summary": "Initial, verified release with source evidence."
    }


class LedgerTests(unittest.TestCase):
    def test_canonical_url_ignores_tracking(self):
        a = ledger.normalize_url("https://Example.com/release/?utm_source=x&v=2#intro")
        self.assertEqual(a, "https://example.com/release?v=2")

    def test_load_empty_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stories.jsonl"
            path.write_text("", encoding="utf-8")
            self.assertEqual(ledger.load(path), [])

    def test_append_and_exact_dedup(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stories.jsonl"
            path.write_text("", encoding="utf-8")
            item = sample()
            ledger.append(path, item)
            self.assertEqual(ledger.classify(ledger.load(path), "model-launch", "initial")["status"], "covered")
            with self.assertRaises(ValueError):
                ledger.append(path, item)

    def test_same_story_major_update_requires_review(self):
        self.assertEqual(ledger.classify([sample()], "model-launch", "general-availability")["status"], "review")

    def test_different_story_same_source_flagged(self):
        self.assertEqual(ledger.classify([sample()], "another-event", "initial",
                         "https://example.com/model-launch?utm_campaign=a")["status"], "review")

    def test_duplicate_urls_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stories.jsonl"
            path.write_text(json.dumps(sample()) + "\n" + json.dumps(sample("another-event")) + "\n",
                            encoding="utf-8")
            with self.assertRaises(ValueError):
                ledger.load(path)

    def test_missing_timezone_rejected(self):
        item = sample()
        item["recorded_at"] = "2026-10-21T08:00:00"
        with self.assertRaises(ValueError):
            ledger.check_record(item)


if __name__ == "__main__":
    unittest.main()
