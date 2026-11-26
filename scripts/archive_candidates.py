"""Stage the verified current Actions scan on the candidate-only Git branch."""
import argparse
from datetime import date, datetime, timedelta
from hashlib import sha256
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo


def stage(artifact, archive, run_id, attempt):
    if not re.fullmatch(r"[1-9][0-9]{0,19}", run_id) or not re.fullmatch(r"[1-9][0-9]{0,4}", attempt):
        raise ValueError("invalid GitHub run identity")
    manifest_name = "digest-candidates.json"
    raw_name = "raw-candidates.jsonl"
    manifest_bytes = (artifact / manifest_name).read_bytes()
    raw = (artifact / raw_name).read_bytes()
    if len(manifest_bytes) > 500_000 or len(raw) > 15_000_000:
        raise ValueError("candidate artifact exceeds metadata bounds")
    manifest = json.loads(manifest_bytes)
    when = datetime.fromisoformat(manifest["as_of"])
    if when.tzinfo is None:
        raise ValueError("scan timestamp has no timezone")
    day = when.astimezone(ZoneInfo("Asia/Ho_Chi_Minh")).date().isoformat()
    if manifest["schema_version"] != 2 or manifest["scan_date_ict"] != day or manifest["status"] not in {"ok", "partial", "degraded"}:
        raise ValueError("candidate manifest schema, date or status invalid")
    if abs(date.fromisoformat(day) - datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).date()) > timedelta(days=1):
        raise ValueError("scan does not belong to the current collection window")
    rows = [json.loads(line) for line in raw.splitlines()]
    shortlisted = [row for row in rows if row["shortlisted"]]
    ordered = sorted(shortlisted, key=lambda r:(r["primary_feed"], r["feed_date"]), reverse=True)
    # Different feed order for equal timestamps is harmless, but contents must match.
    canonical = lambda records: sorted(json.dumps(row, sort_keys=True) for row in records)
    if (len(rows) != manifest["raw_rows"] or sum(s["raw_rows"] for s in manifest["sources"]) != len(rows)
            or len(ordered) != manifest["candidate_count"] or canonical(ordered) != canonical(manifest["candidates"])):
        raise ValueError("raw rows and shortlist do not match manifest")
    run_rel = f"{day}/{run_id}-{attempt}"
    dest = archive / run_rel
    dest.mkdir(parents=True, exist_ok=True)
    for name, content in ((manifest_name, manifest_bytes), (raw_name, raw)):
        target = dest / name
        if target.exists() and target.read_bytes() != content:
            raise ValueError(f"refusing to replace immutable run file {name}")
        target.write_bytes(content)
    pointer = archive / day / "latest.json"
    newest = (when, int(run_id), int(attempt))
    if pointer.exists():
        old = json.loads(pointer.read_text(encoding="utf-8"))
        if newest < (datetime.fromisoformat(old["as_of"]), old["run_id"], old["attempt"]):
            return day
    value = {k:manifest[k] for k in ("schema_version","as_of","scan_date_ict","status","raw_rows","candidate_count")}
    value.update(run_id=int(run_id), attempt=int(attempt), manifest=f"{run_rel}/{manifest_name}",
                 raw=f"{run_rel}/{raw_name}", raw_sha256=sha256(raw).hexdigest(),
                 manifest_sha256=sha256(manifest_bytes).hexdigest())
    pointer.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    return day


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("artifact", type=Path)
    p.add_argument("archive", type=Path)
    p.add_argument("run_id")
    p.add_argument("attempt")
    a = p.parse_args()
    try:
        print(stage(a.artifact, a.archive, a.run_id, a.attempt))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        p.exit(1, f"candidate archive: {error}\n")
