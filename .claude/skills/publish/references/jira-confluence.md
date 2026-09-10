# Jira & Confluence Patterns — publish

How to push the PRD out. Read when running `/publish`. Project key, space, and
prefixes come from `domains/<domain>/config.json`.

## Confluence
- Publish/update the PRD page under the configured space + parent page.
- Show the user what will be created/updated BEFORE writing (approval gate).
- Preserve the PRD version stamp on the page.

### Figma link as embedded card
If the source artifact (PRD/spec/discovery) has a Figma link, embed it —
don't paste it as plain text. Add a "Design" heading followed by an
`embed-card` block with the Figma URL as an iframe src, in the same shape
Confluence renders when you paste a Figma link directly:

```html
<p><strong>Design</strong></p>
<div data-type="embed-card" data-layout="center" data-width="100">
  <iframe src="https://www.figma.com/design/..."></iframe>
</div>
```

Place it after the flow it illustrates (e.g. after User Journey, before
Assumptions) unless the page template says otherwise. If a Figma link already
exists on the page as an embed card, preserve it as-is when overwriting —
don't flatten it to plain text.

### Overwrites and comment preservation
Before updating or overwriting an existing page:

1. Retrieve the existing inline and page comments and identify the text each
  inline comment references.
2. Compare every commented text span with the proposed page content.
3. Keep comments attached normally when the referenced text remains unchanged.
4. When referenced text will be deleted or materially changed, add an appendix
  named **Comment History** to the proposed page and include a table with these
  exact columns:

  | Original commented text | Comment | PM response |
  |---|---|---|
  | [Original sentence, paragraph, or relevant text span] | [Comment copied without changing its meaning] | |

Keep separate rows for comments that refer to different text or raise different
points. Leave **PM response** empty. Do not move a comment into the appendix when
its referenced text remains unchanged and the comment can stay attached.

Never silently resolve, dismiss, rewrite, or discard comments. If the available
Confluence tooling cannot retrieve comments or verify that they will be
preserved, report that limitation and stop before showing the overwrite for
approval or writing the page.

## Jira
- Hierarchy: Initiative (multi-quarter strategic only) → Milestone (each
  roadmap item) → Epic (new-functionality or bucket) → Story/Bug → optional
  Subtask. See `initiative-template.md`, `milestone-template.md`,
  `epic-template.md`, `story-template.md` for the Description-field content
  per level. Not every feature needs an Initiative — most PRDs land at
  Milestone → Epic → Story.
- Derive from the PRD's goals/user-story section (acceptance criteria become
  story descriptions).
- Show a DIFF of what will be created/changed before writing.
- **Flag any existing story that is In Progress** — changing those mid-sprint is
  high-stakes; make the user approve them deliberately.
- Use the configured project key + epic prefix. Inherit the authenticated user's
  permissions — never broaden scope.

## Partial approval
Create only approved items. Leave rejected ones flagged
"diverged from PRD vN" so they resurface next run — never silently drop.

## Output
Record what was pushed (with IDs/links) and what was left diverged in
`outputs/<feature>/publish/publish-log.md`.
