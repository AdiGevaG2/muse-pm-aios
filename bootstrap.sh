#!/usr/bin/env bash
# One-time prerequisite check + best-effort clone, before handing off to
# Claude Code's /setup skill for the conversational part. Safe to re-run.
set -uo pipefail

GREENLIGHT_REPO="https://github.com/g2webservices/greenlight"
DESIGN_SYSTEM_REPO="https://github.com/evercompliant/g2rs-design-system.git"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pass=0
fail=0

ok()   { echo "  OK   $1"; pass=$((pass + 1)); }
warn() { echo "  WARN $1"; }
bad()  { echo "  FAIL $1"; fail=$((fail + 1)); }

echo "Checking prerequisites..."

if command -v git >/dev/null 2>&1; then
  ok "git found ($(git --version))"
else
  bad "git not found — install git before continuing"
fi

if command -v claude >/dev/null 2>&1; then
  ok "Claude Code CLI found"
else
  warn "Claude Code CLI not found on PATH — you may still be able to open this folder via the VS Code/desktop extension instead"
fi

echo ""
echo "Attempting to clone repos (safe to skip if access isn't granted yet)..."
mkdir -p "$REPO_DIR/repos"

if [ -d "$REPO_DIR/repos/greenlight/.git" ]; then
  ok "Greenlight repo already cloned at ./repos/greenlight"
else
  if git clone --depth 1 "$GREENLIGHT_REPO" "$REPO_DIR/repos/greenlight" >/tmp/greenlight-clone.log 2>&1; then
    ok "Cloned Greenlight repo to ./repos/greenlight"
  else
    warn "Could not clone Greenlight repo yet — this is expected if your GitHub access hasn't been granted. Details: /tmp/greenlight-clone.log"
  fi
fi

echo ""
read -r -p "Also clone the Unified Platform design-system repo now? [y/N] " reply
if [[ "$reply" =~ ^[Yy]$ ]]; then
  if [ -d "$REPO_DIR/repos/g2rs-design-system/.git" ]; then
    ok "Design-system repo already cloned at ./repos/g2rs-design-system"
  else
    if git clone "$DESIGN_SYSTEM_REPO" "$REPO_DIR/repos/g2rs-design-system" >/tmp/design-system-clone.log 2>&1; then
      ok "Cloned design-system repo to ./repos/g2rs-design-system"
    else
      warn "Could not clone design-system repo. Details: /tmp/design-system-clone.log"
    fi
  fi
else
  echo "  Skipped — you can do this later from inside /setup."
fi

echo ""
echo "Prerequisite check: $pass ok, $fail blocking failure(s)."

if [ "$fail" -gt 0 ]; then
  echo ""
  echo "Fix the FAIL item(s) above, then re-run ./bootstrap.sh."
  exit 1
fi

echo ""
echo "Next step: run 'claude' in this folder, then type /setup"
