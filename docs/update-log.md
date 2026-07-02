# Lingxing MCP Update Log

This log records MCP tool-surface changes. Each entry must list added tools, removed tools, and role allowlist changes.

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
