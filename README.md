# AI Agentic News Digest

A GitHub-backed, event-level news ledger for the **ChatGPT AI Agentic Deep Research Digest**.

**Schedule:** Monday–Friday, 08:00 Asia/Singapore (flexible, within ~1 hour). This repository **does not schedule or deliver** ChatGPT notifications; the existing ChatGPT scheduled task does. GitHub Actions here runs validation only.

## How it works

1. **Read** `data/stories.jsonl` and available `digests/YYYY-MM-DD.md` before researching.
2. **Research** original announcements, technical release notes, new research papers and relevant reporting; check the *event date*, not just article publication date.
3. **Cluster** multiple articles about one underlying event; use a stable, human-curated `story_id`.
4. **Filter**: publish a new `story_id` once. Revisit only when a material milestone merits a new `update_id`; include the precise delta and label it **UPDATE**.
5. **Publish/archive** a dated digest in `digests/`, with citations and original event dates.
6. **Record** each included story/update in the ledger. A ledger entry means *included in an archived digest*, **not proof that a ChatGPT notification was delivered**.

If the connector cannot read/write the repository during a scheduled run, **do not pretend persistent de-duplication succeeded**. Deliver a best-effort digest, mark the ledger as unavailable, and do not claim any ledger update.

## Ledger format

Each nonblank line of `data/stories.jsonl` is an independent JSON object conforming to `config/story.schema.json`. The tuple `(story_id, update_id)` must be unique:

```json
{"story_id":"openai-example-agent-release","update_id":"initial","title":"Example agent released","event_date":"2026-10-21","recorded_at":"2026-10-22T00:15:00Z","digest_date":"2026-10-22","category":"model_release","canonical_url":"https://example.com/announcement","source_urls":["https://example.com/announcement"],"change_summary":"Initial release"}
```

The example above is illustrative, **not** a real news record. The ledger begins empty and will only contain verified stories included in future digests. For a major follow-up, use the *same* `story_id` with a distinct `update_id`, e.g. `general-availability`. A different URL or headline about the same event is not a new story.

## Guardrails

- Prioritize first-party announcements, then independent reporting; verify dates and sources.
- Distinguish preprints from peer-reviewed papers; disclose benchmark limitations.
- Avoid fabricating citations, reported performance, or GitHub release details.
- Never mark stories as `sent` unless notification delivery is independently confirmed.
- Treat title similarity as **review evidence**, not enough to automatically drop a new event.
- Use SHA-guarded GitHub updates; do not overwrite concurrent ledger modifications.
- Do not store API keys, user personal data, or scraped full articles.

## Layout

```text
data/stories.jsonl              Append-oriented event/update ledger
digests/YYYY-MM-DD.md           Human-readable dated digests
config/story.schema.json        Data contract
config/sources.yaml             Preferred sources and editorial policy
scripts/ledger.py               Validate, check, append and summarize ledger
tests/test_ledger.py            Automated regression tests
.github/workflows/validate.yml  Validation on pushes and PRs, NOT a second scheduler
```

## Local/CI validation (optional)

```bash
python -m unittest discover -s tests -v
python scripts/ledger.py validate data/stories.jsonl
python scripts/ledger.py check --story-id example-event --update-id initial
```

## Integration status

- GitHub repository and ledger: initialize in this scaffold.
- ChatGPT Scheduled Task: configured separately and can be instructed to read and update these paths.
- **Unattended scheduled GitHub writes:** must be validated on an actual task run. Connector permissions in an interactive chat are not sufficient proof of unattended access.
