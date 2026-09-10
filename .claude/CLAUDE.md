# Runtime Pointer

The canonical Claude contract is `../CLAUDE.md`. Do not add independent PM rules
here; this file exists only because Claude Code discovers `.claude/CLAUDE.md`.

Engine machinery lives in this folder:
- `skills/` - callable workflows, loaded only when relevant.
- `agents/` - isolated specialists for evidence-heavy work.
- `hooks/` - mechanical guardrails.

Response style lives in `../CLAUDE.md` under "Response Style". It used to sit in
a `style.md` here, which nothing loaded — so those rules never applied. Style
belongs in the canonical contract, not in a sidecar file.

If a rule belongs everywhere, put it in `../CLAUDE.md`. If it belongs to a
domain, put it in that domain's `CLAUDE.md` or `INDEX.md`. If it is a workflow,
put it in one skill.

A file in this folder only takes effect if something loads it: `CLAUDE.md` is
auto-loaded, skills load on match, hooks are wired in `settings.json`. Prose
dropped anywhere else is dead weight.
