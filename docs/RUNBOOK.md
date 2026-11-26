# Scheduled digest runbook

See [GitHub Actions pipeline](ACTIONS.md) for the editorial bundle contract and publication controls.

1. GitHub Actions collects candidate links daily near 06:37 Vietnam time. Candidates are discovery only; source and event verification remain editorial.
2. At the start of the ChatGPT digest, read the source config, ledger, latest archives, and today's editorial/ archive file status. Use the latest successful archive to determine gaps. No ledger access means no verified deduplication and no handoff write.
3. Verify first-party sources and underlying dates; cluster cross-posts by story ID and introduce a new update ID only for material events. Start with the highest-signal items and write their standalone analysis first.
4. Hand off one reviewed editorial bundle via a single GitHub connector write. Do not write article, archive or ledger paths from the task. If the bundle already exists, check status; never overwrite it as a retry.
5. Actions validates and pushes articles, digest and ledger together, then verifies the remote. Only read-back evidence justifies reporting SYNCED. On failure, distinguish missing research, handoff error, pending workflow and publication failure.
6. ChatGPT remains the notification channel. An archived ledger row does not prove notification delivery.
7. Never commit credentials, personal data, copied articles or fictional rows. No daily.dev or paid API is in this workflow.
