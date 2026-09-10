# PRD AI sections (load only for AI features)

Paste these into the PRD when the discovery gate answered Yes — including the
"we consume an upstream model" case. Skip this file entirely for deterministic
features; that is the point of keeping it separate.

`Model-Quality Metric` belongs under `Success Metrics`, after the Guardrail
Metric. `AI Behavior and Acceptance` is its own top-level section, placed after
`Data and Analytics`.

Thresholds, per-band routing, failure-mode behavior, and versioning are NOT
here — they belong to the spec's `AI Behavior Contract`. Keep each fact in one
artifact so the two cannot drift.

---

##### **Model-Quality Metric: [Name]**

<!--
  REQUIRED when this feature has AI behavior; delete the whole block when it does not.
  A model-quality metric is not a product KPI. It answers: "is the output good
  enough to ship?" A feature can hit every adoption target and still be
  unshippable because the model is wrong too often, or wrong in the costly
  direction. State the direction that costs more, and hold the bar there.
-->

- **Measure:** [Precision / recall / F1 / exact-match / groundedness / win-rate vs. baseline / human-agreement rate]
- **Baseline:** [Current system, human, or naive-heuristic score, or `Unknown - not yet measured`]
- **Ship bar:** [The number below which we do not launch]
- **Costlier error direction:** [False positive or false negative — and what it costs in this workflow]
- **Measured on:** [Eval set name + size + how it was sampled. `TBD` is a blocker, not a gap.]

## AI Behavior and Acceptance

<!--
  DELETE THIS ENTIRE SECTION if no model, score, ranking, generation,
  classification, or extraction affects what the user sees — including one
  produced by another team. Otherwise every row is required; `Unknown` and
  `TBD` are legal values, invented numbers are not.

  This section is PM-owned intent only. Confidence thresholds, per-band routing,
  failure-mode behavior, and versioning live in the spec's `AI Behavior
  Contract` — do not restate them here, or the two will drift apart and each
  will look authoritative.
-->

### Capability Framing

| Field | Value |
| --- | --- |
| AI role in this feature | [Decides / Recommends / Drafts / Ranks / Extracts / Classifies / Summarizes / **Consumes an upstream model output**] |
| Do we own the model | [We build it / We consume it and cannot change it / Both] |
| If consumed: owner + change notification | [Team, and how we learn it changed — `None` is itself a finding] |
| Automation level | [Human approves each / Human reviews sample / Human-on-the-loop. **Fully automated contradicts the standing domain constraint** that no machine-derived outcome affects a merchant without human review — if this feature needs it, raise it as a conflict, do not just select it.] |
| Cost of being wrong | [What the user, customer, or business loses on a bad output] |
| Error-cost ratio | [Roughly what one miss costs versus one false alarm. Without this the threshold is a guess, not a decision.] |
| Reversibility | [Can the user override the output? Note separately if the raw model output is immutable but its downstream effect is adjustable.] |

### Measurement Level

<!--
  Per-item accuracy and the accuracy a user experiences are different numbers
  whenever outputs roll up. 95% per-finding precision across 200 findings per
  merchant is not 95% at the merchant level. State both, or the bar measures
  something nobody experiences.
-->

| Field | Value |
| --- | --- |
| Model output measured at | [Item level — finding, document, row] |
| User experiences quality at | [Entity level — merchant, account, case — or `same as measured`] |
| Aggregation rule between them | [Max / any / weighted rollup — and who owns that rule. An undefined rollup is where correctness quietly fails.] |

### Human Corrections as Labels

<!--
  Where users correct model output in the course of their work, the feature
  produces ground-truth labels for free. This is usually the most valuable and
  most-ignored asset an AI feature creates. If corrections go nowhere, say so
  deliberately rather than by omission.
-->

| Field | Value |
| --- | --- |
| Do users correct output as part of the workflow | [Yes / No] |
| Captured where | [Event, table, or `Not captured` — which is a decision, not a gap] |
| Usable as eval labels | [Yes / No / Unknown — and who owns making them usable] |
| Known bias in what gets corrected | [e.g. decided items stop re-surfacing, so we never learn whether suppressed items were wrong. State it; do not silently retrain on a censored sample.] |

### Evaluation Commitment

| Field | Value |
| --- | --- |
| Eval set owner | [Name or TBD] |
| Blocks release | [Yes / No — if No, name who accepted that risk] |

<!-- Set design, sampling, and labeling detail belong in `ai-eval.md`. -->

### Failure Posture

<!--
  Which failure modes are real for this feature, and the product posture on
  each. The spec's AI Behavior Contract defines the exact system behavior;
  this is the PM decision about what is acceptable.
-->

- **Costliest realistic failure:** [Which one, and why it is worse than the others here]
- **Unacceptable at any confidence:** [What must never reach the user — becomes an invariant in the spec]
- **Posture when quality is uncertain:** [Abstain / show with warning / route to human / proceed anyway — and why]

### Governance and Explainability

<!--
  DELETE if the feature has no regulated or externally-reported output.
  Required where model-influenced decisions affect a customer, a merchant, or a
  regulatory report — accuracy alone is not the shipping bar in those contexts.
-->

| Field | Value |
| --- | --- |
| Decision affects an external party | [Yes / No — if yes, name them] |
| Explanation owed | [What the affected party or auditor must be able to see, or `None required`] |
| Decision records retained | [What, for how long, and where] |
| Fairness/consistency check required | [Across which segments, by what method, or `Not required` with reason] |
| Owner of that obligation | [Compliance contact or TBD] |

