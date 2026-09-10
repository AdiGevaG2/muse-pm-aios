---
feature_name: [Feature Name]
artifact: confluence-prd-page
status: draft
version: 0.1
last_updated: [YYYY-MM-DD]
source_prd: [path]
alignment_status: draft
---

<!--
  This is the Confluence RENDERING of prd.md, not a second source of truth.
  Product intent lives in prd.md; changes flow there first, then republish.
  Diagrams here are uploaded as page attachments and embedded with <ac:image>,
  not inlined as SVG the way the markdown artifacts do it.
-->

# [Feature Name] - PRD

<ac:structured-macro ac:name="toc" ac:schema-version="1">
	<ac:parameter ac:name="style">none</ac:parameter>
</ac:structured-macro>

<p>
	<ac:structured-macro ac:name="status" ac:schema-version="1">
		<ac:parameter ac:name="title">[Draft or Approved]</ac:parameter>
		<ac:parameter ac:name="colour">[Yellow or Green]</ac:parameter>
	</ac:structured-macro>
	<ac:structured-macro ac:name="status" ac:schema-version="1">
		<ac:parameter ac:name="title">Monitoring</ac:parameter>
		<ac:parameter ac:name="colour">Blue</ac:parameter>
	</ac:structured-macro>
</p>

<ac:structured-macro ac:name="info" ac:schema-version="1">
	<ac:rich-text-body>
		<p><strong>Document intent</strong>: [One sentence on what the PRD defines and why it matters now.]</p>
		<p><strong>Scope principle</strong>: [One sentence that guards the MVP boundary.]</p>
	</ac:rich-text-body>
</ac:structured-macro>

<table>
	<tbody>
		<tr>
			<td>
				<h3>At A Glance</h3>
				<table>
					<tbody>
						<tr><th>Primary user</th><td>[Primary operator]</td></tr>
						<tr><th>Business outcome</th><td>[Outcome]</td></tr>
						<tr><th>MVP boundary</th><td>[Boundary]</td></tr>
						<tr><th>Launch posture</th><td>[Launch scope]</td></tr>
					</tbody>
				</table>
			</td>
			<td>
				<ac:structured-macro ac:name="panel" ac:schema-version="1">
					<ac:parameter ac:name="title">Decision Gate</ac:parameter>
					<ac:parameter ac:name="borderStyle">solid</ac:parameter>
					<ac:parameter ac:name="borderColor">#dfe1e6</ac:parameter>
					<ac:parameter ac:name="bgColor">#f7f8f9</ac:parameter>
					<ac:rich-text-body>
						<ul>
							<li>[Key dependency or blocker]</li>
							<li>[Key risk or unresolved question]</li>
							<li>[What approval means]</li>
						</ul>
					</ac:rich-text-body>
				</ac:structured-macro>
			</td>
		</tr>
	</tbody>
</table>

## Overview

<!-- Diagram: editable transparent draw.io SVG attached to this page. The publisher uploads {feature-name}-overview.drawio.svg as an attachment and embeds it. -->
<ac:image ac:align="center"><ri:attachment ri:filename="{feature-name}-overview.drawio.svg" /></ac:image>

## Vision / North Star

## Business Intent

## User Problem

## Proposed Direction

<!-- Diagram: editable transparent draw.io SVG attached to this page. The publisher uploads {feature-name}-proposed-direction.drawio.svg as an attachment and embeds it. -->
<ac:image ac:align="center"><ri:attachment ri:filename="{feature-name}-proposed-direction.drawio.svg" /></ac:image>

<ac:structured-macro ac:name="panel" ac:schema-version="1">
	<ac:parameter ac:name="title">Decision Summary</ac:parameter>
	<ac:parameter ac:name="borderStyle">solid</ac:parameter>
	<ac:parameter ac:name="borderColor">#dfe1e6</ac:parameter>
	<ac:parameter ac:name="bgColor">#f7f8f9</ac:parameter>
	<ac:rich-text-body>
		<ul>
			<li>[Decision 1]</li>
			<li>[Decision 2]</li>
			<li>[Decision 3]</li>
		</ul>
	</ac:rich-text-body>
</ac:structured-macro>

## MVP Scope

## Non-Goals

## Current Data

### Mixpanel

## Success Metrics

## Risks And Dependencies

## Open Questions

## Approval Status

<ac:structured-macro ac:name="warning" ac:schema-version="1">
	<ac:rich-text-body>
		<p><strong>Approval note</strong>: [What remains open, what has been accepted as risk, and what moves to the Product Spec.]</p>
	</ac:rich-text-body>
</ac:structured-macro>
