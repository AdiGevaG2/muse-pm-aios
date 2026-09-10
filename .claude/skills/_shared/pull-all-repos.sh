#!/usr/bin/env bash
# Pull all locally-cloned repos onto their own current branch (whatever it's
# named — master/develop/main/feature). Never pulls a dirty repo. Never
# switches branches. Repo list source of truth:
# domains/unified-platform/second-brain/context/platform.md
#
# Usage: ./pull-all-repos.sh [--include-worktrees]

set -uo pipefail

BASE="${CODE_REPOS_ROOT:-$HOME/vsCode/code-repos-git}"

REPOS=(
  "single-platform-legacy-g2/g2-singlePlatform"
  "merchant-view-legacy-ec/app-infra-devops"
  "merchant-view-legacy-ec/everc-global-services"
  "merchant-view-legacy-ec/gateway"
  "merchant-view-legacy-ec/merchantviewui"
  "merchant-view-legacy-ec/merv-global-services"
  "merchant-view-legacy-ec/mvnextgen"
  "merchant-view-legacy-ec/mvserver"
  "unified-platform-new/everc-global-services"
  "unified-platform-new/marketview-portal"
  "unified-platform-new/mlrc-account"
  "unified-platform-new/mlrc-analysis"
  "unified-platform-new/mlrc-bff-2.0"
  "unified-platform-new/mlrc-finding"
  "unified-platform-new/mlrc-infra"
  "unified-platform-new/mlrc-merchant"
  "unified-platform-new/mlrc-monitoring"
  "unified-platform-new/mlrc-notification"
  "unified-platform-new/mlrc-risk"
  "unified-platform-new/mlrc-sdk-test"
  "unified-platform-new/mlrc-status"
  "unified-platform-new/ufp-automation"
)

# In-progress feature worktree with known uncommitted changes — excluded
# unless explicitly requested, since pulling/fetching here is low-risk but
# the intent of this script is "sync mainline repos," not touch active work.
WORKTREES=(
  "unified-platform-new/marketview-portal-001-category-risk-config"
)

INCLUDE_WORKTREES=false
if [[ "${1:-}" == "--include-worktrees" ]]; then
  INCLUDE_WORKTREES=true
fi

TARGETS=("${REPOS[@]}")
if $INCLUDE_WORKTREES; then
  TARGETS+=("${WORKTREES[@]}")
fi

updated=()
current=()
skipped_dirty=()
skipped_missing=()
failed=()

for rel in "${TARGETS[@]}"; do
  path="$BASE/$rel"
  name="$rel"

  if [[ ! -d "$path/.git" ]]; then
    skipped_missing+=("$name")
    continue
  fi

  if [[ -n "$(git -C "$path" status --porcelain 2>/dev/null)" ]]; then
    skipped_dirty+=("$name")
    continue
  fi

  branch="$(git -C "$path" rev-parse --abbrev-ref HEAD 2>/dev/null)"
  before="$(git -C "$path" rev-parse HEAD 2>/dev/null)"

  if ! git -C "$path" fetch --quiet 2>/dev/null; then
    failed+=("$name (fetch failed)")
    continue
  fi

  if ! git -C "$path" pull --ff-only --quiet 2>/dev/null; then
    failed+=("$name (pull failed — diverged or no upstream for '$branch')")
    continue
  fi

  after="$(git -C "$path" rev-parse HEAD 2>/dev/null)"

  if [[ "$before" == "$after" ]]; then
    current+=("$name [$branch]")
  else
    updated+=("$name [$branch] $before -> $after")
  fi
done

echo "=== Updated ==="
printf '%s\n' "${updated[@]:-(none)}"
echo
echo "=== Already current ==="
printf '%s\n' "${current[@]:-(none)}"
echo
echo "=== Skipped (uncommitted changes — not touched) ==="
printf '%s\n' "${skipped_dirty[@]:-(none)}"
echo
echo "=== Skipped (path not found locally) ==="
printf '%s\n' "${skipped_missing[@]:-(none)}"
echo
echo "=== Failed ==="
printf '%s\n' "${failed[@]:-(none)}"

if ! $INCLUDE_WORKTREES; then
  echo
  echo "Note: worktrees excluded by default (${WORKTREES[*]}). Re-run with --include-worktrees to sync them too."
fi
