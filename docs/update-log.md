# Lingxing MCP Update Log

This log records MCP tool-surface changes. Each entry must list added tools, removed tools, built-in role allowlist changes, production `LINGXING_MCP_ROLE_TOOLS` changes when touched, and validation results.

## 2026-07-13

### Added Tools
- `lingxing_shipment_settlement_report`
  - Official API: `POST /cost/center/api/settlement/report`
  - Supports targeted queries by `sids` or `amazon_seller_ids`; if neither is provided, the service resolves all Amazon stores and submits the complete SID/seller ID arrays in one MCP call.
  - Automatically merges all pages with the official `offset/length` page size limit of 1000.
  - Defaults to `response_mode=summary`; `response_mode=full` is reserved for the local Excel exporter.
- `lingxing_sales_outbound_orders`
  - Official API: `POST /erp/sc/routing/wms/order/wmsOrderList`
  - Supports targeted queries by `sids` or `amazon_seller_ids`; if neither is provided, the service omits optional `sid_arr` for an all-store query in one MCP call.
  - Automatically merges all pages with the official `page/page_size` page size limit of 200.
  - Defaults to `response_mode=summary`; `response_mode=full` is reserved for the local Excel exporter.

### Export Orchestration
- Added `scripts/export_mcp_xlsx.py` and the dependency-free `lib/lingxing_openapi/xlsx_export.py` writer.
- Added `lib/lingxing_openapi/xlsx_profiles.py` with fixed ERP web-export layouts for the 52-column shipment settlement report, 56-column Transaction report, and 68-column sales outbound report.
- Extended the exporter to support the existing `lingxing_profit_report_order_list` tool. All three large-report tools now default to summary mode and reserve `response_mode=full` for the local exporter.
- One exporter run makes one MCP `tools/call`; all official pagination remains inside the MCP service, and the client does not loop over SID or seller ID.
- Full records stay inside the exporter process. Terminal and MCP text content contain compact metadata only, while the generated `.xlsx` includes all verified rows.
- The exporter uses an explicit non-secret User-Agent so Cloudflare does not reject Python's default `urllib` signature with error 1010.
- Added `docs/mcp-excel-export.md` with MCP-only Codex prompting, authentication sources, targeted/full-store examples, pagination guarantees, and truncation checks.
- Long identifiers are written as text; empty reports retain fixed headers; outbound `product_info` is expanded to product rows with order-level vertical merges.
- Columns shown by ERP but absent from the corresponding OpenAPI response remain blank and are reported in `unavailable_columns`; the exporter does not guess finance values by joining unrelated reports.
- Real-export reconciliation confirmed that the outbound OpenAPI omits the ERP `库位` column; it is retained as a blank, explicitly unavailable field.
- Corrected outbound ERP field semantics for order type codes 2/3, full consignee address, product-level declaration currency, and declaration weight with the web-export `g` suffix.

### Existing Tool Changes
- `lingxing_profit_report_order_list`: added compact `response_mode` and `preview_limit` behavior for safe large-result handling; no endpoint change.
- `lingxing_shipment_settlement_report`: all-store selection now sends only active (`status=1`) Amazon stores. Explicit SID or seller-ID filters can still target inactive stores. Selected stores are grouped by `marketplace_code` inside the service before pagination because a mixed-marketplace request can return an empty result; clients still make one MCP call.
- `lingxing_sales_outbound_orders`: no MCP schema change; Excel output now follows the ERP web export and expands product details.

### Removed Tools
- None

### Built-In Role Allowlist Changes
- `operations`: 73 -> 75
  - Added: `lingxing_shipment_settlement_report`, `lingxing_sales_outbound_orders`
  - Removed: None
- `finance`: 19 -> 22
  - Added: `lingxing_shipment_settlement_report`, `lingxing_sales_outbound_orders`, existing tool `lingxing_profit_report_order_list`
  - Removed: None
- `minimal`: no change

### Active Production Role Snapshot
- `operations`: production override updated to include both new tools.
- `finance`: both new tools and the existing Transaction tool are available through built-in role defaults.
- Tool descriptions use MCP invocation language and do not instruct agents to operate the Lingxing browser UI.

### Validation
- `python -m compileall -q lib mcp-servers scripts skills` passed locally and remotely.
- OpenAPI/client/service tests passed locally and remotely: 41 tests.
- MCP/auth/server tests passed locally and remotely: 8 tests.
- `validate_role_permissions.py` passed with `minimal_count=13`, `operations_count=75`, and `finance_count=22`.
- Production `LINGXING_MCP_ROLE_TOOLS` was backed up at `/etc/lingxing-mcp/lingxing-mcp.env.backup-20260713223531`; `operations` was updated from 73 to 75 tools, while `codex_ads_test` remained at 28.
- `lingxing-mcp.service` restarted successfully and remained `active`; `/healthz` reported 15 active member tokens.
- Live HTTP MCP `tools/list` returned 75 tools for `operations` and 22 for `finance`. Both roles included all three exportable report tools, `response_mode`, and visible `限流：` guidance.
- The first all-store shipment settlement smoke test returned zero rows. Further live diagnosis showed the decisive upstream behavior: 20 active US stores returned 6314 rows, while a mixed-marketplace array returned zero. The service now groups by marketplace internally; active-store filtering remains in place to keep the default scope operationally correct.
- Final all-store shipment settlement export returned 7006 data rows across 23 upstream pages. Its 52-column header exactly matched the ERP workbook, and all 6290 ERP sample keys `(订单号, 配送编号, MSKU)` were present in the MCP export.
- Final Transaction export returned 8958 rows across 9 upstream pages. Its 56-column/two-row header and complete row multiset exactly matched the ERP workbook after applying the ERP percentage display format.
- Final sales outbound export returned 729 orders across 4 upstream pages and expanded them to 786 product rows. The overlapping ERP sample order matched all 68 columns except `库位`, which the OpenAPI does not return and the exporter now reports as unavailable.
- MCP-only Excel comparison for sales outbound orders used the same date range: all stores returned 729 rows across 4 pages, while SID 7806 returned 79 rows across 1 page. All 79 filtered `wo_number` values were present in the all-store workbook, and every filtered row had SID 7806.
- The two comparison workbooks were generated without printing record JSON: `lingxing-sales-outbound-all-2026-06.xlsx` and `lingxing-sales-outbound-sid-7806-2026-06.xlsx`.
- The required release audit could not run because neither `/public/_templates/scripts/release_audit.py` nor `/public/lingxing-mcp/scripts/release_audit.py` exists. This repository/template gap is recorded rather than reported as a passing audit.

## 2026-07-08

### Added Tools
- `lingxing_voice_of_buyer`
  - Official API: `POST /basicOpen/customerService/voiceOfBuyer/list`
  - Purpose: dedicated buyer voice list query for ASIN/MSKU/SKU health, NCX metrics, satisfaction status, return reason, and return badge.

### Removed Tools
- None

### Built-In Role Allowlist Changes
- `operations`: 72 -> 73
  - Added: `lingxing_voice_of_buyer`
  - Removed: None
- `minimal`: no change
- `finance`: no change

### Active Production Role Snapshot
- `codex_ads_test`: unchanged in production override.
- `operations`: 73 tools through the active `LINGXING_MCP_ROLE_TOOLS` override.

Notable production role exposure:
- `operations` includes `lingxing_voice_of_buyer` through the active `LINGXING_MCP_ROLE_TOOLS` override.

### Validation
- `python -m compileall -q lib mcp-servers skills` passed locally.
- `python -m unittest discover -s skills/zach-lingxing-openapi-client/tests -v` passed locally.
- `python -m unittest discover -s skills/zach-lingxing-mcp/tests -v` passed locally.
- `python mcp-servers/lingxing-openapi/deploy/validate_role_permissions.py` passed locally with `operations_count=73` and `finance_count=19`.
- The same compile, role validation, OpenAPI client tests, and MCP server tests passed remotely.
- Tool snapshot regenerated from `LingxingMCPApplication`.
- Production `LINGXING_MCP_ROLE_TOOLS` was updated and backed up at `/etc/lingxing-mcp/lingxing-mcp.env.backup-20260708162518`.
- `lingxing-mcp.service` was restarted; service was `active`.
- Remote loopback `tools/list` returned 73 tools for `operations`, included `lingxing_voice_of_buyer`, and showed visible `限流：` guidance.
- Remote loopback `tools/call` for `lingxing_voice_of_buyer` reached `/basicOpen/customerService/voiceOfBuyer/list` with `ok=true`, `page_count=1`, and zero rows for the narrow sid 7806 + ASIN `B0DX74Z1MR` smoke filter.

## 2026-07-08

### Added Tools
- None; this change exposes existing registered tools to additional roles.

### Removed Tools
- None

### Built-In Role Allowlist Changes
- `operations`: 67 -> 72
  - Added: `lingxing_source_transaction`, `lingxing_report_export_create`, `lingxing_report_export_query`, `lingxing_report_export_download`, `lingxing_report_export_refresh_url`
  - Removed: None
- `finance`: 15 -> 19
  - Added: `lingxing_report_export_create`, `lingxing_report_export_query`, `lingxing_report_export_download`, `lingxing_report_export_refresh_url`
  - Already present: `lingxing_source_transaction`
  - Removed: None
- `minimal`: no change

### Active Production Role Snapshot
- `codex_ads_test`: 28 tools
- `operations`: 72 tools
- `finance`: 19 tools through built-in role defaults.

Notable production role exposure:
- `operations` includes `lingxing_source_transaction`, `lingxing_report_export_create`, `lingxing_report_export_query`, `lingxing_report_export_download`, and `lingxing_report_export_refresh_url` through the active `LINGXING_MCP_ROLE_TOOLS` override.
- `finance` includes the same five tools through the built-in role defaults.

### Validation
- `python -m compileall -q lib mcp-servers` passed locally and remotely.
- `python -m unittest discover -s skills/zach-lingxing-openapi-client/tests -v` passed locally and remotely.
- `python -m unittest discover -s skills/zach-lingxing-mcp/tests -v` passed locally and remotely.
- `python mcp-servers/lingxing-openapi/deploy/validate_role_permissions.py` passed with `operations_count=72` and `finance_count=19`.
- Tool snapshot regenerated from `LingxingMCPApplication`.
- Production `LINGXING_MCP_ROLE_TOOLS` was updated and backed up at `/etc/lingxing-mcp/lingxing-mcp.env.backup-20260708152803`.
- `lingxing-mcp.service` was restarted; service was `active/running`.
- Remote loopback `tools/list` returned 72 tools for `operations` and 19 tools for `finance`; both roles included all five requested tools with visible `req/s` rate-limit guidance on report export tools.

## 2026-07-03

### Added Tools
- `lingxing_ads_sp_negative_targets_or_keywords`
- `lingxing_ads_sd_negative_targets`
- `lingxing_ads_sb_negative_keywords`
- `lingxing_ads_sb_negative_targets`
- `lingxing_ads_operation_logs`
- `lingxing_ads_update_sp_campaign`
- `lingxing_ads_update_sp_ad_group`
- `lingxing_ads_update_sp_keyword`
- `lingxing_ads_update_sp_target`
- `lingxing_ads_update_sp_product_ads`
- `lingxing_ads_add_sp_keywords`
- `lingxing_ads_add_sp_negative_keywords`
- `lingxing_ads_add_sp_negative_targets`
- `lingxing_ads_archive_sp_negatives`

### Removed Tools
- None

### Built-In Role Allowlist Changes
- `operations`: 13 -> 67
  - Added: approved advertising read tools, negative targeting read tools, `lingxing_asin_ads_daily_rollup`, selected non-hourly `lingxing_exp_ads_*` daily reports, `lingxing_ads_operation_logs`, and gated SP advertising management tools.
  - Excluded by design: hourly advertising reports, `lingxing_asin_weekly_rollup`, and `lingxing_exp_ads_aba_report`.
- `minimal`: no change
- `finance`: no change

### Active Production Role Snapshot
- `codex_ads_test`: 28 tools
- `operations`: 67 tools

Notable production role exposure:
- `operations` includes the approved advertising read tools and gated SP advertising management tools through the active `LINGXING_MCP_ROLE_TOOLS` override.
- `operations` intentionally excludes hourly advertising reports, `lingxing_asin_weekly_rollup`, and `lingxing_exp_ads_aba_report`.

### Safety Notes
- SP advertising management tools default to `dry_run=true`.
- A Lingxing write endpoint is called only when a request includes `confirm=true` and `dry_run=false`.
- Dry-run responses return the prepared request body and an execution warning without calling Lingxing.

### Validation
- `python -m unittest skills.zach-lingxing-openapi-client.tests.test_lingxing_services` passed.
- `python -m unittest skills.zach-lingxing-mcp.tests.test_mcp_server` passed.
- `python mcp-servers/lingxing-openapi/deploy/validate_role_permissions.py` passed with `operations_count=67`.
- Local operations `tools/list` returned 67 tools and excluded hourly advertising reports, `lingxing_asin_weekly_rollup`, and `lingxing_exp_ads_aba_report`.
- Tool snapshot regenerated from `LingxingMCPApplication`.
- Release audit template `../_templates/scripts/release_audit.py` was not available in the remote deployment directory, so release audit could not be run.
- Production `LINGXING_MCP_ROLE_TOOLS` was updated and backed up at `/etc/lingxing-mcp/lingxing-mcp.env.backup-20260703104448`.
- `lingxing-mcp.service` was restarted; service was `active/running`.
- Remote loopback operations `tools/list` returned 67 tools, included the new advertising management tools, had visible `req/s` rate-limit guidance, and excluded hourly advertising reports, `lingxing_asin_weekly_rollup`, and `lingxing_exp_ads_aba_report`.
- Live dry-run call to `lingxing_ads_update_sp_keyword` returned `executed=false` and warning `dry_run=true 或 confirm 未开启，未调用领星广告写接口。`

## 2026-07-02

### Added Tools
- `lingxing_multi_channel_orders`

### Removed Tools
- None

### Built-In Role Allowlist Changes
- `operations`: 12 -> 13
  - Added: `lingxing_multi_channel_orders`
  - Removed: None
- `minimal`: no change
- `finance`: no change

### Active Production Role Snapshot
- `codex_ads_test`: 31 tools
- `finance`: 15 tools
- `minimal`: 13 tools
- `operations`: 26 tools

Notable production role exposure:
- `operations` includes `lingxing_multi_channel_orders` through the active `LINGXING_MCP_ROLE_TOOLS` override.
- `lingxing_multi_channel_orders` is backed by `/order/amzod/api/orderList` and can optionally enrich records with product, logistics, return, and transaction detail endpoints.

### Validation
- `python -m compileall -q lib mcp-servers` passed.
- `python -m unittest discover -s skills/zach-lingxing-openapi-client/tests -v` passed.
- `python -m unittest discover -s skills/zach-lingxing-mcp/tests -v` passed.
- `python mcp-servers/lingxing-openapi/deploy/validate_role_permissions.py` passed.
- Tool snapshot regenerated from `LingxingMCPApplication` and active role allowlists.
- Production `LINGXING_MCP_ROLE_TOOLS` was updated and backed up at `/etc/lingxing-mcp/lingxing-mcp.env.backup-20260702170637`.
- `lingxing-mcp.service` was restarted; service was `active/running`.
- Live operations `tools/list` returned 26 tools and included `lingxing_multi_channel_orders` with visible `限流：` guidance.
- Live `tools/call` reached `/order/amzod/api/orderList`; Lingxing upstream returned `code=500 | 失败` for the small sid/date smoke request, so endpoint permission/data behavior still needs upstream-side follow-up before treating this as data-ready.

## 2026-06-30

### Added Tools
- `lingxing_amazon_listing`
- `lingxing_profit_report_order_list`
- `lingxing_refund_orders`
- `lingxing_return_analysis`

### Removed Tools
- None

### Built-In Role Allowlist Changes
- `minimal`: 12 -> 13
  - Added: `lingxing_amazon_listing`
  - Removed: None
- `operations`: 11 -> 12
  - Added: `lingxing_profit_report_order_list`
  - Removed: None

### Active Production Role Snapshot
- `codex_ads_test`: 31 tools
- `finance`: 15 tools
- `minimal`: 13 tools
- `operations`: 25 tools

Notable production role exposure:
- `operations` includes `lingxing_amazon_listing`, `lingxing_profit_report_order_list`, `lingxing_refund_orders`, and `lingxing_return_analysis` through the active `LINGXING_MCP_ROLE_TOOLS` override.
- `codex_ads_test` includes `lingxing_amazon_listing` through the active `LINGXING_MCP_ROLE_TOOLS` override.

### Validation
- `python3 -m py_compile lib/lingxing_openapi/endpoint_specs.py lib/lingxing_openapi/services.py lib/lingxing_openapi/mcp.py` passed.
- Tool snapshot regenerated from `LingxingMCPApplication` and active role allowlists.
- `lingxing-mcp.service` was restarted after adding `lingxing_profit_report_order_list`; service was `active/running`.
