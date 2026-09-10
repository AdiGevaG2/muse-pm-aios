# Run mode (standalone runs)

Do not ask which mode to use. Default to **Quick**. Use **Strict** only when the
PM said so, or when the artifact is going to engineering or a stakeholder as-is.
State the mode in one line in the closing report.

- **Quick** (also written "Quick one-off") — targeted evidence. One strong source
  per important claim when that is sufficient. Make the safest reasonable
  interpretation on gaps, flag every assumption inline (clearly marked, e.g.
  "ASSUMED: ...") so the PM can override. Unresolved detail becomes `Unknown`,
  not a question.
- **Strict** — same scope as Quick, higher confidence. Independently verify
  high-risk, high-consequence, and contradictory claims; normally two strong
  sources for critical claims when available.

Strict raises confidence, not scope. It does not mean examining every file,
enumerating every value, tracing every path, or duplicating the whole
investigation with a second pass. Neither mode is a licence to interrupt the PM
at every gap — a gap is recorded as an assumption or an `Unknown` and the run
continues.

## Gaps: assume and mark, do not ask (applies in BOTH modes)
Assume freely and proceed: formatting, ordering, section structure, placeholder
copy, obvious defaults, run mechanics, artifact naming, scope boundaries, product
framing, metric choice, requirement and behavior decisions, and anything
derivable from what the PM supplied. Mark each one inline as `ASSUMED:` so the PM
can override in review — the artifact is the place to raise these, not chat.

These get an explicit `ASSUMED:` line **and** a call-out in the closing report,
because a wrong guess is expensive to unwind:
- Anything compliance / regulatory / policy-related.
- An invented UI component or a value not in the design kit (prototype).
- A metric target with no baseline anchor.

Still stop and ask only for an **external write** — Confluence, Jira, Slack,
email — or for deleting/overwriting work that is not trivially recoverable.
Writing to a local artifact or a brain is not an external write; do it and report.

Rule of thumb: if the PM can see and correct it in the file, assume it and mark
it. Only reach for a question when the action leaves this repo.
