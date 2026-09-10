---
feature_name: [Feature Name]
artifact: analytics-plan
status: draft
version: 0.1
last_updated: [YYYY-MM-DD]
source_prd: [path]
source_spec: [path]
analytics_owner: [Owner]
product_owner: [Owner]
engineering_owner: [Owner]
data_sources: [Source system(s) / warehouse / event stream]
alignment_status: draft
---

# Analytics Plan: [Feature Name]

## Measurement Objective

**Decision supported:** [What launch, rollout, investment, or iteration decision this plan enables]  
**Primary success definition:** [What outcome defines success for this feature]  
**Guardrail failure definition:** [What negative outcome would trigger concern, rollback, or further investigation]  

[What we need to learn, prove, or monitor in order to support the decision above.]

## Hypotheses

| Hypothesis | Expected Behavior Change | Primary Metric | Guardrail Metric | Confidence |
|---|---|---|---|---|
| [Hypothesis] | [Expected user or system behavior change] | [Metric] | [Metric] | Low / Medium / High |

## Product Questions

| Question | Why It Matters | Launch Phase | Decision It Supports |
|---|---|---|---|
| [Question] | [Reason] | Before / During / After Launch | [Decision] |

## Metrics

| Metric | Role | Definition / Formula | Grain | Window | Segment | Baseline | Target | Source | Owner |
|---|---|---|---|---|---|---|---|---|---|
| [Metric] | North Star / Primary / Input / Guardrail / Diagnostic | [Definition or formula] | [User / account / session / event / order / day] | [7-day / 30-day / launch window / experiment window] | [Segment or All users] | [Baseline] | [Target] | [Source] | [Owner] |

## Analysis Design

| Analysis Method | Eligible Population | Exclusions | Primary Metric | Guardrail Metrics | Minimum Detectable Effect | Analysis Window | Decision Rule |
|---|---|---|---|---|---|---|---|
| [Experiment / holdout / pre-post / cohort / trend / rollout comparison] | [Population] | [Exclusions] | [Metric] | [Metric(s)] | [MDE] | [Window] | [Decision rule] |

## Events

| Event | Trigger | Description | Source | Platform | Required Properties | Property Types | Example Values | Identity Required | Required For MVP |
|---|---|---|---|---|---|---|---|---|---|
| [Event] | [Trigger] | [What the event captures] | [Client / server / warehouse / partner] | [Web / iOS / Android / API / backend] | [Property list] | [string, enum, boolean, number, timestamp] | [Example values] | [Anonymous / user_id / account_id / both] | Yes / No |

## Funnel / Workflow

| Step | Event | Eligibility | Success Definition | Drop-Off / Failure Signal | Conversion Window |
|---|---|---|---|---|---|
| [Step] | [Event] | [Who should enter this step] | [What counts as success] | [Failure or drop-off signal] | [Window] |

## Segmentation

| Segment | Definition | Why It Matters | Required For MVP |
|---|---|---|---|
| [Segment] | [Definition] | [Why this cut matters for decisions] | Yes / No |

## Dashboards / Reporting

| Dashboard / Report | Audience | Purpose | Cadence | Key Decisions Supported | Alert Threshold | MVP Required |
|---|---|---|---|---|---|---|
| [Dashboard / report] | [Audience] | [Purpose] | [Real-time / daily / weekly / launch review] | [Decision] | [Threshold] | Yes / No |

## Data Quality And Governance

| Governance Area | Requirement | Owner | Enforcement Method | MVP Required |
|---|---|---|---|---|
| Event Naming | [Naming convention and taxonomy requirement] | [Owner] | [Tracking plan review / schema registry / code review] | Yes / No |
| Schema Validation | [Required schema validation rule] | [Owner] | [Validation tests / contract checks / ingestion checks] | Yes / No |
| Identity Resolution | [Identity stitching and deduplication requirement] | [Owner] | [Identity rules / warehouse model / QA check] | Yes / No |
| Privacy / PII | [PII handling, redaction, or restriction requirement] | [Owner] | [Data policy / linting / access control / audit] | Yes / No |
| Consent | [Consent capture and enforcement requirement] | [Owner] | [Consent gate / tag manager rule / downstream filter] | Yes / No |
| Data Freshness | [Latency or refresh requirement] | [Owner] | [SLA / freshness monitor / pipeline alert] | Yes / No |
| QA | [Pre-launch and post-launch QA requirement] | [Owner] | [QA checklist / test cases / production validation] | Yes / No |

## Risks And Limitations

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| [Risk or limitation] | [Impact on decisions, measurement, or trust] | [Mitigation] | [Owner] |

## Open Questions

| Question | Owner | Needed Before | Priority |
|---|---|---|---|
| [Question] | [Owner] | [Launch / instrumentation / experiment / review] | High / Medium / Low |
