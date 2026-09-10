# PRD: {Feature Name}

## Document Metadata

| Field | Value |
| --- | --- |
| Feature | [Feature name] |
| Product Area | [Product area] |
| Release | [MVP / Phase] |
| Owner | [Owner or TBD] |
| Status | [Draft / In Review / Approved / Blocked] |
| Version | [vN] |
| Date | [Date or TBD] |

## Executive Summary

Write 2-4 concise paragraphs covering: what problem this solves, who for, what
the MVP introduces, why this scope is the right first step, and what outcome it
enables.

## Problem Statement

| Area | Description |
| --- | --- |
| Current gap | [Gap] |
| User pain points | [Pain] |
| Business impact | [Impact] |
| Risk if unsolved | [Risk] |
| Evidence | [Source-cited evidence or Unknown] |

## Goals

- [Goal]

## Assumptions

- [Assumption and validation need]

## Target Personas

| Persona | Description |
| --- | --- |
| [Persona] | [Need and role] |

## Scope

### In Scope - MVP

- [Capability]

### Out of Scope

- [Excluded item]

## User Journeys

### Primary Journey

Describe the main workflow in 5-8 steps.

1. [Start]
2. [Action]
3. [System response]
4. [Decision or validation]
5. [Outcome]
6. [Data / audit / reporting captured, if relevant]

Embed an editable, transparent draw.io SVG inline here, named
`{feature-name}-primary-journey`. Follow `../../_shared/diagram-drawio.md`.

## Acceptance Criteria

Write acceptance criteria as Gherkin `Given / When / Then`. There is no separate
Use Cases section — every primary use case and persona must appear here as at
least one scenario. Cover both:

* **Happy path** — one or more per primary use case / persona.
* **Unhappy flow / error handling** — invalid input, permission denied, failed
  save or recalculation, conflicting or stale state, empty data, and any
  boundary condition the user can hit.

IDs are stable. Retire an AC rather than renumbering the ones after it.

### AC-001: [Happy path — use case / persona]

**As a** [persona]
**I want to** [action]
**So that** [outcome]

```gherkin
Given [initial context or state]
When [the persona takes an action]
Then [the expected result occurs]
```

### AC-002: [Unhappy flow — error handling]

**As a** [persona]
**I want to** [be protected when the action fails or input is invalid]
**So that** [I do not lose work or act on incorrect data]

```gherkin
Given [a failure, invalid, or unauthorized condition]
When [the persona attempts the action]
Then [the system handles it safely and shows a clear recovery path]
```

[Repeat for every remaining use case, persona, and unhappy path.]

## Permissions, Roles, and Visibility

| Action / Capability | Role | Access | Notes |
| --- | --- | --- | --- |
| [Action] | [Role] | [Allowed / Denied] | [Notes] |

## UX and Product Behavior

| Area | Requirement |
| --- | --- |
| Entry point | [Requirement] |
| Main action | [Requirement] |
| Empty state | [Requirement] |
| Error state | [Requirement and recovery] |
| Success state | [Requirement] |
| Notifications / communication | [Requirement or N/A] |
| Accessibility / usability | [Requirement or N/A] |

## Data and Analytics

### Current Data

#### Mixpanel

[One or two sentences framing the legacy/current usage baseline for the surfaces
this feature touches. If the feature is net-new with no dedicated events yet,
name the closest existing proxy surfaces and say so.]

| Surface / Flow | Coverage | Usage (90-day) | Top Clients |
| --- | --- | --- | --- |
| [Surface or flow name] | [e.g. 91.5% (54/59) or N/A - reason] | [e.g. 10,306 or N/A - reason] | [Client A, Client B] |

> _*Source:* 90-day customer Mixpanel window; coverage is accounts with at least
> one tracked interaction, of the instrumented customer accounts. Note any scope
> limits (e.g. Mixpanel covers EC UI features only)._

### Success Metrics

#### **Objective (OKR)**

> [One-sentence outcome this feature drives, or TBD until the objective is set.]
> _*Note:* Targets are initial estimates and will be recalibrated after 30 days
> of post-launch data._

#### **KPIs**

##### **Primary Metric: [Name]**
- **Baseline:** [Value or TBD]
- **Target:** [Value or TBD]
- **Timeline:** [Timeline or TBD]

##### **Secondary Metric: [Name]**
- **Baseline:** [Value or TBD]
- **Target:** [Value or TBD]
- **Timeline:** [Timeline or TBD]

##### **Guardrail Metric: [Name]**
- **Baseline:** [Value or TBD]
- **Minimum Allowed:** [Floor the feature must not drop below — use **Maximum Allowed:** instead for ceilings such as error or leakage limits]
- **Timeline:** [Ongoing / Timeline]

### Required Events / Signals

| Event / Signal | Trigger | Key Properties | Purpose | Required for MVP |
| --- | --- | --- | --- | --- |
| [Event] | [Trigger] | [Properties] | [Purpose] | [Yes / No] |

## Risks and Mitigations

| Risk | Why It Matters | Impact | Likelihood | Mitigation |
| --- | --- | --- | --- | --- |
| [Risk] | [Reason] | [H/M/L] | [H/M/L] | [Mitigation] |

## Open Questions

| Question | Owner | Needed Before | Priority | Decision Type |
| --- | --- | --- | --- | --- |
| [Question] | [Owner or TBD] | [PRD / Spec / Launch] | [H/M/L] | [Product / Design / Engineering / Data / Security / Compliance] |

## Future Phases

| Phase | Purpose | Candidate Scope |
| --- | --- | --- |
| Phase 1 - MVP | [Purpose] | [Scope] |
| Phase 2 - Fast Follow | [Purpose] | [Scope] |
| Phase 3 - Expansion | [Purpose] | [Scope] |
