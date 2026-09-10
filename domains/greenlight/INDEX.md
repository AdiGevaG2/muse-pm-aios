# Greenlight Index

Use this file as the router for domain context. Load the target file only when
the current task needs it. This is a fresh scaffold — most rows are empty
until content is added.

| Need | Read |
|---|---|
| Active feature work | `../../outputs/<feature-name>/README.md` |
| Feature list | `../../outputs/` |
| Tool IDs and approval defaults | `config.json` |
| Feature learning notes (from /learn-feature) | `second-brain/context/features/` |
| Open domain and repository questions | `second-brain/hypotheses/README.md` |
| Domain decisions | `second-brain/decisions/` |
| Glossary | `second-brain/glossary/` |
| Stakeholders | `second-brain/stakeholders/` |
| Ingested source wiki | `second-brain/ingestion/` |
| Org-wide context | `../../org-brain/context/` |
| Org glossary | `../../org-brain/glossary/` |
| Legacy Greenlight background | `../../docs/greenlight-context.md` |
| Repo access | `../../docs/github-setup.md` |
| Design system / Figma setup | `../../docs/figma-integration.md` |

Org-brain rows are a separate tree, deliberately. Org facts bind every domain
and win over a domain fact on conflict; a domain page may extend one, never
contradict it.

Indexes are routers, not evidence. Verify important implementation facts
against source files. Rows pointing to empty folders will stay empty until
`/ingest`, `/discovery`, or `/retro` populate them.
