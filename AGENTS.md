# AGENTS.md

This file is the operating guide for Codex and other coding agents working in this repository. It is based on the repository's `skills/zach-lingxing-mcp` and `skills/zach-lingxing-openapi-client` design, operational notes, and tests. Do not install those skills as part of normal project work; use them as local reference material.

## Project Scope

This repository provides a Lingxing ERP OpenAPI client and MCP service that is read-oriented by default, with a small, explicitly gated set of advertising management write tools.

Core goals:

Important positioning from repository docs:

- This project is not an Amazon API replacement and not a Lingxing ERP UI replacement.
- Prefer Lingxing MCP for ERP/store-operations views and team-shared queries.
- Prefer Amazon APIs when the user explicitly needs raw Amazon platform API data.
- Personal validation can use local `stdio`; team sharing should use a fixed-egress HTTP gateway.

- Provide a reusable Lingxing OpenAPI client for authentication, signing, pagination, document metadata, and business requests.
- Expose selected Lingxing data and approved management actions as MCP tools over stdio and HTTP.
- Support a fixed-egress gateway deployment because Lingxing OpenAPI access is constrained by IP allowlists.
- Keep team HTTP access protected by Bearer token or tokens file.
- Prefer small, business-oriented MCP tools over exposing every low-level API by default.

## Important Paths

- `lib/lingxing_openapi/client.py`: OpenAPI token, signing, request, pagination, and download parsing.
- `lib/lingxing_openapi/services.py`: business service layer and high-level aggregation tools.
- `lib/lingxing_openapi/endpoint_specs.py`: declarative MCP endpoint specs for simple read APIs.
- `lib/lingxing_openapi/ad_management.py`: advertising management write-tool metadata and safety-oriented request specs.
- `lib/lingxing_openapi/mcp.py`: MCP tool registry, allowlist filtering, stdio/HTTP JSON-RPC handling.
- `mcp-servers/lingxing-openapi/server.py`: stdio MCP entrypoint.
- `mcp-servers/lingxing-openapi/http_server.py`: HTTP MCP entrypoint.
- `skills/zach-lingxing-mcp/`: reference skill for MCP operations and troubleshooting.
- `skills/zach-lingxing-openapi-client/`: reference skill for OpenAPI client behavior and tests.
- `docs/`: repository docs and generated tool snapshots.

Deployment paths used by the current gateway:

- Source and live app directory: `/public/lingxing-mcp`
- Service working directory: `/public/lingxing-mcp`
- Service: `lingxing-mcp.service`
- Env file: `/etc/lingxing-mcp/lingxing-mcp.env`
- Tokens file: `/etc/lingxing-mcp/tokens.json`

## Security Rules

- Never print or commit real `LINGXING_APP_ID`, `LINGXING_APP_SECRET`, Bearer tokens, member tokens, document keys, Cloudflare Access credentials, or Authorization headers.
- When showing service files, env files, logs, or MCP config, redact secrets before returning output.
- Keep business APIs read-only unless the user explicitly asks for a write-capable endpoint and confirms the risk.
- Write-capable MCP tools must default to `dry_run=true`, require `confirm=true` plus `dry_run=false` before calling Lingxing, and return the request body without execution when not confirmed.
- Treat Lingxing `403` as likely authorization, API permission, authorization expiry, or IP allowlist issue before changing code.
- Treat HTTP `missing_or_invalid_bearer` as MCP gateway authentication failure, not Lingxing API failure.
- Do not expose all MCP tools by default. Use role-based allowlists in `LINGXING_MCP_ROLE_TOOLS` or the built-in role defaults; `LINGXING_MCP_ENABLED_TOOLS` is deprecated and should not be reintroduced.
- MCP tool descriptions must be written in Chinese. Tool names may remain English, but `description`, user-facing schema explanations, warnings, and business field notes should use Chinese unless an upstream API field name is being quoted.
- Public examples under `mcp-servers/lingxing-openapi/examples/public/` must remain sanitized placeholders only. Never replace example values with real credentials, real tokens, real server addresses, or internal URLs.
- Treat `manage_tokens.py list --show-token` output as secret material; do not paste it into chat or logs.

## Current MCP Tool Policy

The default member-token role is `minimal`. Tokens without a `role` field are treated as `minimal`. Role-specific visibility must be enforced in both `tools/list` and `tools/call`; hiding a tool from the list is not sufficient. Current built-in roles are `minimal`, `operations`, and `finance`. Every role must include `lingxing_health_check`, `lingxing_smoke_check`, and `lingxing_rate_limit_policy`; code should enforce these base tools even when role mappings are overridden.

The production service should expose role-based allowlists, not all registered tools. The current expected `minimal` role set is:

```text
lingxing_health_check
lingxing_smoke_check
lingxing_rate_limit_policy
lingxing_seller_lists
lingxing_marketplaces
lingxing_order_details
lingxing_order_lists
lingxing_asin_product_snapshot
lingxing_fba_warehouse_detail
lingxing_amazon_listing
lingxing_local_product_costs
lingxing_product_performance
lingxing_finance_report_asin
```

The built-in `operations` role includes operational query tools plus the approved advertising read and SP management surface. It intentionally includes buyer voice, daily SP/SD/SB advertising reports, base advertising objects, negative targeting reads, ASIN advertising daily rollup, and SP advertising management tools. It intentionally excludes hourly advertising reports, `lingxing_asin_weekly_rollup`, and `lingxing_exp_ads_aba_report` unless a production override explicitly adds them.

When adding, removing, or renaming MCP tools:

- Update the tool definition or `EndpointSpec`.
- Update the built-in role mapping or `LINGXING_MCP_ROLE_TOOLS` if the tool must be visible to a role.
- Run `tools/list` against the running HTTP MCP endpoint after restart.
- Update `docs/lingxing-mcp-tool-snapshot-*.md/json` when the visible tool surface changes materially.
- Update `docs/update-log.md` for every MCP tool-surface change. Each entry must explicitly list added tools, removed tools, built-in role allowlist changes, production `LINGXING_MCP_ROLE_TOOLS` changes when touched, and the validation result.

## Lingxing API Design Rules

- For direct Amazon order lookup by order number, use `lingxing_order_details` backed by `/erp/sc/data/mws/orderDetail`; do not scan date-range order lists when exact order IDs are available.
- For Amazon store listing, use `lingxing_seller_lists`; keep it in the minimal allowlist because order detail enrichment depends on sid-to-store-name lookup.

Use the shared client and service layer instead of hand-rolled HTTP calls.

- All business requests go to `https://openapi.lingxing.com` through `LingxingOpenAPIClient`.
- Signing must follow the existing `client.py` implementation and tests: business params plus public params, ASCII sort, omit empty strings, keep null, MD5 uppercase, AES/ECB/PKCS5 padding with app id, then URL encode.
- Use `paged_post_detailed` for paginated APIs and pass `data_path`, `total_path`, `next_token_path`, and pagination mode from `EndpointSpec` when available.
- Preserve the standard service result envelope: `ok`, `data`, `meta`, and `warnings`.
- Prefer structured API parsing over ad hoc string parsing.

### Large MCP exports

- Large paginated report tools must default to a compact summary or bounded preview. Do not return an unbounded record list to an LLM by default.
- Keep `response_mode=full` available only for non-interactive export orchestration such as `scripts/export_mcp_xlsx.py`; tool descriptions and docs must warn agents not to call full mode directly into model context.
- Full-store exports must remain one MCP call. The service may paginate internally, but clients must not loop over SID or seller ID when the upstream endpoint supports an all-store request.
- Export scripts must consume the MCP response inside the local process, write the artifact directly, and print only compact metadata. Never print full business records or authentication headers.
- Before writing an artifact, verify that returned and expected record counts match. Refuse to create a silently truncated Excel file.

## OpenAPI Rate Limiting

Lingxing OpenAPI throttling is centralized in `lib/lingxing_openapi/client.py`. Do not add ad hoc sleeps or per-tool throttling in service methods unless there is a tool-specific business reason.

Current behavior:

- `LINGXING_OPENAPI_RATE_LIMIT_ENABLED` defaults to enabled.
- Throttling is process-wide and grouped by normalized OpenAPI endpoint path.
- Capacity-1 endpoints are queued at `1 request/second` with burst `1`.
- Capacity-10 endpoints are queued at `10 requests/second` with burst `10`.
- Endpoints without local capacity documentation default to `LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_RPS=1` and `LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_BURST=1`.
- `LINGXING_OPENAPI_RATE_LIMIT_WAIT_TIMEOUT` defaults to `60` seconds. If the queue cannot obtain a token in time, return a local `local_rate_limit_timeout` error instead of leaking upstream Lingxing rate-limit failures.
- `LINGXING_OPENAPI_RATE_LIMIT_OVERRIDES` can tune rules without code changes, using comma-separated `endpoint=rate:burst` entries, for example `/bd/profit/report/open/report/asin/list=5:5`.

Every registered MCP tool must expose a visible `限流：` line in its `tools/list` description. Simple `EndpointSpec` tools inherit this automatically from `spec.endpoint`; handwritten tools must set `rate_limit_endpoints` explicitly or intentionally leave it empty only when the tool is local-only. Keep `lingxing_rate_limit_policy` available in every role so clients can obtain machine-readable endpoint policies.

When adding a new MCP tool backed by a new Lingxing endpoint, check the official OpenAPI document for token bucket capacity and update `KNOWN_RATE_LIMIT_RULES` in `client.py`. If the capacity is unknown, keep the default conservative rule and document the uncertainty in the tool metadata and snapshot.

## ASIN Product Snapshot Rules

`lingxing_asin_product_snapshot` is the primary high-level business tool for an ASIN snapshot.

Minimum input:

```json
{"sid": 7806, "asins": ["B0DX74Z1MR"]}
```

Optional input:

```json
{"start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"}
```

Default date logic:

- If no date range is provided, `end_date` is the day before the request date.
- `start_date` is `end_date - 29 days`.
- Do not require `country`; `sid` already determines the store/site context.
- The MCP schema exposes only `asins`; single-ASIN queries still pass a one-item array.
- `asins` is capped at 50 ASINs because `productPerformance.search_value` supports at most 50 values. Client agents must split larger jobs into serial batches of 50 or fewer ASINs and follow the visible `限流：` guidance.

Data source rules:

- Product name: prefer `FBAStock_v2.product_name`; fall back to `productPerformance.local_name` or `item_name`.
- Purchase cost: prefer `FBAStock_v2.cg_price`; fallback to local product costs only if needed.
- First-leg transport cost: `FBAStock_v2.cg_transport_costs`.
- Frontend price: `productPerformance.price_list.price` matched by local SKU or seller SKU.
- Product link: `productPerformance.asins[].amazon_url`; fallback to a generic Amazon DP URL only with a warning.
- FBA real-time inventory: `FBAStock_v2` with `fulfillment_channel_type="FBA"` only.
- Do not include FBM inventory in snapshot inventory totals. FBM stock is operator-maintained, not Amazon FBA real-time stock.
- FBA available: `afn_fulfillable_quantity`.
- FBA direct inbound: `stock_up_num`.
- FBA transferring: `reserved_fc_processing`.
- FBA researching: `afn_researching_quantity`.
- Total inventory: sum of the four FBA fields above.
- Sales volume in the snapshot comes from `productPerformance.volume`.
- For batch snapshots, use one FBAStock_v2 batch request with `senior_search_list`, one productPerformance batch request with `search_field=asin` and `search_value=[...]`, and one local product cost fallback request only when needed.
- Do not include FBA/FBM order counts in `lingxing_asin_product_snapshot` unless the user explicitly approves a new order-count design.
- Do not treat bdASIN `fbaSalesQuantity`, `fbmSalesQuantity`, or `totalSalesQuantity` as order counts; those fields are sales quantity metrics.
- Do not infer FBA/FBM from SKU names, MSKU suffixes, or `productPerformance.price_list`.
- Do not include raw upstream API objects such as `raw_refs` in the MCP output unless the user explicitly asks for raw debugging.

## bdASIN / Finance Report Rules

The ASIN finance report endpoint is the authoritative source for FBA/FBM split in this project:

```text
lingxing_finance_report_asin
POST /bd/profit/report/open/report/asin/list
Official doc: https://apidoc.lingxing.com/#/docs/Finance/bdASIN
```

Implementation notes:

- The old experimental name `lingxing_exp_finance_report_asin` should not be exposed.
- The public tool name is `lingxing_finance_report_asin`.
- The endpoint returns multiple `data.records` rows for a date range; aggregate all rows.
- Use `searchField=asin` and `searchValue=[asin]` through the existing profit-like spec builder.
- Preserve `start_date` and `end_date` as user-controlled input where the high-level tool exposes a date range.

## Inventory Rules

`FBAStock_v2` / `/basicOpen/openapi/storage/fbaWarehouseDetail` is a current inventory interface.

- It does not support arbitrary historical date ranges for inventory snapshots.
- Passing date-like fields such as `start_date`, `end_date`, `startDate`, `endDate`, or `event_date` should not be treated as meaningful unless official docs and tests prove otherwise.
- For ASIN snapshot inventory, query only FBA rows with `fulfillment_channel_type="FBA"`.
- `fulfillment_channel_type="FBM"` can return FBM rows, but do not use them for FBA inventory totals.
- Empty `fulfillment_channel_type` may return FBA plus FBM rows; avoid it in the ASIN snapshot unless explicitly debugging.

## Documentation Sync

Documentation is part of the implementation contract. Whenever source code changes affect MCP behavior, update the matching documentation in the same work item. This includes tool registration, allowlist policy, tool descriptions, input schemas, output fields, endpoint mappings, deployment behavior, and test or smoke-check commands.
Before every commit, scan the changed files and relevant documentation/configuration files to confirm their wording and behavior contracts are consistent, and remove conflicts between descriptions, examples, setup notes, and implementation details.

For MCP tool changes, refresh or update the tool snapshot documents under `docs/` so they match the current registered tool names, descriptions, schemas, categories, and enablement rationale. Do not leave stale names such as old experimental tool names, removed parameters, or outdated output descriptions in docs. If a relevant document cannot be updated in the current turn, explicitly report the gap and the reason.

## Testing And Verification

Minimum static verification after Python changes:

```bash
cd /public/lingxing-mcp
python3 -m compileall -q lib mcp-servers
```

Useful unit tests from the reference skills:

```bash
cd /public/lingxing-mcp
python3 -m unittest \
  skills.zach-lingxing-openapi-client.tests.test_lingxing_client \
  skills.zach-lingxing-openapi-client.tests.test_lingxing_services \
  skills.zach-lingxing-mcp.tests.test_mcp_server \
  skills.zach-lingxing-mcp.tests.test_token_auth
```

For deployed MCP changes, verify the running service, not only local imports:

```bash
systemctl restart lingxing-mcp.service
systemctl is-active lingxing-mcp.service
```

Then run HTTP MCP `tools/list` and at least one real `tools/call` for changed business tools. Do not print Bearer tokens used for the call.

For `lingxing_asin_product_snapshot`, a known smoke-test case is:

```json
{"sid": 7806, "asins": ["B0DX74Z1MR"]}
```

Expected shape:

- Required input schema contains `sid` and `asins`; `start_date` and `end_date` are optional.
- `asins` accepts 1 to 50 ASINs and always returns a batch shape with `items`.
- `sales.volume` comes from `productPerformance.volume`.
- Output should not contain FBA/FBM order counts by default.
- `inventory` contains FBA-only fields.
- Output should not contain raw upstream response blobs by default.

## Deployment Workflow

When modifying production-relevant code on the gateway:

Before using repository deployment scripts, note:

- `deploy_gateway_via_ssh.sh` expects real `LINGXING_APP_ID`, `LINGXING_APP_SECRET`, and `LINGXING_MCP_BEARER_TOKEN` in the caller environment; avoid echoing the expanded command.
- `sync_gateway_bundle.sh` uses `rsync --delete` for the target bundle. Do not use it against the currently hand-maintained deployment path unless that destructive sync is intended.
- The deployment scripts default to the current live service layout: `/public/lingxing-mcp` and `/etc/lingxing-mcp/lingxing-mcp.env`. Do not reintroduce the older upstream default paths unless explicitly migrating.

1. Work in `/public/lingxing-mcp`.
2. Check `git status --short` before edits.
3. Compile in `/public/lingxing-mcp`.
4. Restart `lingxing-mcp.service` when runtime Python code or service env changed.
5. Verify `systemctl is-active` and HTTP MCP behavior.
6. Report changed files and verification results.

Do not use destructive git commands such as `git reset --hard` or `git checkout --` unless explicitly requested by the user.

## Troubleshooting Order

For MCP availability or data issues:

Use this high-level routing before deep debugging:

- Lingxing backend setup requires a super administrator in `设置 -> 业务配置 -> 基础 -> 开放接口`.
- Confirm the allowlisted IP is the fixed-egress server public outbound IP, not the operator laptop IP.
- If the chain has not reached `healthz`, `lingxing_health_check`, `lingxing_rate_limit_policy`, and then `lingxing_smoke_check`, do not start debugging high-level business tools.

1. Check whether the MCP gateway process is running.
2. Check Bearer authentication and token file validity.
3. Run `lingxing_health_check`.
4. Check `LINGXING_APP_ID`, `LINGXING_APP_SECRET`, and token cache state without printing secrets.
5. Check Lingxing authorization expiry, interface permissions, and IP allowlist for `403` errors.
6. Check request shape, pagination settings, `data_path`, and date range semantics.
7. Only then modify client or service code.

For rate-limit errors such as Lingxing `code=103` or local `local_rate_limit_timeout`:

- First inspect `lingxing_rate_limit_policy` and the `限流：` line in `tools/list`.
- Do not parallelize calls to the same constrained endpoint.
- Prefer serial calls with short delay or retry.
- Avoid broad scans when a specific `sid` and `asin` are available.

## Coding Style

- Keep changes scoped to the relevant module.
- Follow existing dataclass and service-layer patterns.
- Prefer adding an `EndpointSpec` for simple read endpoints.
- Use a handwritten service method for multi-step aggregation, normalization, business-specific output, or write-capable tools that need a safety gate.
- Keep MCP outputs compact and business-readable.
- Write MCP tool `description` text in Chinese so `tools/list` is readable for Chinese operators.
- Add warnings for fallback behavior, missing matches, generated URLs, or source mismatch.
- Avoid introducing new dependencies unless necessary and approved.
- Keep comments short and useful.

## Public Release Gate

Repository docs describe a public-release audit step. Before pushing public changes, run the release audit when the template script is available:

```bash
python3 ../_templates/scripts/release_audit.py --repo "$(pwd)"
```

Only continue with a public push when the audit result is not `BLOCKED`. If the template script is unavailable in the current environment, report that the release audit could not be run instead of pretending it passed.

## Completion Reporting

When finishing work, report:

- What changed.
- Where it changed.
- How it was verified.
- Whether deployment was restarted.
- Backup path if production files were touched.
- Any residual warning or limitation.

Use these status words when helpful: `DONE`, `DONE_WITH_CONCERNS`, `BLOCKED`, `NEEDS_CONTEXT`.
