#!/usr/bin/env bash
set -euo pipefail

ENV_FILE="${LINGXING_LOCAL_ENV_FILE:-$HOME/.config/lingxing-mcp/client.env}"
REMOTE_URL="${LINGXING_LOCAL_MCP_URL:-http://127.0.0.1:18099/mcp}"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "missing_env_file: $ENV_FILE" >&2
  exit 1
fi

set -a
source "$ENV_FILE"
set +a

: "${LINGXING_AUTH_HEADER:?missing LINGXING_AUTH_HEADER in $ENV_FILE}"

exec /opt/homebrew/bin/npx -y mcp-remote@latest \
  "$REMOTE_URL" \
  --allow-http \
  --transport http-only \
  --header "Authorization:${LINGXING_AUTH_HEADER}" \
  --silent
