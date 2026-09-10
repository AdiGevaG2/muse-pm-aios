# Org Brain — company-wide knowledge

Knowledge that applies across **every** domain, not just one. Separate from the
domain second brains by design: an org fact has one home here, not a copy in
each domain.

## What lives here (org-wide only)
- `glossary/` — company-wide terms, product names, entities every PM shares.
- `context/` — org-wide facts: company systems, security/data policies,
  compliance rules that apply everywhere, shared platform architecture.
- `decisions/` — standing org-level decisions every domain must respect.

## What does NOT live here
Domain-specific knowledge. That belongs in
`domains/<domain>/second-brain/`. If a fact only matters to one domain, it is
not org-level.

## Provenance — tag every load-bearing claim
Same discipline as the domain brains. Tag each claim by evidence strength:
`[documented]` > `[verbal]` > `[hunch]` > `[industry]`. Never present a weak
claim as documented; stronger tag wins on conflict unless a human overrides.

## Precedence (important)
Agents read **org-brain first, then the domain second-brain**. On conflict, the
**org brain wins** — policy, compliance, and company facts are authoritative and
must not be locally overridden. A domain brain may **extend** an org fact with
domain detail; it may not **contradict** one.

If a domain genuinely needs to depart from an org fact, that is a PM decision,
not an agent's: surface both sources with their provenance tags and stop. Do not
silently follow the domain copy.

## Routing — which brain does a fact go to?
`/ingest` classifies scope before writing:
- Clearly org-wide (company policy, shared systems, competitors, company-wide
  glossary) → confirm with the PM, then write here.
- Clearly domain-specific → the active domain's second brain.
- Unclear → default to the domain brain (narrower) and note the call.

Governance content — compliance and access-controlled policy — is human-owned
here. `/ingest` never authors it.

## Not the engine
This is knowledge, not machinery. It deliberately sits OUTSIDE `.claude/` so the
engine stays portable (packageable as a plugin) without carrying company data.
