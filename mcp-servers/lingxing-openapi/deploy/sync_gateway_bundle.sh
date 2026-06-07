#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
REMOTE="${1:-}"
REMOTE_DIR="${2:-/public/lingxing-mcp}"

if [[ -z "$REMOTE" ]]; then
  cat <<'EOF' >&2
用法：
  bash mcp-servers/lingxing-openapi/deploy/sync_gateway_bundle.sh user@server [/public/lingxing-mcp]

说明：
  该脚本会把运行领星 MCP 所需的最小代码集同步到远端服务器。
EOF
  exit 1
fi

ssh "$REMOTE" "sudo mkdir -p '$REMOTE_DIR' && sudo chown -R \$(id -un):\$(id -gn) '$REMOTE_DIR' && [ ! -d '$REMOTE_DIR/Users' ] || rm -rf '$REMOTE_DIR/Users' && rm -rf '$REMOTE_DIR/amazon_spapi' '$REMOTE_DIR/lingxing_openapi' '$REMOTE_DIR/deploy' '$REMOTE_DIR/http_server.py' '$REMOTE_DIR/server.py' '$REMOTE_DIR/README.md'"
(
  cd "$ROOT_DIR"
  rsync -az --delete --relative \
    "./lib" \
    "./mcp-servers/lingxing-openapi" \
    "$REMOTE:$REMOTE_DIR/"
)

echo "已同步到 $REMOTE:$REMOTE_DIR"
