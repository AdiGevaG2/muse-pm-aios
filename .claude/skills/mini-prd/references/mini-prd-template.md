# {Feature Name} — Mini PRD

**TL;DR:**
[One line: what's being built and why.]

<br>

## Problem and Goal

[1-2 sentences: what's broken/missing.]

Goal: [1 sentence: what success looks like.]

<br>

## Feature Behavior

**Prerequisite:** [condition that must hold before the flow starts, if any — omit if none.]

1. [Numbered happy-path steps, one action per step, ending in the outcome and confirmation.]

**[Named sub-choice, if the flow branches — e.g. "Option A vs. option B"]**
- [Option]: [what it does].
- [Option]: [what it does].

**Empty state** (omit this sub-block if there's nothing to specify)
- [expected behavior]

**Errors**
1. [Condition]: [result].
2. [Condition]: [result].

**Permissions** (if relevant)
- [Role]: [access].

**API** (if relevant)
- [Backward-compatibility or contract requirement, stated as a fact.]
- Assumption: [anything unverified about the contract] — confirm during spec.

<br>

Figma: [link] (omit this line if no design exists for this feature)
<br>

## Acceptance Criteria

**Scenario: [name]**
- Given [precondition]
- And [additional precondition, if needed]
- When [action]
- Then [observable, testable result]

[One scenario per distinct behavior. Fold a precondition or read-only check into an existing scenario's Given/And rather than writing a separate scenario for it.]

<br>

## Open Questions / Assumptions

- ASSUMED: [assumption] — or omit this section entirely if none.
