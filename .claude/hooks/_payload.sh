#!/usr/bin/env bash
# Shared payload reader for Claude Code hooks.
#
# CONTRACT (verified against code.claude.com/docs/en/hooks.md):
#   - The hook payload arrives as JSON on STDIN. There are no TOOL_INPUT_* env
#     vars. Only ${CLAUDE_PROJECT_DIR}, ${CLAUDE_PLUGIN_ROOT}, and
#     ${CLAUDE_PLUGIN_DATA} interpolate inside a settings.json command string.
#   - Exit 2 blocks the tool call (PreToolUse) and surfaces stderr to Claude.
#   - Exit 0 with no stdout is a silent pass.
#
# FAIL-CLOSED RULE: a guard that cannot read its payload must say so, not pass
# silently. Every function here distinguishes "nothing to check" from "could not
# check" and the callers escalate the latter.

set -uo pipefail

HOOK_PAYLOAD=""
HOOK_PAYLOAD_OK=0

hook_read_payload() {
  # stdin is the only supported transport. Non-blocking read so a hook invoked
  # with no stdin (manual test, misconfiguration) does not hang the session.
  if [[ ! -t 0 ]]; then
    HOOK_PAYLOAD="$(cat || true)"
  fi
  if [[ -n "$HOOK_PAYLOAD" ]] && printf '%s' "$HOOK_PAYLOAD" | jq -e . >/dev/null 2>&1; then
    HOOK_PAYLOAD_OK=1
  fi
}

hook_have_jq() { command -v jq >/dev/null 2>&1; }

hook_field() { # $1 = jq path, e.g. .tool_input.file_path
  printf '%s' "$HOOK_PAYLOAD" | jq -r "${1} // empty" 2>/dev/null
}

hook_tool_name() { hook_field '.tool_name'; }

# Every file path the tool call touches, one per line.
hook_file_paths() {
  printf '%s' "$HOOK_PAYLOAD" | jq -r '
    [ .tool_input.file_path?,
      .tool_input.notebook_path?,
      (.tool_input.edits[]?.file_path?),
      (.tool_input.file_paths[]?)
    ] | map(select(. != null and . != "")) | unique | .[]' 2>/dev/null
}

# Every chunk of content the tool call would write, concatenated.
# Covers Write(file_text/content), Edit(edits[].new_str/new_string),
# NotebookEdit(notebook_edits[].content), and legacy str_replace shapes.
hook_written_content() {
  printf '%s' "$HOOK_PAYLOAD" | jq -r '
    [ .tool_input.file_text?,
      .tool_input.content?,
      .tool_input.new_str?,
      .tool_input.new_string?,
      (.tool_input.edits[]?.new_str?),
      (.tool_input.edits[]?.new_string?),
      (.tool_input.notebook_edits[]?.content?)
    ] | map(select(. != null)) | join("\n")' 2>/dev/null
}

hook_bash_command() { hook_field '.tool_input.command'; }
