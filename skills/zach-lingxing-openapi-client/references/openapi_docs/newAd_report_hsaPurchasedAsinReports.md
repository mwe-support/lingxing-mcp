# SB广告归因于广告的购买报告
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/hsaPurchasedAsinReports` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报告日期，格式：Y-m-d|是|[string]|2022-06-01|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认15|否|[int]|15|

## 请求示例
```
{
    "sid": 109,
    "report_date": "2022-06-01",
    "offset": 0,
    "length": 15
}
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|4e95c95f-42bc-42e2-ac35-1fef22fef4f7|
|response_time|响应时间|是|[string]|2023-08-17 16:16:51|
|total|总数|是|[int]|126|
|data|响应数据|是|[array]| |
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>report_date|报告日期|是|[string]|2022-12-10|
|data>>campaign_name|广告活动名称|是|[string]|B07BWBQ66J CampaignName|
|data>>campaign_id|广告活动id<br>【亚马逊官方解释：如果是非SB2，则campaign_id为空】|是|[number]|230107425919319 |
|data>>ad_group_name|广告组名称|是|[string]|B07BWBQ66J AdGroupName|
|data>>ad_group_id|广告组id<br>【亚马逊官方解释：如果是非SB2，则ad_group_id为空】|是|[number]|256144625584796 |
|data>>asin|已购买的asin|是|[string]|B07BWBQ66J|
|data>>attribution_type|引流类型 ：<br />Promoted   促销<br />Brand Halo  品牌光环|是|[string]|Promoted|
|data>>sales14d|14天总销售额|是|[number]|6037.94|
|data>>orders14d|14天总订单数|是|[number]|33|
|data>>units_sold14d|14天总件数|是|[number]|49|
|data>>new_to_brand_sales14d|14天新客户订单销售额|是|[number]|853.37|
|data>>new_to_brand_purchases14d|14天新客户订单|是|[number]|37|
|data>>new_to_brand_units_sold14d|14天新客户订单件数|是|[number]|26|
|data>>new_to_brand_sales_percentage14d|14天新客户订单销售额百分比|是|[number]|36.26|
|data>>new_to_brand_purchases_percentage14d|14天新客户订单百分比|是|[number]|52.9|
|data>>new_to_brand_units_sold_percentage14d|14天新客户订单件数百分比|是|[number]|27.41|
|data>>units|销量|是|[number]|453|
|data>>same_units|直接成交量|是|[number]|453|

## 返回成功示例

```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "2fc8aff8-46dd-469a-8fec-d0a85cea9d04",
    "response_time": "2023-08-17 17:58:53",
    "total": 126,
    "data": [
        {
            "campaign_id": 230107425919319,
            "ad_group_id": 256144625584796,
            "profile_id": 121923590660074,
            "campaign_name": "B07BWBQ66J CampaignName",
            "ad_group_name": "B07BWBQ66J AdGroupName",
            "attribution_type": "Promoted",
            "sales14d": 8295.34,
            "orders14d": 35,
            "new_to_brand_sales14d": 4022.59,
            "new_to_brand_purchases14d": 36,
            "new_to_brand_units_sold14d": 8,
            "new_to_brand_sales_percentage14d": 9.17,
            "new_to_brand_purchases_percentage14d": 77.03,
            "new_to_brand_units_sold_percentage14d": 71.49,
            "report_date": "2022-12-10",
            "asin": "B07BWB066J",
            "units_sold14d": 88
        }
    ]
}
```
