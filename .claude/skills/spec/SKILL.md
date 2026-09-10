---
name: spec
description: Write or amend the feature spec from the PRD and relevant design/code evidence. Use when the user says "write the spec", "draft the build behavior", "reconcile with Figma", or "check spec vs design". Resolves mismatches in the artifact, escalating only PRD drift.
---

# Spec + Figma Reconcile

Write the build-behavior spec from the PRD. Reconcile against Figma or code only
when the feature README or user routes you there.

## Before you start
- Confirm active domain and feature name.
- Follow `../../../outputs/README.md`. If the feature workspace does not exist,
   initialize `outputs/<feature-name>/README.md`; otherwise read its README
   first.
- Read the PRD path routed by the README; default for new features is
   `prd/<feature-name>-prd.md`.
- Read only relevant design, context, or source evidence.
- Do not load org/domain brains wholesale.

## Ground in the brains (before drafting)
Run `../_shared/brain-grounding.md`. Required. At this stage it is mainly
terminology and constraints: the glossary governs the spec's terms, and
`context/compliance.md`, `context/platform.md`, and the relevant `ingestion/`
pages carry constraints that belong in build behavior. Cite the files you used.

## Do not re-interrogate the premise
`/prd` already ran `../_shared/business-interrogation.md`. Product intent is
settled — do not reopen it, and do not run that pass again here. The single
quality pass for this stage is the clarify pass in step 2, which folds in the
behavior-level sense-check (does each behavior serve its requirement, do edge
cases and volumes hold up arithmetically, would a user of this flow get the
outcome the PRD promises).

## Steps
1. **Write the spec** using `references/spec-template.md` for shape. Stamp the
   PRD version/source. Mark unresolved requirements inline with
   `[NEEDS CLARIFICATION: ...]` rather than guessing.
2. **Clarify — one pass, covering both ambiguity and sense.** Run
   `references/clarify-checklist.md` against the draft: scan PM-owned categories
   (functional scope, domain concepts, UX flow, edge cases, business rules,
   terminology, completion signals, analytics coverage), and while scanning also
   sense-check each behavior against its requirement — does it serve that
   requirement, do the edge cases and volumes hold up arithmetically, would a
   user of this flow get the outcome the PRD promises.

   Pick the up-to-5 highest-impact items the pass surfaces and resolve each one
   **in the artifact** — take the most reasonable reading, encode it into the
   spec, and mark it `ASSUMED:` so the PM can override in review. Do not put
   these to the user as questions (`../../../CLAUDE.md` → Act, Don't Ask). This
   step is never skipped, even in Quick mode — an unresolved ambiguity here
   becomes a wrong artifact, not a formatting gap. Leave a
   `[NEEDS CLARIFICATION: ...]` marker only where no reasonable reading exists
   at all.

   **Silence vs. contradiction.** This pass handles gaps the PRD left open —
   the PRD says nothing, you take the most reasonable reading and mark it
   `ASSUMED:`. It does not cover cases where the PRD says one thing and the
   evidence says the opposite. That is PRD drift: stop and put it to the PM
   (`../../../CLAUDE.md` → PRD Drift). Never bury a contradiction of stated
   intent as an assumption — an `ASSUMED:` line reads as "the PRD was quiet
   here," and using it to paper over a conflict hides the one thing the PM
   needed to see. Engineering-only categories
   (performance/scale targets, hosting, language/storage) are explicitly out of
   scope — those belong to the target repo's own technical planning, not this
   spec.
3. **Reconcile when routed** — compare against Figma or code only when the user
   asks or the README routes there. Delegate to `spec-reconciler` for large or
   high-stakes Figma comparison. It does not decide which side is right.
4. **Arbitrate the mismatches yourself.** Neither side is automatically ground
   truth, but deciding between them is not a PM question
   (`../../../CLAUDE.md` → Never hand the PM a technical choice). For each
   mismatch, pick the side that better serves the PRD requirement, write it into
   the spec, and mark it `ASSUMED:` with the losing side named so the PM can
   flip it in review. List the calls you made in the closing report.

   Escalate exactly one class: a mismatch that contradicts **stated product
   intent** in the PRD. That is PRD drift — stop and put it to the PM in the four
   lines `../../../CLAUDE.md` → PRD Drift specifies. Layout, spacing, copy,
   component choice, ordering, and states the PRD left open are yours to decide.
5. **Route requirement changes through the PRD.** Cosmetic/design-only fixes can
   update Figma or the spec directly.

## Scope boundary (stop here, do not draft plan.md/tasks.md)
This skill produces `spec.md` only — the dev-handoff artifact. It deliberately
does not draft an implementation plan or task breakdown; the target repo's own
engineering-owned tooling (its own SpecKit `/plan`, `/tasks`, or equivalent)
starts fresh from this spec. Do not draft technical context, architecture, or
task lists here even in outline form — that authority belongs to engineering,
not to this skill.

## Output
Default for new features:
`outputs/<feature-name>/spec/<feature-name>-spec.md`.
If reconciliation happens, write the routed validation artifact or a concise
reconcile section. For historical features, follow the README.

## Folder resources (read these)
- `references/spec-template.md` — the spec template to fill (see Step 1).
- `references/spec-analytics-sections.md` — the two analytics sections; load
  only when the feature emits events.
- `references/clarify-checklist.md` — the clarify pass to run (see Step 2).
- `references/figma-deltas-template.md` — structure for `reconcile-notes.md`
  (see Step 3).
- `../../../domains/<domain>/INDEX.md` — routes domain context.
- `../../../domains/<domain>/config.json` — tool IDs and approval defaults.
- `corrections/` — if it holds entries, apply them; empty is normal (see `../_shared/corrections.md`).

## Run mode (standalone)
Default to Quick; do not ask. Follow `../_shared/run-mode.md`.

## Evidence on completion
Do not just claim done. Show the artifact: the file path written, the actual
query result / figures, the diff, or the mismatch/gap list — whatever this stage
produced. Reviewing the evidence must be faster than re-doing the check. This
catches silent failures (a stage that "ran" but produced nothing usable).
