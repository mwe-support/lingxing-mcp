# 查询亚马逊多渠道订单详情-物流信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/order/amzod/api/orderDetails/logisticsInformation` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|order_info|订单信息，上限200|是|[array]| |
|order_info>>sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|17|
|order_info>>seller_fulfillment_order_id|卖家订单号|是|[string]|quan332122-R|

## 请求示例
```
{
    "order_info": [
        {
            "sid": 17,
            "seller_fulfillment_order_id": "quan332122-R"
        }
    ]
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型       | 示例 |  
| :------------ | :------------ | :------------ |:---------| :------------ |  
|code|状态码，0 成功|是| [int]    |0|
|message|消息提示|是| [string] |操作成功|
|error_details|错误信息|是| [array]  | |
|request_id|消息提示|是| [string] |65b8587be2f545938d083d63e.16886978815026207|
|response_time|响应数据|是| [string] |2023-07-07 10:44:41|
|data|响应数据|是| [array]  | |
|data>>remark|备注|是| [string] |备注|
|data>>sid|店铺id|是| [int]    |17|
|data>>store_name|店铺名称|是| [string] |8sxx-US|
|data>>amazon_order_id|平台订单号|是| [string] |S01-2753860-9360442|
|data>>seller_fulfillment_order_id|卖家订单号|是| [string] |pu-1-R|
|data>>displayable_order_comment|装箱单备注|是| [string] |Thank you for your order!|
|data>>order_status|订单状态|是| [string] |Complete|
|data>>sales_channel|销售渠道|是| [string] |Non-Amazon|
|data>>purchase_date_local|提交时间|是| [string] |2023-05-17 22:33:53|
|data>>ship_date|发货时间（北京时间）|是| [string] |2023-05-22 20:00:00|
|data>>ship_date_utc|发货时间（UTC时间）|是| [string] |2023-05-23T03:00:00Z|
|data>>speed_category|配送服务|是| [string] |标准配送|
|data>>ship_date_locale_norm|发货时间（站点时间）|是|[string]|2023-05-22 20:00:00|
|data>>ship_date_locale_iso|发货时间ISO格式（站点时间）|是|[string]|2023-05-22T20:00:00-7:00|
|data>>shipment_info|配送详情|是| [array]  | |
|data>>shipment_info>>amazon_shipment_id|货件编号|是| [string] |T4nHcc0Ds|
|data>>shipment_info>>fulfillment_shipment_status|ship状态：<br>CANCELLED_BY_FULFILLER <br> CANCELLED_BY_SELLER <br> PENDING <br> PROCESSED <br> SHIPPED|是| [string] |SHIPPED|
|data>>shipment_info>>estimated_arrival_datetime|预计到货时间【站点时间】|是| [string] |2023-05-23 23:59:59|
|data>>shipment_info>>packages|包裹信息|是| [array]  | |
|data>>shipment_info>>packages>>shipItems||是| [array]  | |
|data>>shipment_info>>packages>>shipItems>>title|标题|是| [string] |Waterproof|
|data>>shipment_info>>packages>>shipItems>>quantity|数量|是| [number] |1|
|data>>shipment_info>>packages>>shipItems>>msku|msku|是| [string] |JJ001|
|data>>shipment_info>>packages>>shipItems>>package_number|包裹编号|是| [string] |2018784457|
|data>>shipment_info>>packages>>shipItems>>sid|店铺id|是| [int]    |17|
|data>>shipment_info>>packages>>package_number|包裹编号|是| [string] |2018784457|
|data>>shipment_info>>packages>>carrier_code|承运人code|是| [string] |USPS|
|data>>shipment_info>>packages>>tracking_number|追踪号|是| [string] |9374889745020264809746|
|data>>shipment_info>>packages>>current_status|包裹运输状态|是| [string] | |
|data>>shipment_info>>packages>>estimated_arrival_datetime|预计到货时间【站点时间】|是| [string] |2023-05-22 20:00:00|
|data>>shipment_info>>packages>>ship_date|发货日期【UTC时间】|是| [string] |2023-05-23T03:00:00Z|
|data>>shipment_info>>packages>>tracking_events|跟踪事件|是| [array]  | |
|data>>shipment_info>>packages>>tracking_events>>eventAddress|时间地址|是| [object] | |
|data>>shipment_info>>packages>>tracking_events>>eventAddress>>country|国家|是| [string] |US|
|data>>shipment_info>>packages>>tracking_events>>eventAddress>>city|城市|是| [string] |Columbia|
|data>>shipment_info>>packages>>tracking_events>>eventAddress>>state|地区|是| [string] |SC|
|data>>shipment_info>>packages>>tracking_events>>eventCode|时间编码|是| [string] |EVENT_201|
|data>>shipment_info>>packages>>tracking_events>>event|事件|是| [string] |已在站|
|data>>shipment_info>>packages>>tracking_events>>eventDescription|事件描述|是| [string] |Package arrived at a carrier facility.|
|data>>shipment_info>>packages>>tracking_events>>eventDate|事件日期|是| [string] |2023-05-23 04:21:00|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "65b8587be2f545938d083d63e.16886978815026207",
    "response_time": "2023-07-07 10:44:41",
    "data": [
        {
            "remark": "备注",
            "sid": 17,
            "store_name": "8sxx-US",
            "amazon_order_id": "S01-2753860-9360442",
            "seller_fulfillment_order_id": "pu-1-R",
            "displayable_order_comment": "Thank you for your order!",
            "order_status": "Complete",
            "sales_channel": "Non-Amazon",
            "purchase_date_local": "2023-05-17 22:33:53",
            "ship_date": "2023-05-22 20:00:00",
            "ship_date_utc": "2023-05-23T03:00:00Z",
            "speed_category": "标准配送",
            "shipment_info": [
                {
                    "amazon_shipment_id": "T4nHcc0Ds",
                    "fulfillment_shipment_status": "SHIPPED",
                    "estimated_arrival_datetime": "2023-05-23 23:59:59",
                    "packages": [
                        {
                            "shipItems": [
                                {
                                    "title": "Waterproof",
                                    "quantity": 1,
                                    "msku": "JJ001",
                                    "package_number": "2018784457",
                                    "sid": 17
                                }
                            ],
                            "package_number": "2018784457",
                            "carrier_code": "USPS",
                            "tracking_number": "9374889745020264809746",
                            "current_status": null,
                            "estimated_arrival_datetime": "2023-05-22 20:00:00",
                            "ship_date": "2023-05-23T03:00:00Z",
                            "tracking_events": [
                                {
                                    "eventAddress": {
                                        "country": null,
                                        "city": "Columbia",
                                        "state": "SC"
                                    },
                                    "eventCode": "EVENT_201",
                                    "event": "已在站。",
                                    "eventDescription": "Package arrived at a carrier facility.",
                                    "eventDate": "2023-05-23 04:21:00"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```
