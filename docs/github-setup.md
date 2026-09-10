# GitHub Access: Greenlight Repo

## Repo location

`https://github.com/g2webservices/greenlight` — confirmed as a fourth legacy
repo, distinct from the Unified Platform design-system repo and from
MerchantView/WebShield/Single Platform.

## Access steps

1. Confirm she has a G2 GitHub account under the `g2webservices` org.
2. Request read access (or the access level her work needs) to the Greenlight
   repo from the repo/org admin. This is a permissions grant on a shared
   system — someone with admin rights on that GitHub org has to do it, not
   something this workspace can perform.
3. Once granted, clone read-only for reference (mirrors this workspace's
   pattern for the UP design-system repo — clone locally, never push):
   ```
   git clone https://github.com/g2webservices/greenlight ~/vsCode/code-repos-git/greenlight
   ```
   (or into `./repos/greenlight` inside this workspace — `/setup` defaults to
   that path).
4. If the requirements work needs to reverse-engineer current Greenlight
   behavior from code (not just docs), point Claude Code's `/reverse-engineer`
   or `/legacy-analyzer` agent at the cloned path once it's local.

## Note on staleness

If she's using the clone as evidence for requirements work, re-pull before
relying on it if it's been more than a couple of days — legacy behavior
evidence goes stale the same way design-system state does.

**Need from you:** who to ask for GitHub access to `g2webservices/greenlight`
(repo/org admin contact) — not derivable from this workspace.
