# Business interrogation (product-doc stages)

Before drafting any product document, interrogate the business logic behind the
request. A structurally perfect document about a commercially unexamined idea is
a defect, not a deliverable.

This is not the run-mode assume-vs-ask boundary, which governs *detail* gaps
during drafting. This governs *premise* gaps before drafting: does the feature
make sense as a business proposition at all.

## Pass 1 — Sense-check silently
Work these out yourself from the requirement and routed evidence. Do not ask the
PM anything you can answer from what you already have.

1. **Problem** — Whose problem is this, how do we know they have it, and what do
   they do today instead? A feature with no named sufferer is a solution looking
   for a problem.
2. **Value** — Who pays or retains differently because this exists? Name the
   revenue, cost, risk, or retention mechanism. "Customers asked for it" is a
   signal, not a mechanism.
3. **Why now** — What changed to make this the priority over the alternatives?
   If nothing changed, that is worth saying out loud.
4. **Cheaper path** — Is there a config change, a doc, a manual process, or an
   existing feature that gets most of the value? Say so even when the PM has
   already committed to building.
5. **Cost of not building** — If this ships a quarter late, what breaks? A
   feature with no answer here is probably not the priority it is being treated
   as.
6. **Second-order effects** — Who else is affected: support load, sales
   promises, ops workload, existing customers' workflows, adjacent teams.
7. **Common sense** — Does the volume, pricing, effort, or timeline hold up
   arithmetically? Sanity-check the numbers rather than transcribing them.
8. **Success and failure** — What observable number moves, and what result would
   tell us this was the wrong call?

## Pass 2 — Record what you could not resolve
Do not put these to the user (see `../../../CLAUDE.md` → Act, Don't Ask). Take
the most reasonable reading, draft on it, and write the gap down.

- Carry at most 3–5 open items. Rank by what a wrong answer costs.
- Keep only what changes the document. If the answer would not alter scope,
  framing, or a requirement, it is an `Unknown`, not an open question.
- Write them in plain business language, in the artifact's open-questions
  section, each with the assumption you drafted against.
- Never re-raise what the PM answered or what the evidence already shows.
- If a premise looks genuinely unsound, say so once in the closing report — one
  line, then hand over the drafted document anyway.

## Pass 3 — Record, do not bury
Everything from Pass 1 that survives goes into the document where the template
already has a home for it — problem, value, scope, success signals, open
questions. Do not add a new "business interrogation" section.

Unresolved premise concerns become explicit open questions with a
`RECOMMENDATION`, not silent omissions. Where you sense-checked and it held,
say so briefly; where it did not, say that plainly.

## What this is not
- Not a licence to relitigate an approved decision. If the PM has decided, note
  the concern once and draft the document they asked for.
- Not a challenge quota. If the business logic is sound and evidenced, say so in
  a sentence and proceed. Manufactured objections waste the PM's round.
- Not a gate. Draft under a stated assumption when the PM does not answer.
