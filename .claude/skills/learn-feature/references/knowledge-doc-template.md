# {Feature Name}

> **What this doc is.** An explanation of what this feature is and why it
> exists, for anyone who needs to understand it without building it. It is not
> a spec — it does not define required behavior, and `spec.md` overrides it
> wherever they differ.

| Field | Value |
| --- | --- |
| Product Area | [Product area] |
| Primary user | [Role who actually uses this] |
| Where it lives | [Surface / screen / system] |
| Status | [Live / In build / Legacy / Sunsetting] |
| Owner | [Team or person, or "not recorded"] |
| Last verified | [Date] |
| Verified by | [Who ran the session] |

---

## In one line

[What the feature does, in one sentence a new joiner understands. No internal
names, no jargon. If you cannot do it in one sentence, the feature is two
features — write two docs.]

**Who uses it:** [Role, and roughly how many — with a date and source, or
"usage unknown". Never leave this silent; silence reads as zero.]

## Why it exists

[Two to four sentences. The user problem, then the business reason. What went
wrong before this existed, or what a customer could not do. Source it — if
nobody wrote down why this was built, say exactly that. A plausible invented
rationale is worse than a recorded gap, because the reader cannot tell them
apart and will repeat it as fact.]

## How it works, end to end

[The flow in plain English. Numbered because it is ordered. Each step says what
happens and who or what causes it. Aim for five to eight steps — if it needs
fifteen, you are describing the mechanism, not the flow.]

1. **[Trigger]** — [What starts it, and who or what triggers it.]
2. **[Input]** — [What data comes in, and from where.]
3. **[Processing]** — [What the system does with it, at product altitude. Not
   the algorithm.]
4. **[Output]** — [What gets produced or changed.]
5. **[What the user sees]** — [The visible result, and where.]

[Define every term inline on first use, in six words or fewer — same sentence,
in a dash or parenthesis. Field and status names count as terms:
`PENDING_REVIEW` is jargon even though it looks self-explanatory. Say what the
value means, not just that it exists.]

## What it does *not* do

[The highest-value section in this doc. Stakeholders arrive with assumptions,
and this is where they get corrected before those assumptions reach a roadmap
conversation. Split deliberate non-scope from current limits — they carry
different implications.]

**By design:**
- [Thing people assume it does, and why it deliberately does not.]

**Not yet / known limits:**
- [Real limitation, with what it costs the user. Say if it is on a roadmap and
  if not, say that too.]

## Where it sits

| Relationship | What | Why it matters here |
| --- | --- | --- |
| Depends on | [Upstream system or feature] | [What breaks if it is down] |
| Feeds | [Downstream consumer] | [What they use it for] |
| Often confused with | [Adjacent feature] | [The actual difference, in one line] |

[The "often confused with" rows earn their place. Most wasted meeting time on a
feature is two people using one name for different things.]

---

<!-- Everything below the fold is for the PM and the build team. -->

## Open questions

[What nobody could answer. Each row says what would settle it and who to ask —
an open question with no route to an answer is just a shrug.]

| Question | What would settle it | Who to ask | Blocks |
| --- | --- | --- | --- |
| [Question] | [Doc, query, or conversation] | [Team or person, or "owner not recorded"] | [Discovery / Spec / Launch / Nothing] |

## Confidence and sources

Every claim above traces to something read, or is marked as a gap. Labels:
**read in code** · **read in a doc** · **inferred** · **nobody wrote this down**.

| Claim | Basis | Source |
| --- | --- | --- |
| [The claim, short] | [Label from above] | [File, artifact, dashboard, or person] |

**Not verified:**
- [Anything stated above that is inference rather than fact, called out
  explicitly so a reader can discount it. If a reverse-engineering doc marked
  something inferred, it stays inferred here — retelling does not upgrade it.]

**Numbers used in this doc:**

| Number | What it counts | Population & window | Source | Pulled |
| --- | --- | --- | --- | --- |
| [Value] | [Exact definition — not "usage"] | [Denominator, date range] | [Mixpanel project / Looker model] | [Date] |

[A metric with no date rots into folklore. If a data source was unavailable,
say which one and what it would have told you — do not let the omission read as
evidence of absence.]

## Keeping this current

This doc describes the feature as of **[Last verified]**. It is explanation, not
a controlled document — it does not need an approval to change, but a stale doc
that reads as current is worse than none.

- Re-verify when the feature changes materially, or every [6 months].
- If it contradicts `spec.md`, the spec wins — fix this doc.
- If it contradicts `prd.md` on **product intent**, that is PRD drift. Do not
  quietly write the new behavior forward here; raise it with the PM.
