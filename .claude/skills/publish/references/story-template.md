# Story / Bug

Use this template for the main sprint-sized unit of work. Every Story or Bug should link to a parent Epic. Use `Bug` when the goal is to fix broken or regressed behavior; otherwise use `Story`.

## Issue Type
[Story / Bug]

## Title
As a [persona], I want to [action], so that [benefit]

Example:
As an analyst, I want to assign multiple cases at once, so that I can reduce manual triage time

## User Story
As a [specific persona],
I want to [perform action],
so that [clear user or business value].

## Parent Links
Epic: [Required link]
Milestone: [Optional trace link]
Initiative: [Optional trace link]
Design: [Link]
PRD / spec: [Link]

## Context
Explain why this Story or Bug is needed, what problem it solves, how it fits into the broader epic, and why it should be completable within a single sprint.

## Subtask Guidance
- Subtasks needed: [Yes / No]
- If yes, keep subtasks granular and low-hour.
- If the expected subtask count suggests the work will not fit in one sprint, split this Story or Bug further.

## Target Audience
### Primary user
- [Persona / role]

### Secondary user
- [Persona / role]

### Impacted users
- [Users indirectly affected]

## Persona
Role: [Role]
Goal: [What they want to achieve]
Current pain: [What is hard today]
Expected benefit: [What improves after this story]

## User Flow
### Happy path
1. User starts at [entry point]
2. User sees [screen/state]
3. User performs [action]
4. System validates [input/condition]
5. System completes [operation]
6. User sees [confirmation/result]

### Alternative path
1. User [alternative action]
2. System [response]
3. User [next step]

### Failure path
1. User attempts [action]
2. System detects [issue]
3. User sees [error state]
4. User can [recover/retry]

## Design Requirements
### Design links
- Figma: [Link]
- Prototype: [Link]
- UX copy: [Link]

### UI states required
- Default state
- Hover/focus state
- Loading state
- Success state
- Empty state
- Validation error state
- Permission error state
- System error state

### UX requirements
- [Requirement]
- [Requirement]
- [Requirement]

## Functional Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## Business Rules
- [Rule 1]
- [Rule 2]
- [Rule 3]

## Data & Analytics Requirements
### Events to track
- Event name: [event_name]
  Trigger: [When the event fires]
  Properties: [user_id, account_id, object_id, status, source, timestamp]
- Event name: [event_name]
  Trigger: [When the event fires]
  Properties: [Required properties]

### Metrics impacted
- [Adoption metric]
- [Engagement metric]
- [Efficiency metric]
- [Error rate metric]

### Validation
- Event appears in analytics tool: [Yes / No]
- Required properties populated: [Yes / No]
- Dashboard updated: [Yes / No]

## Acceptance Criteria — User-Oriented
- As a [persona], I can [action] so that [benefit].
- As a [persona], I can see [state/information] so that [benefit].
- As a [persona], I receive clear feedback when [error/edge case] so that [benefit].
- As a [persona/admin], I cannot [restricted action] unless [permission/condition].

## Acceptance Criteria — Gherkin
```gherkin
Scenario: User completes the happy path
  Given I am a [persona]
  And I have [required permission/data/state]
  When I [perform action]
  Then I should see [expected result]
  And the system should [expected system behavior]
  And analytics event [event_name] should be tracked with [properties]

Scenario: Required data is missing
  Given I am a [persona]
  And [required data] is missing
  When I navigate to [screen] or perform [action]
  Then I should see [empty state or validation message]
  And I should understand what to do next

Scenario: User enters invalid input
  Given I am a [persona]
  When I enter [invalid input]
  And I click [CTA]
  Then I should see a validation error for [field/action]
  And the action should not be completed

Scenario: User does not have permission
  Given I am a [persona]
  And I do not have permission to [action]
  When I attempt to [action]
  Then I should see a permission error
  And the restricted action should not be available or should be blocked

Scenario: System fails to complete the request
  Given I am a [persona]
  And the system is unable to complete [operation]
  When I attempt to [action]
  Then I should see a clear error message
  And I should be able to retry or take an alternative action

Scenario: User cancels the flow
  Given I am a [persona]
  And I started [flow]
  When I cancel or close the flow
  Then no changes should be saved unless explicitly confirmed
  And I should return to [expected screen/state]
```

## Edge Cases
- No data exists
- Required data is missing
- Data is stale
- User lacks permission
- User session expires
- User double-clicks or repeats action
- User refreshes during the flow
- API returns an error
- API returns partial success
- Network timeout occurs
- Duplicate records exist
- User cancels before completing
- User attempts unsupported input
- User opens the same flow in multiple tabs

## Error Handling
### Validation error
- Trigger: [Invalid input or missing field]
- Message: [User-facing message]
- Recovery: [How user fixes it]

### Permission error
- Trigger: [Unauthorized user/action]
- Message: [User-facing message]
- Recovery: [Request access / contact admin]

### System error
- Trigger: [Server/API/integration failure]
- Message: [User-facing message]
- Recovery: [Retry / fallback]

### Empty state
- Trigger: [No available data]
- Message: [User-facing message]
- CTA: [Next step]

### Timeout
- Trigger: [Slow or failed response]
- Message: [User-facing message]
- Recovery: [Retry / refresh]

## Rollout Notes
- Behind feature flag: [Yes / No]
- Flag name: [Name]
- Enabled for: [Internal / beta customers / all users]
- Rollback behavior: [Expected behavior if disabled]
- Monitoring required: [Metric / dashboard / alert]

## QA Notes
Test coverage should include:

- Happy path
- Alternative paths
- Empty states
- Error states
- Permission cases
- Analytics tracking
- Regression impact
- Cross-browser/device requirements, if relevant

## Definition of Done
- Functional requirements implemented
- Design matches approved Figma
- User flows work end to end
- Gherkin acceptance criteria pass
- Edge cases handled
- Error states implemented
- Analytics events implemented and validated
- QA completed
- Product review completed
- Documentation updated, if needed
- Feature flag configured, if relevant