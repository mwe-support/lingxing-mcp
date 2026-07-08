# Lingxing MCP Update Log

This log records MCP tool-surface changes. Each entry must list added tools, removed tools, built-in role allowlist changes, production `LINGXING_MCP_ROLE_TOOLS` changes when touched, and validation results.

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
