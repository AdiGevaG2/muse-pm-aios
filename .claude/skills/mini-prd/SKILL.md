---
name: mini-prd
description: Write a short (1-2 page) requirement doc for a dev handoff, skipping discovery/PRD ceremony. Use when the user says "mini prd", "quick requirement doc", "short spec for dev", or the ask is small/well-understood enough that full discovery is overkill. Not /prd, which carries personas, scope, and metrics for larger features.
---

# Mini PRD

A short, dev-ready requirement doc for small or well-understood asks. Replaces
`/prd` + `/spec` for asks that don't warrant either in full — this doc goes
straight to a developer.

## Required reads

1. `../../../outputs/README.md`, then the feature `README.md` if it exists. If
   the feature workspace does not exist, create
   `outputs/<feature-name>/prd/` when writing the artifact — do not require a
   full README init for this doc.
2. `second-brain/context/features/<feature-name>.md`, only if it already
   exists. Do not run full brain-grounding — this is a lighter touch than
   `/prd`.
3. `references/mini-prd-template.md`.

## Write

- Preserve the template's sections and order: TL;DR, Problem and Goal, Feature
  Behavior, Acceptance Criteria, Open Questions / Assumptions. Drop "Open
  Questions / Assumptions" entirely if there is nothing to put in it — don't
  leave it empty with a placeholder. Separate top-level sections with a `<br>`
  line, matching the template.
- Every section as short as possible. No irrelevant detail, no boilerplate
  sentences that restate the section heading.
- Feature Behavior carries the weight a full PRD would defer to `spec.md`:
  numbered happy-path steps (one action per step, ending in the outcome and
  confirmation), a named sub-choice block if the flow branches, then Empty
  state, Errors, Permissions, and API as their own labeled sub-blocks. Include
  a sub-block only when there is an actual specification or requirement to
  state for it — omit it entirely rather than writing "N/A" or "no separate
  empty state." An omitted sub-block is not a gap to flag in Open Questions;
  it means the case doesn't need distinct handling. State what the system
  actually does in each case that does apply; a dev should not have to infer
  it. State a leading **Prerequisite** before the numbered steps if one gates
  the whole flow.
- Feature Behavior opens with the Figma link, if one exists for this feature
  (check discovery/PRD/README before asking; omit the line entirely if none).
- Domain terms that name a product capability or mode (e.g. Monitoring,
  Onboarding) are capitalized as proper nouns throughout the doc.
- Register throughout: plain professional document prose. Not spec-speak
  (clause-stacked sentences, "system shall"), not casual (Slack tone, arrows
  like "→" standing in for verbs). Short declarative sentences, complete and
  grammatical, the way a requirements doc reads — not the way a chat message
  reads.
- One idea per sentence. Split any bullet that needs "and" more than once
  into sub-bullets or a short list. Lead with the actor or condition ("User
  enters X" / "If Y occurs, Z happens"), not a wall of clause after clause.
- TL;DR: one line. Problem and Goal: state the gap in 1-2 sentences, then the
  goal as its own sentence starting "Goal:" — not one dense comma-chained
  sentence, and not an informal aside.
- Errors: numbered list, each item one sentence — condition, then result
  ("X blocks creation and shows Y"), not "X: blocked, Y shown" or "X → Y"
  shorthand.
- Acceptance criteria are Given/When/Then scenarios, one per distinct
  behavior — not a checkbox list. Format:
  ```
  **Scenario: <name>**
  - Given <precondition>
  - And <precondition, if needed>
  - When <action>
  - Then <observable, testable result>
  ```
  Fold a precondition or a read-only display check into an existing
  scenario's Given/And rather than writing a separate scenario for it —
  prefer fewer scenarios with more Ands over many single-purpose scenarios.
  Then is the check, not a re-narration of the mechanism already described in
  Feature Behavior. Ban vague terms ("works correctly", "handles errors
  gracefully").
- Use `ASSUMED:` for anything not verified rather than asking or guessing
  silently into a stated fact.
- No persona section, no scope-in/scope-out table, no metrics/analytics plan —
  those stay in `/discovery` + `/prd` for features big enough to need them.

## Output

`outputs/<feature-name>/prd/<feature-name>-mini-prd.md`.

After writing, report the artifact and any open items, then stop.
