#  查询DSP报告列表-订单

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/dspReport/order/list` | HTTPS | POST | 10 |

## 请求参数

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20|否|[int]|20|
|profile_id|亚马逊店铺数字id，[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】|是|[string]|4796787438420|
|start_date|报告开始日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天|是|[string]|2022-10-01|
|end_date|报告结束日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天|是|[string]|2022-12-25|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "profile_id": "4796787438420",
    "start_date": "2022-10-05",
    "end_date": "2022-12-01"
}
```

## 返回结果
Json Object

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|0|
|data|响应数据|是|[array]||
|data>>profile_id|亚马逊店铺数字id|是|[string]|1196801708955240|
|data>>order_id|订单id|是|[string]|584358905613169595|
|data>>order_name|订单名称|是|[string]|Jarlink Link-In Q3_Clear Packing|
|data>>advertiser_id|广告主id|是|[string]|2142260180301|
|data>>advertiser_name|广告主名称|是|[string]|Jarlink_US|
|data>>order_start_date|开始时间|是|[string]|2022-09-13 00:00:00|
|data>>order_end_date|结束时间|是|[string]|2023-01-01 00:00:00|
|data>>order_budget|预算|是|[string]|2715.00|
|data>>spends|花费|是|[string]|26.88|
|data>>sales|销售额|是|[string]|330.59|
|data>>orders|订单数|是|[string]|10|
|data>>impressions|曝光|是|[string]|4053|
|data>>viewable_impressions|可见展示次数|是|[string]|2176|
|data>>clicks|点击|是|[string]|3|
|data>>dpv|商品详情页浏览次数|是|[string]|51|
|data>>total_add_to_cart|加购次数|是|[string]|22|
|data>>order_currency|币种|是|[string]|USD|
|data>>ad_units|销量|是|[string]|11|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "fab4046bfb224000ad496c1c7d99cdec.1700209671099",
    "response_time": "2023-11-17 16:27:51",
    "data": [
        {
            "profile_id": "1196801708955240",
            "order_id": "584358905613169595",
            "order_name": "Jarlink Link-In",
            "advertiser_id": "2142260180301",
            "advertiser_name": "Jarlink_US",
            "order_start_date": "2022-09-13 00:00:00",
            "order_end_date": "2023-01-01 00:00:00",
            "order_budget": "2715.00",
            "spends": "26.88",
            "sales": "330.59",
            "orders": "10",
            "impressions": "4053",
            "viewable_impressions": "2176",
            "clicks": "3",
            "dpv": "51",
            "total_add_to_cart": "22",
            "order_currency": "USD",
            "ad_units": "11"
        }
    ],
    "total": 1
}
```