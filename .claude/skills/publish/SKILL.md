---
name: publish
description: Publish the PRD to Confluence and create Jira work items (Initiative/Milestone/Epic/Story/Bug/Subtask). Use when the user says "publish to Confluence", "create the Jira tickets", or "push to Jira". Approval-gated — shows a diff, writes only on approval.
---

# Publish (Confluence + Jira)

Push the PRD out to Confluence and Jira. This is the trust boundary — external
state others act on — so it is always gated.

## Confluence and Jira are separate asks
Ask about each independently, show each diff separately, get each approval
separately. A yes to one is never a yes to the other. Run only what was asked
and skip the rest cleanly — the PM may want Confluence without touching Jira.

## Before you start
- Confirm active domain + feature name.
- Follow `../../../outputs/README.md`. If the feature workspace does not exist,
  initialize `outputs/<feature-name>/README.md`; otherwise read its README
  first.
- Require a current PRD (default `prd/<feature-name>-prd.md`; follow the README
  for historical features). Note its version.
- Read `config.json` for space, project key, and hierarchy. Load domain brain
  systems/policy only for a specific unresolved convention question — not
  wholesale.
- Confluence pages and Jira items are renderings of an already-grounded PRD or
  spec, so `../_shared/brain-grounding.md` does not run again here. What carries
  over is terminology: check the source artifact's terms against
  `second-brain/glossary/` before publishing, since these are the artifacts
  people outside the team read. A mismatch is fixed in the source artifact
  first, then republished — never patched only in the rendering.
- Ask which of Confluence, Jira, or both the PM wants this run — do not assume
  "publish" means both.

## Steps
1. **Confluence** (if requested): render into the matching page template
   (`references/confluence-prd-page-template.md` /
   `confluence-spec-page-template.md`). Renderings only — never edit intent
   while rendering.
   **Resolve placement first**: record space, parent page title/ID, and any
   existing page ID in `references/confluence-metadata-template.md`. There is no
   global default parent; ask per feature and keep the answer. Attach diagrams
   as page files embedded with `<ac:image>` — inline SVG does not work here.
   If the source artifact has a Figma link, embed it as a Figma embed card, not
   plain text — see `references/jira-confluence.md`.
   **Audit comments before any overwrite diff** (see
   `references/jira-confluence.md`): preserve comments whose referenced text is
   unchanged; if commented text will be deleted or materially changed, append a
   **Comment History** table. If tooling cannot verify preservation, report that
   and stop before requesting approval.
   Show what will be published/updated. On approval, upload via MCP.
2. **Jira** (only if requested) **— hierarchy.** Default hierarchy (from `config.json` →
   `jira.issue_hierarchy`): **Initiative** (only for multi-quarter strategic
   work) → **Milestone** (required for each roadmap item) → **Epic**
   (new-functionality or bucket) → **Story/Bug** → optional **Subtask**. Derive
   from the PRD's goals/user-story sections, using the matching template in
   `references/` (Initiative only for genuinely multi-quarter work).
   Before creating: **ask whether Initiative, Milestone, and Epic link to
   existing Jira items or are new**, and **confirm Story, Bug, or a mix**.
   Subtasks only when explicitly requested.
3. **Show a DIFF** of what will be created/changed at every level before
   writing. Flag any existing story that is In Progress — changing those
   mid-sprint is high-stakes; make the user approve them deliberately.
4. **Partial approval:** create only approved items; leave rejected ones flagged
   "diverged from PRD vN" for next run.

## Hard rules
- Never write to Jira/Confluence without explicit approval on the shown diff.
- Never silently resolve, dismiss, rewrite, or discard Confluence comments.
- Inherit the authenticated user's permissions; don't broaden scope.
- Record what was pushed vs. left diverged.

## Output
- `outputs/<feature-name>/publish/publish-log.md` — what went to
  Confluence/Jira, with links/IDs, and anything left diverged.
- `publish/confluence-prd.md`, `publish/confluence-spec.md`,
  `publish/confluence-metadata.md` — the rendered pages and their placement,
  kept so the next republish is not a guess.

Historical features may keep these elsewhere; follow the feature README.

## Folder resources (read these)
- `../../../domains/<domain>/config.json` — standing setup (domain, tool IDs,
  naming, gates). Use it instead of re-asking; only ask for what is still blank.
- `corrections/` — if it holds entries, apply them; empty is normal (see `../_shared/corrections.md`).
- `references/jira-confluence.md` — how to call Jira/Confluence.
- `references/initiative-template.md`, `milestone-template.md`,
  `epic-template.md`, `story-template.md` — Jira Description templates. Story
  covers Story and Bug; no Feature level.
- `references/confluence-prd-page-template.md`,
  `confluence-spec-page-template.md`, `confluence-metadata-template.md`.
- `../_shared/diagram-drawio.md` — generating the draw.io SVGs to attach.

## Run mode (standalone)
Default to Quick; do not ask which mode. Follow `../_shared/run-mode.md`.
Prepare the full payload and diff on assumptions, marking each inline. The one
approval this skill needs is the external write itself: show the diff of what
goes to Confluence/Jira and publish only on the PM's go-ahead.

## Evidence on completion
Do not just claim done. Show the artifact: the file path written, the actual
query result / figures, the diff, or the mismatch/gap list — whatever this stage
produced. Reviewing the evidence must be faster than re-doing the check. This
catches silent failures (a stage that "ran" but produced nothing usable).
