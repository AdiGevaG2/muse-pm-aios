# Spec AI Behavior Contract (load only for AI features)

Paste this into the spec when the feature has AI behavior — including one whose
model belongs to another team. Skip this file for deterministic features.

Place it after `UX States`, before `Error / Empty / Loading States`.

The accuracy bar itself lives in the PRD; reference it, do not restate the
number here.

---

## AI Behavior Contract

<!--
  DELETE THIS ENTIRE SECTION if the feature has no model, scoring, ranking,
  generation, classification, or extraction. Otherwise it is required.

  This is the build-behavior counterpart to the PRD's "AI Behavior and
  Acceptance". The PRD says how good it must be; this says exactly what the
  system does at each confidence level and each failure mode, precisely enough
  for engineering to build and QA to test without asking a product question.

  Rule: every threshold here is a NUMBER or `[NEEDS CLARIFICATION: ...]`.
  Never "high confidence" — say what number, measured how.
-->

### Inference Contract

| Field | Specification |
|---|---|
| Inputs to the model | [Exact fields/context passed. Name them; do not say "user data".] |
| Inputs explicitly NOT passed | [PII, credentials, other-tenant data — what is excluded and why] |
| Output shape | [Enum / score 0-1 / ranked list of N / free text / structured JSON schema] |
| Output constraints | [Allowed values, max length, required fields, schema validation on parse] |
| Determinism expectation | [Is identical input required to give identical output? If not, what variance is acceptable?] |
| Grounding source | [What the output must be traceable to, or `Ungrounded generation`] |

### Confidence Thresholds and Routing

<!-- The core table. Every band must have a defined system behavior. -->

| Confidence band | Threshold | System behavior | User-visible treatment |
|---|---|---|---|
| High | [>= X] | [Auto-apply / show as primary] | [UI treatment] |
| Medium | [Y to X] | [Show with hedge / require confirm] | [UI treatment] |
| Low | [< Y] | [Abstain / route to human / hide] | [UI treatment] |
| No output | n/a | [Fallback behavior] | [UI treatment] |

- Threshold owner: [PM name] — thresholds are a product decision, not a tuning detail.
- Threshold change process: [Who can move these post-launch, and what evidence is required.]

### Failure-Mode Behavior

<!--
  These states have no equivalent in deterministic specs. Each row must state
  observable system behavior, not an aspiration.
-->

| Failure mode | Detection signal | System behavior | User message | Logged as |
|---|---|---|---|---|
| Confidently wrong | [How would we even know? Feedback signal, sampling, downstream contradiction] | [Behavior] | [Message] | [Event] |
| Fabricated fact / bad citation | [Grounding check, schema validation, source match] | [Behavior] | [Message] | [Event] |
| Below confidence threshold | [Score < Y] | [Behavior] | [Message] | [Event] |
| Malformed / unparseable output | [Schema validation failure] | [Retry N times, then fallback] | [Message] | [Event] |
| Refusal / safety filter | [Provider refusal response] | [Behavior] | [Message] | [Event] |
| Timeout | [> p95 budget] | [Behavior] | [Message] | [Event] |
| Upstream provider error / outage | [HTTP error, rate limit] | [Behavior — degrade, queue, or disable] | [Message] | [Event] |

### Human-in-the-Loop

**Standing domain constraint:** a machine-derived risk outcome never takes
effect on a merchant without human review
(`domains/unified-platform/second-brain/context/compliance.md`, ACTIVE). This
applies even when the model belongs to another team and this feature only
displays its output. A spec that lets a machine outcome auto-apply contradicts
it — surface that as a conflict for PM arbitration rather than specifying it.

| Field | Specification |
|---|---|
| Who reviews | [Role] |
| What they see | [Output + confidence + grounding evidence + what the model was given] |
| Override mechanism | [Exact UI action] |
| Override precedence | [Does a human decision persist when the model re-runs? For how long? This is a product rule — state it.] |
| Override captured as | [Audit record / eval label / training signal / discarded] |
| Reviewer disagreement | [What happens when two reviewers disagree] |

### Probabilistic Acceptance Criteria

<!--
  You cannot write `Then the output is correct` for a model. Write acceptance
  criteria at these three levels instead:

  1. CONTRACT (deterministic, per-call) — shape, bounds, routing, fallbacks.
     These are ordinary Gherkin and MUST be testable in CI.
  2. AGGREGATE (statistical, over the eval set) — the quality bar from the PRD.
     Asserted over N cases, never over one.
  3. INVARIANT (must never happen) — the outputs that are unacceptable at any
     confidence. These are absolute.
-->

**Level 1 — Contract (deterministic, per-call, CI-testable):**

```gherkin
Scenario: Low-confidence output is withheld from auto-apply
  Given the model returns a confidence score below [Y]
  When the system prepares the response
  Then the result is not auto-applied
    And the user sees [defined low-confidence treatment]
    And event [event_name] is logged with confidence_band = "low"
```

**Level 2 — Aggregate (statistical, asserted over the eval set):**

```gherkin
Scenario: Model clears the ship bar on the held-out eval set
  Given the frozen eval set "[name]" of [N] labeled cases
  When the current model and prompt version are evaluated against it
  Then [metric] is at least [ship bar]
    And [costlier-direction metric] is at most [limit]
    And the result is recorded against the model + prompt version
```

**Level 3 — Invariant (must never happen, at any confidence):**

```gherkin
Scenario: [Unacceptable output class] never reaches the user
  Given any input, including adversarial inputs in the eval set
  When the system produces a response
  Then it never [emits the prohibited output — e.g. exposes another tenant's data,
       invents a citation, or auto-actions an irreversible decision]
```

### Versioning and Drift

| Field | Specification |
|---|---|
| Model + version | [Exact model ID, e.g. `claude-opus-5`. `latest` aliases are not a spec.] |
| Prompt version | [Identifier + where the prompt is stored and reviewed] |
| Change requires re-eval | [Yes / No — and which changes: model, prompt, retrieval, input schema] |
| Drift monitoring | [What is watched, at what cadence, and what threshold triggers action] |
| Rollback plan | [How to revert to the prior model/prompt, and who decides] |
| Provider deprecation | [What happens when the vendor sunsets this model version] |

