# GitHub Actions for Agentic Digest

The code-based pipeline separates discovery, editorial work, and persistence. No paid API, daily.dev, passwords, or personal data are required. The existing ChatGPT notification is a separate concern.

## Collect

`Agentic Digest` collects at 06:37 Asia/Ho_Chi_Minh (23:37 UTC the previous date). A manual `collect` run is also available. It checks the current ledger, fetches fixed feeds, reports counts per source, and uploads a short-lived `digest-candidates` artifact with title, feed date, and source link. This is discovery, not verified news. Lobsters is secondary discovery only. A missing or failed feed is logged, not treated as no news; if all primary feeds fail, collection fails.

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

The script assigns `recorded_at` and `digest_date` on ledger entries. For a genuinely completed scan with no qualifying item, explicitly use `zero_verified_items: true` with an empty list and a Markdown explanation. Do not use this for failed sources or incomplete research. Both the artifact and the repository are public: never include credentials, private data, or copied articles.

## Safety and verification

`collect` and `dry-run` have read-only GitHub permissions. Only the trusted main-branch writer may use `contents: write`; it runs tests before writing, validates linked files, and pushes one ordinary non-force commit. It refuses conflicting prior digests or ledger records. A repeated identical bundle adds no duplicate. `SYNCED` requires verifying the commit is on remote main. The writer runs the validator in the job because GitHub generally does not trigger another push workflow for a commit made with its built-in token.

Do not switch ChatGPT to read-only notification until both handoff and a hosted write with read-back have been verified. A failed publication is not a sent or archived digest. Daily.dev and a dedicated model/search API are intentionally not configured.
