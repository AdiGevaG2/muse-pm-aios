# Greenlight Domain Router

Active domain: `greenlight`. New feature work lives in
`outputs/<feature-name>/` at the workspace root. Existing work under
Feature work lives at `outputs/<feature-name>/`, not under this domain.

Start with the feature `README.md`. Its links and the links in `INDEX.md` are
routing candidates, never automatic reads. Load only the artifact required for
the current stage. Load domain context only for a specific unresolved gap.

`config.json`, the full style guide, writing samples, brains, repository maps,
historical features, and integrations are lazy. A skill may request the exact
one needed; otherwise do not load them. Writing samples are optional even during
artifact drafting.

The PRD owns product intent. The spec owns exact build behavior. Domain context
provides evidence and constraints but cannot silently override either artifact.

Compliance and policy context is human-owned. Brain and external-system writes
require explicit approval.
