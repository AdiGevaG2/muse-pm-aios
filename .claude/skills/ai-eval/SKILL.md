---
name: ai-eval
description: Define, run, or review an eval for a feature's AI behavior — accuracy bar, eval set, whether the model clears it. Use for "eval", "is the model good enough", "accuracy bar", "precision/recall", "build an eval set", or whether AI output is shippable. Not /validation, which checks build against spec.
---

# AI Eval

Decide whether a feature's AI behavior is good enough to ship, and make that
judgment reproducible. Target: $ARGUMENTS (a feature name, an eval question, or
a model/prompt change). If empty, ask which feature's AI behavior is in scope.

**`/validation` asks "did we build the spec?" This asks "is the output good
enough?"** Those fail independently: a feature can match the spec exactly and
still be unshippable because the model is wrong too often. Do not merge them.

## Before you start
- Confirm active domain and feature name.
- Follow `../../../outputs/README.md`. If the feature workspace does not exist,
  initialize `outputs/<feature-name>/README.md`; otherwise read its README
  first.
- Read the PRD's `AI Behavior and Acceptance` and the spec's `AI Behavior
  Contract`. If neither exists, the accuracy bar was never set — say so and
  route back to `/prd` rather than inventing one.
- Do not load org/domain brains wholesale.

## Ground in the brains (before drafting)
Run `../_shared/brain-grounding.md`. Required. Read the feature note and
hypotheses for what the model is actually expected to get right, `ingestion/`
pages on the systems the AI reasons over, and `context/compliance.md` when a
wrong answer carries regulatory cost — that shapes the accuracy bar. Cite what
you used.

## Which mode
Derive the mode from what exists; do not ask. State the call in one line.

- **Define** — no eval exists yet. Produce the bar, the set design, and the
  labeling plan.
- **Run** — an eval set exists. Execute it and report against the bar.
- **Review** — results exist. Judge whether they support shipping.

Routing: no eval set on disk → Define. A frozen set but no results → Run.
Results present → Review. When the request names a mode explicitly, that wins.

## Define
1. **State the decision the eval informs.** "Ship / do not ship at bar X." An
   eval with no decision attached is a metrics exercise.
2. **Set the bar, the paired constraint, and the baseline.** Load
   `references/metric-selection.md` — it covers choosing the metric, why a
   single-sided bar is not a bar, and reading agreement ceilings. Never invent
   a bar, baseline, or set size; `TBD` with an owner beats a plausible number.
3. **Design the set and name the labeler.** Size, sampling, composition,
   segment coverage, tie-break rule. Freeze a held-out set separate from any
   set used for tuning, and say which is which.

## Run
1. Pin the exact model ID and prompt version. `latest` is not a version.
2. Run against the frozen set. Adjusting prompts mid-run turns the held-out set
   into a tuning set and invalidates the ship decision.
3. Report each metric against its bar with a 95% confidence interval, plus the
   paired constraint separately. An interval straddling the bar has not cleared
   it — the honest verdict is "needs a bigger set", not `Pass`.
4. Break down by segment. Collect ten concrete failures; they teach the PM more
   than a percentage.
5. Record model, prompt version, set version, date, and who ran it. An
   unreproducible result cannot be re-checked after the next change.

## Review
Classify: `Clears`, `Below bar`, `Mixed — clears aggregate, fails a segment`, or
`Not evaluable`.

For anything short of `Clears`, state the product options rather than deciding:
narrow scope, add human review, raise the threshold and abstain more, ship to a
limited cohort, or do not ship. **The bar is a PM decision — recommend, then
stop.** Lowering a bar to make a result pass is itself a product decision and
must be recorded as one, with who accepted the risk.

## Output
Default for new features:
`outputs/<feature-name>/ai-eval/<feature-name>-ai-eval.md`.
For historical features, follow the artifact path in the feature README.
If no durable artifact is needed, return the summary in chat.

Include: the decision it informs, metric + bar + baseline, set design, results
by metric and segment, concrete failure examples, model/prompt/set versions, and
the recommendation with unresolved items.

## Stop conditions
- When the bar was never set, do not infer one and do not stop to ask. Record it
  as `TBD` with an owner, report that the bar belongs in the PRD, and deliver
  everything the eval can produce without it (set design, baseline, results).
  A missing bar blocks the ship *verdict*, not the artifact.
- Stop when no ground-truth data exists and none can be sampled; building the
  set is the deliverable, not the eval.
- Do not rewrite the PRD or spec here; propose amendments.
- External writes require explicit scoped approval.

## Folder resources
- `references/eval-template.md` — structure to fill.
- `references/worked-example.md` — a filled example for the inherited-model
  case. Read it once when learning the shape; skip it after that.
- `references/metric-selection.md` — choosing the metric and reading the result.
- `../../../domains/<domain>/config.json` — tool IDs and approval defaults.
- `corrections/` — if it holds entries, apply them; empty is normal (see `../_shared/corrections.md`).

## Run mode (standalone)
Default to Quick; do not ask. Follow `../_shared/run-mode.md`.

## Evidence on completion
Show the artifact path, the actual numbers with the bar next to them, the model
and prompt versions tested, and the failure examples. A reported score with no
version attached is not evidence — it cannot be reproduced or re-checked after
the next prompt change. Mark anything not measured as `Not checked`.
