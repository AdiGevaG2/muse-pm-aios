---
feature_name: [Feature Name]
artifact: confluence-spec-page
status: draft
version: 0.1
last_updated: [YYYY-MM-DD]
source_spec: [path]
alignment_status: draft
---

<!--
  This is the Confluence RENDERING of spec.md, not a second source of truth.
  spec.md is richer (business logic, permissions matrix, analytics requirements,
  AI Behavior Contract). Build behavior changes there first, then republish.
  Diagrams are page attachments embedded with <ac:image>, not inline SVG.
-->

# [Feature Name] - Product Spec

## Overview

<!-- Diagram: editable transparent draw.io SVG attached to this page. The publisher uploads {feature-name}-overview.drawio.svg as an attachment and embeds it. -->
<ac:image ac:align="center"><ri:attachment ri:filename="{feature-name}-overview.drawio.svg" /></ac:image>

## User Journeys

<!-- Diagram: editable transparent draw.io SVG attached to this page. The publisher uploads {feature-name}-primary-journey.drawio.svg as an attachment and embeds it. -->
<ac:image ac:align="center"><ri:attachment ri:filename="{feature-name}-primary-journey.drawio.svg" /></ac:image>

## Requirements

## Business Rules

## Permissions

## UX States

## Error / Empty / Loading States

<!-- Diagram: editable transparent draw.io SVG attached to this page. The publisher uploads {feature-name}-states.drawio.svg as an attachment and embeds it. -->
<ac:image ac:align="center"><ri:attachment ri:filename="{feature-name}-states.drawio.svg" /></ac:image>

## AI Behavior Contract

<!--
  Include only when spec.md has an AI Behavior Contract. Render the confidence
  thresholds, failure-mode behavior, and human override rules — reviewers on
  Confluence need those to review the feature meaningfully. Omit the section
  entirely for deterministic features.
-->

## Analytics

## Acceptance Criteria

Use Gherkin-style acceptance criteria. Keep the `AC-###` IDs from `spec.md`
unchanged — they are the traceability link to validation.

### Basic Scenario Template

```gherkin
Scenario: [Short title describing the specific behavior being tested]
	Given [Preconditions or initial state of the system]
		And [Additional context or prerequisite]
	When [The specific action or event the user performs]
	Then [The expected outcome or resulting state of the system]
		And [Any additional expected results]
```

### Example

```gherkin
Scenario: Successful Account Login
	Given the user is on the login page
	When the user enters a valid username and password
	Then the system should authenticate the user
	And the user should be redirected to their dashboard
```

### Scenario Outline (Data-Driven)

Best for testing multiple inputs without rewriting the entire scenario.

```gherkin
Scenario Outline: Password validation rules
	Given the user is on the registration page
	When the user enters "<password>" as their password
	Then the system should display "<validation_status>"
	And the password strength meter should show "<meter_color>"

	Examples:
		| password   | validation_status  | meter_color |
		| short      | Password too short | Red         |
		| 1234abcd   | Weak password      | Orange      |
		| ValidP@ss1 | Strong password    | Green       |
```

### Quick Tips For Writing Good Gherkin Scenarios

- Keep it user-centric: Focus on what the user experiences rather than technical database updates.
- Make it testable: Ensure the `Then` statement yields a verifiable pass/fail outcome.
- Focus on intent: Do not specify UI design details.

## Open Questions

## Engineering Validation Notes
