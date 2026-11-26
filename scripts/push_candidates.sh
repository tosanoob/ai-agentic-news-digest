#!/usr/bin/env bash
# Invoked by the trusted archival job; it does not execute uploaded content.
set -euo pipefail
: "${RUNNER_TEMP:?}" "${GITHUB_RUN_ID:?}" "${GITHUB_RUN_ATTEMPT:?}" "${GITHUB_STEP_SUMMARY:?}"
branch="${1:?candidate-log branch required}"
[[ "$branch" == candidate-log || "$branch" == candidate-log-qa ]]
trusted="$(mktemp "$RUNNER_TEMP/candidate-archive.XXXXXX")"
cp scripts/archive_candidates.py "$trusted"
initial="$(git rev-parse HEAD)"
for try in 1 2 3 4; do
  git checkout --detach "$initial"
  if git ls-remote --exit-code origin "refs/heads/$branch" >/dev/null; then
    git fetch --no-tags origin "refs/heads/$branch"
    git checkout --detach FETCH_HEAD
  else
    rc=$?
    [ "$rc" = 2 ] || exit "$rc"
    git switch --orphan "candidate-bootstrap-$try"
  fi
  day="$(python "$trusted" "$RUNNER_TEMP/candidate-artifact" . "$GITHUB_RUN_ID" "$GITHUB_RUN_ATTEMPT")"
  [[ "$day" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]
  git add -- "$day"
  if ! git diff --cached --quiet; then
    git -c user.name='github-actions[bot]' -c user.email='41898282+github-actions[bot]@users.noreply.github.com' commit -m "candidates: $day / $GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT"
    if ! git push origin "HEAD:refs/heads/$branch"; then
      sleep "$((try * 2))"
      continue
    fi
  fi
  git fetch --no-tags origin "refs/heads/$branch"
  git merge-base --is-ancestor HEAD FETCH_HEAD
  echo "CANDIDATES_SAVED: $branch:$day/$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT ($(git rev-parse HEAD))" | tee -a "$GITHUB_STEP_SUMMARY"
  exit 0
done
echo 'candidate archive could not be pushed' >&2
exit 1
