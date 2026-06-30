# Lingxing MCP Update Log

This log records MCP tool-surface changes. Each entry must list added tools, removed tools, and role allowlist changes.

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
