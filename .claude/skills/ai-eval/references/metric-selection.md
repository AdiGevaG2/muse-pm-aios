# Metric Selection and Reading Results

Reference for `/ai-eval`. Load when choosing a metric or interpreting a run.
This is judgment guidance, not a formula sheet.

## Precision and recall are one dial, not two choices

Before picking anything: **precision and recall are not independent.** They sit
on one curve, and you slide between them by moving a threshold — at zero model
cost. So a bar naming only one of them is not a bar.

"Recall >= 0.90" is trivially satisfied by flagging everything. Always pair it
with the constraint that makes it real:

> Maximize recall **subject to** precision >= 0.60
> — or, more usable in an operational workflow —
> Maximize recall **subject to** no more than N alerts per analyst per day.

The workload ceiling is usually the better second constraint, because analysts
feel alert volume, not precision. Get the ratio from the PRD's error-cost field:
if one missed case costs roughly twenty false alarms, that ratio *is* where the
threshold belongs.

## Pick the metric from the costlier failure

Given that pairing, name which side of the dial you are protecting. Ask which
mistake hurts more, then hold the bar there.

| The costly failure | Metric to hold | Typical shape |
|---|---|---|
| Acting on something that wasn't real | **Precision** | Analyst wastes time; user trust erodes on false alarms |
| Missing something that was real | **Recall** | Risk escapes; compliance exposure; the thing you exist to catch |
| Both roughly equal | **PR-AUC** across thresholds, or a cost-weighted F-beta | Rare — usually one dominates. Avoid plain F1 on imbalanced data: it ignores true negatives and is not comparable across different base rates. |
| Output must match a known answer | **Exact match / accuracy** | Extraction, classification with one right answer |
| Output must be supported by a source | **Groundedness / citation accuracy** | Summarization, RAG, anything generative over documents |
| No single right answer exists | **Human preference / win-rate vs. baseline** | Drafting, ranking, open generation |
| Replacing a human judgment | **Agreement with human labelers** | Compare to inter-labeler agreement, not to 100% |

**In risk, compliance, and fraud contexts, recall usually dominates** — a missed
true risk costs more than a reviewed false one. But say it explicitly rather
than assuming; a workflow already drowning in alerts may genuinely be
precision-bound, and the analysts will tell you which.

## A bar without a baseline is unreadable

85% means nothing alone. Against these baselines it means three different
things:

- Humans do 70% → strong, ship it.
- Current rules do 84% → you added cost for one point.
- Humans do 97% → do not ship.

If no baseline exists, establishing one is the first task. Never write a bar
without the comparison next to it.

**Ceiling check:** low labeler agreement caps what any model can be shown to
achieve, so measure it before setting a bar. Two cautions:

- **Use kappa, not raw percent agreement.** On a skewed task — say 10%
  positives, normal for finding triage — two labelers guessing at the base rate
  agree about 82% of the time by chance alone. Raw agreement of 80% there is
  *worse than chance*. Use Cohen's kappa (two labelers), Fleiss' kappa (more),
  or Krippendorff's alpha.
- **Agreement is a soft ceiling, not a hard one.** A model scored against an
  *adjudicated* label — several labelers reconciled — can legitimately beat
  pairwise agreement, because adjudication removes noise a single labeler has.
  Say which you scored against.

When agreement is genuinely low, the options are: sharpen the task definition,
adjudicate to a consensus label, add labelers per item, or accept that the
ceiling is low and set the bar under it. Fixing the model is not on that list.

## Aggregates hide the failures that matter

Always break down further than the headline number:

- **By segment** — 92% overall and 61% for one customer cohort is not one
  product. Segment gaps are the most common post-launch AI surprise.
- **By direction** — report the costlier-direction metric separately. An F1 that
  clears the bar can be hiding a recall collapse.
- **By confidence band** — if the model is wrong mostly at low confidence, raise
  the abstain threshold and the product works. If it is wrong at high
  confidence, thresholds cannot save it and the feature needs rethinking.

Confidently wrong is a categorically worse failure than uncertain and wrong.
Separate them in every report.

## Set design

- **Held out means held out.** A set used for tuning cannot support a ship
  decision. Keep two sets and say which is which.
- **Repeated looks leak too.** Checking the held-out set after every prompt
  iteration tunes on it through selection, even though you never "tuned on it".
  Either keep a third set touched only for the final call, or budget the number
  of looks and say how many you spent.
- **Count positives, not rows.** For rare events the binding constraint is how
  many positive cases the set contains. 300 cases at a 2% base rate gives six
  positives and a recall estimate worth nothing. Oversample positives and say
  you did.
- **Size:** a few dozen cases catch gross failures; a few hundred are needed
  before small differences mean anything.
- **Report an interval, not just a point.** Put a 95% confidence interval
  (Wilson, or bootstrap) next to every number. A 3-point gap on 40 cases is
  noise, and the interval is what makes that visible instead of arguable.
- **Split by time or entity, not at random**, whenever rows are related. Several
  findings from one merchant, or a set spanning a change to the upstream model,
  leak across a random split and flatter the result. Split by merchant, or
  train-before / test-after.
- **Composition:** real traffic tells you the average case; curated hard cases
  and adversarial cases tell you the tail. Ship decisions die in the tail.
  State the ratio.
- **Freshness:** a set drawn from last year's traffic measures last year's
  product. Note the window.

## Reading a result honestly

- A single run is a point estimate. On a small set, re-running with a different
  sample can move the number more than a prompt change does.
- **Regression matters more than absolute score** once shipped. Same set, same
  bar, every prompt or model change — that is what catches drift.
- Ten concrete wrong outputs are worth more to the PM than one percentage. Read
  the failures; look for whether they cluster. Clustered failures are often
  fixable by narrowing scope or raising a threshold. Scattered failures usually
  are not.

## The bar is a product decision

Engineering can move a number. Only the PM can decide what number is good
enough, because the answer depends on what a wrong output costs the user.

If a bar gets lowered to make a result pass, that is a product decision and
must be recorded as one, with who accepted the risk and why. Quietly moving a
bar is the most common way an AI feature ships broken with everyone believing
it passed.
