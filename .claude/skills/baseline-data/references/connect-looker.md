# Connecting Looker (Google-hosted)

One-time setup. Claude cannot do this step — the OAuth flow needs your browser
in an interactive session. Once connected, the token is cached and every later
session (including background agents) reuses it.

Google publishes an official Looker MCP server. Google-hosted instances expose
it directly at `<LOOKER_URL>/mcp` — no binary to install.

> This is **Looker Core** (the enterprise BI platform). Looker Studio, formerly
> Data Studio, is a different product with no MCP server. If that is what you
> use, Looker stays `NOT_CONNECTED` and the data comes from elsewhere.

## 1. Register Claude Code as an OAuth app in Looker

Needs Looker admin. In the API Explorer:

```
<LOOKER_URL>/extensions/marketplace_extension_api_explorer::api-explorer/
```

Call **Register OAuth App** with:

| Field | Value |
|---|---|
| Client ID | any unique identifier, e.g. `claude-code` |
| Redirect URI | `http://localhost:58999/callback` |
| Display name | `Claude Code` |
| Description | `AI agent integration` |

## 2. Add the server

In a terminal, from anywhere:

```bash
claude mcp add --transport http looker https://<YOUR-LOOKER-HOST>/mcp
```

Scope it to this project instead of globally with `--scope project` if you only
want it here.

## 3. Authenticate

Start an interactive session, then:

```
/mcp
```

Select `looker` → **Authenticate**. Your browser opens Looker's sign-in
(OAuth 2.1 + PKCE). Approve, and the connection completes.

**No client secret is stored anywhere.** Do not paste a Looker secret into a
repo file, an artifact, or chat — the `secret-guard` hook blocks it, and the
OAuth flow does not need it.

## 4. Verify and record readiness

Back in Claude Code, ask for a real read — listing LookML models is enough.
Then update `domains/unified-platform/config.json`:

```json
"looker": {
  "readiness": "VERIFIED_READ",
  "verified": "<date> via <the call you ran>. Read only — writes untested."
}
```

Configuration is not a connection. Promote to `VERIFIED_READ` only after a call
actually returns data, and only for the capability tested.

## What it exposes

- **Models and queries** — list LookML models, explores, dimensions, measures;
  run saved Looks and ad-hoc queries
- **Content** — read Looks and dashboards, and create them where the account
  has permission
- **Health and LookML** — instance diagnostics, schema inspection

It respects Looker's row-level security and role permissions: the agent sees
exactly what your Looker account sees, nothing more.

**Treat it as read-only for PM work.** Creating a Look or dashboard is an
external write and needs explicit scoped approval, same as Jira or Confluence.

## Known limits

- The hosted MCP server is in **preview** for Looker (original). Tools may
  change; capacity is fixed, so concurrent agents can time out.
- No fine-grained OAuth scopes yet — an authenticated user gets every enabled
  tool or none.
- After an admin enables new tools, **reconnect** — the tool list is cached at
  first connection.
- IP allowlists are unsupported on Looker (original); supported on Looker
  Google Cloud core.
- A non-interactive session cannot refresh an expired token. Re-authenticate
  with `/mcp` in an interactive session when that happens.

## If your Looker is self-hosted

The built-in endpoint is not available. Run Google's MCP Toolbox binary
(`--prebuilt=looker`) with Looker **API 4.0** credentials from
Admin → Users → API Keys, supplied as `LOOKER_BASE_URL`, `LOOKER_CLIENT_ID`,
and `LOOKER_CLIENT_SECRET` environment variables — never inline in a config
file. See https://github.com/googleapis/mcp-toolbox
