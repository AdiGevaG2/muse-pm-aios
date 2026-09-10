# Reverse Engineering: <feature>

> PM behavior evidence. Not a build input, not a code walkthrough, not a
> completeness audit. Every rule is source-cited.

## Product questions this pass answered
1. <question> — <short answer>
2. ...

---

## Confirmed rules
_The code demonstrably does this. Normally ~15 per pass, product-visible first._

| ID | Rule (trigger -> outcome) | Source (file + fn/line) | Edge cases |
|---|---|---|---|
| BR-001 | When X happens, system does Y. | kyc/onboarding.py :: verify() L42 | on timeout, retries once |

---

## Inferred rules
_Intent read from the code but NOT stated by it. Each carries an open question.
Never treat these as fact._

| ID | Rule (trigger -> outcome) | Source | Confidence | Open question |
|---|---|---|---|---|
| BR-014 | Merchant auto-suspended after 2 KYC fails in 24h. | risk/limits.py :: check() L88 | medium | Is the 24h window a business rule or an artifact of the cron schedule? |

---

## Evidence gaps
_What could not be reached, and why it matters to a PM decision. A short list —
not an enumeration of everything in scope._

- <area> — <why unreachable> — <what conclusion it limits>
- Freshness: source `<repo>` was N days stale as of this analysis.
- `NOT VERIFIED`: <platform, if a requested source was inaccessible>

## Closing summary
- Confirmed rules: <n>   Inferred rules: <n>
- Open questions for the PM: <list, or "none">
