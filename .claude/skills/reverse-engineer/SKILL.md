---
name: reverse-engineer
description: Turn targeted legacy or current code into concise, source-cited product behavior evidence. Use for "reverse engineer", "analyze existing behavior", "what does this system do", or when implementation evidence is needed before discovery, PRD, spec, or validation.
---

# Reverse Engineer

Produce concise, source-cited **product behavior** evidence for
$ARGUMENTS (a feature, module, path, or question).

This is a PM reverse-engineering workflow, not a forensic code audit. The
deliverable is what a PM needs to make migration and scope decisions — not a
description of the subsystem.

## Scope (derive it, do not ask)
Four things bound the run:

1. **Feature**
2. **Source platform(s)** — Merchant View, Single Platform, WebShield, Unified
   Platform, or multiple
3. **Target platform**
4. **Quick or Strict** — default Quick per `../_shared/run-mode.md`

Derive every field the PM did not supply and state the derived scope in one line
in the closing report. Abbreviations (MV, SP, WS, UP) count as supplied. Default
the target platform to Unified Platform; default the source platforms to whichever
legacy products plausibly hold the feature, and say which you picked. Never ask
for an output folder or feature-workspace name — derive it from the feature name.

`Reverse engineer Connected Sites from MV, WS and SP. Target UP. Strict.` and a
bare `Reverse engineer Connected Sites` both run to completion with zero
questions; the second just carries more `ASSUMED:` lines.

## Do not interrupt
Make the safest reasonable interpretation, record the assumption or evidence gap,
and continue. **Missing evidence is an `UNKNOWN`, not a question to the PM.** A
technical uncertainty that changes no product decision is never a PM question.

Two materially different **product** interpretations that would lead to different
PM conclusions get recorded as an open decision in the artifact, next to the
evidence — not raised as a question mid-run (`../../../CLAUDE.md` → Act, Don't
Ask).

## Steps

1. **Read existing PM evidence first.** Before any deep code research, check
   narrowly for evidence on this exact feature:
   - active feature artifacts under `outputs/<feature>/`
   - relevant Confluence/Jira via Rovo (targeted search, not a sweep)
   - existing discovery or reverse-engineering material

   If an existing discovery or product decision already scopes the feature, use
   it to **reduce** the code investigation. Do not discover a known feature
   decision after spending most of the run reverse-engineering code.

2. **Write the product questions.** Identify at most **3–7** questions the
   investigation must answer, e.g.:
   - What does the user see today?
   - What creates the object / triggers the behavior?
   - Who owns the data (e.g. does each URL own its findings)?
   - What user actions exist?
   - What business rules must be preserved?
   - What already exists in the target platform?
   - What is genuinely missing?

   These questions are the scope. Search only enough evidence to answer them.
   Do not attempt to document the entire subsystem.

3. **Resolve sources, then probe reachability before analyzing.** Use the
   selected platforms to pick repositories; `code-repos-git/REPO-MAP.md` targets
   the search. Prefer local clones; use GitHub MCP for repos not cloned locally,
   for history, or to read current remote content. Search to locate, then read
   the specific file — never page whole files through the API.

   **Search with Grep and Glob, not shell `grep`/`find`.** The dedicated tools
   bound their own output; a shell grep across repos returns everything it
   matches straight into context, and chained `cd &&` scripts trip permission
   prompts. Reserve Bash for what only it can do — repo freshness, remote
   probes, directory listings.

   **Probe every resolved repo before any analysis begins** — one `git ls-remote`
   (or equivalent single read) per repo, all in one batch. A repo that fails the
   probe is marked `NOT VERIFIED` immediately and its platform is dropped from
   the run per "Missing platform evidence" below. Do not discover an unreachable
   source midway through the investigation, and do not troubleshoot access from
   inside the analysis — one probe, one verdict, continue with what resolved.

4. **Freshness is a caveat, not a workflow.** Inspect available repos read-only.
   Follow `../_shared/repo-freshness-check.md`: report stale evidence as a
   caveat in the artifact and continue. Read current remote content only when
   freshness materially changes the answer. Never pull, fetch, checkout, switch
   branches, or stash, and never ask whether to — unless the PM explicitly asked
   to update the local repo.

5. **Analyze.** Answer the product questions. Inspect targeted files directly
   when the question set is small. Delegate per the subagent rules below when
   delegation reduces main-context noise.

6. **Verify inline (Strict only, narrowly).** Verification happens in this
   workflow — never by the general `verify` agent. Verify only:
   - migration-critical claims
   - contradictory evidence
   - surprising or high-consequence claims

   Verification means checking one additional independent source where useful.
   Do not re-run the investigation, do not perform completeness analysis, and do
   not launch a second full research pass. Stop when the critical claim is
   sufficiently supported, or leave it `Unknown`.

7. **Write the artifact, then report.** Persist to the path below and report the
   concise findings plus that path. A local artifact write is not an external
   write — do it, do not ask (`../_shared/run-mode.md` → Gaps). Only an
   overwrite of existing non-recoverable work needs approval first.

## Hard stopping rule
Stop researching when either:

- the defined product questions are answered with sufficient evidence, or
- the remaining unanswered points would not materially change the PM conclusion.

Do not continue merely because more code exists. Do not search for completeness
for its own sake. Once sufficient evidence exists, do not run further naming or
synonym searches.

## Quick vs Strict
Follow `../_shared/run-mode.md`. Default Quick; do not ask.

Applied to this workflow: Strict does **not** mean inspect every possible file,
enumerate every enum, trace every call chain, produce dozens of behavioral rules,
duplicate the investigation with a verifier, or search every naming synonym once
sufficient evidence exists. Strict verification is the narrow inline pass in
step 6.

## Missing platform evidence
If a requested source platform cannot be accessed: attempt **one** reasonable
alternate evidence route. If still unavailable, mark that platform
`NOT VERIFIED`, note it as an evidence gap, and continue with the other
requested platforms. Do not ask the PM again about the same unavailable source,
and do not troubleshoot infrastructure inside a product reverse-engineering
task.

## Subagent discipline
Use subagents only when they reduce main-context noise. Give each a **small
bounded question set** — never "reverse-engineer this platform."

- Prefer **one bounded pass per materially different platform**.
- Avoid separate backend + frontend + verifier + mapper passes unless genuinely
  necessary.
- Never ask an agent for an exhaustive coverage map or dozens of rules.

`legacy-analyzer` handles a bounded source-platform pass; `target-mapper` handles
the target-side delta. Strict verification is performed inline by the parent
workflow; do not invoke the general `verify` agent.

## PM relevance filter
Include a technical detail only when it affects: user behavior, business rules,
permissions, data ownership, migration parity, UX/state, implementation
feasibility, or significant risk. Do not document engineering implementation
detail that changes no product decision.

## Output
Keep it concise. Structure:

```
# Reverse Engineering: <Feature>

## Executive Summary          (3–6 bullets)
## Current Behavior by Platform   (product behavior only)
## Business Rules to Preserve     (normally 5–15)
## Target Platform: What Already Exists
## Gaps
## Conflicts / Product Decisions  (genuine PM decisions only)
## Evidence Gaps
```

Normally produce **no more than 15–20 behavioral rules total**, unless the PM
explicitly requests a comprehensive technical reference. Cite sources to support
claims — never reproduce the investigation transcript or a code walkthrough.
Include last verified repo/branch/commit where available.

Findings are always persisted to their own current-state document, never merged
into discovery, PRD, or spec. Default path:
`outputs/<feature-name>/current-state/<feature-name>-reverse-engineering.md`. For historical
features, follow the feature README.

## Do not narrate research
Investigate silently. During a normal run do not tell the PM which grep is
running, which repo is opening next, which subagent is still working, or what
intermediate implementation details turned up. Surface something mid-run only
when an immediate PM decision is genuinely required. Report once, when the work
is done.
