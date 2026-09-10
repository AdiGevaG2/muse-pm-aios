# Worked example — an inherited-model feature

A filled example, not a template. Read it to see what "good" looks like, then
work from the blank templates. The feature is fictional but the shape is the
common enterprise one: **the model belongs to another team, and the feature
merely displays its output.** That shape is the one most often missed, because
it does not feel like AI work.

Scenario: a merchant-risk product surfaces machine-generated `Severity` on scan
findings. Analysts triage each finding and record a Decision. The scanning team
owns the model; this feature owns the review workflow.

---

## Why this is an AI feature at all

The team building the review screen writes no model code. They still own:

- whether an analyst can tell a machine judgment from a human one
- what happens when the scanner's behavior shifts under them
- how per-finding errors accumulate into a merchant-level verdict
- whether analyst corrections are captured or thrown away

None of that is the scanning team's problem. All of it is a product decision.
The discovery gate's first question is deliberately worded to catch this:
*whether we build it or inherit it*.

---

## Discovery gate — filled

| Question | Answer |
|---|---|
| Does a model affect what the user sees, built or inherited? | Yes |
| Which step | `Severity` on each finding, authored upstream by the scanner |
| Do we own that model, or consume it? | We consume it and cannot change it |
| What does a wrong output cost? | A wrong High wastes ~10 min of analyst review. A wrong Low means a real risk is never looked at, which is the loss the product exists to prevent. |
| Which wrong direction is worse, and by what ratio? | Missing a real risk. Roughly one miss ≈ 20 false alarms, from the analyst-hour cost versus a single escalated incident. |
| Ground-truth data exists? | Yes, implicitly — every analyst Decision is an adjudication of a Severity |
| Do users correct output as part of their work? | Yes. Decisions are recorded per finding. Today they go to the audit log only. |

### Upstream model table

| Question | Answer |
|---|---|
| Whose model, can it change without telling us? | Scanning team. **No notification path exists** — we would learn from a shift in analyst correction rates. That absence is the finding. |
| Its measured quality, if known | Vendor case study cites ~95% precision. Never measured on our merchant mix or our Severity bands. Treat as `Unknown` for our use. |
| How its errors reach our user | Directly. Severity drives default sort, so a wrong Low is not merely wrong — it is invisible, at the bottom of the queue. |
| What we do when its behavior shifts | TBD — no detection today. Open question for the PRD. |
| Do we aggregate its output? | Yes. Merchant Risk rolls up from finding Severity. Per-finding and per-merchant error rates differ substantially; see below. |

---

## The bar — filled

| Field | Value |
|---|---|
| Primary metric | Recall on High-severity findings |
| Why this metric | A missed real risk is the loss the product exists to prevent; a false alarm costs review time |
| Ship bar | Recall ≥ 0.95 on the High band |
| **Paired constraint** | Precision ≥ 0.55, **and** ≤ 40 findings/analyst/day |
| Baseline | Legacy manual review catches an estimated 0.88. `[hunch]` — confirm before treating as settled |
| Bar set by | [PM] on [date] |

The paired constraint is the part people skip. "Recall ≥ 0.95" alone is met by
marking everything High — which is why the alert-volume ceiling sits next to it.
The volume number came from asking analysts what a day's queue can hold, not
from the model.

### Measurement level — where this feature is unusual

| Field | Value |
|---|---|
| Model output measured at | Finding level |
| User experiences quality at | Merchant level |
| Aggregation rule | Merchant Risk = max(finding Risk). Owner: TBD — **undefined, and this is where correctness actually fails.** |

With `max` aggregation and ~200 findings per merchant, even a low per-finding
false-positive rate makes almost every merchant look High. Per-finding precision
of 0.95 is not merchant-level precision of 0.95. **Measure at the level the user
experiences, or the bar measures something nobody feels.**

---

## Human corrections as labels

| Field | Value |
|---|---|
| Users correct output as part of the workflow | Yes — every Decision |
| Captured where | `finding_decision_updated`, with severity and before/after risk |
| Usable as eval labels | Yes, with cleanup. Nobody owns this today. |
| Known bias | **Decided findings stop re-surfacing.** So we only ever observe corrections on findings the scanner still shows. Anything it quietly stopped surfacing is never adjudicated — a censored sample. Training on it without correcting for that would teach the model its blind spots are correct. |

That last row is the highest-value sentence in this example. The feature
generates free labels continuously; the persistence rule silently biases them;
and neither fact appears anywhere unless a template asks.

---

## What a good verdict reads like

> **Verdict: Mixed — clears aggregate, fails a segment.**
>
> Recall 0.96 (95% CI 0.93–0.98) against a bar of 0.95 — clears, though the
> interval's lower bound sits below the bar, so this is thinner than the point
> estimate suggests. Precision 0.58 against a floor of 0.55 — clears.
>
> But recall on the card-not-present cohort is 0.71 (n=38). That cohort is 12%
> of volume and the one with the highest incident cost. The aggregate hid it.
>
> Recommendation: ship to the other cohorts, hold card-not-present behind human
> review until a larger sample confirms or clears the gap. Not a bar change —
> a scope change. **PM decision: Pending.**

Note what the verdict does: reports the interval, not just the number; names the
segment that fails; and proposes a scope change rather than quietly relaxing the
bar to make the result pass.
