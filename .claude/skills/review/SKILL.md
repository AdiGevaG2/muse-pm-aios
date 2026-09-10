---
name: review
description: Maintenance sweep of the brains. Flags stale, contradictory, weakly-evidenced, or orphaned knowledge to confirm, downgrade, or cut. Use on a cadence or for "review the brain", "sweep for drift", "clean up knowledge". Not /retro, which captures new learnings.
---

# Review (brain maintenance sweep)

Keep the brains from rotting. `/retro` adds knowledge; `/review` audits what's
already there. A brain nobody sweeps quietly fills with stale facts that corrupt
future outputs.

## Before you start
Load `domains/<domain>/second-brain/system-evolution.md`. It names the eight
ways these brains degrade and the staleness thresholds below. The checks here
are the *how*; that file is the *why*. Then read the last two reports in
`second-brain/maintenance/log/` — an item recurring across sweeps is a
different finding from a new one.

## Scope
Sweep the active domain `second-brain/` (glossary, context,
decisions, ingestion, hypotheses, stakeholders).

## What to flag
1. **Contradictions** — two entries that disagree. Surface both with their
   provenance tags; the stronger tag wins unless the user overrides.
2. **Weak evidence still load-bearing** — `[hunch]` or `[industry]` claims that
   downstream artifacts have been relying on as if solid. Flag for confirmation
   or downgrade.
3. **Staleness** — entries whose source is old or whose `context/` fact may have
   changed (systems, regulations). Flag for re-verification.
4. **Orphans** — `ingestion/` synthesis with no `source/` behind it, or source
   never synthesized. Broken provenance chains.
5. **Wiki integrity** — broken `[[wiki-links]]` (pointing to nonexistent pages),
   pages missing from `index.md`, index entries with no page, pages with no
   cross-links (isolated nodes that should connect to the graph).
6. **Hypotheses to resolve** — open hypotheses that now have enough evidence to
   mark supported/refuted, or promote into `context/`.
7. **Confirmed-repeatedly** — a claim reinforced across features; note it's
   durable (keep). A claim contradicted repeatedly; propose cutting it.
8. **Recurrence** — anything flagged in a previous sweep and still open. Report
   how many sweeps it has survived. Three or more means nobody owns it: escalate
   rather than re-listing. Skip items the PM explicitly deferred.
9. **Decision debt** — `pending` decision records, oldest first. Prioritize
   those blocking active work. A conflict pending past two sweeps is itself the
   finding (failure mode 4, tension graveyards).

## Staleness thresholds
Flag, never auto-decay. Defaults from `system-evolution.md`: market intel 30–60
days, interview signals 90, stakeholder positions 30, platform/repo facts 60,
compliance 90 or on known change, strategy quarterly, AI evals on any model or
prompt version change. Past threshold means *unverified*, not *wrong* — the
report must not conflate them.

## Rules
- **Propose, don't auto-edit.** Same gate as `/retro`: the brain is ground truth,
  so show a diff (what to confirm / downgrade / cut / promote) and change only on
  approval.
- Never strengthen a provenance tag on your own — only a human can promote a
  `[hunch]` to `[documented]`.
- Rule of thumb: a rule confirmed repeatedly stays; a contradicted one gets cut.

## Output
A sweep report written to `second-brain/maintenance/log/YYYY-MM-DD.md`, in the
shape defined by `maintenance/README.md`: recurring items first, then new
findings grouped by failure mode, each with a proposed action (confirm /
downgrade / cut / promote / re-verify) and its provenance. Close with the
counts — open hypotheses, pending decisions, TODO, Unknown — so drift across
sweeps is visible.

On approval, apply the edits and record both what was applied and what the PM
deferred. Logging deferrals matters as much as logging fixes: without them the
next sweep re-raises settled items, which is how maintenance turns ceremonial.

Keep the report short. A long report nobody reads is failure mode 7.
