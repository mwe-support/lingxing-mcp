# MCP 全量数据导出 Excel

`lingxing_shipment_settlement_report` 和 `lingxing_sales_outbound_orders` 会在服务端自动完成官方分页。为避免大量明细 JSON 占用模型上下文，两个工具默认使用 `response_mode=summary`，只返回记录总数和最多 20 条预览。

需要完整 Excel 时，运行 `scripts/export_mcp_xlsx.py`。脚本通过一次 MCP `tools/call` 请求传入 `response_mode=full`，在本地进程内接收响应并写入 `.xlsx`，终端只输出文件路径、行列数、文件大小和 SHA-256，不输出明细。

## 连接配置

脚本默认读取 `~/.codex/config.toml` 中的 `mcp_servers.lingxing_mcp`。也可通过以下环境变量覆盖：

- `LINGXING_MCP_URL`
- `LINGXING_MCP_KEY`，对应 `X-Mcp-Key`
- `LINGXING_MCP_BEARER_TOKEN`，用于直连 HTTP gateway

认证值不会写入 Excel，也不会打印到终端。

## 导出方式

全店铺发货结算报告：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_shipment_settlement_report --start-date 2026-06-01 --end-date 2026-06-30 --output shipment-settlement-2026-06.xlsx
```

按 SID 导出销售出库单：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_sales_outbound_orders --start-date 2026-06-01 --end-date 2026-06-30 --sid 7806 --output sales-outbound-7806-2026-06.xlsx
```

按 seller ID 导出：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_shipment_settlement_report --start-date 2026-06-01 --end-date 2026-06-30 --seller-id A1EXAMPLE --output settlement-one-seller.xlsx
```

其他官方筛选参数通过 `--arguments-json` 传入。日期、店铺筛选和 `response_mode` 由明确参数控制，附加 JSON 不能覆盖它们。

## Codex 编排提示词

```text
只通过领星 MCP 获取数据，不要操作领星网页，也不要把 full 模式的 JSON 明细直接返回到对话。运行仓库 scripts/export_mcp_xlsx.py，使用指定工具、日期和店铺筛选生成 Excel。脚本必须只输出紧凑摘要；完成后报告 Excel 文件路径、行数、分页数、文件大小和 SHA-256。无店铺筛选时只执行一次全店铺 MCP 调用，不得按 SID 循环批量调用。
```

## 完整性约束

- 发货结算报告按官方 `offset/length` 每页 1000 条拉取，直到达到 `data.total`。
- 销售出库单按官方 `page/page_size` 每页 200 条拉取，直到达到顶层 `total`。
- 导出器要求 `returned_count == record_count` 且 `truncated=false`，否则拒绝生成可能缺行的 Excel。
- Excel 将嵌套对象展开为点号字段，将数组保存为 JSON 文本；工作表冻结首行并开启筛选。
