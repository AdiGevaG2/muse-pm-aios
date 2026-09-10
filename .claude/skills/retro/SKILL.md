---
name: retro
description: Learning loop. Distill corrections, precedents, arbitration decisions, and repeated agent errors from a feature into the brains. Use at feature close, or for "capture learnings", "run a retro", "what should we remember". Brain writes are approval-gated.
---

# Retro (learning loop)

Close the loop: turn this feature's corrections and decisions into durable
knowledge so the system doesn't start from zero next time. The brains are ground
truth for every agent — so learnings are PROPOSED and only written on approval.

## Before you start
- Confirm active domain + feature name.
- Follow `../../../outputs/README.md`. If the feature workspace does not exist,
  initialize `outputs/<feature-name>/README.md`; otherwise read its README
  first.
- Gather the raw material already produced during the flow. Read only what
  exists in the routed stage folders. Historical features may use flat files or
  older stage subfolders:
  - Human corrections across stages (where you overrode the agent).
  - Reverse-engineering escalations (ambiguities handed to a human).
  - Spec/Figma arbitration decisions and any reconcile notes.
  - Validation failures and their assigned owner.
  - Post-launch: baseline re-measurement vs. the target the PRD set.

## Steps
1. **Extract candidate learnings.** For each, classify:
   - `glossary` — a term used wrong / a new entity worth defining.
   - `context` — a durable fact, constraint, or system behavior discovered.
   - `decision` — a call made worth keeping as precedent.
   - `engine-tuning` — a skill/agent repeatedly produced the same wrong output
     (this edits a `SKILL.md`/agent, NOT the brain).
   - `eval-signal` — a real failure worth adding to a feature's eval set. Field
     failures are the highest-value eval cases there are; capture them while
     they are fresh rather than rediscovering them next release.
2. **Scope each learning.** Org-wide (applies to every domain) -> `org-brain/`.
   Domain-specific -> `domains/<domain>/second-brain/`. When unsure, default to
   domain (narrower). An org-brain write binds every domain, so call it out
   explicitly at the approval gate rather than folding it in with domain edits.
3. **Validate inferred learnings.** A "learning" is often an inference. Before it
   becomes brain ground truth, sanity-check it — optionally delegate to the
   `verify` agent to confirm it's supported, not a one-off. Mark shaky ones as
   tentative.
4. **Approval gate (hard).** Show the proposed brain edits as a diff — which file,
   what's added, at what scope. Write to the brains ONLY on approval. Never
   auto-write; a wrong learning corrupts every future feature.
5. **Engine-tuning suggestions go to a separate list** — they're recommendations
   to edit skills/agents, surfaced for you to action deliberately, not applied
   here.

## Rules
- Facts and durable decisions only. Don't record one-off preferences as
  precedent.
- Distill, don't dump — a learning is a tight entry, not the raw feedback.
- Keep the raw record too (below), so the distilled brain entry is traceable.

## Output
- `outputs/<feature-name>/retro/<feature-name>-retro-learnings.md` — the raw
  candidate list with classification + scope (the audit trail). Follow the
  feature README for historical features.
- On approval: appended entries in the target brain files (`glossary/`,
  `context/`, or `decisions/`).
- `outputs/<feature-name>/retro/<feature-name>-retro-engine-tuning.md` —
  suggested skill/agent improvements, if any.

## Evidence on completion
Show the proposed diff per target file before any brain write, and the artifact
path afterward. Report what was written versus what was left pending approval.
Never report a learning as captured while its approval is still outstanding.
