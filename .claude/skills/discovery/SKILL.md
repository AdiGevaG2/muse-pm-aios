---
name: discovery
description: Write or amend a feature discovery artifact from a business requirement and only the relevant evidence. Use when the user says "write discovery", "start discovery", or has a requirement ready to explore. Stops after the artifact, before the PRD.
---

# Discovery

Write the discovery artifact. Business requirement: $ARGUMENTS (ask for it if
not provided).

## Before you start
- Confirm active domain and feature name.
- Follow `../../../outputs/README.md`. If the feature workspace does not exist,
  initialize `outputs/<feature-name>/README.md` before drafting. Otherwise read
  the existing feature README first and preserve its routed paths.
- Read only routed inputs: requirement, relevant evidence, current PRD/spec if
  amending, and exact domain context from `INDEX.md`.
- Do not load org/domain brains wholesale.

## Ground in the brains (before drafting)
Run `../_shared/brain-grounding.md`. Required, not optional — discovery is the
stage that most often duplicates work the brains already hold. Read the feature
note and hypotheses first. Cite what you used in the artifact's evidence
section, and say so explicitly when the brains cover nothing.

## Interrogate the business logic (before drafting)
Run `../_shared/business-interrogation.md` in full. Discovery is the stage where
a weak premise is cheapest to catch — sense-check the problem, the value
mechanism, why now, and the cheaper path before you write a word of the
artifact. Do this silently — unresolved premise questions go into the artifact's
open-questions section, not to the user as questions.

## What to produce
Follow `references/discovery-template.md` for shape, but keep the artifact
decision-grade and scoped. It calls for:
- A TL;DR / Executive Takeaway (3–5 sentences: problem, direction, why now,
  decision needed).
- Pain points, persona/target audience, and a Data section anchored to the
  90-day customer-only Mixpanel window (`config.json` → `mixpanel`) — write
  `N/A - [reason]` rather than leaving a signal blank.
- What's changing vs. legacy or current behavior, with source-cited evidence IDs
  where available. Keep full evidence as a referenced appendix, not inline.
- Proposed solution (feature behavior + user journey), scope (in/out/future),
  success signals, and open questions.

## Handoff
After writing, report the artifact and stop there — do not roll straight into the
PRD in the same turn. Do not ask for approval; the PM reviews the file and says
what's next.

## Output
Default for new features:
`outputs/<feature-name>/discovery/<feature-name>-discovery.md`.
For historical features, follow the artifact path listed in the feature README.

## Folder resources (read these)
- `../../../domains/<domain>/INDEX.md` — routes domain context.
- `../../../domains/<domain>/config.json` — tool IDs and approval defaults.
- `corrections/` — if it holds entries, apply them; empty is normal (see `../_shared/corrections.md`).
- `references/discovery-template.md` — structure to fill.

## Run mode (standalone)
Default to Quick; do not ask. Follow `../_shared/run-mode.md`.

## Evidence on completion
Do not just claim done. Show the artifact: the file path written, the actual
query result / figures, the diff, or the mismatch/gap list — whatever this stage
produced. Reviewing the evidence must be faster than re-doing the check. This
catches silent failures (a stage that "ran" but produced nothing usable).
