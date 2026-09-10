#!/usr/bin/env bash
# PostToolUse. Enforces CLAUDE.md § "Evidence before assertion" mechanically.
#
# An evidence row with no provenance tag is a claim with no source. CLAUDE.md
# requires evidence before assertion; this hook is the only thing that actually
# checks it. Prose rules are not runtime enforcement.
#
# Scope: files under a second-brain hypotheses/, decisions/, or stakeholders/
# directory, and under org-brain/decisions/. Schema and README templates are
# exempt.
#
# Two tiers, deliberately:
#   BLOCKING (exit 2) — an evidence row with NO tag at all. Always fixable in
#     the same turn: add [documented]/[verbal]/[hunch]/[industry]/[unknown], or
#     move the row to Open questions. No external dependency.
#   WARNING (exit 0) — a [documented] tag with no identifiable artifact. Often
#     an ordering issue (the source file lands later), so it informs, it does
#     not gate.
#
# Rows under "Open questions", "Remaining ambiguities", and "What would settle
# it" are commentary by construction and need no tag.
set -uo pipefail
SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=_payload.sh
source "$SELF_DIR/_payload.sh"

hook_have_jq || exit 0
hook_read_payload
[[ "$HOOK_PAYLOAD_OK" -eq 1 ]] || exit 0

blocking=""
warnings=""

while IFS= read -r target; do
  [[ -z "$target" ]] && continue
  [[ "$target" == *.md ]] || continue
  [[ -f "$target" ]] || continue

  # Only brain claim-files. Templates define the shape, they don't assert.
  # Both brains: the domain second-brain and the org brain carry the same
  # provenance discipline.
  case "$target" in
    */second-brain/hypotheses/*|*/second-brain/decisions/*|*/second-brain/stakeholders/*) ;;
    */org-brain/decisions/*) ;;
    *) continue ;;
  esac
  case "$(basename "$target")" in
    _SCHEMA.md) continue ;;
  esac

  report="$(awk '
    function flush_row() {
      if (row == "") return
      # Untagged bullets that are pure placeholders are fine.
      # Angle-bracket template placeholders are shape, not assertion.
      if (row ~ /^[[:space:]]*<[^>]*>[[:space:]]*$/) { row = ""; return }
      # Empty-state markers, including "none yet — <why>" with trailing prose.
      if (row ~ /^_?\(?[[:space:]]*(none( yet)?|n\/?a|tbd|todo|nothing yet|no evidence( yet)?|not yet|pending|—|-)([[:space:]]*[—–-][[:space:]].*)?[[:space:]]*\)?_?[.!]?$/) { row = ""; return }
      if (row ~ /\[(documented|verbal|hunch|industry|unknown)\]/) {
        # [documented] asserts a written artifact exists. Look for one.
        if (row ~ /\[documented\]/ &&
            row !~ /`[^`]+`/ && row !~ /\]\([^)]+\)/ &&
            row !~ /(source|ingestion|domains|outputs)\// &&
            row !~ /\.(md|py|ts|tsx|js|java|json|yaml|yml)/) {
          warn = warn sprintf("    line %d: [documented] with no artifact cited :: %s\n", rowline, substr(row, 1, 88))
        }
        row = ""; return
      }
      orph = orph sprintf("    line %d: no provenance tag :: %s\n", rowline, substr(row, 1, 88))
      row = ""
    }
    # Fenced code is illustration, never assertion.
    /^[[:space:]]*```/ { infence = !infence; flush_row(); next }
    infence { next }
    # Blockquotes are schema guidance.
    /^[[:space:]]*>/ { flush_row(); next }
    # A markdown heading closes any open evidence context.
    /^#{1,6}[[:space:]]/ { flush_row(); inev = 0; next }
    {
      line = $0
      # Bold-label sections: **Evidence for:** / **Evidence:** open a context;
      # any other bold label closes it.
      if (match(tolower(line), /\*\*[[:space:]]*(evidence([[:space:]]+(for|against))?|explicitly not doing)[[:space:]]*:?\*\*/)) {
        flush_row(); inev = 1
        rest = line
        sub(/^.*\*\*[^*]*\*\*[[:space:]]*/, "", rest)
        if (rest ~ /[A-Za-z0-9]/) { row = rest; rowline = NR; flush_row() }
        next
      }
      if (match(line, /^[[:space:]]*[-*][[:space:]]+\*\*[^*]+\*\*/)) { flush_row(); inev = 0; next }
      if (!inev) next
      # Bullet inside an evidence context.
      if (match(line, /^[[:space:]]*[-*][[:space:]]+/)) {
        flush_row()
        row = substr(line, RLENGTH + 1); rowline = NR
        next
      }
      # Continuation of a wrapped bullet.
      if (row != "" && line ~ /[A-Za-z0-9]/) { row = row " " gensub(/^[[:space:]]+/, "", 1, line); next }
      if (line !~ /[A-Za-z0-9]/) flush_row()
    }
    END {
      flush_row()
      if (orph != "") printf "ORPHAN\n%s", orph
      if (warn != "") printf "WARN\n%s", warn
    }
  ' "$target" 2>/dev/null)"

  [[ -z "$report" ]] && continue

  orphan_block="$(printf '%s' "$report" | awk '/^ORPHAN$/{f=1;next} /^WARN$/{f=0} f')"
  warn_block="$(printf '%s' "$report" | awk '/^WARN$/{f=1;next} /^ORPHAN$/{f=0} f')"

  [[ -n "$orphan_block" ]] && blocking+="  $target"$'\n'"$orphan_block"
  [[ -n "$warn_block" ]] && warnings+="  $target"$'\n'"$warn_block"
done < <(hook_file_paths)

if [[ -n "$warnings" ]]; then
  cat >&2 <<MSG
provenance-guard: warnings (non-blocking) — [documented] should name its artifact:
$warnings
A [documented] claim with no citable artifact is weaker than an honest [verbal].
MSG
fi

if [[ -n "$blocking" ]]; then
  cat >&2 <<MSG
provenance-guard: BLOCKING — evidence rows with no provenance tag. Fix this turn.
$blocking
CLAUDE.md: "Evidence before assertion; missing evidence stays Unknown or TBD."

Every evidence row needs one tag (see second-brain/hypotheses/_SCHEMA.md):
  [documented]  written and verifiable — cite the artifact
  [verbal]      said, not written — name the person and date
  [hunch]       our own read, no external evidence yet
  [industry]    general industry knowledge, not specific to us
  [unknown]     open question, no answer yet

If the row is commentary rather than a claim, move it under "Open questions:"
or "Remaining ambiguities:" — those need no tag. If a row aggregates several
sources, split it into one tagged row per source.
MSG
  exit 2
fi

exit 0
