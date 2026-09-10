#!/usr/bin/env bash
# Blocks writes that would persist a credential into the workspace.
# PreToolUse: exit 2 blocks the write. PostToolUse: exit 2 reports it landed.
set -uo pipefail
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_payload.sh
source "$SELF_DIR/_payload.sh"

if ! hook_have_jq; then
  echo "secret-guard: jq not found — cannot inspect payload; treating as UNGUARDED." >&2
  echo "secret-guard: install jq (brew install jq) or the credential guard is inert." >&2
  exit 2
fi

hook_read_payload

if [[ "$HOOK_PAYLOAD_OK" -ne 1 ]]; then
  echo "secret-guard: no valid JSON payload on stdin — cannot verify this write." >&2
  echo "secret-guard: failing closed. Check the hook wiring in .claude/settings.json." >&2
  exit 2
fi

event="$(hook_field '.hook_event_name')"
payload_text="$(hook_written_content)"

# On PostToolUse the content may already be on disk; scan the file too, which
# also catches writes whose content field shape we do not recognize.
while IFS= read -r p; do
  [[ -n "$p" && -f "$p" ]] && payload_text+=$'\n'"$(cat "$p" 2>/dev/null || true)"
done < <(hook_file_paths)

[[ -z "${payload_text//[[:space:]]/}" ]] && exit 0

token_pattern='(-----BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----|AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|ghp_[A-Za-z0-9_]{30,}|gho_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{40,}|xox[baprs]-[A-Za-z0-9-]{20,}|sk-[A-Za-z0-9]{32,}|sk-ant-[A-Za-z0-9_-]{20,}|glpat-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{35}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,})'
assignment_pattern="(api[_-]?key|secret|token|password|passwd|pwd|client[_-]?secret|private[_-]?key|access[_-]?key|bearer)[[:space:]]*[:=][[:space:]]*[\"']?[A-Za-z0-9_./+=-]{20,}"

hit=""
printf '%s\n' "$payload_text" | grep -Eq  "$token_pattern"      && hit="known credential format"
printf '%s\n' "$payload_text" | grep -Eiq "$assignment_pattern" && hit="${hit:+$hit; }secret-shaped assignment"

if [[ -n "$hit" ]]; then
  echo "secret-guard: possible credential detected ($hit)." >&2
  while IFS= read -r p; do [[ -n "$p" ]] && echo "  path: $p" >&2; done < <(hook_file_paths)
  if [[ "$event" == "PostToolUse" ]]; then
    echo "secret-guard: this write ALREADY LANDED. Remove the value, then rotate it." >&2
  else
    echo "secret-guard: write blocked. Use an env var or local secret store; never a repo file." >&2
  fi
  exit 2
fi
exit 0
