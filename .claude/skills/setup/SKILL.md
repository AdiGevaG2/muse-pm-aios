---
name: setup
description: One-time guided setup for this Greenlight re-platforming PM workspace. Use when the user says "setup", "get started", "configure this workspace", or opens this folder for the first time. Walks through GitHub access, the design-system repo, and Figma auth conversationally, doing every step that can be automated and pausing only for things only the user can provide.
---

# Workspace Setup

This is a standalone Claude Code workspace for requirements work on the
Greenlight re-platforming initiative (Greenlight is a fourth legacy platform
being replaced by Unified Platform, alongside MerchantView, WebShield, and
Single Platform). Run this once, at first use.

Go step by step. Don't dump all steps at once — confirm each before moving on.
Do everything you can yourself; only stop and ask when the action requires
something only the user has (a credential, a URL, an auth click).

## Step 0 — Orient

Read `README.md` and `docs/greenlight-context.md` silently, then tell the
user in 2-3 sentences what this workspace is for and what setup will cover
(GitHub access to the Greenlight repo, cloning it, Figma connector auth,
confirming the skills are working). Ask nothing yet — just orient, then move
to Step 1.

## Step 1 — Greenlight repo access

Read `docs/github-setup.md`. The repo URL is confirmed:
`https://github.com/g2webservices/greenlight`.

- Attempt the clone into `./repos/greenlight`:
  `git clone --depth 1 https://github.com/g2webservices/greenlight ./repos/greenlight`.
- If it fails (auth error, 404), tell the user plainly what failed and that
  she needs access granted by the `g2webservices` org/repo admin before
  retrying — don't guess at fixes for permissions you don't control. Suggest
  re-running `/setup` once access is granted.

## Step 2 — Design system repo (for pixel-perfect prototypes)

Read `docs/figma-integration.md` for the repo details
(`https://github.com/evercompliant/g2rs-design-system.git`, read-only).

- Ask the user: does she want her own local clone of this repo now, or defer
  until she's actually building a prototype? Either answer is fine — act on
  it directly, don't re-ask later in the session.
- If now: clone read-only into `./repos/g2rs-design-system` yourself
  (`git clone https://github.com/evercompliant/g2rs-design-system.git`).
  Confirm it landed and note the key paths (`design-system/`, `src/`,
  `prototypes/`, `CONVENTIONS.md`).

## Step 3 — Figma MCP connector

This cannot be done on her behalf — it requires her own OAuth click.

- Tell her plainly: authorize the Figma connector via claude.ai connector
  settings (or `/mcp` in an interactive session), under her own account.
- Ask her to confirm once done (or to skip if she doesn't need Figma yet,
  since there's no Figma file for Greenlight itself — only relevant if she's
  building UP-styled prototypes for the replacement UI).
- Do not proceed to verify Figma tools work until she confirms she's
  authorized it — don't call any Figma tool speculatively.

## Step 4 — Verify the workspace is sound

Run `scripts/validate-workspace` yourself and report the result plainly (pass
or the specific failures). This checks the same structural rules the source
workspace enforces (required files present, domain wiring intact).

## Step 5 — Orient her on the full toolkit

This workspace has the complete skill set, not just the PRD chain:
`/discovery`, `/prd`, `/spec`, `/critique`, `/mini-prd` for requirements;
`/reverse-engineer` and `/learn-feature` for understanding existing
Greenlight behavior; `/analytics-plan`, `/baseline-data`, `/ai-eval` for
measurement; `/validation` for checking a build against spec; `/ingest` to
start populating her own domain knowledge base (currently empty — see
`domains/greenlight/second-brain/`); `/publish` once she's configured her own
Jira/Confluence targets (not done yet — `domains/greenlight/config.json` has
Jira/Confluence marked `UNVERIFIED`).

Ask which she wants to try first, or suggest `/mini-prd` as the lowest-
friction starting point for her first real Greenlight requirement. Do not
actually run one of these skills unless she gives you a real requirement to
work from — setup ends here, the workflow skills take over from whatever she
brings next.

## Step 6 — Close out

Summarize what's configured, what's still pending (e.g. Figma auth if
skipped, repo access if denied, Jira/Confluence not yet connected), and where
to find things (`docs/` for reference, `.claude/skills/` for the workflow,
`domains/greenlight/` for her knowledge base once she starts building it).
Tell her `/setup` is safe to re-run later if something didn't complete (it
should pick up wherever the TBD/pending markers are, not repeat completed
steps).
