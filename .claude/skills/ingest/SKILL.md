---
name: ingest
description: Ingest a source into the org or domain wiki, routing org-wide material to org-brain/ and domain material to the domain second brain. Use when the user says "ingest this", "add to the brain", "add this source", or drops an article/transcript/notes/data to capture.
---

# Ingest (LLM-maintained wiki)

Take a raw source and fold it into a wiki so knowledge compounds. You maintain
the wiki; the user just supplies sources. Source: $ARGUMENTS (a path, URL, or
pasted material — ask if none given).

There are two brains. Decide which one this source feeds **before** writing
anything.

## Before you start
- Confirm active domain (from `domains/<domain>/config.json`).
- **Route the source (see Scope routing below).** Everything downstream —
  `source/`, `ingestion/`, `index.md`, `log.md` — is relative to the brain you
  picked. Never split one source across both brains.
- Read that brain's `ingestion/index.md` so you know what pages already exist —
  navigate, don't re-read every page.

## Scope routing — which brain?
| Signal | Brain | Root |
|---|---|---|
| Company-wide policy, shared systems, competitors, company glossary, standing org decisions | Org | `org-brain/` |
| Anything specific to the active domain's product, users, or behavior | Domain | `domains/<domain>/second-brain/` |
| Unclear / mixed | Domain (narrower) | `domains/<domain>/second-brain/` |

- **Clearly org-wide → say so and confirm with the PM before writing.** Org
  facts bind every domain, so an org write is never silent.
- **Clearly domain → write it, no prompt needed.**
- **Unclear → default to the domain brain** and state the call in your report so
  the PM can move it up if they disagree.
- A source that is mostly domain material with one org-wide fact: ingest to the
  domain brain, and flag the org-wide fact separately rather than writing both.

Precedence, when the source contradicts what a brain already holds: **org wins
over domain** (`org-brain/README.md`). A domain page may extend an org fact, not
contradict it. Surface the conflict for the PM instead of overwriting either.

## Steps
1. **Store the raw source, untouched.** Copy it into the routed brain's
   `source/` as a dated file. Never edit it. This is the citable original.
2. **Synthesize into wiki pages** under `second-brain/ingestion/`:
   - Update existing pages where the source adds to a known concept/entity.
   - Create new pages (concept / entity / synthesis) for genuinely new material.
   - Each page: 1-2 line summary on top, body below.
3. **Tag provenance.** Every claim gets `[documented] / [verbal] / [hunch] /
   [industry]` and a pointer to the `source/` file. Never dress a weak claim as
   strong.
4. **Cross-link — this is the point.** Add `[[wiki-links]]` connecting this
   material to related pages. Actively look for threads across different sources
   (an insight ↔ a regulation ↔ a prior decision). The denser the graph, the
   more the wiki can answer that no single source could.
5. **Update navigation.** Add new pages to `index.md`. Append a newest-first line
   to `log.md`: what came in, pages created/updated, links drawn.

## Rules
- **Governance boundary:** do NOT create wiki pages for compliance /
  access-controlled policy. Those stay human-owned in `org-brain/context/`
  (org-wide policy) and the domain's `context/compliance.md` (domain-specific
  regulatory detail). The wiki is research knowledge only.
- Compile, don't dump — synthesize in our own words; the raw stays in `source/`.
- If the source conflicts with an existing page, surface the conflict with both
  provenance tags rather than silently overwriting; `/review` resolves drift.

## Output
Updated `source/` (raw), `ingestion/` pages (synthesis + links), `index.md`, and
`log.md` — all within the routed brain. Briefly report which brain the source
was routed to and why, then what was created/updated/linked.

## Evidence on completion
Do not just claim done. Show the artifact: the file path written, the actual
query result / figures, the diff, or the mismatch/gap list — whatever this stage
produced. Reviewing the evidence must be faster than re-doing the check. This
catches silent failures (a stage that "ran" but produced nothing usable).
