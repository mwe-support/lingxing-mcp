# AGENTS.md

This file is the operating guide for Codex and other coding agents working in this repository. It is based on the repository's `skills/zach-lingxing-mcp` and `skills/zach-lingxing-openapi-client` design, operational notes, and tests. Do not install those skills as part of normal project work; use them as local reference material.

## Project Scope

This repository provides a read-only Lingxing ERP OpenAPI client and MCP service.

Core goals:

Important positioning from repository docs:

- This project is not an Amazon API replacement and not a Lingxing ERP UI replacement.
- Prefer Lingxing MCP for ERP/store-operations views and team-shared queries.
- Prefer Amazon APIs when the user explicitly needs raw Amazon platform API data.
- Personal validation can use local `stdio`; team sharing should use a fixed-egress HTTP gateway.

- Provide a reusable Lingxing OpenAPI client for authentication, signing, pagination, document metadata, and business requests.
- Expose selected Lingxing read-only data as MCP tools over stdio and HTTP.
- Support a fixed-egress gateway deployment because Lingxing OpenAPI access is constrained by IP allowlists.
- Keep team HTTP access protected by Bearer token or tokens file.
- Prefer small, business-oriented MCP tools over exposing every low-level API by default.

## Important Paths

- `lib/lingxing_openapi/client.py`: OpenAPI token, signing, request, pagination, and download parsing.
- `lib/lingxing_openapi/services.py`: business service layer and high-level aggregation tools.
- `lib/lingxing_openapi/endpoint_specs.py`: declarative MCP endpoint specs for read-only APIs.
- `lib/lingxing_openapi/mcp.py`: MCP tool registry, allowlist filtering, stdio/HTTP JSON-RPC handling.
- `mcp-servers/lingxing-openapi/server.py`: stdio MCP entrypoint.
- `mcp-servers/lingxing-openapi/http_server.py`: HTTP MCP entrypoint.
- `skills/zach-lingxing-mcp/`: reference skill for MCP operations and troubleshooting.
- `skills/zach-lingxing-openapi-client/`: reference skill for OpenAPI client behavior and tests.
- `docs/`: repository docs and generated tool snapshots.

Deployment paths used by the current gateway:

- Source repo: `/public/lingxing-mcp`
- Deployed app: `/opt/lingxing-mcp/app`
- Service: `lingxing-mcp.service`
- Env file: `/etc/lingxing-mcp/lingxing-mcp.env`
- Tokens file: `/etc/lingxing-mcp/tokens.json`

## Security Rules

- Never print or commit real `LINGXING_APP_ID`, `LINGXING_APP_SECRET`, Bearer tokens, member tokens, document keys, Cloudflare Access credentials, or Authorization headers.
- When showing service files, env files, logs, or MCP config, redact secrets before returning output.
- Keep business APIs read-only unless the user explicitly asks for a write-capable endpoint and confirms the risk.
- Treat Lingxing `403` as likely authorization, API permission, authorization expiry, or IP allowlist issue before changing code.
- Treat HTTP `missing_or_invalid_bearer` as MCP gateway authentication failure, not Lingxing API failure.
- Do not expose all MCP tools by default. Use the server-side allowlist in `LINGXING_MCP_ENABLED_TOOLS`.
- MCP tool descriptions must be written in Chinese. Tool names may remain English, but `description`, user-facing schema explanations, warnings, and business field notes should use Chinese unless an upstream API field name is being quoted.
- Public examples under `mcp-servers/lingxing-openapi/examples/public/` must remain sanitized placeholders only. Never replace example values with real credentials, real tokens, real server addresses, or internal URLs.
- Treat `manage_tokens.py list --show-token` output as secret material; do not paste it into chat or logs.

## Current MCP Tool Policy

The production service should expose a minimal allowlist, not all registered tools. The current expected minimal business set is:

```text
lingxing_health_check
lingxing_seller_lists
lingxing_marketplaces
lingxing_order_details
lingxing_asin_product_snapshot
lingxing_fba_warehouse_detail
lingxing_local_product_costs
lingxing_product_performance
lingxing_finance_report_asin
```

When adding or renaming MCP tools:

- Update the tool definition or `EndpointSpec`.
- Update `LINGXING_MCP_ENABLED_TOOLS` if the tool must be visible to clients.
- Run `tools/list` against the running HTTP MCP endpoint after restart.
- Update `docs/lingxing-mcp-tool-snapshot-*.md/json` when the visible tool surface changes materially.

## Lingxing API Design Rules

- For direct Amazon order lookup by order number, use `lingxing_order_details` backed by `/erp/sc/data/mws/orderDetail`; do not scan date-range order lists when exact order IDs are available.
- For Amazon store listing, use `lingxing_seller_lists`; keep it in the minimal allowlist because order detail enrichment depends on sid-to-store-name lookup.

Use the shared client and service layer instead of hand-rolled HTTP calls.

- All business requests go to `https://openapi.lingxing.com` through `LingxingOpenAPIClient`.
- Signing must follow the existing `client.py` implementation and tests: business params plus public params, ASCII sort, omit empty strings, keep null, MD5 uppercase, AES/ECB/PKCS5 padding with app id, then URL encode.
- Use `paged_post_detailed` for paginated APIs and pass `data_path`, `total_path`, `next_token_path`, and pagination mode from `EndpointSpec` when available.
- Preserve the standard service result envelope: `ok`, `data`, `meta`, and `warnings`.
- Prefer structured API parsing over ad hoc string parsing.

## ASIN Product Snapshot Rules

`lingxing_asin_product_snapshot` is the primary high-level business tool for an ASIN snapshot.

Minimum input:

```json
{"sid": 7806, "asin": "B0DX74Z1MR"}
```

Optional input:

```json
{"start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"}
```

Default date logic:

- If no date range is provided, `end_date` is the day before the request date.
- `start_date` is `end_date - 29 days`.
- Do not require `country`; `sid` already determines the store/site context.

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
- FBA/FBM sales quantity split: use `lingxing_finance_report_asin` / bdASIN only.
- FBA orders: sum `fbaSalesQuantity`.
- FBM orders: sum `fbmSalesQuantity`.
- Total sales quantity: sum `totalSalesQuantity`. This is the only total sales quantity field to expose.
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

For MCP tool changes, refresh or update the tool snapshot documents under `docs/` so they match the current registered tool names, descriptions, schemas, categories, and enablement rationale. Do not leave stale names such as old experimental tool names, removed parameters, or outdated output descriptions in docs. If a relevant document cannot be updated in the current turn, explicitly report the gap and the reason.

## Testing And Verification

Minimum static verification after Python changes:

```bash
cd /public/lingxing-mcp
/opt/miniconda3/bin/python -m compileall -q lib mcp-servers
```

Useful unit tests from the reference skills:

```bash
cd /public/lingxing-mcp
/opt/miniconda3/bin/python -m unittest \
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
{"sid": 7806, "asin": "B0DX74Z1MR"}
```

Expected shape:

- Required input schema only contains `sid` and `asin`; `start_date` and `end_date` are optional.
- `sales_quantity.fba_orders` comes from `fbaSalesQuantity`.
- `sales_quantity.fbm_orders` comes from `fbmSalesQuantity`.
- `sales_quantity.totalSalesQuantity` comes from `totalSalesQuantity`.
- `inventory` contains FBA-only fields.
- Output should not contain raw upstream response blobs by default.

## Deployment Workflow

When modifying production-relevant code on the gateway:

Before using repository deployment scripts, note:

- `deploy_gateway_via_ssh.sh` expects real `LINGXING_APP_ID`, `LINGXING_APP_SECRET`, and `LINGXING_MCP_BEARER_TOKEN` in the caller environment; avoid echoing the expanded command.
- `sync_gateway_bundle.sh` uses `rsync --delete` for the target bundle. Do not use it against the currently hand-maintained deployment path unless that destructive sync is intended.
- The public install script defaults from upstream docs may use `/opt/lingxing-mcp/current` and `/etc/lingxing-mcp.env`; the current live gateway in this environment uses `/opt/lingxing-mcp/app` and `/etc/lingxing-mcp/lingxing-mcp.env`. Prefer the live environment paths unless explicitly migrating.

1. Work in `/public/lingxing-mcp`.
2. Check `git status --short` before edits.
3. Back up changed deployment files under `/opt/lingxing-mcp/backups/<purpose>-YYYYMMDD-HHMMSS/` before syncing.
4. Compile in the source repo.
5. Sync only the changed files to `/opt/lingxing-mcp/app`.
6. Compile in `/opt/lingxing-mcp/app`.
7. Restart `lingxing-mcp.service`.
8. Verify `systemctl is-active` and HTTP MCP behavior.
9. Report changed files, backup directory, and verification results.

Do not use destructive git commands such as `git reset --hard` or `git checkout --` unless explicitly requested by the user.

## Troubleshooting Order

For MCP availability or data issues:

Use this high-level routing before deep debugging:

- Lingxing backend setup requires a super administrator in `设置 -> 业务配置 -> 基础 -> 开放接口`.
- Confirm the allowlisted IP is the fixed-egress server public outbound IP, not the operator laptop IP.
- If the chain has not reached `healthz`, `lingxing_health_check`, and then `lingxing_smoke_check`, do not start debugging high-level business tools.

1. Check whether the MCP gateway process is running.
2. Check Bearer authentication and token file validity.
3. Run `lingxing_health_check`.
4. Check `LINGXING_APP_ID`, `LINGXING_APP_SECRET`, and token cache state without printing secrets.
5. Check Lingxing authorization expiry, interface permissions, and IP allowlist for `403` errors.
6. Check request shape, pagination settings, `data_path`, and date range semantics.
7. Only then modify client or service code.

For rate-limit errors such as Lingxing `code=103`:

- Do not parallelize calls to the same constrained endpoint.
- Prefer serial calls with short delay or retry.
- Avoid broad scans when a specific `sid` and `asin` are available.

## Coding Style

- Keep changes scoped to the relevant module.
- Follow existing dataclass and service-layer patterns.
- Prefer adding an `EndpointSpec` for simple read-only endpoints.
- Use a handwritten service method for multi-step aggregation, normalization, or business-specific output.
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
