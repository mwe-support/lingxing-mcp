# 查询亚马逊源报表-每日库存
查询 FBA Daily Inventory History Report 报表

>由于亚马逊对应报表下线，2023年12月1日后不再更新此接口数据，获取数据请使用 [查询库存分类账summary数据](docs/Finance/summaryQuery)

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/dailyInventory` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id【欧洲传UK下的店铺，美国传US下的店铺】 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|event_date|报表日期，格式：Y-m-d|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0| 
|length|分页长度，默认1000|否|[int]|1000| 

## 请求示例
```
{
    "sid": 109,
    "event_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码， 0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details| 错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|69F77F67-F288-B0C8-F453-C653E4D0FA93|
|response_time|响应时间|是|[string]|2021-05-14 18:08:36|
|data|响应数据|是|[array]|  |
|data>>snapshot_date|快照时间|是|[string]|2019-05-03T07:00:00+00:00|
|data>>fnsku|FNSKU|是|[string]|X001T62RU61|
|data>>sku|SKU|是|[string]|8524J1854|
|data>>product_name|品名|是|[string]|[Newest Metal Version] Mobile Game Controller|
|data>>quantity|数量|是|[number]|7|
|data>>fulfillment_center_id|存储库存的运营中心|是|[string]|EWR4|
|data>>detailed_disposition|商品状态（例如，可售、残损等）|是|[string]|SELLABLE|
|data>>country|库存存放地所在的国家/地区代码|是|[string]|US|
