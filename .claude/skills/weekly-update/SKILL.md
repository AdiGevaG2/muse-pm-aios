---
name: weekly-update
description: Capture and draft the weekly Slack product-team update. Two modes — (1) continuous capture: after any substantive product/work task in this workspace, silently decide if the outcome belongs in the weekly update and log it to weekly-updates/current.md; also triggers on /weekly-capture <update> or phrases like "add this to my weekly update", "log this for the update", "note this for Slack". (2) Thursday draft: on /weekly-update, or "draft the weekly update", "write this week's Slack update", synthesize current.md plus the week's evidence into a copy-ready draft. Never posts to Slack or anywhere else — drafting and archiving only, sending is always a manual step.
---

# Weekly update

A running capture file plus a weekly synthesis step, so the Thursday update
writes itself from evidence instead of being reconstructed from memory under
deadline. Two triggers, described below. Never call any Slack tool from this
skill — the one hard rule throughout is draft/archive only, never send.

Files:
- `weekly-updates/current.md` — running capture for the week in progress.
- `weekly-updates/archive/YYYY-MM-DD.md` — past weeks' sent drafts.

## Trigger 1 — Continuous capture

Runs two ways: autonomously, right after you finish a substantive task in
this workspace (a PRD, spec, discovery doc, validation, published artifact,
resolved decision, a scan that surfaces a blocker); or explicitly via
`/weekly-capture <update>` or a phrase like "add this to my weekly update."

This is judgment, not a keyword filter. Ask: would a teammate reading the
Thursday Slack update actually want to know this happened? Most tasks are
routine and produce nothing worth logging — that's the expected, silent
outcome most of the time. Log only:

- Meaningful product progress, a decision that changed direction, a
  validated learning, or a shipped artifact.
- A concrete next step worth flagging ahead of time.
- A blocker, dependency, risk, or an explicit ask for help.

Never log: routine housekeeping (file cleanup, formatting, running a skill
that produced no new decision), a meeting with no outcome, "task N of the
day is done" busywork, speculation dressed up as progress ("this should
unblock X" when it hasn't yet), or anything confidential/NDA'd.

When it's a yes, act autonomously — this workspace's default is act, don't
ask, and capture is expressly listed as running without a check-in. Read
`weekly-updates/current.md`, then:

1. **Find the initiative.** Match an existing `##` heading in the file first.
   If none fits, infer one — usually the `outputs/<feature-name>/` folder
   name, or the domain/second-brain area the work touched. Don't invent a
   new initiative heading for something that clearly belongs under an
   existing one just because the wording differs.
2. **Merge, don't pile on.** If a bullet under that initiative already
   covers this thread, update or fold into it rather than adding a
   near-duplicate. Three bullets that each restate "made progress on X" on
   different days should become one bullet that reflects the current state.
3. **Write the bullet with evidence.** State only what's actually evidenced
   by the work just done — no invented dates, owners, metrics, or
   commitments. Link the source inline (file path, PR, doc) so the claim is
   traceable later; these links are for this file only and get stripped at
   draft time.
4. **File it under the right subsection** — Progress, Next, or
   Blockers/risks/help needed — using the structure already in
   `current.md` (see the commented template at the top of that file the
   first time you open it).

If `current.md` doesn't exist or was just reset after an archive, recreate
it from `references/draft-template.md`'s structure (initiative heading with
Progress / Next / Blockers subsections) — don't wait for a specific
initiative to define the file's shape.

## Trigger 2 — Thursday draft (`/weekly-update`)

Produces a Slack-ready draft for the PM to review and paste in manually.
Never send, post, or write to Slack, Confluence, Jira, or anything external
from this trigger — the output is always a draft handed back in the
conversation.

1. **Read `weekly-updates/current.md`.** This is the primary source — most
   of the week's material should already be here if capture ran as work
   happened.
2. **Sweep for gaps.** Check what the capture file might have missed:
   `git log --since=<date of last archive or 7 days ago> --oneline` and
   recently modified files under `outputs/` and the domain
   `second-brain/`. Only pull in something substantive enough to have
   passed the Trigger 1 bar above — don't backfill routine commits just
   because they exist. If nothing new turns up, say so rather than padding.
3. **Synthesize per initiative**, using `references/draft-template.md` for
   the exact section format and rules (no internal links in the final copy,
   no placeholder next-steps, order by significance).
4. **Self-check against the quality bar before presenting:**
   - Every progress claim traces back to a file, PR, doc, or commit —
     if it doesn't, cut it or flag it as unverified rather than stating it
     as fact.
   - Each initiative's "Progress & wins" states what *changed* (a decision
     made, a state moved from X to Y), not a bare list of activities.
   - Each "Planned next" is a specific action, not "continue working on X."
   - Each blocker names the actual help needed, not just that something is
     blocked.
   - The whole draft reads in under two minutes — cut anything that
     doesn't change what the reader believes about an initiative.
5. **Present the draft in the conversation**, not as a file the PM has to
   go find, and tell them plainly: this is a draft only, nothing has been
   sent anywhere. Note that once they've actually pasted it into Slack,
   telling you it's sent (or running `/weekly-update` again) will archive
   this draft and reset `current.md` for the next week.

### Archiving (only after the PM confirms it was sent)

Only do this on explicit confirmation — "sent", "archive it", "posted it",
or a second `/weekly-update` call after a draft already exists this week.
Don't archive on the strength of having produced a draft; drafting and
sending are different events and only the human knows the second one
happened.

1. Write the final draft text to `weekly-updates/archive/YYYY-MM-DD.md`,
   dated today (or the Thursday it was sent, if the PM says otherwise).
2. Reset `weekly-updates/current.md` back to the empty templated structure
   (same shape as `references/draft-template.md`'s section headers, no
   content) so next week's capture starts clean.
3. Confirm both steps happened in one line — don't narrate the mechanics.
