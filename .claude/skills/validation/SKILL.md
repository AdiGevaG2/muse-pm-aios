---
name: validation
description: Validate implementation, Figma, tests, or release evidence against the approved feature spec. Use when the user says "validate", "check acceptance", "verify implementation", "compare build to spec", or asks whether a feature is ready.
---

# Validation

Validate evidence against the approved spec. This is acceptance validation, not
user research feedback collection.

**Scope boundary:** this checks whether the build matches the spec. Acceptance
results and artifact drift fail independently — keep them separate.

## Before you start
- Confirm active domain and feature name.
- Follow `../../../outputs/README.md`. If the feature workspace does not exist,
  initialize `outputs/<feature-name>/README.md`; otherwise read its README
  first.
- Read the spec path routed by the README; default for new features is
  `spec/<feature-name>-spec.md`.
- Read implementation/test/Figma evidence only as needed for the validation
  question.
- Do not load org/domain brains wholesale.

## Ground in the brains (before validating)
Run `../_shared/brain-grounding.md`, scoped tightly. The spec is what you
validate against — the brains do not override it. Read them for constraints a
build can violate without violating the spec's letter: `context/compliance.md`,
the relevant `ingestion/` pages, and the glossary for whether shipped UI uses
the domain's terminology. Anything you find that the spec omits is a finding,
not a pass/fail criterion.

## Process
1. Identify the spec version and acceptance criteria in scope.
2. Map evidence to AC IDs or behavior IDs.
3. Run or read the narrowest relevant checks: tests, screenshots, source paths,
   Figma frames, logs, or manual QA notes.
4. Classify each item: `Pass`, `Fail`, `Blocked`, or `Not checked`.
5. For failures, state the exact mismatch and owner: product/spec, design,
   implementation, data, or unknown.

## Two artifacts, two questions
This skill covers both; they fail independently, so keep them separate.

- **Acceptance validation** (`validation.md`) — does the built feature pass its
  acceptance criteria? Evidence mapped to `AC-###`, each marked `Pass`, `Fail`,
  `Blocked`, or `Not checked`. This is the default output.
- **Alignment report** (`alignment-report.md`) — do the downstream artifacts
  still match the spec after it changed? Fill
  `references/alignment-report-template.md`. Produce this when the spec has
  moved, when a PRD change was propagated, or before an external handoff — not
  on every run.

An artifact set can be perfectly aligned around a spec the build does not meet,
and a build can pass every AC while Confluence and Jira describe an older spec.
Do not let one verdict stand in for the other.

## Output
Default for new features:
- `outputs/<feature-name>/validation/<feature-name>-validation.md` — acceptance
  results.
- `outputs/<feature-name>/validation/<feature-name>-alignment-report.md` — only
  when a drift check was actually run.

For historical features, follow the README. If no durable artifact is needed,
return a concise validation summary in chat.

## Stop Conditions
- On product ambiguity: take the most likely reading, validate against it, and
  record the ambiguity as a finding. Do not stop to ask.
- Stop on external writes unless explicitly approved.
- Do not rewrite PRD or spec during validation; propose amendments instead.

## Folder resources
- `references/alignment-report-template.md` — the drift-check template.
- `corrections/` — if it holds entries, apply them; empty is normal (see `../_shared/corrections.md`).

## Evidence
Show the evidence reviewed: command output summary, source paths, test names,
screenshots/Figma references, or artifact paths. Mark anything not checked.