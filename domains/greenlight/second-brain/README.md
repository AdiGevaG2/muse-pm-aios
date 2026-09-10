# Second Brain — greenlight (domain knowledge)

Accumulated knowledge for this domain. This is the single brain: agents read it
(which holds company-wide knowledge), and it wins on conflict because it's more
specific. Keep it current — stale context here silently corrupts every
downstream artifact.

**Only put domain-specific facts here.** Anything that applies across all
domains (shared systems, org-wide policy) is prefixed `org-` in `context/`.

## Structure
- `source/` — **immutable originals.** Ingested material copied untouched
  (interview notes, docs, data pulls). Never edited. The audit trail.
- `ingestion/` — **synthesis.** Distilled knowledge derived from `source/`,
  written in our own words. Points back to the source it came from.
- `glossary/` — domain terms, entities, acronyms. One concept per entry.
- `context/` — durable facts: platform, constraints, regulations.
- `decisions/` — standing decisions + rationale; prevents re-litigating.
- `hypotheses/` — things we believe but haven't confirmed, with the evidence
  for/against and what would settle them.
- `stakeholders/` — one file per person: their asks, concerns, what they own.
- `maintenance/` — dated `/review` sweep reports. Recurrence across sweeps is
  itself a finding.

`hypotheses/`, `decisions/`, and `stakeholders/` each carry a `_SCHEMA.md`
defining their shape. Read it before writing into that directory — the
`provenance-guard` hook enforces the evidence rules it states.

`system-evolution.md` names the eight ways these brains degrade and the
staleness thresholds. Load it before `/review`.

## Provenance — tag every load-bearing claim
Knowledge is only as trustworthy as its source. Tag each claim so the strength
of evidence is visible and overridable:
- `[documented]` — written, verifiable (interview transcript, doc, data pull).
- `[verbal]` — said in a meeting/call, not documented.
- `[hunch]` — our belief, not yet evidenced.
- `[industry]` — general industry knowledge, not specific to us.
- `[unknown]` — an open question with no answer yet.

Strength runs documented > verbal > hunch > industry. When claims conflict, the
stronger tag wins unless a human overrides. An agent must never present a
`[hunch]` or `[industry]` claim as if it were `[documented]`.

This is enforced, not just stated: `.claude/hooks/provenance-guard.sh` blocks a
write that puts an untagged row under an Evidence heading in `hypotheses/`,
`decisions/`, or `stakeholders/`. A `[documented]` tag with no citable artifact
draws a warning — it is weaker than an honest `[verbal]`.

## Rules
- Facts only. If something is uncertain, mark it uncertain — agents treat this as
  ground truth.
- When a feature's PRD sets a precedent worth keeping, distill it into
  `decisions/` so future features inherit it.
- If an agent needs a domain fact that is not here, it flags the gap rather than
  inventing one. Fill the gap here, don't let it guess.
