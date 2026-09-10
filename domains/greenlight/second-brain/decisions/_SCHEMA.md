# Decision Record Schema

> **Read before writing or editing any file under `decisions/`.** The
> `provenance-guard` hook blocks writes where an evidence row carries no
> provenance tag.
>
> **Pre-save self-check:**
> 1. **COUNT THE TAGS.** Every bullet under `**Evidence:**` and
>    `**Explicitly not doing:**` carries one tag from the enum in
>    `../hypotheses/_SCHEMA.md § Provenance enum`.
> 2. `**Status:**` is exactly one of `pending | decided | superseded`.
> 3. `**What would reverse this:**` is specific and observable — a metric
>    threshold, a named signal, a date. Not "if things change."
> 4. Gaps and caveats go under `**Remaining ambiguities:**`, never under
>    Evidence.

Filename: `YYYY-MM-DD-<slug>.md`, or grouped in `README.md` for standing calls.

## Shape

```markdown
### <Decision title> — <YYYY-MM-DD>
- **Status:** pending | decided | superseded
- **Decision:** <what was decided; empty while pending>
- **Rationale:** <the actual reasoning, specific>
- **Applies to:** <scope — one feature, a class of features, all domains>
- **Evidence:**
  - <claim>  [documented] `<artifact path or link>`
  - <claim>  [verbal] <name>, <YYYY-MM-DD>
- **Explicitly not doing:**
  - <the rejected option>  [documented] `<why, sourced>`
- **What would reverse this:** <observable condition>
- **Remaining ambiguities:** <known unknowns; no tags required>
- **Supersedes:** <prior decision, if any>
```

## Rules

- **Append-only.** To reverse a decision, write a new record that supersedes it
  and set the old one's status to `superseded`. Never edit a decided record's
  substance.
- **Authority.** A decision record is precedent, not product intent. Product
  intent lives in a feature `prd.md`; build behavior in `spec.md`. Where a
  decision and an approved PRD conflict, surface it — do not silently pick one
  (`../../../../CLAUDE.md § Authority`).
- **Mixed-trust decisions wear it.** A record resting on `[verbal]` and
  `[hunch]` must show that on its face. A reader should never have to dig to
  learn how much of the reasoning was ever written down.
- **Decision debt.** `pending` records are unresolved forks. `/review` surfaces
  them, and prioritizes those blocking active work.
- **PM authority.** Agents draft decisions and recommend. They never mark one
  `decided` — that is the PM's call (`../../../../CLAUDE.md § Authority`).
