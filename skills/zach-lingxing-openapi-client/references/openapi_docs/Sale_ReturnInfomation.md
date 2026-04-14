# 查询亚马逊多渠道订单详情-退货换货信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/order/amzod/api/orderDetails/returnInformation` | HTTPS | POST | 1 |

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

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|1fe1c50c7d7443bd9a9be97d3485b01b.97.16886996825918301|
|response_time|响应时间|是|[string]|2023-07-07 11:14:42|
|data|响应数据|是|[array]| |
|data>>remark|备注|是|[string]|备注|
|data>>phone|电话|是|[string]|暂停显示|
|data>>sid|店铺id|是|[int]|17|
|data>>store_name|店铺名称|是|[string]|8sxx-US|
|data>>amazon_order_id|平台订单号|是|[string]|S01-2049720-600229|
|data>>seller_fulfillment_order_id|卖家订单号|是|[string]|124341-666|
|data>>displayable_order_comment|装箱单备注|是|[string]|Thank you for your order!|
|data>>order_status|订单状态|是|[string]|CANCELLED|
|data>>sales_channel|销售渠道|是|[string]|Non-Amazon|
|data>>purchase_date_local|提交时间|是|[string]|2023-05-27 01:25:50|
|data>>ship_date|发货时间（北京时间）|是|[string]|2023-05-22 20:00:00|
|data>>ship_date_utc|发货时间（UTC时间）|是|[string]|2023-05-23T03:00:00Z|
|data>>speed_category|配送服务|是|[string]|标准配送|
|data>>ship_date_locale_norm|发货时间（站点时间）|是|[string]|2023-05-22 20:00:00|
|data>>ship_date_locale_iso|发货时间ISO格式（站点时间）|是|[string]|2023-05-22T20:00:00-7:00|
|data>>order_return_replace_tab| |是|[object]| |
|data>>order_return_replace_tab>>return_tab|退货信息|是|[array]| |
|data>>order_return_replace_tab>>return_tab>>sid|店铺id|是|[string]|17|
|data>>order_return_replace_tab>>return_tab>>order_id|订单号|是|[string]|124341-666|
|data>>order_return_replace_tab>>return_tab>>return_date|退货时间|是|[string]|2023-03-01|
|data>>order_return_replace_tab>>return_tab>>msku|msku|是|[string]|MSKUFCE4860|
|data>>order_return_replace_tab>>return_tab>>asin|asin|是|[string]|B0ABC5016|
|data>>order_return_replace_tab>>return_tab>>return_quantity|退货数量|是|[string]|1|
|data>>order_return_replace_tab>>return_tab>>return_reason|退货原因|是|[string]|NOT_AS_DESCRIBED|
|data>>order_return_replace_tab>>return_tab>>return_status|退货状态|是|[string]|Unit returned to inventory|
|data>>order_return_replace_tab>>return_tab>>lpn|lpn编号|是|[string]|LPNAK756277752|
|data>>order_return_replace_tab>>return_tab>>customer_comments|买家备注|是|[string]|thank you|
|data>>order_return_replace_tab>>return_tab>>local_sku|本地产品sku|是|[string]|sku2|
|data>>order_return_replace_tab>>replace_tab|换货信息|是|[array]| |
|data>>order_return_replace_tab>>replace_tab>>replacement_reason|换货原因|是|[string]|Policy exception/customer error|
|data>>order_return_replace_tab>>replace_tab>>msku|msku|是|[string]|sku1|
|data>>order_return_replace_tab>>replace_tab>>asin_url|asin地址|是|[string]|https://www.amazon.com/dp/B0ABC41222|
|data>>order_return_replace_tab>>replace_tab>>shipment_date|换货时间|是|[string]|2022-02-10|

## 返回成功示例

```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "1fe1c50c7d7443bd9a9be97d3485b01b.97.16886996825918301",
    "response_time": "2023-07-07 11:14:42",
    "data": [
        {
            "remark": "备注",
            "phone": "暂停显示",
            "sid": 17,
            "store_name": "8sxx-US",
            "amazon_order_id": "S01-2049720-6429229",
            "seller_fulfillment_order_id": "124341-666",
            "displayable_order_comment": "Thank you for your order!",
            "order_status": "CANCELLED",
            "sales_channel": "Non-Amazon",
            "purchase_date_local": "2023-05-27 01:25:50",
            "ship_date": "2023-05-22 20:00:00",
            "ship_date_utc": "2023-05-23T03:00:00Z",
            "speed_category": "标准配送",
            "order_return_replace_tab": {
                "return_tab": [
                    {
                        "sid": "17",
                        "order_id": "124341-666",
                        "return_date": "2023-03-01",
                        "msku": "MSKUFCE4860",
                        "asin": "B0ABC5016",
                        "return_quantity": "1",
                        "return_reason": "NOT_AS_DESCRIBED",
                        "return_status": "Unit returned to inventory",
                        "lpn": "LPNAK756277752",
                        "customer_comments": "thank you",
                        "local_sku": "sku2",
                        "name": "this is s"
                    }
                ],
                "replace_tab": [
                    {
                        "replacement_reason": "Policy exception/customer error",
                        "msku": "sku1",
                        "name": "zhis is",
                        "asin_url": "https://www.amazon.com/dp/B0ABC41222",
                        "shipment_date": "2022-02-10"
                    }
                ]
            }
        }
    ]
}
```

