# 查询销售出库单列表

- 官方文档：https://apidoc.lingxing.com/#/docs/Warehouse/WmsOrderList
- API：`POST /erp/sc/routing/wms/order/wmsOrderList`
- MCP：`lingxing_sales_outbound_orders`
- 令牌桶容量：1

## MCP 查询方式

- 传 `sids`：写入官方 `sid_arr`，按指定店铺查询。
- 传 `amazon_seller_ids`：先解析为对应 SID，再写入 `sid_arr`。
- 同时传两者：校验映射一致。
- 均不传：省略官方可选的 `sid_arr`，在一次 MCP 调用中查询全部店铺。

`start_date`、`end_date` 必填。`time_type` 默认 `stock_delivered_at`，表示库存流水出库时间。

默认 `response_mode=summary`，只返回前 20 条预览以及完整记录数。`preview_limit` 可设为 0 到 100。`response_mode=full` 会返回全部明细，仅供 `scripts/export_mcp_xlsx.py` 在进程内生成 Excel，不应由模型直接调用。

## 分页

官方单页上限为 200。MCP 使用 `page/page_size` 顺序翻页，直到累计记录数达到顶层 `total`。调用方不需要按店铺或页码批量调用工具；摘要模式只控制最终响应大小，不影响服务端完成全部分页。

指定 SID 的 Excel 示例：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_sales_outbound_orders --start-date 2026-06-01 --end-date 2026-06-30 --sid 7806 --output sales-outbound-7806-2026-06.xlsx
```
