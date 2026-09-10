# AI solution gate (discovery)

Run this whenever it is not already obvious that the feature is purely
deterministic. It is cheap, and getting it wrong is expensive: a probabilistic
feature discovered at spec time is a rewrite.

Paste the filled result into discovery under `Proposed Solution`, before
`Feature Behavior`.

---

### Solution Nature: Deterministic or Probabilistic

<!--
  Answer this before designing the solution. It is the cheapest place to get it
  right and the most expensive to discover later.

  If the answer is "probabilistic", the feature needs an accuracy bar, an eval
  set, and defined failure behavior before it is buildable — and those change
  scope, cost, and timeline. Discovering that at spec time is a rewrite.
-->

| Question | Answer |
|---|---|
| Does a model, score, ranking, or generated text affect what the user sees — **whether we build it or inherit it from another system**? | [Yes / No] |
| Which step | [The specific step. Be narrow — usually one step, not the whole flow.] |
| Do we own that model, or consume it? | [We build it / We consume an upstream output we cannot change / Both] |
| What does a wrong output cost? | [User, customer, and business consequence] |
| Which wrong direction is worse, and roughly by what ratio? | [e.g. "one missed high-risk merchant costs ~20 analyst-hours of false alarms". The ratio is what makes a threshold a decision instead of a guess.] |
| Does ground-truth data exist to evaluate against? | [Yes - where / No - would need to be built / Unknown] |
| Do users correct the output in the course of their work? | [Yes — then this feature generates labels as a byproduct; say where they go / No] |

**If the first answer is "No", this is a deterministic feature.** Delete this
subsection and the AI sections in the PRD and spec templates, and proceed.

**If we BUILD the model:** the accuracy bar and eval commitment go in the PRD
(`AI Behavior and Acceptance`); thresholds and failure behavior go in the spec
(`AI Behavior Contract`). Missing ground-truth data is an open question now —
building an eval set is project work, not a footnote.

**If we CONSUME an upstream model** (the common enterprise case, and the one
most often missed — the feature is "just displaying a score", so nobody treats
it as AI work), fill the table below instead. Do not skip the AI sections just
because the model belongs to another team: you own how its errors reach your
user, even when you cannot change the model.

| Question | Answer |
|---|---|
| Whose model, and can it change without telling us? | [Team / system, and the notification path — or `None`, which is itself the finding] |
| Its measured quality, if known | [Value + source, or `Unknown - never measured for our use case`] |
| How its errors reach our user | [The specific surface and what the user then does] |
| What we do when its behavior shifts | [Detection signal and response, or `TBD`] |
| Do we aggregate its output? | [If per-item errors roll up to an entity — a merchant, an account — the user experiences a different error rate than the model's. State both levels.] |



