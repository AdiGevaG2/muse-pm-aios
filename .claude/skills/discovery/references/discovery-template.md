# Discovery Doc Template

Use this template for short discovery documents that are easy to read, easy to
scan, and easy to act on. This is the canonical discovery template; do not fall
back to an older "legacy compatibility" variant.

## Writing Rules

- Use plain language. Prefer common words such as `use`, `show`, `save`, and `change`.
- Keep sentences short. Aim for one idea per sentence and no more than 25 words.
- Rewrite dense sentences in direct subject-action-outcome language.
- Simplify wording without losing factual qualifiers or evidence boundaries,
  including confirmed versus unverified and current versus proposed behavior.
- Explain the user problem and product behavior before technical details.
- Keep the TL;DR to 3 to 5 short sentences.
- Use short bullets and small tables. Split or remove tables that are hard to scan.
- Define necessary technical terms the first time they appear. Remove jargon that
  does not help a product decision.
- Do not repeat the same point in several sections. Link the evidence to the
  decision it supports.
- Mark unknown facts as `TBD`, `Unknown`, or `N/A - [reason]`. Never hide
  uncertainty in complex wording.
- End each section with a clear takeaway, decision, risk, or question when the
  meaning is not obvious.

# Discovery: [Feature Name]

Document Name: [feature-name-stage-discovery, lowercase kebab-case]

Feature Name: [Feature Name]
Owner: [Owner]
Product: [Product]
Last Updated: [YYYY-MM-DD]

## TL;DR

### Executive Takeaway

[Write 3 to 5 short sentences. Explain the problem, the direction, why it
matters now, and the decision that is needed. Use plain language and one idea
per sentence.]

## Problem

### Pain Points

- [Pain point]
- [Pain point]
- [Pain point]

## Proposed Solution

### Feature Behavior

[Explain in simple language what should change for the user and any key rules
to keep in mind.]

### User Journey

1. [Entry point]
2. [Key user action]
3. [System response]
4. [Outcome]

Diagram (optional): embed an editable, transparent draw.io SVG inline, named
`{feature-name}-user-journey`. Follow `../../_shared/diagram-drawio.md`.

### Assumptions

List the existing capabilities, rules, or constraints that the proposed solution
relies on as its baseline.

- Verify each assumption against the current product, code, data, or another
  named source.
- Describe what exists today. Do not put new requirements or desired behavior in
  this section.
- State important limits, scope differences, or partial coverage.
- Mark unverified assumptions as `TBD` and add the decision or validation need to
  **Open Questions**.
- Remove assumptions that evidence proves false.

| Assumption | Current behavior or evidence | Caveat or validation needed |
|---|---|---|
| [Existing capability or rule the solution relies on] | [What exists today and how it was verified] | [Known limit, scope difference, or `None`] |

## Scope

### In Scope

- [In-scope item]
- [In-scope item]
- [In-scope item]

### Out of Scope

- [Out-of-scope item]
- [Out-of-scope item]
- [Out-of-scope item]

## Success Signals

- [What should get easier or faster]
- [What should become clearer or more accurate]
- [What should lead to fewer avoidable issues]

## Open Questions

- [Question that still needs a decision]
- [Question that still needs validation]
- [Question that still needs alignment]

## Appendix

### Persona / Target Audience

**Primary user:**
[Who this is mainly for]

**Secondary audience:**
[Who else is affected, if anyone]

**Job to be done:**
[What the person is trying to get done]

### Data

- Number of users affected: [Count or estimate]
- Current usage: [Volume, frequency, or adoption signal]
- CS tickets: [Ticket count, recurring themes, or trend]

#### Legacy EverC Mixpanel Analytics

Use the 90-day customer-only legacy EverC Mixpanel window when available (see
domain `config.json` → `mixpanel.customer_filter`). If a signal is not
instrumented, write `N/A - [reason]` instead of leaving it blank.

| Signal | Legacy EverC evidence | Discovery implication |
|---|---|---|
| Coverage | [Coverage percentage and covered customer count, or N/A with reason] | [What coverage means for problem size, migration confidence, or baseline quality] |
| Usage | [Usage volume or aggregate parent-workflow usage] | [What usage means for MVP priority, validation, or rollout] |
| Key clients | [Top clients using the legacy feature] | [Which clients or cohorts should inform validation or rollout] |

### Future Considerations

- [Future item]
- [Future item]
