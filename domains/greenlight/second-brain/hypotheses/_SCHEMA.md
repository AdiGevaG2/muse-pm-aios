# Hypothesis Schema

> **Read before writing or editing any file under `hypotheses/`.** The
> `provenance-guard` hook (`.claude/hooks/provenance-guard.sh`) blocks writes
> where an evidence row carries no provenance tag.
>
> **Pre-save self-check:**
> 1. **COUNT THE TAGS.** Count bullet rows under `**Evidence for:**` and
>    `**Evidence against:**`. Count provenance tags in those rows. The numbers
>    must match. Six rows and four tags means two orphans — tag them, or move
>    them to `**Open questions:**` if they are not really claims.
> 2. Every evidence row carries exactly one tag from the enum below.
> 3. Commentary, gaps, and inferences live under `**Open questions:**`, never
>    under Evidence. Those rows need no tag.
> 4. Aggregation rows ("N=3, mixed sentiment") are meta-observations, not
>    evidence. They go under `**Open questions:**`, or split into one tagged row
>    per source.

Filename: `<topic-slug>.md`, or grouped in `README.md` for short-lived items.

## Provenance enum

Defined in `../README.md § Provenance`. Strength runs
`[documented]` > `[verbal]` > `[hunch]` > `[industry]`.

| Tag | Means | Trust |
|---|---|---|
| `[documented]` | Written and verifiable — transcript, doc, data pull, repo evidence. Cite the artifact. | Highest |
| `[verbal]` | Said in a meeting or call, nothing written. Name the person and date. | Medium |
| `[hunch]` | Our own read, no external evidence yet. Legitimate as a hypothesis input; never presentable as fact. | Low |
| `[industry]` | General industry knowledge, not specific to us. | Low — flag for replacement |

A `[documented]` claim should carry its artifact: a repo path, a
`source/`/`ingestion/` link, or a named document. A `[documented]` tag with no
identifiable artifact is weaker than an honest `[verbal]`.

Also valid on any row: `[unknown]`, for an open question with no answer yet.

## Shape

```markdown
### <Hypothesis> — <YYYY-MM-DD>
- **Belief:** <what we think is true>
- **Evidence for:**
  - <claim>  [documented] `<artifact path or link>`
  - <claim>  [verbal] <name>, <YYYY-MM-DD>
- **Evidence against:**
  - _(none yet)_
- **Open questions:** <!-- gaps, inferences, caveats. No tags required. -->
  - <what we don't know that would change confidence>
- **What would settle it:** <the test, data, or interview needed>
- **Status:** open | supported | refuted
- **Action:** <what this blocks, and which skill must re-ask it>
```

## Empty state

When a section has no claims, write `_(none yet)_` or leave it empty. Do not
write meta-rows like "no counter-evidence found" as bullets — absence of
evidence is not evidence, and an untagged row fails the guard. If you actively
searched and found nothing, record that under `**Open questions:**`.

## Lifecycle

- **open** — evidence accumulating.
- **supported** — confirmed. Distill into `../decisions/` so it stops being a
  hypothesis.
- **refuted** — contradicted. Keep it, with why; a refuted belief is knowledge.

A hypothesis that goes `supported` without a matching decision record is
hypothesis theater — the sweep in `/review` flags it.
