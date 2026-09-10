---
name: prd
description: Write or amend the feature PRD from approved discovery or explicit PM direction. Use when the user says "write the PRD", "draft the PRD", or asks to amend product intent. The PRD is product intent, not implementation detail.
---

# PRD

Create or amend a PRD from approved discovery or explicit PM direction.

## Required reads
1. `../../../outputs/README.md`, then the feature `README.md`. If the feature
  workspace does not exist, initialize `outputs/<feature-name>/README.md`
  before drafting.
2. Approved discovery, or the explicit PM direction replacing it.
3. Existing PRD only when amending.
4. `references/prd-template.md`.

5. `../_shared/brain-grounding.md`, and the brain files it routes you to.

README links are routing candidates, not required reads. Do not load `INDEX.md`,
`config.json`, style guides, samples, corrections, repos, analytics, designs,
integrations, or agents unless the source exposes a gap.

## Ground in the brains (before drafting)
Run `../_shared/brain-grounding.md`. Required. Discovery's brain reads carry
forward — re-read only the feature note, hypotheses, and decisions, plus
anything the PRD asserts that discovery did not. Requirements use glossary
terms. Cite the brain files behind any requirement's rationale.

## Interrogate the business logic (before drafting)
Work `../_shared/business-interrogation.md` silently. Carry forward what
discovery already answered. What the evidence cannot answer goes into the PRD's
open-questions section — do not put it to the user as questions.

Requirements are the specific target: for each one, be able to say which
business outcome it serves. A requirement that traces to no outcome is either
missing its rationale or does not belong in the PRD — surface which.

## Write
- Preserve every template section and order. Mark N/A sections `N/A - [reason]`.
- Direct, concise, verdict first. No hype or invented precision.
- Keep product behavior in the PRD, not implementation or Figma detail.
- AC as Gherkin: happy paths, failures, permissions, stale/conflicting state,
  empty data, boundaries.
- Use `Unknown` or `TBD` for missing evidence. Do not invent owners, dates,
  metrics, targets, behavior, or decisions.
- Stamp version `vN`. Intent changes flow through the PRD first.
- Surface source conflicts for PM arbitration.

## Output
Default for new features:
`outputs/<feature-name>/prd/<feature-name>-prd.md`, with the version stamped at
the top. For historical features, follow the README.

After writing, report the artifact and unresolved items, then stop — do not roll
into the spec in the same turn. Do not ask for approval.
