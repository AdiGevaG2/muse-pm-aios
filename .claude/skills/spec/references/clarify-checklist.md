# Spec clarify checklist

Adapted from the proven `speckit.clarify` taxonomy (`PM-unified-platform/tools/spec-kit/templates/commands/clarify.md`), trimmed to PM-owned categories only. Engineering-only categories (performance/scalability targets, hosting, language/storage constraints) are deliberately excluded here — those belong to the target repo's own `/plan`, not a PM-authored spec.

Run this scan against the drafted spec before Figma reconciliation. For each category, mark **Clear / Partial / Missing**. Only raise a question for Partial/Missing categories where the gap would materially change what the feature does or how it's tested — not for gaps better left to engineering's own planning.

- **Functional Scope & Behavior:** core user goals & success criteria; explicit out-of-scope declarations; user roles/personas differentiation.
- **Domain concepts (business-level, not schema):** entities and what they represent; identity/uniqueness rules a user would recognize; lifecycle/state transitions (e.g. `Active`/`Inactive`, `Approved`/`Rejected`).
- **Interaction & UX Flow:** critical user journeys/sequences; error/empty/loading states; accessibility or localization notes.
- **Edge Cases & Failure Handling:** negative scenarios; conflict resolution the user would experience (e.g. concurrent edits shown to two operators).
- **Business Rules & Logic:** decision rules, overrides, priority/conflict resolution — anything in the spec's Business Logic / Business Rules sections still marked as a placeholder.
- **Terminology & Consistency:** canonical glossary terms used correctly (cross-check `second-brain/glossary/`); no ad hoc synonyms for a term the brain already defines.
- **Completion Signals:** every acceptance criterion is testable (a real Given/When/Then, not a vague statement); success criteria are measurable and anchored to a baseline figure.
- **Analytics coverage:** every event needed to measure the success criteria is listed; no placeholder rows left in the Analytics sections if analytics are required for MVP.
- **AI behavior (only if the feature has a model, score, ranking, generation, classification, or extraction):** confidence thresholds stated as numbers rather than "high"/"low"; behavior defined for every confidence band including abstain; failure modes answered (confidently wrong, fabrication, malformed output, refusal, timeout, provider outage); human override precedence over model re-runs; model ID and prompt version pinned, not `latest`; the accuracy bar traced to the PRD rather than invented here. An unanswered threshold is a product gap, not an engineering detail — it decides what the user sees.
- **Misc / Placeholders:** any remaining `[NEEDS CLARIFICATION: ...]` marker, `[TODO]`, or bracketed placeholder text.

## Question budget
Ask **up to 5** highly targeted questions per clarify pass, prioritized by which gap would most change implementation or testing if guessed wrong. This mirrors the proven `speckit.clarify` discipline — unbounded question loops stall the PM, and a capped, prioritized pass forces real triage instead of asking everything.

## Encoding answers back
Resolve each answered question directly in the spec (replace the `[NEEDS CLARIFICATION: ...]` marker or fill the relevant table row) rather than logging the answer only in chat — the spec must be self-contained for whoever reads it next.
