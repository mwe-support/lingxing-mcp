#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${1:-http://127.0.0.1:8099}"
BEARER_TOKEN="${2:-${LINGXING_MCP_BEARER_TOKEN:-}}"
RUN_SMOKE="${3:-0}"

if [[ -z "$BEARER_TOKEN" ]]; then
  echo "缺少 Bearer Token。用法：" >&2
  echo "  bash mcp-servers/lingxing-openapi/deploy/verify_gateway.sh http://127.0.0.1:8099 your-token [0|1]" >&2
  exit 1
fi

echo "==> healthz"
curl -fsS "${BASE_URL}/healthz"
echo
echo

echo "==> lingxing_health_check"
curl -fsS \
  -H "Authorization: Bearer ${BEARER_TOKEN}" \
  -H "Content-Type: application/json" \
  -X POST \
  "${BASE_URL}/mcp" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"lingxing_health_check","arguments":{}}}'
echo
echo

if [[ "$RUN_SMOKE" == "1" ]]; then
  echo "==> lingxing_smoke_check"
  curl -fsS \
    -H "Authorization: Bearer ${BEARER_TOKEN}" \
    -H "Content-Type: application/json" \
    -X POST \
    "${BASE_URL}/mcp" \
    -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"lingxing_smoke_check","arguments":{}}}'
  echo
fi
