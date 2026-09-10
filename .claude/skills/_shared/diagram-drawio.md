# Editable draw.io diagrams in Markdown artifacts

Shared by discovery, PRD, spec, and publish. Load only when a diagram is
actually being produced.

Write the flow as a fenced ` ```mermaid ` block, then run:

```bash
python3 scripts/mermaid_to_drawio.py <path-to-artifact.md>
```

It replaces the mermaid block **in place** with inline `<svg>` markup, preceded
by a provenance comment:

```
<!-- diagram: {feature-name}-{diagram-name}.drawio.svg -->
```

The SVG carries an `mxfile` in its `content` attribute, so it stays editable in
the Draw.io VS Code extension, and it renders with a transparent background.

Rules:
- Inline in the Markdown. Not a separate file, and not a left-over mermaid block.
- Name the diagram for what it shows: `-primary-journey`, `-overview`,
  `-states`, `-user-journey`.
- `--stdout` converts without touching the source; `--dry-run` reports only.
- Confluence pages are the exception: there the SVG is uploaded as a page
  attachment and embedded with `<ac:image>`, not inlined. See the publish skill.
