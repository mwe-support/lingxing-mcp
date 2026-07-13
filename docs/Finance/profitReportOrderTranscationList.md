# 查询利润报表订单 Transaction

- 官方文档：https://apidoc.lingxing.com/#/docs/Finance/profitReportOrderTranscationList
- API：`POST /basicOpen/finance/profitReport/order/transcation/list`
- MCP：`lingxing_profit_report_order_list`
- 令牌桶容量：1

## MCP 查询方式

`start_date`、`end_date` 必填。官方接口可通过 `sids` 一次筛选多个店铺，不支持 seller ID。`search_date_field` 默认 `posted_date_locale`，即结算时间；也可选择转账、发货、下单或入账时间。

`fee_type` 映射为官方 `eventSource`，`listing_owner` 映射为 `principalUids`。其他筛选字段保持现有 MCP schema 定义。

默认 `response_mode=summary`，只返回前 20 条预览和完整记录数。`preview_limit` 可设为 0 到 100。`response_mode=full` 仅供 `scripts/export_mcp_xlsx.py` 在本地进程内生成 Excel，不应将完整明细直接放入模型上下文。

## 分页与 Excel

官方单页上限为 1000。MCP 使用 `offset/length` 顺序翻页，直到累计记录数达到 `data.total`。

Excel 使用领星 ERP 网页端`已发放订单`的固定 56 列模板：首行合并为`基础信息`，第二行为字段名，毛利率写为百分比文本，订单号和 Settlement ID 按文本保存。官方 OpenAPI 不返回网页端`延迟时间`，该列保留为空。

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_profit_report_order_list --start-date 2026-06-01 --end-date 2026-06-30 --output profit-order-transaction-2026-06.xlsx
```
