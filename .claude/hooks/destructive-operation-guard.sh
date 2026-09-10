#!/usr/bin/env bash
# Blocks irreversible shell operations so they require explicit human approval.
set -uo pipefail
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_payload.sh
source "$SELF_DIR/_payload.sh"

if ! hook_have_jq; then
  echo "destructive-operation-guard: jq not found — cannot inspect command; failing closed." >&2
  exit 2
fi

hook_read_payload

if [[ "$HOOK_PAYLOAD_OK" -ne 1 ]]; then
  echo "destructive-operation-guard: no valid JSON payload on stdin — cannot verify this command." >&2
  echo "destructive-operation-guard: failing closed. Check .claude/settings.json hook wiring." >&2
  exit 2
fi

command_text="$(hook_bash_command)"
[[ -z "${command_text//[[:space:]]/}" ]] && exit 0

blocked_pattern='(^|[;&|`(){}[:space:]])(sudo[[:space:]]+)?rm[[:space:]]+-[A-Za-z]*[rR][A-Za-z]*f|(^|[;&|`(){}[:space:]])(sudo[[:space:]]+)?rm[[:space:]]+-[A-Za-z]*f[A-Za-z]*[rR]|git[[:space:]]+reset[[:space:]]+--hard|git[[:space:]]+clean[[:space:]]+-[A-Za-z]*f|git[[:space:]]+checkout[[:space:]]+--|git[[:space:]]+branch[[:space:]]+-D|git[[:space:]]+push[^;]*(--force([[:space:]]|$|=)|-f([[:space:]]|$))|git[[:space:]]+filter-branch|find[[:space:]][^;]+[[:space:]]-delete|find[[:space:]][^;]+-exec[[:space:]]+rm|chmod[[:space:]]+-R[[:space:]]+777|chown[[:space:]]+-R|mkfs\.|diskutil[[:space:]]+erase|dd[[:space:]][^;]*of=/dev/|>[[:space:]]*/dev/(sd|disk|nvme)|truncate[[:space:]]+-s[[:space:]]*0|shred[[:space:]]|:\(\)\{.*\|:&.*\};:'

if printf '%s\n' "$command_text" | grep -Eq "$blocked_pattern"; then
  echo "destructive-operation-guard: irreversible operation requires explicit human approval." >&2
  echo "  command: $command_text" >&2
  echo "  If intended, run it yourself in a terminal — the guard will not authorize it." >&2
  exit 2
fi
exit 0
