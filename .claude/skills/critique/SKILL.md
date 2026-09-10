---
name: critique
description: Critique a product document for contradictions, duplication, unclear or unnecessary statements, untestable requirements, and missing scope boundaries. Use for "critique this", "review my doc", "is this clear", "tighten this", "check for contradictions", or before sharing a PRD or spec. Judges the text as written — it does not check claims against evidence.
---

# Critique a document

Runs the `doc-critic` agent against one artifact and reports its findings.

## Resolve the target
- Path given → use it.
- Feature named → the newest artifact under `outputs/<feature-name>/`, preferring
  `prd/` then `spec/` then `discovery/`.
- Nothing given → the artifact written or edited most recently this session.
- Still ambiguous → pick the most likely and say which in one line. Do not ask.

## Run
Spawn `doc-critic` with the resolved path. One agent, one pass — do not spawn
several critics per doc, and do not read the document yourself first. Reading it
in the main thread defeats the isolation the agent exists for.

Pass the PRD path too when the target is downstream of one, so the agent can
judge contradictions against stated intent.

## Report
Relay the findings — the agent's output is not shown to the PM. Keep the four
lines per finding and the ranking. Lead with the verdict line.

Then, in one line, offer to apply the fixes. Do not apply them unprompted: some
findings are judgement calls the PM may reject, and a critic that silently
rewrites is no longer a critic.

## When a finding hits product intent
A `Consistent` finding between the spec and the PRD is PRD drift, not a wording
defect. Stop and run the four-line drift protocol from `CLAUDE.md` — Drift,
Source, Why it matters, Options. Never resolve it by editing the PRD.
