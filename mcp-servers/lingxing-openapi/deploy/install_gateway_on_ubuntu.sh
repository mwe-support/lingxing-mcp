#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/opt/lingxing-mcp/current"
SERVICE_NAME="lingxing-mcp"
SERVICE_USER="lingxing-mcp"
ENV_FILE="/etc/lingxing-mcp.env"
TEMPLATE_PATH="mcp-servers/lingxing-openapi/deploy/lingxing-mcp.service.template"
DEFAULT_HOST="${LINGXING_MCP_HOST:-127.0.0.1}"
DEFAULT_PORT="${LINGXING_MCP_PORT:-8099}"

usage() {
  cat <<'EOF'
用法：
  sudo bash mcp-servers/lingxing-openapi/deploy/install_gateway_on_ubuntu.sh [选项]

选项：
  --repo-dir PATH        服务器上的仓库目录，默认 /opt/lingxing-mcp/current
  --service-name NAME    systemd 服务名，默认 lingxing-mcp
  --service-user NAME    运行服务的 Linux 用户，默认 lingxing-mcp
  --env-file PATH        环境变量文件，默认 /etc/lingxing-mcp.env

可通过环境变量直接注入：
  LINGXING_APP_ID
  LINGXING_APP_SECRET
  LINGXING_TOKEN_CACHE_FILE
  LINGXING_MCP_BEARER_TOKEN
  LINGXING_MCP_TOKENS_FILE
  LINGXING_MCP_HOST
  LINGXING_MCP_PORT
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-dir)
      REPO_DIR="$2"
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
    *)
      echo "未知参数: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ $EUID -ne 0 ]]; then
  echo "请使用 root 或 sudo 运行。" >&2
  exit 1
fi

if [[ ! -f "$REPO_DIR/$TEMPLATE_PATH" ]]; then
  echo "未找到模板文件：$REPO_DIR/$TEMPLATE_PATH" >&2
  echo "请先把仓库同步到服务器，再运行本脚本。" >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y python3 python3-venv curl rsync ca-certificates

if ! id -u "$SERVICE_USER" >/dev/null 2>&1; then
  useradd --system --home /var/lib/lingxing-mcp --shell /usr/sbin/nologin "$SERVICE_USER"
fi

mkdir -p /var/lib/lingxing-mcp /var/log/lingxing-mcp
chown -R "$SERVICE_USER:$SERVICE_USER" /var/lib/lingxing-mcp /var/log/lingxing-mcp

TOKEN_CACHE_FILE="${LINGXING_TOKEN_CACHE_FILE:-/var/lib/lingxing-mcp/token_cache.json}"
TOKENS_FILE="${LINGXING_MCP_TOKENS_FILE:-/etc/lingxing-mcp/tokens.json}"
mkdir -p "$(dirname "$TOKEN_CACHE_FILE")"
chown -R "$SERVICE_USER:$SERVICE_USER" "$(dirname "$TOKEN_CACHE_FILE")"
mkdir -p "$(dirname "$TOKENS_FILE")"
chown -R "$SERVICE_USER:$SERVICE_USER" "$(dirname "$TOKENS_FILE")"
if [[ ! -f "$TOKENS_FILE" ]]; then
  cat >"$TOKENS_FILE" <<'EOF'
{
  "version": 1,
  "tokens": []
}
EOF
  chown "$SERVICE_USER:$SERVICE_USER" "$TOKENS_FILE"
  chmod 600 "$TOKENS_FILE"
fi

cat >"$ENV_FILE" <<EOF
LINGXING_APP_ID=${LINGXING_APP_ID:-replace-me}
LINGXING_APP_SECRET=${LINGXING_APP_SECRET:-replace-me}
LINGXING_TOKEN_CACHE_FILE=${TOKEN_CACHE_FILE}
LINGXING_MCP_BEARER_TOKEN=${LINGXING_MCP_BEARER_TOKEN:-replace-me}
LINGXING_MCP_TOKENS_FILE=${TOKENS_FILE}
LINGXING_MCP_HOST=${DEFAULT_HOST}
LINGXING_MCP_PORT=${DEFAULT_PORT}
PYTHONUNBUFFERED=1
EOF
chmod 600 "$ENV_FILE"

SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
sed \
  -e "s#__SERVICE_USER__#${SERVICE_USER}#g" \
  -e "s#__REPO_DIR__#${REPO_DIR}#g" \
  -e "s#__ENV_FILE__#${ENV_FILE}#g" \
  "$REPO_DIR/$TEMPLATE_PATH" >"$SERVICE_FILE"

systemctl daemon-reload
systemctl enable --now "${SERVICE_NAME}.service"

echo
echo "部署完成。"
echo "服务名: ${SERVICE_NAME}.service"
echo "环境文件: ${ENV_FILE}"
echo "仓库目录: ${REPO_DIR}"
echo
echo "下一步："
echo "1. 运行 mcp-servers/lingxing-openapi/deploy/check_egress_ip.sh，拿到服务器公网 IP"
echo "2. 把这个公网 IP 加入领星 OpenAPI 白名单"
echo "3. 运行 mcp-servers/lingxing-openapi/deploy/verify_gateway.sh 做本地验证"
echo
echo "如果当前 env 文件里还是 replace-me，请先把真实值填进去，再执行："
echo "  sudo systemctl restart ${SERVICE_NAME}.service"
