# Scheduled digest runbook

This repository is the persistent **archive and de-duplication reference**, not a second notification system.

1. At task start read `README.md`, `config/sources.yaml`, `data/stories.jsonl`, and the latest available digest archives. If missing/unreadable, state **best-effort only**; do not claim a persistent lookup.
2. Scan the period since the previous successful dated archive; include weekends after Friday. If no archive exists, scan the last 72 hours, optionally look back further for significant first-run stories.
3. Verify the date of **the underlying event** and first-party URL. Use secondary coverage only to contextualize.
4. Cluster cross-posts as ONE story using stable kebab-case `story_id`. Evaluate duplicates by `(story_id,update_id)`; use URL and headline similarity as secondary signals; preserve genuinely new material update under the old story ID.
5. Write 5–10 high-signal stories if available (fewer is fine), sections: Breaking; Models/Agents; Papers & Benchmarks; GitHub Releases; What to Watch. Each entry includes date, source link, technical significance and evidence caveats.
6. Before publishing, archive dated digest `digests/YYYY-MM-DD.md` and update `data/stories.jsonl` **without losing existing records**. Prefer an atomic Git commit containing both changes. If GitHub write fails, continue with a digest marked **ledger write failed**, and do not assert new entries were saved.
7. A ledger row means *archived/included*, never `sent`. Do not claim a ChatGPT notification was delivered, since this repository cannot validate delivery.
8. On retries, if a digest archive already exists for the day, compare and only issue materially new BREAKING/UPDATE content; otherwise prevent re-publication.
9. Never commit secrets or automatically scrape full copyrighted articles.

## Integration limitation

Interactive connector write permission **does not establish** unattended GitHub permissions inside ChatGPT scheduled tasks. This needs a verified task execution. There is no GitHub Actions news delivery job in this repository; CI only validates the ledger.
