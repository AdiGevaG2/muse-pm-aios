# Repo freshness check (before reading local source)

Any workflow that reads a local repo clone for current behavior runs this check
before producing analysis from that source.

## Steps
1. **Identify which repos are in scope.** Use the feature README, domain index,
  and `code-repos-git/REPO-MAP.md` to resolve the question to a concrete list
  of local repo paths. If no repo route resolves, record that as an evidence gap
   and continue with the sources that did resolve; ask only when no source at all
   can be reached and the analysis cannot proceed.
2. **Check freshness per repo automatically**, without mutating anything:
  - Use `git ls-remote` to read the remote branch tip without changing local
    refs or `FETCH_HEAD`. If remote access is unavailable, state that limitation.
  - Compare local `HEAD` to the remote tip when ancestry is already available;
    otherwise report only whether the commit IDs match.
   - Note the local last-commit date, and whether the working tree is dirty
     (uncommitted changes) — `git status --porcelain`.
3. **Record staleness as a caveat and continue.** A repo counts as stale if it's
   behind the remote branch at all, or its last local commit is older than
   ~3 weeks (a default threshold — adjust if the domain context specifies
   otherwise). Do not stop the analysis for staleness. Carry it forward as a
   visible caveat in the stage's output artifact itself (not just in chat) —
   e.g. "Source `<repo>` was N days stale as of this analysis; recent changes may
   not be reflected", with how far behind and the last local commit date. A
   silent staleness gap is exactly the kind of failure that has to surface in
   the artifact rather than disappear into the chat log.
4. **When freshness materially changes the answer,** read current remote content
   without mutating the clone — remote reads via GitHub MCP, or `git ls-remote`
   for refs. Prefer reading the specific file remotely over updating the clone.
   If current content cannot be read without mutation, analyze what is available
   and mark the freshness limitation.

Read-only inspection never needs approval. Never pull, fetch, checkout, switch
branches, stash, or otherwise change repository state as part of an analysis
task — and do not ask whether to, merely to continue analyzing. Ask about repo
mutation only when the PM explicitly asked to update or change the local repo,
and never modify a dirty working tree.
