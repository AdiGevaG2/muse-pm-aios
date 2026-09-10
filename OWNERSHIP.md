# Ownership

Who owns what. Ownership means: this person curates the folder, reviews changes
to it, and is accountable for its accuracy. Others propose via PR; the owner
approves. This is what makes the repo self-serving without rotting — every folder
has someone accountable for keeping it true.

## Engine
| Path | Owner | Notes |
|---|---|---|
| `.claude/` (skills, agents, CLAUDE.md) | <engine owner / you> | Machinery. One owner bumps versions; others propose via PR. |

## Org knowledge
| Path | Owner | Notes |
|---|---|---|
| `org-brain/context/policies.md` | <compliance / security lead> | Governed. Human-owned, never LLM-maintained. |
| `org-brain/context/systems.md` | <platform / eng lead> | Shared systems facts. |
| `org-brain/glossary/`, `org-brain/decisions/` | <org owner> | Company-wide. |
| `org-brain/ingestion/`, `org-brain/source/` | <org owner> | LLM-maintained org wiki. `/ingest` confirms before writing here. |

## Domain: greenlight
Domain PM: **<you>**. See `domains/greenlight/second-brain/stakeholders/`.

| Path | Owner | Notes |
|---|---|---|
| `domains/greenlight/CLAUDE.md` + `config.json` | <you> | Domain index + setup. |
| `second-brain/context/compliance.md` | <compliance lead> | Governed, human-owned. |
| `second-brain/ingestion/` (wiki), `source/` | <you> | LLM-maintained; PM curates. |
| `second-brain/stakeholders/`, `hypotheses/` | <you> | |
| `outputs/` | <you>, per feature | Each feature's outputs owned by its PM. |
| analytics / baseline outputs | <data scientist / analytics owner> | Metric definitions + queries. |

## Rules
- Every folder has exactly one accountable owner (not "the team").
- Governed folders (compliance, policy) are human-owned — never auto-written by
  `/ingest`, `/retro`, or `/review`; those skills propose, the owner approves.
- Changes to a folder route through its owner. This is the team-scale version of
  the approval gates.

_(Fill in the &lt;owners&gt; as the pilot expands past a single PM.)_
