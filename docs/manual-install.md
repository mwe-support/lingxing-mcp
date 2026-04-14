# Manual Install

如果你不想让 AI 自动帮你接入，也可以手动配置。

> [!WARNING]
> 手动安装时最容易出问题的不是命令本身，而是把真实凭证填进示例文件后又继续传播或提交到 Git。
>
> - 不要把真实 `APP ID / AppSecret` 写回公开示例
> - 不要把真实 Bearer 或 `tokens.json` 发群
> - 不要把真实服务器 IP 和内部地址直接截图公开

如果你还没理解为什么要固定出口、领星后台要做什么，建议先看：

- [../README.md](../README.md)
- [./admin-setup.md](./admin-setup.md)
- [./tencent-cloud-buying-guide.md](./tencent-cloud-buying-guide.md)

## 方式 1：本地 stdio 模式

适合你自己本机持有领星 OpenAPI 凭证，并希望直接本地跑 MCP。
这条路线默认只是 **个人验证模式**。

1. 准备环境变量：
   - `LINGXING_APP_ID`
   - `LINGXING_APP_SECRET`
   - `LINGXING_TOKEN_CACHE_FILE`
2. 启动本地 MCP：

```bash
python3 mcp-servers/lingxing-openapi/server.py
```

3. 参考以下示例，把 MCP 接到你的 IDE：
   - `mcp-servers/lingxing-openapi/examples/public/claude_code.mcp.json`
   - `mcp-servers/lingxing-openapi/examples/public/cursor.mcp.json`

> 提醒：
> 本地 `stdio` 更适合个人验证和试跑。  
> 如果你是团队共享或白名单受限场景，不要把它当主方案，更推荐直接走下面的 `HTTP gateway`。

## 方式 2：HTTP gateway 模式

适合团队共享或受 IP 白名单限制的场景。
这也是当前公开版默认推荐的主路线。

1. 在固定出口服务器上准备：
   - `LINGXING_APP_ID`
   - `LINGXING_APP_SECRET`
   - `LINGXING_TOKEN_CACHE_FILE`
   - `LINGXING_MCP_TOKENS_FILE`
2. 启动 HTTP MCP：

```bash
python3 mcp-servers/lingxing-openapi/http_server.py --host 127.0.0.1 --port 8099 --tokens-file /etc/lingxing-mcp/tokens.json
```

3. 用示例配置把客户端接到 HTTP 入口：
   - `mcp-servers/lingxing-openapi/examples/public/claude_desktop_http_config.json`

如果你还没有服务器，直接看：

- [./tencent-cloud-buying-guide.md](./tencent-cloud-buying-guide.md)

## 令牌管理

初始化令牌文件：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py --tokens-file /etc/lingxing-mcp/tokens.json init --id admin --description "Gateway admin"
```

新增成员令牌：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py --tokens-file /etc/lingxing-mcp/tokens.json add --id alice-mac --description "Alice MacBook"
```

## 固定出口部署脚本

仓库中已包含公开版脚本：

- `deploy/install_gateway_on_ubuntu.sh`
- `deploy/deploy_gateway_via_ssh.sh`
- `deploy/sync_gateway_bundle.sh`
- `deploy/check_egress_ip.sh`
- `deploy/verify_gateway.sh`

如需更安全的远程访问，也可以选用仓库里的 Tailscale 相关脚本。

如果你在 macOS 上本地使用成员令牌接入共享网关，也可以使用：

- `deploy/run_local_lingxing_mcp_bridge.sh`
