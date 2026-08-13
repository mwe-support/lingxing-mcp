# MCP 审计日志

HTTP MCP 默认启用紧凑结构化审计日志。每个有审计价值的 POST 请求最多写入一行 JSON，事件名为 `mcp_audit`。

为控制日志量，成功的 `ping` 和 `notifications/initialized` 不写审计日志；这两类请求发生错误或断连时仍会记录。`initialize`、`tools/list`、所有 `tools/call`、认证失败和异常请求均记录。

未经认证的请求只记录 `mcp_method=unauthenticated`，不会从请求体提取工具名或参数键。主审计流写入失败时，服务只向标准错误输出 `mcp_audit_write_failed` 和 `audit_id`，不输出请求值或业务响应。

## 记录范围

审计日志记录以下必要元数据：

- 审计 ID、UTC 时间、HTTP 状态和请求结果
- 成员 token ID、角色和认证模式
- MCP 方法和工具名
- 参数名称、参数总数以及列表参数的元素数量
- `confirm`、`dry_run` 和 `response_mode` 等安全控制状态
- 请求/响应字节数、耗时、导出记录数量和错误代码

审计日志不记录：

- Bearer token、Cloudflare Access 凭证或 Authorization 请求头
- 参数值、SID、订单号、SKU、ASIN、日期范围或广告修改内容
- 响应正文、业务明细、上游请求体或异常消息全文

HTTP 响应头 `X-Mcp-Audit-Id` 可用于将客户端错误与服务端日志关联。

## 查询

生产 systemd 服务使用独立 journal namespace：

```bash
journalctl --namespace=lingxing-mcp -u lingxing-mcp.service --since today -o cat
```

只查看工具调用：

```bash
journalctl --namespace=lingxing-mcp -u lingxing-mcp.service --since "24 hours ago" -o cat \
  | grep '"event":"mcp_audit"'
```

按审计 ID 定位：

```bash
journalctl --namespace=lingxing-mcp -u lingxing-mcp.service -o cat \
  | grep 'AUDIT_ID'
```

部署后可运行不输出凭证和业务数据的自动验证：

```bash
python3 scripts/verify_mcp_audit.py --expected-tool-count 75
```

验证脚本还会调用一次成功的 `ping` 并确认该审计 ID 未写入 journal，用于验证低价值保活日志抑制实际生效。

## 保留策略

`mcp-servers/lingxing-openapi/deploy/journald-retention.conf` 对独立 namespace 设置：

- 最长保留 30 天
- 目标占用上限约 256MB；journald 只删除已归档文件，轮换期间可能短时略高
- 单个 journal 文件最大 32MB
- 每天至少轮换一次并启用压缩
- 关闭 namespace 的日志速率丢弃，确保授权请求突发时审计记录不被默认限流丢弃
- 始终为文件系统保留至少 1GB 空间

30 天是最长保留时间；达到约 256MB 或磁盘保留空间限制时，已归档的旧日志会更早清理。生产环境不要取消容量上限。

部署脚本要求独立 journald namespace 成功启动；namespace 启动失败会中止部署，避免服务在缺少审计日志的状态下被误判为成功。

## 断连处理

如果客户端或 Cloudflare 在响应写回前断开，服务将审计结果记录为 `client_disconnected`。这类连接异常不会再产生整段 Python traceback。

可通过环境变量关闭审计，但生产环境不建议关闭：

```text
LINGXING_MCP_AUDIT_ENABLED=0
```
