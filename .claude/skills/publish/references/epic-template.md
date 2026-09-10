# Epic

## Epic Type
[New Functionality / Bucket]

Use `New Functionality` for net-new capabilities or phased MVP delivery. Use `Bucket` for organizing technical debt, maintenance, or small enhancements within a domain of ownership.

## Title
[Capability] for [persona] — [Outcome]

Example:
Bulk case assignment for analysts — Reduce manual triage time

## Summary
Describe the product capability, who it serves, and the outcome it should create.

Template:
This [new-functionality or bucket] epic enables [persona/team] to [capability/action] so they can [outcome]. It supports [milestone and, when relevant, initiative] by improving [KPI, delivery phase, operational hygiene, or user behavior].

## Parent Links
Initiative: [Link or derive through milestone]
Milestone: [Link or N/A if standalone smaller implementation]
PRD: [Link]
Design: [Link]

## Target Audience
### Primary users
- [Persona / role]

### Secondary users
- [Persona / role]

### Impacted internal teams
- [Support / CS / Ops / Risk / Sales / Finance / Compliance]

## Personas
### Primary persona
Role: [Role]
Goal: [Goal]
Current workflow: [How they work today]
Pain point: [Pain]
Desired outcome: [Outcome]

### Secondary persona
Role: [Role]
Goal: [Goal]
Pain point: [Pain]
Desired outcome: [Outcome]

## Problem Statement
[Persona] needs to [goal], but today they cannot because [constraint/problem]. This causes [impact]. This epic will address the problem by [solution].

## User Value
As a [persona], I want to [action/capability], so that [benefit/outcome].

## Business Value
This epic is expected to:

- Improve [metric]
- Reduce [cost/risk/time]
- Increase [adoption/conversion/retention/revenue]
- Enable [strategic capability]

## Goals
- [Goal 1]
- [Goal 2]
- [Goal 3]

## Non-Goals
- [Non-goal 1]
- [Non-goal 2]
- [Non-goal 3]

## User Flows
### Primary happy path
1. User enters from [entry point]
2. User views [screen/data]
3. User takes [action]
4. System processes [logic]
5. User receives [confirmation/result]
6. Event is tracked: [analytics event]

### Alternative flow
1. User enters from [alternative entry point]
2. User takes [alternative action]
3. System responds with [result]

### Failure flow
1. User attempts [action]
2. System detects [issue]
3. User sees [error/empty state]
4. User can [recover/retry/contact support]

## Functional Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
- [Requirement 4]

## Design Requirements
### Required artifacts
- User journey: [Link]
- Wireframes: [Link]
- High-fidelity designs: [Link]
- Prototype: [Link]
- UX copy: [Link]

### UX considerations
- Entry points: [Where users access this]
- Navigation: [How users move through the flow]
- Empty states: [Required behavior]
- Loading states: [Required behavior]
- Error states: [Required behavior]
- Accessibility: [Requirements]
- Responsive behavior: [Desktop/mobile/tablet, if relevant]

## Data & Analytics Requirements
### Events
- Event name: [event_name]
	Trigger: [When event fires]
	Properties: [Required properties]
	Success/failure status: [Required / not required]
- Event name: [event_name]
	Trigger: [When event fires]
	Properties: [Required properties]

### Metrics
- Adoption: [Metric]
- Engagement: [Metric]
- Conversion/funnel: [Metric]
- Efficiency: [Metric]
- Error rate: [Metric]
- Business KPI: [Metric]

### Dashboards
- Product dashboard: [Link]
- Operational dashboard: [Link]
- Experiment dashboard: [Link]

### Data quality requirements
- [Required fields]
- [Freshness expectations]
- [Data validation rules]
- [Known data gaps]

## Acceptance Criteria — User-Oriented
- As a [persona], I can [perform action] so that [benefit].
- As a [persona], I can [understand system state] so that [benefit].
- As a [persona], I can [recover from error] so that [benefit].
- As an internal user, I can [monitor/support/administer] so that [business benefit].

## Acceptance Criteria — Gherkin
```gherkin
Scenario: Successful completion of primary flow
	Given I am a [persona]
	And I have [required permissions/data/state]
	When I [perform primary action]
	Then I should see [expected result]
	And the system should [expected system behavior]
	And analytics event [event_name] should be tracked

Scenario: User sees an empty state
	Given I am a [persona]
	And there is no available [data/object]
	When I navigate to [page/screen]
	Then I should see an empty state explaining [reason]
	And I should see [recommended action or next step]

Scenario: User lacks permission
	Given I am a [persona]
	And I do not have permission to [action]
	When I attempt to [action]
	Then I should see a permission error
	And I should not be able to complete the action

Scenario: System error occurs
	Given I am a [persona]
	And the system cannot complete [operation]
	When I attempt to [action]
	Then I should see a clear error message
	And I should be able to retry or understand the next step

Scenario: Analytics are captured
	Given I am a [persona]
	When I complete [tracked action]
	Then [event_name] should be sent
	And it should include [required properties]
```

## Edge Cases
- User has no data
- User has partial data
- User lacks permissions
- User has expired session
- User refreshes mid-flow
- User performs duplicate action
- User changes data in another tab
- API returns partial success
- Integration is unavailable
- Data is stale or inconsistent
- User attempts unsupported input
- User cancels before completion

## Error Handling
### Validation errors
- Condition: [Invalid input]
- Message: [User-facing copy]
- Recovery: [How user fixes it]

### Permission errors
- Condition: [Unauthorized action]
- Message: [User-facing copy]
- Recovery: [Request access / contact admin]

### System errors
- Condition: [API/server failure]
- Message: [User-facing copy]
- Recovery: [Retry / fallback / support]

### Empty states
- Condition: [No data]
- Message: [User-facing copy]
- CTA: [Next step]

### Partial success
- Condition: [Some actions succeed, others fail]
- Message: [User-facing copy]
- Recovery: [Review failed items / retry]

## Rollout Plan
### Rollout type
- [Feature flag / internal alpha / customer beta / phased GA / full GA]

### Rollout phases
1. Internal testing: [Audience, date, criteria]
2. Beta: [Customers/users, date, criteria]
3. Phased rollout: [% of users/accounts, dates, criteria]
4. GA: [Date and criteria]

### Rollback plan
- Rollback trigger: [Metric, error rate, severity]
- Rollback owner: [Name]
- Rollback method: [Feature flag / deployment rollback / config change]

### Launch communication
- Internal announcement: [Required / not required]
- Customer communication: [Required / not required]
- Release notes: [Required / not required]
- Support enablement: [Required / not required]

## Dependencies
- Frontend: [Dependency]
- Backend: [Dependency]
- Data: [Dependency]
- Design: [Dependency]
- QA: [Dependency]
- Security/compliance: [Dependency]
- GTM/CS/support: [Dependency]

## Definition of Done
- Functional requirements implemented
- Design reviewed and approved
- Main user flows implemented
- Edge cases handled
- Error states implemented
- Analytics implemented and validated
- Acceptance criteria pass
- QA completed
- Feature flag configured, if needed
- Rollout plan approved
- Documentation and enablement completed