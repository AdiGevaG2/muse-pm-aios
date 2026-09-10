# Greenlight Re-platforming Workspace

A complete, ready-to-open Claude Code workspace for the teammate PM doing
requirements work on re-platforming legacy Greenlight onto Unified Platform.
Full parity with the source `muse-ai-os` engine (same skills, agents, hooks,
rules), minus the accumulated Unified Platform brain content — her domain
starts as an empty scaffold. Self-contained: nothing here depends on
`muse-ai-os` at runtime, and nothing was written back into that workspace.

## How to hand this off

Share this entire folder and point her at `GETTING-STARTED.md` — a plain
step-by-step guide: run `./bootstrap.sh` first (checks prerequisites, clones
what it can), then open Claude Code and run `/setup`. Setup is conversational:
it explains what it's doing, does everything it can automatically, and only
pauses to ask for things only she can provide (GitHub access, Figma auth).

## What's in this folder

- `GETTING-STARTED.md` — the step-by-step guide to hand her, start to finish.
- `bootstrap.sh` — prerequisite check + best-effort repo clone, run before
  opening Claude Code.
- `CLAUDE.md`, `.claude/CLAUDE.md`, `AGENTS.md`, `OWNERSHIP.md` — the full PM
  workspace contract: response style, evidence rules, source-of-truth
  precedence, PRD drift handling. Identical to the source workspace's rules.
- `.claude/skills/` — every skill from the source workspace: `discovery`,
  `prd`, `spec`, `critique`, `mini-prd`, `ai-eval`, `analytics-plan`,
  `baseline-data`, `ingest`, `learn-feature`, `publish`, `retro`,
  `reverse-engineer`, `review`, `validation`, `weekly-update`, `wireframer`,
  plus `setup` (new, only in this package).
- `.claude/agents/` — `legacy-analyzer`, `spec-reconciler`, `target-mapper`,
  `verify`, `doc-critic`, `propagate`.
- `.claude/hooks/`, `.claude/settings.json` — the same guardrails (ask-gate,
  destructive-operation guard, secret guard, provenance guard, PRD-change
  guard) and permission defaults.
- `scripts/` — workspace validation and template tooling (`validate-workspace`,
  `validate-ai-readiness`, `validate-spec`, `verify-scope`, etc.), repointed
  from `unified-platform` to the `greenlight` domain.
- `org-brain/`, `domains/greenlight/second-brain/` — the same knowledge-base
  structure (context, decisions, glossary, hypotheses, ingestion,
  stakeholders), **empty**. No Unified Platform content copied in.
- `domains/greenlight/CLAUDE.md`, `INDEX.md`, `config.json` — domain router
  and standing config, reset for a fresh domain (all tool readiness marked
  `UNVERIFIED`, no stakeholder names carried over).
- `outputs/` — feature-work root, with the same initialization contract as
  the source workspace (`outputs/README.md`).
- `docs/github-setup.md` — Greenlight repo access steps. Repo URL confirmed:
  `https://github.com/g2webservices/greenlight`. Access still needs to be
  granted by the repo/org admin.
- `docs/figma-integration.md` — Figma connector setup + the Unified Platform
  design-system repo details, for pixel-perfect prototypes of the
  replacement UI.
- `docs/greenlight-context.md` — confirmed: Greenlight is a fourth legacy
  platform being replaced, distinct from MerchantView/WebShield/Single
  Platform. No Figma file exists for Greenlight itself.
- `repos/` — created by `/setup` when it clones the Greenlight and/or
  design-system repos; empty until then.

## What's intentionally different from the source workspace

- **No brain content.** `org-brain/` and `second-brain/` exist with the same
  folder structure but no facts, decisions, or history — those are Unified
  Platform's accumulated knowledge and don't transfer. Brain-grounding steps
  in skills will run against an empty base until she (or `/ingest`) populates
  it.
- **`config.json` reset.** All tool integrations (Mixpanel, Jira, Confluence,
  Figma, Looker, GitHub) show `UNVERIFIED` — none of the source workspace's
  verified connections carry over; she authorizes and verifies her own.
- **`OWNERSHIP.md` genericized.** Stakeholder names (Adi Geva, Alla
  Avgustinov, Dana Friedman) removed from the domain section — placeholders
  left for her to fill in.
- **No Jira/Confluence space configured.** `/publish` is present but has no
  destination wired — she sets her own space/project before using it.

## Still open

**GitHub access** — repo URL is confirmed
(`https://github.com/g2webservices/greenlight`), but she still needs the
repo/org admin to grant her access before `/setup` can clone it.
