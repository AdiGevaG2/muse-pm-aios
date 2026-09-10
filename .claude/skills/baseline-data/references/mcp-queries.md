# MCP Query Patterns

Per-source mechanics for `/baseline-data`. Project IDs, endpoints, and readiness
come from `domains/<domain>/config.json` → `tools`.

MCP tool schemas are deferred: search for the tool you need rather than assuming
a name. `ToolSearch` with `+mixpanel query`, `+coralogix dataprime`, etc.

## Query discipline (all sources)

Every query specifies four things. Missing any one means it is underspecified —
tighten before running:

- **Behavior** — the event, action, or signal
- **Population** — which users or services, and the filter that defines them
- **Timeframe** — an explicit window with real dates, never "recently"
- **Output** — funnel, retention, segmentation, count, or time series

Record each figure with its query and window. A number without them cannot be
re-derived, which defeats the point of a baseline.

## Mixpanel — product and funnel metrics

- Call `Get-Business-Context` first in a new conversation. It resolves project
  nicknames, internal acronyms, and which events actually matter. Skipping it
  causes wrong-project picks and wasted calls.
- List available events and properties before querying. Never assume a name; an
  unconfirmed event is not a fact.
- Apply the customer-only filter by default (`config.json` →
  `mixpanel.customer_filter`, currently `is_customer = true`). Say so explicitly
  when you deliberately query all traffic.
- Typical pulls: coverage (accounts with ≥1 tracked interaction), usage volume,
  funnel conversion by step, drop-off %, segmentation by client or cohort.
- Break funnels down by platform, channel, or cohort. Separate paid from free in
  retention. Aggregate-only figures hide what you are looking for.
- Scope limit worth stating in artifacts: Mixpanel covers instrumented UI
  surfaces only. Legacy or UP-native surfaces without events return nothing —
  that is a coverage gap, not a zero.

## Coralogix — error and performance signals

- Send `mcp-version: v2`. Region endpoint from config; OAuth or API key from the
  environment, never from a repo file or chat.
- Log queries run against **archive** storage, not frequent-search-only tiers.
- **One active connection at a time** — do not run parallel Coralogix pulls.
- DataPrime is the query language; `query_dataprime` for logs,
  `query_promql_instant` / `query_promql_range` for metrics.
- Typical pulls: error rate by service, p95/p99 latency on the relevant route,
  failure counts on the flow the feature touches.
- Use `get_datetime` for the current time rather than assuming it — windows must
  be absolute in the recorded query.

## Looker — business and warehouse metrics

**Not connected.** No Looker MCP server is available in this workspace.

When a figure genuinely needs Looker:
1. Say which figure and why Mixpanel or Coralogix cannot supply it.
2. Record it as `Not available - Looker not connected` in the baseline.
3. Do not approximate it from another source. A product metric and a warehouse
   metric that "look similar" are different numbers, and substituting one for
   the other silently corrupts the baseline.

To enable: see `connect-looker.md`. Google publishes an official MCP server
built into hosted Looker instances; setup is `claude mcp add --transport http`
plus a browser OAuth the user runs themselves.

## Readiness

`config.json` keeps every integration `UNVERIFIED` until a real runtime query
succeeds. Promote to `VERIFIED_READ` only for the capability actually tested —
a successful read does not verify write access, and a successful Mixpanel call
says nothing about Coralogix.

If a call fails, report the failure and the readiness state. Never fall back to
an estimate.
