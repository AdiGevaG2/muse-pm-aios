---
feature: "[feature-name]"
document_name: "[feature-name]-ai-eval"
artifact: ai-eval
status: draft
version: v0.1
last_updated: [DATE]
spec_source: ../spec/[feature-name]-spec.md
prd_source: ../prd/[feature-name]-prd.md
---

# AI Eval: [FEATURE NAME]

## Decision This Informs

> [The exact decision. "Ship / do not ship the auto-triage suggestion at the
> MVP bar." An eval with no attached decision is a metrics exercise.]

**Verdict:** [Clears / Below bar / Mixed — clears aggregate, fails a segment / Not evaluable / Not yet run]

## The Bar

| Field | Value |
|---|---|
| Primary metric | [Precision / recall / PR-AUC / exact-match / groundedness / human-agreement / win-rate] |
| Why this metric | [Which failure it protects against — tie to the costlier direction] |
| Ship bar | [Number] |
| Baseline | [Current system / human performance / naive heuristic, or `Unknown - not yet measured`] |
| Costlier error direction | [False positive or false negative, and what it costs here] |
| Paired constraint | [The floor or ceiling that makes the bar real — e.g. precision >= X, or <= N alerts/analyst/day. A single-sided bar is not a bar.] |
| Bar set by | [PM name] on [date] |

<!--
  A bar without a baseline is unreadable. 85% precision may be excellent or
  unshippable depending on what a human already achieves. If the baseline is
  unknown, establishing it is the first task, not a footnote.
-->

## Eval Set

| Field | Value |
|---|---|
| Set name / version | [Identifier — results are meaningless without it] |
| Size | [N cases] |
| Positive cases | [N — for rare events this, not total size, decides whether recall is measurable] |
| Sampling method | [Random from production / stratified by segment / curated / mixed] |
| Composition | [e.g. 60% real traffic, 25% hard cases, 15% adversarial] |
| Segment coverage | [Which customer/data segments are represented, and any known gaps] |
| Held out from tuning | [Yes / No — if No, this cannot support a ship decision] |
| Ground truth by | [Who labels] |
| Disagreement rule | [How labeler conflicts resolve] |
| Inter-labeler agreement | [Value or `Not measured` — low agreement means the task itself is ambiguous] |
| Location | [Path or system] |

## What Was Tested

| Field | Value |
|---|---|
| Model ID | [Exact version, e.g. `claude-opus-5`. `latest` is not a version.] |
| Prompt version | [Identifier + location] |
| Retrieval / context config | [If applicable] |
| Run date | [DATE] |
| Run by | [Name] |

<!-- Without these, the result cannot be reproduced or re-checked later. -->

## Results

| Metric | Result | 95% CI | Bar | Status |
|---|---|---|---|---|
| [Primary] | [Value] | [low-high] | [Bar] | [Pass / Fail] |
| [Paired constraint] | [Value] | [low-high] | [Floor or ceiling] | [Pass / Fail] |
| [Secondary] | [Value] | [low-high] | [Bar or n/a] | [Pass / Fail / Informational] |

<!--
  A result whose interval straddles the bar has not cleared it — it is
  unresolved, and the honest verdict is "needs a bigger set", not "Pass".
  A recall/precision number with no paired constraint is not a bar: recall
  alone is satisfiable by flagging everything.
-->

### By Segment

<!-- An aggregate pass can hide a segment failure. Break down where it matters. -->

| Segment | N | [Primary metric] | Status | Notes |
|---|---|---|---|---|
| [Segment] | [N] | [Value] | [Pass / Fail] | [Notes] |

### Invariant Violations

<!-- Outputs that must never occur, at any confidence. Any hit blocks release. -->

| Invariant | Violations | Blocking |
|---|---|---|
| [e.g. never fabricates a citation] | [Count] | [Yes / No] |

## Failure Examples

<!--
  Required when the verdict is anything but Clears. Percentages tell the PM
  whether to worry; examples tell them what to do. Include the model's
  confidence — confidently wrong is a different product problem than uncertain
  and wrong.
-->

| # | Input (abbreviated) | Expected | Model output | Confidence | Failure type |
|---|---|---|---|---|---|
| 1 | [Input] | [Expected] | [Actual] | [Score] | [Confidently wrong / fabrication / miss / refusal] |

**Pattern observed:** [Do the failures cluster? A clustered failure is often
fixable by scope or threshold; a scattered one usually is not.]

## Recommendation

<!-- Recommend. Do not decide. The bar and the ship call belong to the PM. -->

**Recommendation:** [Ship as specified / Ship narrowed to X / Ship with human
review / Raise threshold and abstain more / Do not ship / Build the set first]

**Reasoning:** [2-4 sentences tied to the numbers above.]

**If the bar is not met, the options are:**

| Option | What changes | Cost | Residual risk |
|---|---|---|---|
| [Option] | [Change] | [Cost] | [Risk] |

**PM decision:** [Pending / Decided — what, by whom, on what date]

<!--
  If the bar was lowered to make this pass, that is a product decision and must
  be recorded here with who accepted the risk. Silently moving a bar is the
  single most common way an AI feature ships broken.
-->

## Post-Ship Monitoring

<!--
  Every offline eval decays. A rigorous pre-ship number with no production
  counterpart means quality is unobserved from launch onward — the most common
  way an AI feature degrades without anyone noticing.
  Keep this to what will actually be watched.
-->

| Signal | Where it comes from | Who watches | Threshold that triggers action |
|---|---|---|---|
| Human correction/override rate | [Event] | [Owner] | [Value or TBD] |
| Output volume vs. expected | [Event] | [Owner] | [Value or TBD] |
| Score distribution shift | [Source] | [Owner] | [Value or TBD] |
| Upstream model changed | [Notification path, or `None` — which is the finding] | [Owner] | [Any change] |

**Re-run this eval when:** [prompt change / model version change / retrieval or
input schema change / upstream model change / cadence]. Keep this list in one
place; the spec's `Change requires re-eval` field points here.

## Unresolved

| Question | Owner | Needed before | Priority |
|---|---|---|---|
| [Question] | [Owner or TBD] | [Milestone] | [High / Medium / Low] |
