# Spec analytics sections

Load only when the feature emits analytics events. Paste these two sections into
the spec between `## Error / Empty / Loading States` and `## Assumptions`
(events) and before `## Approval Readiness` (properties).

If the feature emits no events, omit both sections and say so in the spec rather
than leaving empty tables.

---

## Analytics Events

Events a product analyst would use to understand how this feature is used. Each
row must read standalone: `snake_case` verb_noun name, one-sentence description
of what happened and why it matters, exact trigger. Not QA, release-validation,
or deployment signals — those belong in a QA plan.

| Event | Description | Trigger | Key Properties | Business Purpose |
|---|---|---|---|---|
| [event_name] | [What happened and why it matters] | [Exact trigger] | [property1, property2] | [Decision or measurement it enables] |

## Analytics And Measurement Requirements

Property definitions and validation rules that engineering needs to implement
the events above.

| Property | Type | Required | Description | Example |
|---|---|---|---|---|
| [property_name] | string / number / boolean / enum / timestamp | Yes / No | [Description] | [Example] |

| Validation requirement | Reason | Owner |
|---|---|---|
| [Requirement] | [Reason] | Product / Data / Engineering |

Measurement design — metric definitions, grain, window, baselines, funnels,
segmentation, dashboards, and data governance — belongs to `/analytics-plan`
and its `analytics-plan.md`. Do not restate it here; the two would drift.
