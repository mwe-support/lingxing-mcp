# LingXing OpenAPI MCP

> GitHub README draft only. Do not publish before final review.

LingXing OpenAPI MCP is a read-only MCP server for LingXing ERP. It wraps LingXing OpenAPI into a consistent MCP tool set so agents and IDE clients can query store lists, sales, orders, marketplaces, and promotion data through a fixed-egress gateway.

## Why This Exists

LingXing OpenAPI is powerful, but many teams run into the same two deployment problems:

- API access is constrained by IP whitelist rules
- multiple teammates need the same data from different locations and networks

This project solves that by combining:

- a fixed-egress HTTP gateway
- a local stdio MCP mode
- normalized read-only business tools
- promotion-type classification for daily operations

## What It Supports

- health check and smoke check
- seller lists
- marketplaces with timezone mapping
- store sales
- ASIN daily metrics
- orders
- promotion listing
- Lightning Deal / Best Deal classification
- coupon / managed promotion / discount classification
- daily promotion resolution per ASIN

## Deployment Modes

### 1. Local stdio

Run the MCP server locally and connect from an MCP client that supports stdio.

### 2. Shared HTTP gateway

Run the server on a fixed-egress machine and let teammates connect through a secure local bridge or tunnel. This is the recommended mode when LingXing enforces IP whitelist restrictions.

## Authentication

This project supports:

- single bootstrap bearer token
- multi-member token file for team sharing

Multi-token mode is recommended for team environments because individual member tokens can be revoked or rotated without affecting everyone else.

## Security Boundaries

- read-only by design in P0
- no write endpoints
- no business credentials on teammate laptops
- fixed-egress gateway recommended for whitelist stability

## Quick Start

### Start local stdio mode

```bash
python3 mcp-servers/lingxing-openapi/server.py
```

### Start HTTP mode

```bash
python3 mcp-servers/lingxing-openapi/http_server.py \
  --host 127.0.0.1 \
  --port 8099 \
  --bearer-token "replace-me"
```

Or use a member token file:

```bash
python3 mcp-servers/lingxing-openapi/http_server.py \
  --host 127.0.0.1 \
  --port 8099 \
  --tokens-file /etc/lingxing-mcp/tokens.json
```

## Public Example Files

See:

- `examples/public/gateway.env.example`
- `examples/public/tokens.example.json`
- `examples/public/claude_code.mcp.json`
- `examples/public/cursor.mcp.json`
- `examples/public/claude_desktop_http_config.json`

## FAQ

### Does this bypass LingXing authorization?

No. It improves deployment and reuse, but does not bypass LingXing authorization, permissions, or whitelist rules.

### Is this suitable for team sharing?

Yes, especially in fixed-egress mode with per-member tokens.

### Does it support write operations?

Not in this version. P0 is read-only.

## Status

Prepared for public release, but not published yet.
