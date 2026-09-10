# Figma Integration Setup

## 1. Connect the Figma MCP server

The Figma integration is a claude.ai connector, not something granted from
inside a workspace. She needs to:

1. Go to claude.ai connector settings (or run `/mcp` in an interactive Claude
   Code session) and authorize the Figma connector under her own account/org
   access.
2. Confirm she can see the Figma files relevant to Greenlight re-platforming
   (existing Greenlight designs, if any, and the Unified Platform design
   system file(s) — see below).

This step requires her own auth flow — it can't be completed on her behalf
from this session.

## 2. Unified Platform design system (read-only reference)

If her re-platformed Greenlight screens should look and behave like the rest
of Unified Platform (not like a separate visual system), point her at the
same source of truth this workspace uses for pixel-perfect prototypes:

- Repo: `https://github.com/evercompliant/g2rs-design-system.git`
  (read-only clone; push is disabled)
- Local clone convention in this workspace:
  `/Users/adig/vsCode/code-repos-git/g2rs-design-system` — she should clone
  her own read-only copy rather than share this one.
- Key paths inside: `design-system/`, `src/`, `prototypes/`,
  `CONVENTIONS.md` — read `CONVENTIONS.md` before generating any prototype
  markup.
- **Freshness rule:** pull before using if the local clone is more than 2
  days old (`git log -1 --format=%cd` to check).

**ASSUMED:** Greenlight re-platforming should target the same Unified
Platform design system, since UP is explicitly replacing Greenlight
(alongside MerchantView and WebShield). If Greenlight is meant to keep its
own distinct visual identity instead, this pointer doesn't apply — confirm
with the design/UP leads.

## 3. Generating/updating prototypes

Once Figma is connected and the design system repo is cloned:

- Use the Figma MCP tools (`get_design_context`, `get_screenshot`,
  `get_variable_defs`, `use_figma`) to pull design intent from Figma frames
  for the Greenlight replacement screens.
- Build prototype markup from the design-system repo's actual components and
  tokens — not visual approximation — the same rule this workspace follows
  for UP prototypes (pixel-perfect to the design system, because
  stakeholders treat prototypes as representative of the real product).
- If she wants the same automated wireframe/prototype skill used in this
  workspace (`wireframer` / `lofi-wireframe`), those aren't copied into this
  package since they're deliberately tuned to UP's sketch style and JSX
  conventions — treat as a follow-up if she wants that tooling, not included
  here by default.

**Confirmed:** no Figma file exists for Greenlight. The Figma connector setup
above applies only to the Unified Platform design system (for building
re-platformed Greenlight screens to UP's visual standard) — there is no
legacy Greenlight design source to reconcile against.
