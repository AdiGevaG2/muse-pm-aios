#!/usr/bin/env python3
"""Generates scripts/test-hooks.

Test vectors are stored base64-encoded here and emitted base64-encoded, so that
neither this generator nor the generated suite ever contains a plaintext
credential or a literal destructive command. That keeps the guards from
blocking their own test harness.
"""
import base64
import pathlib
import sys

# base64 of realistic-but-fake credential strings
SECRETS = {
    "FX_AWS":   "YXdzX2FjY2Vzc19rZXlfaWQgPSBBS0lBSU9TRk9ETk43RVhBTVBMRQ==",
    "FX_ANT":   "a2V5OiBzay1hbnQtYXBpMDMtYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4",
    "FX_PW":    "cGFzc3dvcmQgPSBodW50ZXIyaHVudGVyMmh1bnRlcjJodW50ZXIy",
    "FX_GHPAT": "Z2l0aHViX3BhdF8xMUFCQ0RFRkcwYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXoxMjM0NTY3ODkw",
    "FX_SLACK": "dG9rZW4gPSB4b3hiLTEyMzQ1Njc4OTAxMi1hYmNkZWZnaGlqa2w=",
    "FX_JWT":   "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnpkV0lpT2lJeE1qTTBOVFkzT0Rrd0luMC5kQmpmdEplWjRDVlBtQjkySzI3dWhiVUpVMXAxci13VzFnRldGT0VqWGs=",
}

# base64 of commands the destructive guard MUST block
BLOCKED = [
    "cm0gLXJmIC90bXAveA==",
    "c3VkbyBybSAtZnIgfi9kYXRh",
    "Z2l0IHJlc2V0IC0taGFyZCBIRUFEfjM=",
    "Z2l0IHB1c2ggLS1mb3JjZSBvcmlnaW4gbWFpbg==",
    "Z2l0IHB1c2ggLWY=",
    "Z2l0IGNsZWFuIC1mZA==",
    "Z2l0IGNoZWNrb3V0IC0tIC4=",
    "Z2l0IGJyYW5jaCAtRCBmZWF0dXJlL3g=",
    "ZmluZCAuIC1uYW1lICcqLm1kJyAtZGVsZXRl",
    "Y2htb2QgLVIgNzc3IC8=",
    "ZGQgaWY9L2Rldi96ZXJvIG9mPS9kZXYvZGlzazI=",
]

# base64 of commands the destructive guard MUST allow
ALLOWED = [
    "Z2l0IHN0YXR1cw==",
    "Z2l0IGxvZyAtLW9uZWxpbmU=",
    "Z3JlcCAtcm4gVE9ETyAu",
    "cm0gL3RtcC9vbmVmaWxlLnR4dA==",
    "bnBtIHJ1biBidWlsZA==",
    "Z2l0IGRpZmYgLS1zdGF0",
    "YmFzaCBzY3JpcHRzL3ZhbGlkYXRlLXdvcmtzcGFjZQ==",
]

lines = []
A = lines.append

A('#!/usr/bin/env bash')
A('# Proves the hooks actually fire against real Claude Code payload shapes.')
A('# Run after any hook or settings.json change. Exit 0 = all guards behave.')
A('#')
A('# Why this exists: the previous hooks read a TOOL_INPUT_PATH env var that')
A('# Claude Code never sets, and exited 0 on empty input -- so they passed')
A('# everything silently while appearing configured. Untested guards are theatre.')
A('#')
A('# Test vectors are base64-encoded so that running this suite does not trip')
A('# the guards under test.')
A('set -uo pipefail')
A('cd "$(dirname "$0")/.." || exit 1')
A('H=".claude/hooks"; pass=0; fail=0')
A('d() { printf %s "$1" | base64 --decode; }')
A('')
for k, v in SECRETS.items():
    A(f'{k}="{v}"')
A('')
A('check() { # name expected_exit payload script')
A('  local name="$1" want="$2" payload="$3" script="$4" out got')
A('  out="$(printf %s "$payload" | bash "$script" 2>&1)"; got=$?')
A('  if [[ "$got" == "$want" ]]; then')
A(r'    printf "  PASS  %-52s (exit %s)\n" "$name" "$got"; pass=$((pass+1))')
A('  else')
A(r'    printf "  FAIL  %-52s want %s got %s\n" "$name" "$want" "$got"')
A(r'    printf "        output: %s\n" "$(printf %s "$out" | head -2 | tr "\n" " ")"; fail=$((fail+1))')
A('  fi')
A('}')
A('')
A("bash_payload() { jq -nc --arg c \"$(d \"$1\")\" '{hook_event_name:\"PreToolUse\",tool_name:\"Bash\",tool_input:{command:$c}}'; }")
A("write_payload() { jq -nc --arg t \"$(d \"$1\")\" '{hook_event_name:\"PreToolUse\",tool_name:\"Write\",tool_input:{file_path:\"/tmp/hooktest.md\",file_text:$t}}'; }")
A('')
A('notify_check() { # name payload want(yes|no)')
A('  local name="$1" payload="$2" want="$3" out')
A('  out="$(printf %s "$payload" | bash "$H/prd-change-guard.sh" 2>&1)"')
A('  if [[ "$want" == "yes" ]]; then')
A('    if printf %s "$out" | grep -q "Product intent moved"; then')
A(r'      printf "  PASS  %-52s (notified)\n" "$name"; pass=$((pass+1))')
A(r'    else printf "  FAIL  %-52s (stayed silent)\n" "$name"; fail=$((fail+1)); fi')
A('  else')
A(r'    if [[ -z "$out" ]]; then printf "  PASS  %-52s (silent)\n" "$name"; pass=$((pass+1))')
A(r'    else printf "  FAIL  %-52s (spoke when it should not)\n" "$name"; fail=$((fail+1)); fi')
A('  fi')
A('}')
A('')
A('echo "secret-guard - BLOCK (2) on credentials, PASS (0) on clean prose"')
A('check "Write: cloud access key in file_text" 2 "$(write_payload "$FX_AWS")" "$H/secret-guard.sh"')
A('check "Write: vendor api key in file_text"   2 "$(write_payload "$FX_ANT")" "$H/secret-guard.sh"')
A('check "Write: JWT-shaped string"             2 "$(write_payload "$FX_JWT")" "$H/secret-guard.sh"')

edit_new_str = ("check \"Edit: secret in edits[].new_str\" 2 \"$(jq -nc --arg t \"$(d \"$FX_PW\")\" "
                "'{hook_event_name:\"PreToolUse\",tool_name:\"Edit\",tool_input:"
                "{file_path:\"/tmp/hooktest.md\",edits:[{old_str:\"x\",new_str:$t}]}}')\" \"$H/secret-guard.sh\"")
A(edit_new_str)

edit_legacy = ("check \"Edit: secret in legacy new_string\" 2 \"$(jq -nc --arg t \"$(d \"$FX_GHPAT\")\" "
               "'{hook_event_name:\"PreToolUse\",tool_name:\"Edit\",tool_input:"
               "{file_path:\"/tmp/hooktest.md\",old_string:\"x\",new_string:$t}}')\" \"$H/secret-guard.sh\"")
A(edit_legacy)

nb = ("check \"NotebookEdit: secret in cell content\" 2 \"$(jq -nc --arg t \"$(d \"$FX_SLACK\")\" "
      "'{hook_event_name:\"PreToolUse\",tool_name:\"NotebookEdit\",tool_input:"
      "{notebook_path:\"/tmp/h.ipynb\",notebook_edits:[{content:$t}]}}')\" \"$H/secret-guard.sh\"")
A(nb)

clean = ("check \"Write: clean PM prose\" 0 '{\"hook_event_name\":\"PreToolUse\",\"tool_name\":\"Write\","
         "\"tool_input\":{\"file_path\":\"/tmp/hooktest.md\","
         "\"file_text\":\"# PRD. Good PRDs cite evidence, they do not assert.\"}}' \"$H/secret-guard.sh\"")
A(clean)
A('check "FAIL-CLOSED: empty stdin"    2 "" "$H/secret-guard.sh"')
A('check "FAIL-CLOSED: malformed JSON" 2 "not json at all" "$H/secret-guard.sh"')
A('')
A('echo')
A('echo "destructive-operation-guard - BLOCK (2) irreversible, ALLOW (0) safe"')
for c in BLOCKED:
    A(f'check "block: $(d "{c}")" 2 "$(bash_payload "{c}")" "$H/destructive-operation-guard.sh"')
A('')
for c in ALLOWED:
    A(f'check "allow: $(d "{c}")" 0 "$(bash_payload "{c}")" "$H/destructive-operation-guard.sh"')
A('check "FAIL-CLOSED: empty stdin" 2 "" "$H/destructive-operation-guard.sh"')
A('')
A('echo')
A('echo "prd-change-guard - NOTIFY on prd paths, silent elsewhere"')

def notify(name, path, want):
    payload = ('{"hook_event_name":"PostToolUse","tool_name":"Write","tool_input":'
               f'{{"file_path":"{path}"}}}}')
    return f"notify_check \"{name}\" '{payload}' {want}"

A(notify("notify: outputs/f/prd/f-prd.md", "outputs/f/prd/f-prd.md", "yes"))
A(notify("notify: outputs/f/prd/nested-prd.md", "outputs/f/prd/nested-prd.md", "yes"))
A(notify("silent: outputs/f/spec/f-spec.md", "outputs/f/spec/f-spec.md", "no"))
# domains/*/features/ is retired: outputs/ is the only feature path.
A(notify("silent: retired domains/d/features/f/prd.md", "domains/d/features/f/prd.md", "no"))
A('')
A('echo')
A('echo "provenance-guard - BLOCK (2) untagged evidence, PASS (0) tagged"')
A('PVDIR="$(mktemp -d)/second-brain/hypotheses"; mkdir -p "$PVDIR"')
A('pv_payload() { jq -nc --arg p "$1" \'{hook_event_name:"PostToolUse",tool_name:"Write",tool_input:{file_path:$p}}\'; }')
A('')
A("cat > \"$PVDIR/tagged.md\" <<'PVEOF'")
A('### Tagged — 2026-08-27')
A('- **Evidence for:**')
A('  - Three leads asked for weekly default  [documented] `source/x.md`')
A('  - Naomi confirmed priority  [verbal] Naomi, 2026-05-13')
A('  - Friction reduces conversion  [industry]')
A('- **Evidence against:**')
A('  - _(none yet)_')
A('- **Open questions:**')
A('  - Untagged commentary is legal here')
A('PVEOF')
A('')
A("cat > \"$PVDIR/untagged.md\" <<'PVEOF'")
A('### Untagged — 2026-08-27')
A('- **Evidence for:**')
A('  - Acme ops lead stopped acting on notifications')
A('PVEOF')
A('')
A("cat > \"$PVDIR/emptystate.md\" <<'PVEOF'")
A('### Empty state — 2026-08-27')
A('- **Evidence for:** none yet — pure naming-convention assumption.')
A('- **Evidence against:** <with provenance tags>')
A('PVEOF')
A('')
A("cat > \"$PVDIR/_SCHEMA.md\" <<'PVEOF'")
A('### Template — the schema itself must never be gated')
A('- **Evidence for:**')
A('  - <claim>  <provenance-tag>')
A('PVEOF')
A('')
A('check "pass: every evidence row tagged" 0 "$(pv_payload "$PVDIR/tagged.md")" "$H/provenance-guard.sh"')
A('check "BLOCK: evidence row with no tag" 2 "$(pv_payload "$PVDIR/untagged.md")" "$H/provenance-guard.sh"')
A('check "pass: empty-state and placeholder rows" 0 "$(pv_payload "$PVDIR/emptystate.md")" "$H/provenance-guard.sh"')
A('check "pass: _SCHEMA.md exempt" 0 "$(pv_payload "$PVDIR/_SCHEMA.md")" "$H/provenance-guard.sh"')
A('check "pass: file outside second-brain ignored" 0 \'{"hook_event_name":"PostToolUse","tool_name":"Write","tool_input":{"file_path":"README.md"}}\' "$H/provenance-guard.sh"')
A('rm -rf "$(dirname "$(dirname "$PVDIR")")"')
A('')
A('echo')
A('echo "settings.json - must not reference nonexistent TOOL_INPUT_* env vars"')
A('if grep -q "TOOL_INPUT_" .claude/settings.json 2>/dev/null; then')
A('  echo "  FAIL  settings.json still uses TOOL_INPUT_* (never set by Claude Code)"; fail=$((fail+1))')
A('else')
A('  echo "  PASS  settings.json uses the stdin payload contract"; pass=$((pass+1))')
A('fi')
A('')
A('echo')
A('echo "----- $pass passed, $fail failed -----"')
A('[[ "$fail" -eq 0 ]] || exit 1')

out = pathlib.Path(sys.argv[1])
out.write_text("\n".join(lines) + "\n")
out.chmod(0o755)
print(f"wrote {out} ({len(lines)} lines)")
