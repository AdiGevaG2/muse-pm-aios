# Hypotheses

> Shape and provenance rules: [`_SCHEMA.md`](_SCHEMA.md). Read it before writing here.

Things we believe but have NOT confirmed. Keeping them explicit stops a hunch
from silently hardening into a "fact."

### <Hypothesis> — <date>
- **Belief:** <what we think is true>
- **Evidence for:** <with provenance tags>
- **Evidence against:** <with provenance tags>
- **What would settle it:** <the test / data / interview needed>
- **Status:** open / supported / refuted

### Which branch/tag per repo reflects what's actually deployed to production — 2026-07-05
- **Belief:** [hunch] the branch currently checked out locally (per `platform.md`
  — `master` for G2RS, `develop` for legacy EverC and most target repos, `main`
  for `ufp-automation`) is assumed to be close to production, but this is
  unverified. Branch names alone don't guarantee what's actually live for
  clients — `develop` in particular is commonly an integration branch that can
  run ahead of production.
- **Evidence for:** none yet — pure naming-convention assumption.
- **Evidence against:** none yet — no CI/CD, release-tag, or deploy-dashboard
  check has been done per repo.
- **What would settle it:** ask engineering, per repo family, which
  branch/tag/commit is currently deployed to production — or check a release
  system (CI/CD tool, ArgoCD, release tags) directly.
- **Status:** open. **Action:** `/legacy-analyze` must re-ask this before
  treating any repo's checked-out branch as "current production behavior,"
  until this is resolved and `platform.md` is updated with a confirmed
  production-branch mapping per repo.

## Imported open questions — 2026-08-26

Source: `MUSE-KNOWLEDGE-PACK.md` (retired PM workspace audit, 2026-08-26).
Every item is `[unknown]`; none is a current status claim or product decision.

### Which legacy system owns each overlapping capability?
- **Belief:** `[unknown]` G2RS, EverC, and WebShield may each contain overlapping
  monitoring or compliance behavior.
- **What would settle it:** PM and engineering confirmation plus targeted
  repository evidence for the capability in scope.
- **Status:** open.

### Is everc-global-services shared target infrastructure or unmigrated legacy?
- **Belief:** `[unknown]` Duplicate checkouts may represent reuse rather than two
  independently owned implementations.
- **What would settle it:** Repository identity, deployment, and service-owner
  confirmation.
- **Status:** open.

### What target parity exists for Content Compliance and Merchant Risk History?
- **Belief:** `[unknown]` Retired evidence documents G2 behavior but did not
  establish complete Unified Platform equivalents.
- **What would settle it:** Approved scope plus G2 and target reverse engineering.
- **Status:** open.

### What is the current legacy role of WorkStream and WebShield code?
- **Belief:** `[unknown]` Retired sources referenced these families, but neither
  is available in the current local repository workspace.
- **What would settle it:** Current repository access and ownership/deployment
  confirmation.
- **Status:** open.

### What are the roles of the category-risk worktree, SDK test, and UP automation repositories?
- **Belief:** `[unknown]` Checkout names do not establish current ownership,
  deployment, or authority.
- **What would settle it:** Repository documentation and engineering confirmation.
- **Status:** open.

### What is the current legacy-to-target data coexistence strategy?
- **Belief:** `[unknown]` The retired audit did not establish migration,
  synchronization, or cutover behavior.
- **What would settle it:** Approved architecture evidence and current service
  contracts for the feature in scope.
- **Status:** open.

### Which historical feature migration decisions remain approved?
- **Belief:** `[unknown]` Dated feature dispositions may have changed.
- **What would settle it:** Latest approved PRD/decision record and PM confirmation.
- **Status:** open; never treat the historical inventory as current authority.
