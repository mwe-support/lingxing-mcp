# SB广告创意报告
## 接口信息
| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/listHsaProductAdReport` | HTTPS | POST | 10 |

## **请求参数**

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报告日期，时间格式：yyyy-MM-dd|是|[string]|2022-06-01|
|offset| 分页偏移量，默认0             |否|[int]|0|
|length| 分页长度，默认15              |否|[int]|15|

## 请求示例
```
{
    "sid": 109,
    "report_date": "2022-06-01",
    "offset": 0,
    "length": 15
}
```

##  **返回结果**

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code                                | 状态码，0 成功       | 是   | [int]    | 0                                    |
| message                             | 提示消息             | 是   | [string] | 操作成功                             |
| error_details                       | 错误信息             | 是   | [array]  |                                      |
| request_id                          | 请求链路id           | 是   | [string] | 6bb694e1-3d25-4821-8db8-d55dc903f6ba |
| response_time                       | 响应时间             | 是   | [string] | 2023-02-17 09:59:19                  |
| total                               | 总数                 | 是   | [int]    | 1                                    |
| data                                | 响应数据             | 是   | [array]  | |
|data>>campaign_id|广告活动id|是|[number]|800000000000137200|
|data>>ad_group_id|广告组id|是|[number]|800000000000137700|
|data>>ad_creative_id|广告创意id|是|[number]|800000000000140800|
|data>>profile_id|亚马逊店铺数字id|是|[number]|9000000000000013|
|data>>impressions|展示量|是|[int]|54|
|data>>clicks|点击量|是|[int]|6|
|data>>cost|花费|是|[number]|8.4|
|data>>vtr|vtr|是|[number]|88.89|
|data>>vctr|vctr|是|[number]|12.5|
|data>>report_date|报告日期|是|[string]|2024-05-13|
|data>>same_orders|直接成交订单|是|[int]|1|
|data>>orders|订单数|是|[int]|1|
|data>>same_sales|直接成交销售额|是|[number]|10.8|
|data>>sales|销售额|是|[number]|10.8|
|data>>new_to_brand_orders|品牌新买家订单数量|是|[int]|0|
|data>>new_to_brand_order_percentage|品牌新买家订单百分比|是|[number]|0|
|data>>new_to_brand_order_rate|品牌新买家转换率|是|[number]|0|
|data>>new_to_brand_sales|品牌新买家销售额|是|[number]|0|
|data>>new_to_brand_units|品牌新买家销量|是|[int]|0|
|data>>units|销量|是|[number]|453|
|data>>same_units|直接成交量|是|[number]|453|

## **返回成功示例**
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "campaign_id": 800000000000137254,
            "ad_group_id": 800000000000137738,
            "profile_id": 9000000000000013,
            "impressions": 54,
            "clicks": 6,
            "cost": 8.40,
            "vtr": 88.89,
            "vctr": 12.50,
            "ad_creative_id": 800000000000140764,
            "report_date": "2024-05-13",
            "same_orders": 1,
            "orders": 1,
            "same_sales": 10.80,
            "sales": 10.80,
            "new_to_brand_orders": 0,
            "new_to_brand_order_percentage": 0.00,
            "new_to_brand_order_rate": 0.00,
            "new_to_brand_sales": 0.00,
            "new_to_brand_units": 0
        }
    ],
    "total": 45,
    "error_details": [],
    "request_id": "656099da-907f-4932-bc7b-fc56c3fb1ab3",
    "response_time": "2024-05-22 15:45:37"
}
```
