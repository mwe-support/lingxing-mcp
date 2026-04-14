#!/usr/bin/env bash
set -euo pipefail

PUBLIC_IP=""
if PUBLIC_IP="$(curl -fsS https://api.ipify.org)"; then
  :
elif PUBLIC_IP="$(curl -fsS https://ifconfig.me)"; then
  :
else
  echo "无法获取公网出口 IP，请检查服务器网络。" >&2
  exit 1
fi

echo "当前服务器公网出口 IP: ${PUBLIC_IP}"
echo "请把这个 IP 加入领星 OpenAPI 白名单。"
