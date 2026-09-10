# Brain grounding (product-doc stages)

Every product document — discovery, PRD, spec, analytics plan, eval, validation,
and anything published to Confluence or Jira — is grounded in the brains before
it is written. A document that only reflects the requirement in front of you
repeats whatever the requester already believed. The brains are where the
company's actual knowledge lives.

This is a **required lookup**, not a suggestion. "Do not load the brains
wholesale" is about volume, not about skipping them.

## What to read

Targeted reads, in this order. Stop when you have enough to write.

1. **Feature note** — `domains/<domain>/second-brain/context/features/<feature-name>.md`.
   The single highest-value file when it exists: a prior session already worked
   this feature out. Read it first, always.
2. **Hypotheses** — `domains/<domain>/second-brain/hypotheses/<feature-name>.md`
   and any adjacent file. Open beliefs about this feature, with their evidence
   and status. A PRD that contradicts a live hypothesis without addressing it is
   incomplete.
3. **Decisions** — `domains/<domain>/second-brain/decisions/`. Standing calls
   already made. Do not re-decide something the domain settled.
4. **Domain context** — `context/product-areas.md` to place the feature,
   `context/platform.md` for how the system fits together, `context/compliance.md`
   when the feature touches regulated behavior, `glossary/` for terminology.
   Match the artifact's terms to the glossary; do not invent parallel names.
5. **Ingestion pages** — `second-brain/ingestion/`. Check `index.md` for pages
   on the systems this feature touches, then read only those. These are
   synthesized knowledge, not history — unlike `ingestion/log.md`, which stays
   out of product-doc work.
6. **Org brain** — `org-brain/context/`. Company-wide facts: customers, market,
   how G2RS operates, standing org decisions. Read when the document makes a
   claim about the business rather than the product.
7. **Stakeholders** — `second-brain/stakeholders/` when the document names an
   owner, an approver, or an affected team.

Org wins over domain on conflict (`org-brain/README.md`). A domain page may
extend an org fact, never contradict it.

## How to use what you find

- **Terminology comes from the glossary.** Same concept, same word, across every
  artifact.
- **A brain fact is evidence, not intent.** It informs the document; `prd.md`
  still owns product intent (`../../../CLAUDE.md` → Source of Truth).
- **Cite what you used.** Name the brain file in the artifact's evidence or
  sources section, the way any other source is cited. A reader must be able to
  tell which claims came from recorded knowledge.
- **Contradiction is a finding.** When the brain contradicts the requirement
  you were handed, that belongs in the artifact — as an open question, a risk,
  or a flagged conflict. Do not silently pick the requirement.
- **Silence is a finding too.** When the brains cover none of this feature, say
  so in the artifact rather than writing as if the gap were not there. It tells
  the PM the document rests on the requirement alone.

## Gap loop

If reading a brain file exposes a gap that changes the document, follow the
routing it points at — a repo in `context/repo-feature-map.md`, a source in
`second-brain/source/`, an analytics query. One hop, not an investigation.

Knowledge worth keeping that surfaced during the work goes back into the brain
via `/ingest` or `/retro`, not inline into the brain from a drafting skill.
