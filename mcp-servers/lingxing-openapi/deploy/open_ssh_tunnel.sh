#!/usr/bin/env bash
set -euo pipefail

REMOTE="${1:-}"
LOCAL_PORT="${2:-8099}"
REMOTE_PORT="${3:-8099}"

usage() {
  cat <<'EOF'
用法：
  bash mcp-servers/lingxing-openapi/deploy/open_ssh_tunnel.sh user@server [local_port] [remote_port]

说明：
  在本机建立一个 SSH Tunnel，把本地端口转发到远端服务器上的领星 MCP HTTP 服务。
  这个 user@server 可以是公网 IP，也可以是 Tailscale 主机名 / 100.x 地址。
EOF
}

if [[ -z "$REMOTE" || "$REMOTE" == "-h" || "$REMOTE" == "--help" ]]; then
  usage
  exit 0
fi

echo "本地访问地址：http://127.0.0.1:${LOCAL_PORT}"
echo "保持这个终端窗口开启，按 Ctrl+C 可关闭隧道。"
echo

exec ssh -N -L "${LOCAL_PORT}:127.0.0.1:${REMOTE_PORT}" "$REMOTE"
