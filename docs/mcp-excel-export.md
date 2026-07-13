# MCP 全量数据导出 Excel

`lingxing_shipment_settlement_report`、`lingxing_profit_report_order_list` 和 `lingxing_sales_outbound_orders` 会在服务端自动完成官方分页。为避免大量明细 JSON 占用模型上下文，三个工具默认使用 `response_mode=summary`，只返回记录总数和最多 20 条预览。

需要完整 Excel 时，运行 `scripts/export_mcp_xlsx.py`。脚本通过一次 MCP `tools/call` 请求传入 `response_mode=full`，在本地进程内接收响应并写入 `.xlsx`，终端只输出文件路径、行列数、文件大小和 SHA-256，不输出明细。

## 连接配置

脚本默认读取 `~/.codex/config.toml` 中的 `mcp_servers.lingxing_mcp`。也可通过以下环境变量覆盖：

- `LINGXING_MCP_URL`
- `LINGXING_MCP_KEY`，对应 `X-Mcp-Key`
- `LINGXING_MCP_BEARER_TOKEN`，用于直连 HTTP gateway

认证值不会写入 Excel，也不会打印到终端。

导出器会发送固定的 `Codex-Lingxing-MCP-Exporter/1.0` User-Agent，避免 Cloudflare 将 Python 默认 `urllib` 客户端误判为受限浏览器签名。

## 导出方式

全店铺发货结算报告：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_shipment_settlement_report --start-date 2026-06-01 --end-date 2026-06-30 --output shipment-settlement-2026-06.xlsx
```

全店铺利润报表 Transaction：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_profit_report_order_list --start-date 2026-06-01 --end-date 2026-06-30 --output profit-order-transaction-2026-06.xlsx
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

`lingxing_profit_report_order_list` 只接受 SID，不接受 seller ID。其官方 `search_date_field` 默认是结算时间 `posted_date_locale`。

## 网页端格式对齐

导出器按领星 ERP 网页端实际导出模板写入固定表头，而不是直接输出 OpenAPI 英文字段：

- 发货结算：工作表 `结算差异报告`，固定 52 列；空结果仍保留完整表头。`结算类型`根据发货月与结算月生成。
- 利润报表 Transaction：工作表 `已发放订单`，固定 56 列；首行合并为`基础信息`，第二行为字段名，毛利率写为百分比文本。
- 销售出库：工作表 `sheet1`，固定 68 列；`product_info` 按商品拆行，同一出库单的前 48 列纵向合并。
- 订单号、Settlement ID、系统单号、平台单号、跟踪号等标识字段按文本写入，避免 Excel 科学计数法和 15 位精度丢失。
- 表头使用网页端的粗体居中样式，首列宽度约 20.71，其余列约 13；数值列使用对应的整数、两位或四位小数格式。

OpenAPI 与 ERP 网页端的数据层并不完全相同。发货结算接口不返回`到账状态`以及平台费、发货费、成本和毛利等 10 个网页端计算字段；Transaction 接口不返回`延迟时间`。模板保留这些列但保持空白，导出摘要的 `unavailable_columns` 会列出它们，禁止跨报表猜算或伪造。

## Codex 编排提示词

```text
只通过领星 MCP 获取数据，不要操作领星网页，也不要把 full 模式的 JSON 明细直接返回到对话。运行仓库 scripts/export_mcp_xlsx.py，使用指定工具、日期和店铺筛选生成 Excel。脚本必须只输出紧凑摘要；完成后报告 Excel 文件路径、行数、分页数、文件大小和 SHA-256。无店铺筛选时只执行一次全店铺 MCP 调用，不得按 SID 循环批量调用。
```

## 完整性约束

- 发货结算报告按官方 `offset/length` 每页 1000 条拉取，直到达到 `data.total`。
- 利润报表 Transaction 按官方 `offset/length` 每页 1000 条拉取，直到达到 `data.total`。
- 销售出库单按官方 `page/page_size` 每页 200 条拉取，直到达到顶层 `total`。
- 导出器要求 `returned_count == record_count` 且 `truncated=false`，否则拒绝生成可能缺行的 Excel。
- 全量发货结算只选择状态为启用的亚马逊店铺；显式传入 SID 或 seller ID 时仍允许查询停用店铺。
