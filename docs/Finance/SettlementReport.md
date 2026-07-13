# 查询发货结算报告

- 官方文档：https://apidoc.lingxing.com/#/docs/Finance/SettlementReport
- API：`POST /cost/center/api/settlement/report`
- MCP：`lingxing_shipment_settlement_report`
- 令牌桶容量：3

## MCP 查询方式

- 传 `sids`：按领星店铺 SID 查询，并自动补齐对应 `seller_id`。
- 传 `amazon_seller_ids`：按亚马逊 seller ID 查询，并自动补齐对应 SID。
- 同时传两者：校验 SID 与 seller ID 映射一致。
- 均不传：自动读取全部亚马逊店铺，在一次 MCP 调用中提交完整 `sids` 和 `amazonSellerIds` 数组。

全量模式要求每个店铺都同时具备 SID 和 seller ID；只要发现缺失配对的店铺，工具会直接失败并提示修复资料，避免以“全部店铺”名义静默漏数。

`start_date`、`end_date` 必填。`time_type` 默认 `04`，表示按结算时间筛选。

默认 `response_mode=summary`，只返回前 20 条预览以及完整记录数。`preview_limit` 可设为 0 到 100。`response_mode=full` 会返回全部明细，仅供 `scripts/export_mcp_xlsx.py` 在进程内生成 Excel，不应由模型直接调用。

## 分页

官方单页上限为 1000。MCP 使用 `offset/length` 顺序翻页，直到累计记录数达到 `data.total`。调用方不需要按店铺或页码批量调用工具；摘要模式只控制最终响应大小，不影响服务端完成全部分页。

全店铺 Excel 示例：

```powershell
python scripts/export_mcp_xlsx.py --tool lingxing_shipment_settlement_report --start-date 2026-06-01 --end-date 2026-06-30 --output shipment-settlement-2026-06.xlsx
```
