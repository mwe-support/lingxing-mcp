# 查询亚马逊订单详情
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws/orderDetail` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|order_id|亚马逊订单号，多个使用英文逗号分隔，上限200|是|[string]|123-1234567-1234567,789-1234567-1234567|


## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]| 502B9DD9-1BA0-03C5-6C61-D77C830440A6|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[int]|8|
|data>>amazon_order_id|亚马逊订单号|是|[string]|209-3501178-3501387|
|data>>fulfillment_channel|发货渠道|是|[string]|AFN|
|data>>order_status|订单状态|是|[string]|Shipped|
|data>>order_total_amount|订单总金额|是|[number]|5.49|
|data>>currency|订单金额币种|是|[string]|GBP|
|data>>icon|订单金额币种符号|是|[string]|￡|
|data>>is_assessed|是否为推广订单： 0 否，1 是|是|[int]| |
|data>>is_mcf_order|是否多渠道订单：0 普通订单，1 多渠道订单|是|[int]| |
|data>>is_return_order|是否为退货订单：0 否，1 是|是|[int]| |
|data>>is_replaced_order|是否已换货：0 否，1 是|是|[int]| |
|data>>is_replacement_order|是否为换货订单：0 否，1 是|是|[int]| |
|data>>purchase_date_local|订购时间（站点时间）|是|[string]|2021-01-01 00:08:26|
|data>>purchase_date_local_utc|订购时间（utc时间）|是|[string]|2021-01-01 08:08:26|
|data>>last_update_date|订单更新（站点时间）|是|[string]|2021-01-06 08:03:01|
|data>>last_update_date_utc|订单更新时间（utc时间）|是|[string]|2021-01-06 00:03:01|
|data>>posted_date|结算时间（站点时间）|是|[string]|2021-01-06 00:03:01|
|data>>shipment_date|发货时间（站点时间）|是|[string]|2021-01-06 00:03:01|
|data>>earliest_ship_date|发货时限（站点时间）|是|[string]|2021-01-06 08:03:01|
|data>>earliest_ship_date_utc|发货时限（utc时间）|是|[string]|2021-01-06 00:03:01|
|data>>is_business_order|是否为B2B订单：0 否，1 是|是|[int]|0|
|data>>is_prime|是否prime订单：0 否，1 是|是|[int]|0|
|data>>is_premium_order|是否优先配送订单：0 否，1 是|是|[int]|0|
|data>>is_promotion|是否促销订单：0 否，1 是|是|[int]|0|
|data>>taxes_included|费用是否含税：1 含税，2 不含税<br>仅针对欧洲市场订单使用，对应字段如下：item_price_amount、shipping_price_amount、gift_wrap_price_amount、shipping_discount_amount、promotion_discount_amount、cod_fee_amount|是|[int]| 1|
|data>>ship_service_level|配送服务|是|[string]|Expedited|
|data>>shipment_service_level_category|装运服务级别|是|[string]|Expedited|
|data>>purchase_order_number|采购订单编号（买家结账时输入）|是|[string]| |
|data>>payment_method|付款方式：<br>COD (Cash on delivery)<br>CVS（Convenience store）<br>Other（A payment method other than COD and CVS）|是|[string]|Other|
|data>>cba_displayable_shipping_label|亚马逊结账（CBA）的自定义发货标签|是|[string]| |
|data>>order_type|订单类型|是|[string]|StandardOrder|
|data>>latest_ship_date|最晚发货时间（承诺配送订单的最晚发货时间）|是|[string]|2021-01-02T23:59:59Z|
|data>>earliest_delivery_date|最早送达时间（承诺送达订单的最早送达时间）<br>备注：UTC时间|是|[string]| |
|data>>latest_delivery_date|最晚送达时间（承诺送达订单的最晚送达时间）<br>备注：UTC时间|是|[string]| |
|data>>number_of_items_shipped|已发货的商品数|是|[int]|1|
|data>>number_of_items_unshipped|未发货的商品数|是|[int]| |
|data>>sales_channel|销售渠道|是|[string]|Amazon.co.uk|
|data>>item_list|订单明细|是|[array]| |
|data>>item_list>>id|订单商品自增id|是|[long]|3319575|
|data>>item_list>>title|商品标题|是|[string]|lingxing amazon product title 1444CA2EDB|
|data>>item_list>>seller_sku|MSKU|是|[string]|MSKUD33BAE7|
|data>>item_list>>asin|ASIN|是|[string]|B0ABC49975|
|data>>item_list>>asin_url|asin链接|是|[string]|https://www.amazon.co.uk/dp/xxxx|
|data>>item_list>>sid|店铺id|是|[int]|8|
|data>>item_list>>sku|本地SKU|是|[string]|SKU7A67306|
|data>>item_list>>product_id|本地产品id|是|[int]|1312|
|data>>item_list>>product_name|品名|是|[string]|[演示数据]带2件装相机镜头保护膜|
|data>>item_list>>pic_url|图片链接|是|[string]|https://image-125421xxx.com/8A%A4%E8%86%9C.jpg|
|data>>item_list>>order_item_id|订单商品编码【订单下唯一，但亚马逊返回值可能会发生变更，以最新数据为准】|是|[string]|04022905984851|
|data>>item_list>>points_monetary_value_amount|积分成本（日本站会有此数据）|是|[string]|0.00|
|data>>item_list>>quantity_ordered|下单量|是|[int]|1|
|data>>item_list>>quantity_shipped|已配送|是|[int]|1|
|data>>item_list>>item_price_amount|商品支付金额|是|[string]|5.49|
|data>>item_list>>item_tax_amount|商品税|是|[string]|0.92|
|data>>item_list>>shipping_price_amount|买家运费|是|[string]|0.00|
|data>>item_list>>shipping_tax_amount|商品运费税|是|[string]|0.00|
|data>>item_list>>gift_wrap_price_amount|礼品包装费|是|[string]|0.00|
|data>>item_list>>gift_wrap_tax_amount|礼品包装税|是|[string]|0.00|
|data>>item_list>>shipping_discount_amount|配送折扣|是|[string]|0.00|
|data>>item_list>>cod_fee_amount|COD服务费用（货到付款服务费）|是|[string]|0.00|
|data>>item_list>>promotion_ids|商品促销id|是|[array]| |
|data>>item_list>>shipping_discount_tax_amount|配送折扣税|是|[string]|0.00|
|data>>item_list>>promotion_discount_amount|商品促销折扣|是|[string]|0.00|
|data>>item_list>>promotion_discount_tax_amount|商品促销折扣税|是|[string]|0|
|data>>item_list>>cod_fee_discount_amount|COD服务费用折扣|是|[string]|0.00|
|data>>item_list>>gift_message_text|礼品信息（买家提供）|是|[string]| |
|data>>item_list>>gift_wrap_level|礼品包装级别（买家提供）|是|[string]| |
|data>>item_list>>condition_note|商品状况说明（卖家提供）|是|[string]| |
|data>>item_list>>condition_id|商品状况（卖家提供）|是|[string]| |
|data>>item_list>>condition_subtype_id|商品子状况（卖家提供）|是|[string]| |
|data>>item_list>>scheduled_delivery_start_date|计划交货开始日期|是|[string]| |
|data>>item_list>>scheduled_delivery_end_date|计划交货结束日期|是|[string]| |
|data>>item_list>>price_designation|B2B价格|是|[string]| |
|data>>item_list>>cg_price|采购成本|是|[number]|-147.36|
|data>>item_list>>fee_name|其他费名称，比如推广费|是|[string]|推广费|
|data>>item_list>>cg_transport_costs|头程费用|是|[number]|-9|
|data>>item_list>>fba_shipment_amount|FBA发货费|是|[number]|-2.18|
|data>>item_list>>commission_amount|平台费|是|[number]|-0.45|
|data>>item_list>>other_amount|亚马逊收取的其他费用，比如参与“Amazon Exlusives Program”产生的费用|是|[number]| |
|data>>item_list>>fee_currency|其他费币种，比如推广费|是|[string]|CNY|
|data>>item_list>>fee_icon|其他费币种符号，比如推广费|是|[string]|￥|
|data>>item_list>>fee_cost_amount|自定义费用本金（店铺对应的币种，例：站外推广费本金）|是|[number]| |
|data>>item_list>>fee_cost|自定义费用本金（fee_currency对应的币种，例：站外推广费本金）|是|[number]| |
|data>>item_list>>sales_price_amount|销售收益|是|[number]|5.49|
|data>>item_list>>unit_price_amount|单价|是|[number]|4.57|
|data>>item_list>>tax_amount|税费|是|[number]|-0.92|
|data>>item_list>>promotion_amount|促销费|是|[number]| |
|data>>item_list>>profit|毛利润|是|[number]|-154.42|
|data>>item_list>>item_discount|商品折扣|是|[number]|0.00|
|data>>item_list>>customized_json|订单定制化信息json|是|[string]||
|data>>item_list>>is_settled|商品已结算标识:0 未结算,1 已结算|是|[int]||


## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "22A65D65-F133-3402-DED6-700E58FC4AE2",
    "response_time": "2023-04-14 14:20:57",
    "data": [
        {
            "amazon_order_id": "114-1821948-7841000",
            "fulfillment_channel": "MFN",
            "sid": 101,
            "order_status": "Shipped",
            "is_assessed": 0,
            "order_total_amount": "145.00",
            "currency": "USD",
            "icon": "$",
            "is_mcf_order": 0,
            "is_return_order": 0,
            "is_replaced_order": 0,
            "is_replacement_order": 0,
            "earliest_ship_date":"2020-11-06 11:25:38",
            "earliest_ship_date_utc":"2020-11-06 19:25:38",
            "purchase_date_local":"2020-11-06 11:25:38",
            "purchase_date_local_utc":"2020-11-06 19:25:38",
            "last_update_date": "2023-02-03 02:27:25",
            "last_update_date_utc":"2023-02-03 10:27:25",
            "posted_date": "",
            "hide_time": 0,
            "shipment_date": "",
            "is_business_order": 0,
            "is_prime": 0,
            "is_premium_order": 0,
            "is_promotion": 0
            "is_return": 0,
            "taxes_included": 2,
            "ship_service_level": "Std US D2D Dom",
            "shipment_service_level_category": "Standard",
            "purchase_order_number": "",
            "payment_method": "Other",
            "cba_displayable_shipping_label": "",
            "order_type": "StandardOrder",
            "latest_ship_date": "2020-11-11T07:59:59Z",
            "earliest_delivery_date": "2020-12-01T08:00:00Z",
            "latest_delivery_date": "2020-12-23T07:59:59Z",
            "number_of_items_shipped": 1,
            "number_of_items_unshipped": 0,
            "sales_channel": "Amazon.com",
            "item_list": [
                {
                    "id": 481,
                    "title": "Fit for Mercedes-Benz",
                    "seller_sku": "sku-355",
                    "asin": "xxxxxx",
                    "order_item_id": "6004266666460",
                    "points_monetary_value_amount": "0.00",
                    "quantity_ordered": 1,
                    "quantity_shipped": 1,
                    "item_price_amount": "135.99",
                    "item_tax_amount": "9.01",
                    "shipping_price_amount": "0.00",
                    "shipping_tax_amount": "0.00",
                    "gift_wrap_price_amount": "0.00",
                    "gift_wrap_tax_amount": "0.00",
                    "shipping_discount_amount": "0.00",
                    "cod_fee_amount": "0.00",
                    "promotion_ids": [],
                    "shipping_discount_tax_amount": "0.00",
                    "promotion_discount_amount": "0.00",
                    "promotion_discount_tax_amount": "0",
                    "cod_fee_discount_amount": "0.00",
                    "gift_message_text": "",
                    "gift_wrap_level": "",
                    "condition_note": "",
                    "condition_id": "New",
                    "condition_subtype_id": "New",
                    "scheduled_delivery_start_date": "",
                    "scheduled_delivery_end_date": "",
                    "price_designation": "",
                    "sid": 101,
                    "sku": "",
                    "product_name": "",
                    "cg_price": 0,
                    "product_id": 0,
                    "pic_url": "/",
                    "fee_name": "推广费",
                    "cg_transport_costs": 0,
                    "fba_shipment_amount": 0,
                    "commission_amount": 0,
                    "other_amount": 0,
                    "asin_url": "https://www.amazon.com/dp/xxxxxx",
                    "fee_currency": "CNY",
                    "fee_icon": "￥",
                    "fee_cost_amount": 0,
                    "fee_cost": 0,
                    "sales_price_amount": 145,
                    "unit_price_amount": 135.99,
                    "tax_amount": -9.01,
                    "promotion_amount": 0,
                    "profit": 135.99,
                    "item_discount": 0,
                    "customized_json":""
                }
            ]
        }
    ],
    "total": 1
}
```

## 附加说明
order_status 说明如下：
1. PendingAvailability：只有预订订单才有此状态；订单已生成，但是付款未授权且商品的发售日期是将来的某一天，订单尚不能进行发货；<br>【注意】仅在日本 (JP)，Preorder 才可能是一个 OrderType 值；
2. Pending：订单已生成，但是付款未授权，订单尚不能进行发货；<br>【注意】<br>对于 OrderType = Standard 的订单，初始的订单状态是 Pending；<br>对于 OrderType = Preorder 的订单（仅适用于 JP），初始的订单状态是 PendingAvailability，当进入付款授权流程时，订单状态将变为 Pending；
3. Unshipped：付款已经过授权，订单已准备好进行发货，但订单中商品尚未发运；
4. PartiallyShipped：订单中的一个或多个（但并非全部）商品已经发货；
5. Shipped：订单中的所有商品均已发货；
6. InvoiceUnconfirmed：订单中的所有商品均已发货，但是卖家还没有向亚马逊确认已经向买家寄出发票；请注意：此参数仅适用于中国地区；
7. Canceled：订单已取消；
8. Unfulfillable：订单无法进行配送，该状态仅适用于通过亚马逊零售网站之外的渠道下单但由亚马逊进行配送的订单；