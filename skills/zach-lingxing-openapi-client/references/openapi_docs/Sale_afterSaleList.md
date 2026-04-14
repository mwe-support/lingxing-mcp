# 查询售后订单列表

支持查询【销售】>【售后订单】数据

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/amzod/order/afterSaleList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id，多个使用英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[string]|1|
|start_date|查询时间，左闭右开，格式：Y-m-d|是|[string]|2022-02-01|
|end_date|查询时间，左闭右开，格式：Y-m-d|是|[string]|2022-03-01|
|date_type|查询时间类型：【默认1】<br>1 售后时间，对应data>>deal_time字段<br>2 订购时间<br>3 更新时间|否|[int]|1|
|after_type|售后类型，多个使用英文逗号分隔：<br>1 退款<br>2 退货<br>3 换货|否|[string]|1,2|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|
|amazon_order_id_list|亚马逊订单id列表，上限50|否|[Array]|["113-9870855-8214638","113-9870855-8214639"]|

## 请求示例
```
{
    "sid":"6,7,19",
    "start_date":"2022-02-01",
    "end_date":"2022-03-01",
    "data_type":2,
    "after_type":"1,2",
    "offset":0,
    "length":1000
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|3EE1982B-EDC3-0531-83DF-2BEA6F080DDA|
|response_time|响应时间|是|[string]|2022-12-0714:54:56|
|total|总记录数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>id|记录id，【非唯一键】|是|[long]|12|
|data>>amazon_order_id|亚马逊订单号|是|[string]|687-0075130-7007581|
|data>>sid|店铺id|是|[int]|1|
|data>>asin|asin|是|[string]|B0ABC50521|
|data>>msku|msku|是|[string]|MSKU52FB8CE|
|data>>correlation_id|关联id|是|[int]|1|
|data>>purchase_time|订购时间|是|[string]|2022-05-12 20:35:18|
|data>>deal_time|售后时间<br>【同一个订单存在多个售后订单时，需以 item_list>>after_time 为准】|是|[string]|2022-05-12 20:35:18|
|data>>gmt_modified|更新时间<br>【同一个订单存在多个售后订单时，需以 item_list>>data_update_time 为准】|是|[string]|2022-05-12 20:35:18|
|data>>interval_days|售后间隔天数|是|[int]|10|
|data>>is_mcf_order|是否为多渠道订单：<br>0 默认值<br>1 普通订单<br>2 多渠道订单|是|[int]|1|
|data>>seller_country|店铺国家信息|是|[string]|XPXC美国|
|data>>delivery_type|配送方式|是|[string]|FBA|
|data>>order_total_amount|订单总金额|是|[string]|7.99|
|data>>order_total_amount_currency_code|订单总金额-货币单位|是|[string]|$|
|data>>order_total_amount_number|订单总金额-金额|是|[string]|2.35|
|data>>total_refund_amount|退款总金额|是|[string]|5.555555|
|data>>total_refund_amount_currency_code|退款总金额-货币单位|是|[string]|$|
|data>>total_refund_amount_number|退款总金额-金额|是|[string]|-4.700|
|data>>total_refund_cost|退款总费用|是|[string]|8.545622|
|data>>total_refund_cost_currency_code|退款总金额-货币单位|是|[string]|$|
|data>>total_refund_cost_number|退款总成本-金额|是|[string]|0.300|
|data>>after_type_tag|售后类型标签|是|[array]|["退款","退货","换货"]|
|data>>item_list|商品列表|是|[array]||
|data>>item_list>>small_image_url|商品缩略图地址|是|[string]||
|data>>item_list>>item_name|商品标题|是|[string]|product title 07E1A4C731 |
|data>>item_list>>local_sku|本地产品sku|是|[string]||
|data>>item_list>>local_name|本地商品名称|是|[string]|[演示数据]Sony儿童耳机|
|data>>item_list>>asin|asin|是|[string]|B0ABC50521|
|data>>item_list>>asin_url|asin_url|是|[string]|https://xxxx/xxxx|
|data>>item_list>>msku|msku|是|[string]|MSKU52FB8CE|
|data>>item_list>>after_type|售后类型|是|[string]|退款，退货，换货|
|data>>item_list>>after_quantity|售后数量|是|[int]|2|
|data>>item_list>>after_reason|售后原因|是|[string]|5|
|data>>item_list>>after_time|售后时间|是|[string]|2022-02-10 16:00:05|
|data>>item_list>>after_interval|售后间隔|是|[string]|1天|
|data>>item_list>>data_update_time|数据更新时间|是|[string]|2022-02-11 11:03:05|
|data>>item_list>>refund_amount|退款金额|是|[string]|-$28.0200|
|data>>item_list>>refund_amount_details|退款金额详情（有退款金额才会返回详情）|是|[array]| |
|data>>item_list>>refund_amount_details>>type|退款金额类型|是|[string]|ShippingCharge|
|data>>item_list>>refund_amount_details>>amount|退款金额|是|[string]|-$6.3800|
|data>>item_list>>refund_cost|退款花费|是|[string]|$10.4300|
|data>>item_list>>refund_cost_details|退款花费详情（有退款花费才会返回详情）|是|[array]| |
|data>>item_list>>refund_cost_details>>type|退款花费类型|是|[string]|RefundCommission|
|data>>item_list>>refund_cost_details>>amount|退款花费|是|[string]|-$0.6000|
|data>>item_list>>return_status|退货状态|是|[string]|Approved|
|data>>item_list>>inventory_attributes|库存属性|是|[string]| |
|data>>item_list>>lpn_number|LPN编号|是|[string]| |
|data>>item_list>>buyers_note|买家备注|是|[string]| |
|data>>item_list>>rma_order_number|RMA单号|是|[string]|D5LCqzJZRRMA|
|data>>item_list>>carriers|承运商|是|[string]|USPS|
|data>>item_list>>waybill_number|运单号|是|[string]|9202090153540168949151|
|data>>item_list>>exchange_order_number|换货订单号|是|[string]|113-2766421-2949046|
|data>>item_list>>md5|md5唯一值【已废弃】|是|[string]|c416fba9801f5c59bf5f787a7ea0a641|
|data>>item_list>>md5_new|新md5唯一值【已废弃】,可参考两个唯一字段：item_identifier，md5_v2|是|[string]|c416fba9801f5c59bf5f787a7ea0a642|
|data>>item_list>>item_identifier|唯一标识|是|[string]||
|data>>item_list>>md5_v2|压缩后的唯一标识|是|[string]||
|data>>item_list>>orderDateYear|订单数据年份|是|[int]||
|data>>item_list>>row_index|解析数据编号|是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "680C4F7A-D8F1-32B1-E078-BAEBE6230B85",
    "response_time": "2023-02-18 17:12:37",
    "data": [
        {
            "id": 33,
	        "asin": "B09MT9BKAD",
            "msku": "Pink_Head_Rope_12",
            "amazon_order_id": "113-9870855-8214638",
            "sid": 101,
            "purchase_time": "2023-02-07 23:41:08",
            "deal_time": "2023-02-16 23:50:50",
            "gmt_modified": "2023-02-17 11:36:17",
            "correlation_id": 3,
            "interval_days": 10,
            "is_mcf_order": 1,
            "seller_country": "8p-US 美国",
            "delivery_type": "FBM",
            "order_total_amount": "$2.35",
            "order_total_amount_currency_code": "$",
            "order_total_amount_number": "2.35",
            "total_refund_amount": "-$4.700",
            "total_refund_amount_currency_code": "$",
            "total_refund_amount__number": "-4.700",
            "total_refund_cost": "$0.300",
            "total_refund_cost_currency_code": "$",
            "total_refund_cost_number": "0.300",
            "after_type_tag": [
                "退款",
                "退货"
            ],
            "item_list": [
                {
                    "small_image_url": "https://xxxx/xxx.jpg",
                    "item_name": "Love Pearl Bottom Hair Circle",
                    "local_sku": "auto010",
                    "local_name": "自动010",
                    "asin": "B09MT9BKAD",
                    "asin_url": "https://www.amazon.com/dp/B09MT9BKAD",
                    "msku": "Pink_Head_Rope_12",
                    "after_type": "退货",
                    "after_time": "2023-02-17 00:00:00",
                    "data_update_time": "2023-02-17 16:54:14",
                    "after_interval": "10天",
                    "refund_amount": "",
                    "refund_cost": "",
                    "refund_currency_icon": "",
                    "after_quantity": 1,
                    "after_reason": "CR-ORDERED_WRONG_ITEM",
                    "return_status": "Approved",
                    "inventory_attributes": "",
                    "lpn_number": "",
                    "buyers_note": "自动化备注",
                    "rma_order_number": "D5LCqzJZRRMA",
                    "carriers": "USPS",
                    "waybill_number": "9202090153540168949151",
                    "exchange_order_number": "",
                    "md5": "e3e9ca874381650df28121eb1c74d8a9",
                    "md5_new": "e3e9ca874381650df28121eb1c74d8a1"
                },
                {
                    "small_image_url": "https://xxxx/xxx.jpg",
                    "item_name": "Love Pearl Bottom Hair Circle",
                    "local_sku": "auto010",
                    "local_name": "自动010",
                    "asin": "",
                    "asin_url": "",
                    "msku": "Pink_Head_Rope_12",
                    "fid": "1PBCVYGW03FZY",
                    "after_type": "退款",
                    "after_time": "2023-02-16 23:50:50",
                    "data_update_time": "2023-02-17 11:36:17",
                    "after_interval": "10天",
                    "refund_amount": "-$4.700",
                    "refund_amount_details": [
                        {
                            "type": "Goodwill",
                            "amount": "-$2.350"
                        },
                        {
                            "type": "Principal",
                            "amount": "-$2.000"
                        },
                        {
                            "type": "ShippingCharge",
                            "amount": "-$0.350"
                        }
                    ],
                    "refund_cost": "$0.300",
                    "refund_cost_details": [
                        {
                            "type": "Commission",
                            "amount": "$0.260"
                        },
                        {
                            "type": "ShippingHB",
                            "amount": "$0.040"
                        }
                    ],
                    "after_quantity": 1,
                    "after_reason": "",
                    "return_status": "",
                    "inventory_attributes": "",
                    "lpn_number": "",
                    "buyers_note": "",
                    "rma_order_number": "",
                    "carriers": "",
                    "waybill_number": "",
                    "exchange_order_number": "",
                    "md5": "a3f4403419630bb77076eac32bd6277c",
                    "md5_new": "a3f4403419630bb77076eac32bd6276c",
                    "row_index": 1
                }
            ]
        }
    ],
    "total": 1
}
```
