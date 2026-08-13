# Cloudflare Tunnel 部署

生产 Tunnel 使用 `mcp-servers/lingxing-openapi/deploy/cloudflared-compose.yml.example` 作为基线。

## 安全要求

- Tunnel token 必须存放在 `/etc/cloudflared/lingxing-mcp.token`，所有者为 `root:root`，权限为 `0600`。
- 不要把 token 写入 Compose `command`、环境变量、Git、聊天记录或可被普通用户读取的文件。
- 容器通过只读 `/run/secrets/cloudflared_tunnel_token` 读取 token。
- 使用固定镜像版本，不依赖已经运行数月但未重新拉取的 `latest`。
- 使用 HTTP/2 Tunnel 传输，避免当前服务器网络上观察到的 QUIC 空闲超时和频繁连接重建。
- Docker JSON 日志限制为 10MB x 3，避免 Tunnel 连接波动占满磁盘。

## 部署检查

复制示例 Compose 后，先验证配置不会展开或打印 secret：

```bash
docker compose config --quiet
```

部署后检查：

```bash
docker compose up -d
docker inspect -f '{{.State.Status}} restart_count={{.RestartCount}}' cloudflared-lingxing-mcp
docker logs --since 10m cloudflared-lingxing-mcp
```

进程参数应包含 `--protocol http2` 和 `--token-file /run/secrets/cloudflared_tunnel_token`，不应出现 token 值。

## 升级

先修改并提交 Compose 中固定的 cloudflared 版本，再执行：

```bash
docker compose pull
docker compose up -d
```

不要只保留 `latest` 后假设运行中的容器会自动升级；配置使用 `--no-autoupdate`，升级必须由管理员明确执行并验证。
