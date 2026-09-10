#!/usr/bin/env bash
# PreToolUse on AskUserQuestion. CLAUDE.md allows exactly two reasons to stop and
# ask: an external write, or destroying work that is not trivially recoverable.
# Every other question is a contract violation — the run should assume, mark the
# assumption in the artifact, and continue.
#
# This exists because the prose already said all of this and was ignored anyway:
# one reverse-engineer run asked 14 questions that were each pre-answered in the
# skill files. Advisory text failed; this gate is mechanical.
set -uo pipefail
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_payload.sh
source "$SELF_DIR/_payload.sh"

hook_have_jq || exit 0
hook_read_payload
[[ "$HOOK_PAYLOAD_OK" -eq 1 ]] || exit 0

# All question text plus headers, lowercased, as one blob to match against.
questions="$(printf '%s' "$HOOK_PAYLOAD" | jq -r '
  [ (.tool_input.questions[]?.question?),
    (.tool_input.questions[]?.header?)
  ] | map(select(. != null)) | join(" ")' 2>/dev/null | tr '[:upper:]' '[:lower:]')"

# Nothing to inspect — do not block on a payload shape we do not recognize.
[[ -z "$questions" ]] && exit 0

# Allowed: the question is about pushing to an external system, or about
# deleting/overwriting something. These are the two CLAUDE.md exceptions.
allow_re='confluence|jira|slack|email|publish|push to|create the ticket'
allow_re+='|overwrite|delete|discard|replace the existing|destroy'

# Third exception: /learn-feature is a teaching conversation, so asking IS the
# deliverable (CLAUDE.md exception 4). Opt in explicitly by tagging the question
# text with [learn-feature] so this stays impossible to trip into by accident.
if printf '%s' "$questions" | grep -qF '[learn-feature]'; then
  exit 0
fi

if printf '%s' "$questions" | grep -Eq "$allow_re"; then
  exit 0
fi

cat >&2 <<'MSG'
BLOCKED: AskUserQuestion is gated by the PM workflow contract.

CLAUDE.md -> "Default Behavior: Act, Don't Ask". The only two reasons to stop:
  1. An external write (Confluence, Jira, Slack, email).
  2. Deleting or overwriting work that is not trivially recoverable.

This question matched neither. These are already decided for you:
  - Run mode          -> default Quick (_shared/run-mode.md)
  - Workspace name    -> derive from the feature name, state it in one line
  - Stale/dirty repo  -> caveat in the artifact, never ask to pull
  - Unreachable repo  -> mark NOT VERIFIED, continue with what resolved
  - Which gaps to close -> the skill's hard stopping rule decides
  - Artifact shape, scope, framing, metric choice -> your call

Take the most reasonable reading, write it into the artifact marked `ASSUMED:`,
and continue. The PM corrects it in review — that is cheaper than a round-trip.

If this genuinely is an external write or a destructive overwrite, say so in the
question text (name the system, or the word overwrite/delete) and re-issue it.
MSG
exit 2
