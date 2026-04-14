# 查询广告发票活动列表
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/ads/invoice/campaign/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|offset|分页偏移量，默认值0|否|[int]|0|
|length|分页大小，默认20|否|[int]|20|
|invoice_id|广告发票编号|是|[string]|CDLPWKJPR-21|
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|ads_type|广告类型：<br>SPONSORED PRODUCTS<br>SPONSORED DISPLAY<br>SPONSORED BRANDS<br>SPONSORED BRANDS VIDEO|否|[array]|["SPONSORED PRODUCTS"，"SPONSORED DISPLAY"]|
|search_type|搜索类型：<br>ads_campaign【对应页面广告活动】<br>item【对应页面承担商品】|否|[string]|ads_campaign|
|search_value|搜索值|否|[string]|CD3433L1|

## 请求示例
```
{
    "invoice_id": "TRF6K4FJN-1",
    "sid": 136
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|81CA6A9A-A5C4-8B5E-5FED-E1C2EC04753C|
|response_time|响应时间|是|[string]|2023-04-07 12:11:12|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>campaign_name|广告活动|是|[string]|shampoo brush_SB_221122|
|data>>campaign_id|活动id|是|[string]|103754268477832|
|data>>ads_type|广告类型|是|[string]|SPONSORED BRANDS|
|data>>price_type|计价方式|是|[string]|CPC|
|data>>cost_event_count|点击量|是|[number]|26|
|data>>currency_icon|币种符号|是|[string]|€|
|data>>cost_amount|费用|是|[number]|10.92|
|data>>cost_per_unit|平均点击单价|是|[number]|0.42|
|data>>other_allocation_fee|其他费分摊|是|[number]|0|
|data>>items|承担商品|是|[array]|["B07P6X4CJ7","B095WCH2TD","B09L12TZ2S"]|

## 返回成功示例
```
{
    "code": 0,
    "message": null,
    "data": [
        {
            "items": [
                "HM300-BLACK"
            ],
            "campaign_name": "HM300-Green-pink yoga pants for women-2024-04-11-09:39:41-勿归档",
            "campaign_id": "337037646660608",
            "ads_type": "SPONSORED PRODUCTS",
            "price_type": "CPC",
            "cost_event_count": 2,
            "currency_icon": "$",
            "cost_amount": 1.9400,
            "cost_per_unit": 0.9700,
            "other_allocation_fee": 0.0000
        }
    ],
    "error_details": null,
    "request_id": "656b0028-22ed-45d0-ad25-28f04f21f324.1721879425928",
    "response_time": "2024-07-25 11:50:25",
    "total": 1
}
```