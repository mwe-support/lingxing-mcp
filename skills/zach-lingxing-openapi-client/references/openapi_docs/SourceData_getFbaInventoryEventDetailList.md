# 查询亚马逊源报表——Inventory Event Detail
查询 FBA Inventory Event Detail 报表
>2023年3月后不再更新此接口数据【亚马逊对应报表下线】，获取之后的数据请使用 [查询亚马逊库存分类账detail数据](docs/Finance/centerOdsDetailQuery)

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/getFbaInventoryEventDetailList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|snapshot_date_after|快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天|是|[string]|2024-06-01|
|snapshot_date_before|快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天|是|[string]|2024-06-07|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "snapshot_date_after": "2024-06-01",
    "snapshot_date_before": "2024-06-07",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sid|店铺id|是|[int]|1|
|data>>snapshot_date|快照时间|是|[string]|2019-10-31T07:00:00+00:00|
|data>>snapshot_date_locale|快照时间|是|[string]|2019-10-31T00:00:00-07:00|
|data>>snapshot_date_timestamp|快照时间对应时间戳|是|[int]|1572505200|
|data>>snapshot_date_report| |是|[string]|2019-10-31|
|data>>transaction_type| |是|[string]|Adjustments|
|data>>fnsku|FNSKU|是|[string]|FN803BE7D|
|data>>sku|SKU|是|[string]|MSKU89A17DF|
|data>>product_name||是|[string]|[演示数据]高清全屏钢化玻璃膜9H硬度|
|data>>fulfillment_center_id| |是|[string]|AKS1|
|data>>quantity| |是|[number]|-1|
|data>>disposition| |是|[string]|WAREHOUSE_DAMAGED|
|total|总数|是|[int]|1758748|
