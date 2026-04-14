#!/usr/bin/env bash
set -euo pipefail

REMOTE=""
REMOTE_DIR="/opt/lingxing-mcp/current"
TAILSCALE_HOSTNAME="${TAILSCALE_HOSTNAME:-lingxing-mcp-hk}"
TAILSCALE_ENABLE_SSH="${TAILSCALE_ENABLE_SSH:-0}"
TAILSCALE_ADVERTISE_TAGS="${TAILSCALE_ADVERTISE_TAGS:-}"
TAILSCALE_ACCEPT_ROUTES="${TAILSCALE_ACCEPT_ROUTES:-0}"

usage() {
  cat <<'EOF'
用法：
  bash mcp-servers/lingxing-openapi/deploy/install_tailscale_via_ssh.sh [选项] user@server

说明：
  通过 SSH 在远端 Ubuntu 服务器上安装 Tailscale。
  如果设置了 TAILSCALE_AUTH_KEY，会自动把服务器加入 tailnet。

选项：
  --repo-dir PATH   远端仓库目录，默认 /opt/lingxing-mcp/current
  -h, --help        显示帮助

可选环境变量：
  TAILSCALE_AUTH_KEY
  TAILSCALE_HOSTNAME
  TAILSCALE_ENABLE_SSH
  TAILSCALE_ADVERTISE_TAGS
  TAILSCALE_ACCEPT_ROUTES
EOF
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

REMOTE_SCRIPT="${REMOTE_DIR}/mcp-servers/lingxing-openapi/deploy/install_tailscale_on_ubuntu.sh"

AUTH_KEY_ESC="$(escape "${TAILSCALE_AUTH_KEY:-}")"
HOST_ESC="$(escape "$TAILSCALE_HOSTNAME")"
ENABLE_SSH_ESC="$(escape "$TAILSCALE_ENABLE_SSH")"
TAGS_ESC="$(escape "$TAILSCALE_ADVERTISE_TAGS")"
ACCEPT_ESC="$(escape "$TAILSCALE_ACCEPT_ROUTES")"
REMOTE_SCRIPT_ESC="$(escape "$REMOTE_SCRIPT")"

ssh "$REMOTE" \
  "sudo env \
    TAILSCALE_AUTH_KEY=${AUTH_KEY_ESC} \
    TAILSCALE_HOSTNAME=${HOST_ESC} \
    TAILSCALE_ENABLE_SSH=${ENABLE_SSH_ESC} \
    TAILSCALE_ADVERTISE_TAGS=${TAGS_ESC} \
    TAILSCALE_ACCEPT_ROUTES=${ACCEPT_ESC} \
    bash ${REMOTE_SCRIPT_ESC}"
