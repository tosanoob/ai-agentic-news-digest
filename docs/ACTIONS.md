# GitHub Actions for Agentic Digest

The code-based pipeline separates discovery, editorial work, and persistence. No paid API, daily.dev, passwords, or personal data are required. The existing ChatGPT notification is a separate concern.

## Collect

`Agentic Digest` collects at 06:37 Asia/Ho_Chi_Minh (23:37 UTC the previous date). A manual collect on `main` is also available. The 3-day upload is transport/fallback only. A separate trusted job commits metadata to the [candidate-log branch](https://github.com/tosanoob/ai-agentic-news-digest/tree/candidate-log) and reports `CANDIDATES_SAVED` only after Git remote read-back.

- Lookup: on `candidate-log`, read `YYYY-MM-DD/latest.json` for today's Vietnam date, then read the relative paths in `manifest` and `raw`. Each scan is kept under `YYYY-MM-DD/<Actions run ID>-<attempt>/`; a retry stores a separate scan and doesn't overwrite prior ones. Use a full workflow rerun or a new manual collect after a failed upload/archive.
- `digest-candidates.json` is a compact editorial starting point. Its source diagnostics report returned, dated, out-of-window, keyword-matched, logged, and shortlisted counts; flag counts can overlap. A partial scan means at least one feed failed even though some primary coverage remains. A brief title or feed date is not original-source verification.
- `raw-candidates.jsonl` records every returned entry in the configured time window, plus undated entries. It keeps public link, source, title and feed timestamp before editorial review, including keyword misses, exact URL duplicates, links already in the ledger and entries beyond the per-source shortlist cap. Invalid or credential-bearing URLs are omitted from the row; out-of-window entries are counted, not logged individually. Scope is the returned feed snapshots, not all news on the web. Caps (20 per feed, 30 for arXiv) apply only to the shortlist after filtering known ledger links and exact URL duplicates, never to the raw log.
- Source errors are visible, not counted as no news; Lobsters is secondary discovery only. If all primary feeds or the ledger fail, the scan is marked degraded and retained for diagnosis, but independently research the news. Missing, stale or unusable scan pointers are not evidence of zero news. Continue searching beyond these feeds; the shortlist can miss worthwhile stories.

## Editorial handoff

Verify event dates, significance and original sources before preparing a bundle. Compare against the latest ledger by underlying event; use a new update ID only for a material, verified update. The publisher enforces exact keys and canonical URL reuse, but cannot infer event-level semantic equivalence or authenticity from syntax. The editor must read primary sources and write the digest and articles. A feed date is not proof of the event date.

Use one `editorial/YYYY-MM-DD.json` file per push on `main`, or run the workflow manually with `mode: dry-run` or `publish` and the same JSON. Do not stage test bundles on main. Save initial setup and smoke tests off main.

```json
{
  "digest_date": "2026-11-26",
  "digest_markdown": "# Digest\n\n[Article](../articles/example-event/initial.md)",
  "items": [{
    "record": {
      "story_id": "example-event",
      "update_id": "initial",
      "title": "Illustrative example event",
      "event_date": "2026-11-25",
      "category": "agent_framework",
      "canonical_url": "https://example.com/announcement",
      "source_urls": ["https://example.com/announcement"],
      "change_summary": "Illustrative example; never publish."
    },
    "article_markdown": "# Example\n\nOriginal analysis. Source: https://example.com/announcement"
  }]
}
```

The script assigns `recorded_at` and `digest_date` on ledger entries. For a genuinely completed scan with no qualifying item, explicitly use `zero_verified_items: true` with an empty list and a Markdown explanation. Do not use this for failed sources or incomplete research. Both the artifacts and candidate branch are public: never include credentials, private data, or copied articles.

## Safety and verification

`collect` and `dry-run` have read-only GitHub permissions. A separate main-branch-only archival job validates the candidate artifact and may write only the candidate-log branch; it does not touch digest, articles or ledger. The trusted publisher runs tests before writing, validates linked files, and pushes one ordinary non-force commit to main. It refuses conflicting prior digests or ledger records. A repeated identical bundle adds no duplicate. `SYNCED` requires verifying the commit is on remote main. The writer runs the validator in the job because GitHub generally does not trigger another push workflow for a commit made with its built-in token.

Do not switch ChatGPT to read-only notification until both handoff and a hosted write with read-back have been verified. A failed publication is not a sent or archived digest. Daily.dev and a dedicated model/search API are intentionally not configured.
