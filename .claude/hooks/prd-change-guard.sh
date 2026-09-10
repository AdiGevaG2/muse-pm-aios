#!/usr/bin/env bash
# PostToolUse. When a PRD changes, product intent moved — downstream artifacts
# are now suspect. Non-blocking: it informs, it does not gate.
set -uo pipefail
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_payload.sh
source "$SELF_DIR/_payload.sh"

hook_have_jq || exit 0
hook_read_payload
[[ "$HOOK_PAYLOAD_OK" -eq 1 ]] || exit 0

while IFS= read -r changed; do
  [[ -z "$changed" ]] && continue
  case "$changed" in
    *outputs/*/prd/*.md)
      feature_dir="${changed%/prd*}"
      cat <<MSG
PRD changed: $changed
Product intent moved. Downstream artifacts are stale until re-checked:
  - $feature_dir/spec/        (build behavior may no longer match intent)
  - $feature_dir/validation/  (prior Pass verdicts were against the old PRD)
  - any external handoff already published (Jira / Confluence / deck)
Bump the PRD version, then propagate deliberately. Do not treat downstream as current.
MSG
      ;;
  esac
done < <(hook_file_paths)
exit 0
