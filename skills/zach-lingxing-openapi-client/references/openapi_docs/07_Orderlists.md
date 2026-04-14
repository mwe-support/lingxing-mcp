# 查询亚马逊订单列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws/orders` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[int]| 113 |
|sid_list|店铺id列表，最大长度20|否|[array]| [113,112] |
|start_date|查询时间，左闭右开，格式：Y-m-d 或 Y-m-d H:i:s<br />当date_type=3时，需要传入时间格式为：Y-m-d H:i:s|是|[string]|2022-04-18 11:23:47|
|end_date|查询时间，左闭右开，格式：Y-m-d 或 Y-m-d H:i:s<br />当date_type=3时，需要传入时间格式为：Y-m-d H:i:s|是|[string]|2022-05-18 11:23:47|
|date_type|查询日期类型：【默认1】<br>1 订购时间【站点时间】<br>2 订单修改时间【北京时间】<br>3 平台更新时间【UTC时间】<br>10 发货时间【站点时间】<br>查询时间范围不超过一年|否|[int]|1|
|order_status|Pending 待处理<br />Unshipped 未发货<br />PartiallyShipped 部分发货<br />Shipped 已发货<br />Canceled 取消|否|[array]|["Pending"]|
|sort_desc_by_date_type|是否按查询日期类型排序：0 否，1 降序，2 升序【默认0】|否|[int]|1|
|fulfillment_channel|配送方式：1 亚马逊订单-AFN，2 自发货-MFN |否|[int]|1|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000，上限5000|否|[int]|1000|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]| 502B9DD9-1BA0-03C5-6C61-D77C830440A6|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[string]|101|
|data>>seller_name|店铺名称|是|[string]|店铺8|
|data>>amazon_order_id|亚马逊订单号|是|[string]|111-8056674-6381837|
|data>>order_status|订单状态|是|[string]|Unshipped|
|data>>order_total_amount|订单金额|是|[string]|8.99|
|data>>fulfillment_channel|配送方式：亚马逊订单-AFN，自发货-MFN|是|[string]|AFN|
|data>>postal_code|邮编|是|[string]|LA1 5DS|
|data>>is_return|退款状态：0 未退款，1 退款中，2 退款完成|是|[int]|0|
|data>>is_mcf_order|是否多渠道订单：0 否，1 是<br>【2023年后的多渠道订单数据均不在此接口返回】|是|[int]|0|
|data>>is_assessed|是否推广订单：0 否，1 是|是|[int]|0|
|data>>is_replaced_order|是否换货订单：0 否，1 是|是|[int]|0|
|data>>is_replacement_order|是否已换货订单：0 否，1 是|是|[int]|0|
|data>>is_return_order|是否退货订单：0 否，1 是|是|[int]|0|
|data>>order_total_currency_code|币种，order_total_amount为0时，币种信息为空|是|[string]|GBP|
|data>>sales_channel|销售渠道|是|[string]|Amazon.co.uk|
|data>>tracking_number|物流运单号|是|[string]|D5714B7AB|
|data>>refund_amount|退款金额(含币种)|是|[number]| -5.83 |
|data>>item_list|商品信息|是|[array]| |
|data>>item_list>>asin|ASIN|是|[string]|B0ABC49975|
|data>>item_list>>quantity_ordered|数量|是|[string]|1|
|data>>item_list>>seller_sku|MSKU|是|[string]|MSKUD33BAE7|
|data>>item_list>>local_sku|本地sku|是|[string]|SKU7A67306|
|data>>item_list>>local_name|本地品名|是|[string]|[演示数据]带2件装相机镜头保护膜|
|data>>purchase_date_local|订购时间【站点时间】|是|[string]|2020-11-06 19:25:38|
|data>>purchase_date_local_utc|订购时间【UTC】|是|[string]|2020-11-07 03:25:38|
|data>>shipment_date|发货日期【亚马逊返回时间，不一定为站点时间】|是|[string]|2021-01-02T12:59:13+00:00|
|data>>shipment_date_utc|发货日期【UTC】|是|[string]|2021-01-02 12:59:13|
|data>>shipment_date_local|发货日期【站点时间】|是|[string]|2021-01-02 12:59:13|
|data>>last_update_date|订单更新时间【站点时间】|是|[string]|2023-02-03 02:27:25|
|data>>last_update_date_utc|订单更新时间【UTC】|是|[string]|2023-02-03 10:27:25|
|data>>posted_date|付款时间【亚马逊返回时间，不一定为站点时间】|是|[string]|2020-11-07 03:25:38|
|data>>posted_date_utc|付款时间【UTC】|是|[string]|2020-11-07 03:25:38|
|data>>purchase_date|订购时间【亚马逊返回时间，不一定为站点时间】|是|[string]|2020-11-07T03:25:38Z|
|data>>purchase_date_utc|订购时间【UTC】|是|[string]|2020-11-07 03:25:38|
|data>>earliest_ship_date|发货时限【亚马逊返回时间，不一定为站点时间】|是|[string]|2020-11-09T08:00:00Z|
|data>>earliest_ship_date_utc|发货时限【UTC】|是|[string]|2020-11-09 08:00:00|
|data>>gmt_modified|订单修改时间|是|[string]|2022-06-17 15:57:04|
|data>>gmt_modified_utc|订单修改时间【UTC】|是|[string]|2022-06-17 07:57:04|

## 返回成功示例
```
{
    "code":0,
    "message":"success",
    "error_details":[],
    "request_id":"FAFAE080-A0E1-D12E-8151-5CEDA5540D29",
    "response_time":"2023-04-14 12:14:50",
    "data":[
        {
            "sid":101,
            "seller_name":"8p-US",
            "amazon_order_id":"110-1821908-7840000",
            "order_status":"Shipped",
            "order_total_amount":"145.00",
            "fulfillment_channel":"MFN",
            "postal_code":"",
            "is_return":0,
            "is_mcf_order":0,
            "is_assessed":0,
            "is_return_order": 0,
            "is_replaced_order": 0,
            "is_replacement_order": 0,
            "order_total_currency_code":"USD",
            "sales_channel":"Amazon.com",
            "tracking_number":"",
            "hide_time":"2020-11-06 19:25:38",
            "refund_amount":0,
            "item_list":[
                {
                    "asin":"B08xxxxx",
                    "quantity_ordered":1,
                    "seller_sku":"sku-355",
                    "local_sku":"SKU7A67306",
                    "local_name":"[演示数据]带2件装相机镜头保护膜"
                }
            ],	    
            "purchase_date_local":"2020-11-06 19:25:38",
            "purchase_date_local_utc":"2020-11-07 03:25:38",
            "shipment_date":"",
            "shipment_date_utc":"",
            "shipment_date_local":"",
            "last_update_date":"2023-02-03 02:27:25",
            "last_update_date_utc":"2023-02-03 10:27:25",
            "posted_date":"2020-11-07 03:35:38",
            "posted_date_utc":"2020-11-07 03:35:38",
            "purchase_date":"2020-11-07T03:25:38Z",
            "purchase_date_utc":"2020-11-07 03:25:38",
            "earliest_ship_date":"2020-11-09T08:00:00Z",
            "earliest_ship_date_utc":"2020-11-09 08:00:00",
            "gmt_modified":"2023-02-03 18:38:10",
            "gmt_modified_utc":"2023-02-03 10:38:10"
        }
    ],
    "total":1
}
```

## 附加说明
order_status 说明如下：

作为**入参**时：除了Pending、Unshipped、PartiallyShipped、Canceled其余的状态不支持，Pending、Unshipped、Canceled没有发货时间，当date_type为10时，传入这三个参数无意义。

1. PendingAvailability：只有预订订单才有此状态；订单已生成，但是付款未授权且商品的发售日期是将来的某一天，订单尚不能进行发货；<br>【注意】仅在日本 (JP)，Preorder 才可能是一个 OrderType 值；
2. Pending：订单已生成，但是付款未授权，订单尚不能进行发货；<br>【注意】<br>对于 OrderType = Standard 的订单，初始的订单状态是 Pending；<br>对于 OrderType = Preorder 的订单（仅适用于 JP），初始的订单状态是 PendingAvailability，当进入付款授权流程时，订单状态将变为 Pending；
3. Unshipped：付款已经过授权，订单已准备好进行发货，但订单中商品尚未发运；
4. PartiallyShipped：订单中的一个或多个（但并非全部）商品已经发货；
5. Shipped：订单中的所有商品均已发货；
6. InvoiceUnconfirmed：订单中的所有商品均已发货，但是卖家还没有向亚马逊确认已经向买家寄出发票；请注意：此参数仅适用于中国地区；
7. Canceled：订单已取消；
8. Unfulfillable：订单无法进行配送，该状态仅适用于通过亚马逊零售网站之外的渠道下单但由亚马逊进行配送的订单；