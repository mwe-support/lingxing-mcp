#!/usr/bin/env bash
set -euo pipefail

TAILSCALE_HOSTNAME="${TAILSCALE_HOSTNAME:-lingxing-mcp-hk}"
TAILSCALE_ENABLE_SSH="${TAILSCALE_ENABLE_SSH:-0}"
TAILSCALE_ADVERTISE_TAGS="${TAILSCALE_ADVERTISE_TAGS:-}"
TAILSCALE_ACCEPT_ROUTES="${TAILSCALE_ACCEPT_ROUTES:-0}"

usage() {
  cat <<'EOF'
用法：
  sudo bash mcp-servers/lingxing-openapi/deploy/install_tailscale_on_ubuntu.sh

说明：
  在 Ubuntu 服务器上安装 Tailscale，并在提供 TAILSCALE_AUTH_KEY 时自动加入 tailnet。

可通过环境变量注入：
  TAILSCALE_AUTH_KEY        可选。提供后自动执行 tailscale up
  TAILSCALE_HOSTNAME        可选。默认 lingxing-mcp-hk
  TAILSCALE_ENABLE_SSH      可选。1 表示启用 tailscale ssh，默认 0
  TAILSCALE_ADVERTISE_TAGS  可选。逗号分隔，例如 tag:ops,tag:lingxing
  TAILSCALE_ACCEPT_ROUTES   可选。1 表示 tailscale up 时带 --accept-routes，默认 0
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $EUID -ne 0 ]]; then
  echo "请使用 root 或 sudo 运行。" >&2
  exit 1
fi

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y curl ca-certificates

curl -fsSL https://tailscale.com/install.sh | sh
systemctl enable --now tailscaled

if [[ -n "${TAILSCALE_AUTH_KEY:-}" ]]; then
  cmd=(tailscale up --reset --authkey "${TAILSCALE_AUTH_KEY}" --hostname "${TAILSCALE_HOSTNAME}")
  if [[ "$TAILSCALE_ENABLE_SSH" == "1" ]]; then
    cmd+=(--ssh)
  fi
  if [[ -n "$TAILSCALE_ADVERTISE_TAGS" ]]; then
    cmd+=(--advertise-tags "${TAILSCALE_ADVERTISE_TAGS}")
  fi
  if [[ "$TAILSCALE_ACCEPT_ROUTES" == "1" ]]; then
    cmd+=(--accept-routes)
  fi
  "${cmd[@]}"
fi

echo
echo "Tailscale 安装完成。"
if command -v tailscale >/dev/null 2>&1; then
  tailscale version || true
  echo
  tailscale ip -4 || true
  echo
fi

if [[ -z "${TAILSCALE_AUTH_KEY:-}" ]]; then
  echo "尚未加入 tailnet。下一步："
  echo "  sudo tailscale up --hostname ${TAILSCALE_HOSTNAME}"
  if [[ "$TAILSCALE_ENABLE_SSH" == "1" ]]; then
    echo "如需启用 Tailscale SSH，可追加 --ssh"
  fi
fi
