# 查询亚马逊源报表-FBA退货订单

- MCP tool: lingxing_refund_orders
- Endpoint: /erp/sc/data/mws_report/refundOrders
- Method: POST
- Source: 领星 API 文档 SourceData / RefundOrders
- Token bucket capacity: 1

## 用途

查询 FBA customer returns 报表，返回订单级 FBA 退货原始数据。适合按店铺和日期范围核对退货订单、退货原因、退货状态、买家评论、FNSKU、ASIN、SKU 和退货处理结果。

## MCP 参数

| 参数 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| sid | 是 | integer | 领星店铺 ID。 |
| start_date | 是 | string | 查询开始日期，格式 Y-m-d，左闭右开。 |
| end_date | 是 | string | 查询结束日期，格式 Y-m-d，左闭右开。 |
| date_type | 否 | integer | 日期类型。1 表示退货时间（站点时间），2 表示更新时间（北京时间）。不传时按领星接口默认值。 |

分页参数 offset 和 length 由 MCP 网关自动补充并合并分页结果。

## 主要返回字段

返回 data 数组和 total。常用字段包括 sid、order_id、local_sku、product_name、sku、asin、fnsku、quantity、return_date、return_date_locale、purchase_date、purchase_date_locale、gmt_modified、fulfillment_center_id、detailed_disposition、reason、status、license_plate_number、customer_comments、remark，以及 tag.tag_name、tag.tag_color。
