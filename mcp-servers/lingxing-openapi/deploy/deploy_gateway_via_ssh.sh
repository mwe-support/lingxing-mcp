#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
SYNC_SCRIPT="$ROOT_DIR/mcp-servers/lingxing-openapi/deploy/sync_gateway_bundle.sh"
REMOTE=""
REMOTE_DIR="/opt/lingxing-mcp/current"
SERVICE_NAME="lingxing-mcp"
SERVICE_USER="lingxing-mcp"
ENV_FILE="/etc/lingxing-mcp.env"

usage() {
  cat <<'EOF'
用法：
  bash mcp-servers/lingxing-openapi/deploy/deploy_gateway_via_ssh.sh [选项] user@server

说明：
  该脚本会在本机完成两件事：
  1. 把领星 MCP 最小运行代码同步到远端服务器
  2. 通过 SSH 调用远端安装脚本，完成 systemd 部署

必需环境变量：
  LINGXING_APP_ID
  LINGXING_APP_SECRET
  LINGXING_MCP_BEARER_TOKEN

可选环境变量：
  LINGXING_TOKEN_CACHE_FILE
  LINGXING_MCP_TOKENS_FILE
  LINGXING_MCP_HOST
  LINGXING_MCP_PORT
  TAILSCALE_AUTH_KEY
  TAILSCALE_HOSTNAME
  TAILSCALE_ENABLE_SSH

选项：
  --repo-dir PATH        远端仓库目录，默认 /opt/lingxing-mcp/current
  --service-name NAME    systemd 服务名，默认 lingxing-mcp
  --service-user NAME    systemd 运行用户，默认 lingxing-mcp
  --env-file PATH        远端环境文件，默认 /etc/lingxing-mcp.env
  -h, --help             显示帮助
EOF
}

require_env() {
  local name="$1"
  if [[ -z "${!name:-}" ]]; then
    echo "缺少环境变量：$name" >&2
    exit 1
  fi
}

escape() {
  printf '%q' "$1"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-dir)
      REMOTE_DIR="$2"
      shift 2
      ;;
    --service-name)
      SERVICE_NAME="$2"
      shift 2
      ;;
    --service-user)
      SERVICE_USER="$2"
      shift 2
      ;;
    --env-file)
      ENV_FILE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      echo "未知参数：$1" >&2
      usage
      exit 1
      ;;
    *)
      if [[ -n "$REMOTE" ]]; then
        echo "只能提供一个远端地址，当前多余参数：$1" >&2
        exit 1
      fi
      REMOTE="$1"
      shift
      ;;
  esac
done

if [[ -z "$REMOTE" ]]; then
  usage
  exit 1
fi

require_env "LINGXING_APP_ID"
require_env "LINGXING_APP_SECRET"
require_env "LINGXING_MCP_BEARER_TOKEN"

if [[ ! -x "$SYNC_SCRIPT" ]]; then
  echo "未找到同步脚本：$SYNC_SCRIPT" >&2
  exit 1
fi

TOKEN_CACHE_FILE="${LINGXING_TOKEN_CACHE_FILE:-/var/lib/lingxing-mcp/token_cache.json}"
TOKENS_FILE="${LINGXING_MCP_TOKENS_FILE:-/etc/lingxing-mcp/tokens.json}"
MCP_HOST="${LINGXING_MCP_HOST:-127.0.0.1}"
MCP_PORT="${LINGXING_MCP_PORT:-8099}"

echo "==> 同步运行代码到 ${REMOTE}:${REMOTE_DIR}"
bash "$SYNC_SCRIPT" "$REMOTE" "$REMOTE_DIR"

REMOTE_INSTALL_SCRIPT="${REMOTE_DIR}/mcp-servers/lingxing-openapi/deploy/install_gateway_on_ubuntu.sh"
REMOTE_IP_SCRIPT="${REMOTE_DIR}/mcp-servers/lingxing-openapi/deploy/check_egress_ip.sh"

APP_ID_ESC="$(escape "$LINGXING_APP_ID")"
APP_SECRET_ESC="$(escape "$LINGXING_APP_SECRET")"
BEARER_ESC="$(escape "$LINGXING_MCP_BEARER_TOKEN")"
TOKEN_CACHE_ESC="$(escape "$TOKEN_CACHE_FILE")"
TOKENS_FILE_ESC="$(escape "$TOKENS_FILE")"
HOST_ESC="$(escape "$MCP_HOST")"
PORT_ESC="$(escape "$MCP_PORT")"
REMOTE_DIR_ESC="$(escape "$REMOTE_DIR")"
SERVICE_NAME_ESC="$(escape "$SERVICE_NAME")"
SERVICE_USER_ESC="$(escape "$SERVICE_USER")"
ENV_FILE_ESC="$(escape "$ENV_FILE")"
REMOTE_INSTALL_ESC="$(escape "$REMOTE_INSTALL_SCRIPT")"
REMOTE_IP_ESC="$(escape "$REMOTE_IP_SCRIPT")"

echo "==> 远端安装 systemd 服务"
ssh "$REMOTE" \
  "sudo env \
    LINGXING_APP_ID=${APP_ID_ESC} \
    LINGXING_APP_SECRET=${APP_SECRET_ESC} \
    LINGXING_MCP_BEARER_TOKEN=${BEARER_ESC} \
    LINGXING_TOKEN_CACHE_FILE=${TOKEN_CACHE_ESC} \
    LINGXING_MCP_TOKENS_FILE=${TOKENS_FILE_ESC} \
    LINGXING_MCP_HOST=${HOST_ESC} \
    LINGXING_MCP_PORT=${PORT_ESC} \
    bash ${REMOTE_INSTALL_ESC} \
      --repo-dir ${REMOTE_DIR_ESC} \
      --service-name ${SERVICE_NAME_ESC} \
      --service-user ${SERVICE_USER_ESC} \
      --env-file ${ENV_FILE_ESC}"

echo
echo "==> 远端出口公网 IP"
ssh "$REMOTE" "bash ${REMOTE_IP_ESC}"
echo
echo "下一步："
echo "1. 把上面的公网出口 IP 加入领星 OpenAPI 白名单"
echo "2. 如需安装 Tailscale，可执行："
echo "   TAILSCALE_AUTH_KEY=... bash ${ROOT_DIR}/mcp-servers/lingxing-openapi/deploy/install_tailscale_via_ssh.sh ${REMOTE}"
echo "3. 白名单生效后，执行："
echo "   ssh ${REMOTE} 'bash ${REMOTE_DIR}/mcp-servers/lingxing-openapi/deploy/verify_gateway.sh http://127.0.0.1:${MCP_PORT} ${LINGXING_MCP_BEARER_TOKEN} 1'"
echo "4. 需要团队多人令牌时，执行："
echo "   ssh ${REMOTE} 'python3 ${REMOTE_DIR}/mcp-servers/lingxing-openapi/deploy/manage_tokens.py --tokens-file ${TOKENS_FILE} list'"
