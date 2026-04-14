# 查询亚马逊源报表-FBM退货订单
查询 Returns Reports 报表

##  接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/data/order/fbmReturnOrderList` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|start_date|开始时间，左闭区间，格式：Y-m-d|是|[string]|2020-01-01|
|end_date|结束时间，右开区间，格式：Y-m-d|是|[string]|2024-08-05|
|date_type|时间查询类型：【默认1】<br>1 退货日期<br>2 下单日期|否|[int]|1|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "date_type": 1,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|2E9941CD-3A26-3550-52A3-F83F4D1977F1|
|response_time|响应时间|是|[string]|2023-06-30 17:28:41|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>id|订单id|是|[long]|2|
|data>>order_hash|订单唯一hash|是|[string]|b7ec98d3d3d11092b8838ef29508aa20|
|data>>sid|店铺id|是|[int]|101|
|data>>order_id|亚马逊订单id|是|[string]|112-6283972-5349000|
|data>>order_date|订购时间|是|[string]|2023-05-22|
|data>>return_date|退货时间|是|[string]|2023-05-24|
|data>>return_status|退货状态|是|[string]|Approved|
|data>>rma_id|RMA单号|是|[string]|DjMbMZrvRRMA|
|data>>label_type|标签类型|是|[string]|AmazonPrePaidLabel|
|data>>label_cost|标签费用|是|[string]|4.13|
|data>>currency_code|币种|是|[string]|USD|
|data>>return_carrier|承运商|是|[string]|USPS|
|data>>tracking_id|运单号|是|[string]|9202090339598309314960|
|data>>label_payer|标签支付方|是|[string]|Customer|
|data>>a_to_z_claim|"A-to-Z"标签, N代表否，Y代表是|是|[string]|N|
|data>>is_prime|"Prime"标签, N代表否，Y代表是|是|[string]|N|
|data>>asin|asin|是|[string]|B0B4WP82TG|
|data>>seller_sku|seller_sku【MSKU】|是|[string]|Hair-Ties-P0360|
|data>>item_name|标题|是|[string]|YiWu HENGFU.hi Heart Pearl Black Hair Ties|
|data>>return_quantity|退货数量|是|[number]|1|
|data>>return_reason|退货原因|是|[string]|CR-UNWANTED_ITEM(客户退货-不想要的商品)|
|data>>in_policy|是否符合政策：N代表否，Y代表是|是|[string]|Y|
|data>>return_type|退货类型|是|[string]|C-Returns|
|data>>resolution|解决方法|是|[string]|StandardRefund|
|data>>invoice_number|发票号码|是|[string]| |
|data>>return_delivery_date|退货送达日期|是|[string]| |
|data>>order_amount|订单金额|是|[string]|5.83|
|data>>order_quantity|商品信息--原始数量|是|[int]|1|
|data>>safet_action_reason|Safe-T索赔原因|是|[string]| |
|data>>safet_claim_id|Saft-T索赔单号|是|[string]| |
|data>>safet_claim_state|Saft-T索赔状态|是|[string]| |
|data>>safet_claim_creation_time|Saft-T索赔时间|是|[string]| |
|data>>safet_claim_reimbursement_amount|Safe-T索赔金额|是|[string]| |
|data>>refunded_amount|退款金额|是|[string]|5.83|
|data>>sync_time|同步数据时间戳|是|[int]|1685260468|
|data>>rma_id_provider|RMA单号提供者(amazon或者Merchant)|是|[string]|Amazon|
|data>>remark|备注|是|[string]|自动化备注|
|data>>tag_type_ids|标签信息|是|[array]| |
|data>>tag_type_ids>>tag_name|标签名称|是|[string]|尺码问题|
|data>>tag_type_ids>>tag_color|标签颜色|是|[string]|E76A5D|
|data>>local_sku|本地产品sku|是|[string]|ZDH1688113470.6414766|
|data>>local_name|品名|是|[string]|自动化单品|
|data>>brand_title|品牌名|是|[string]|xx|
|data>>category_title_path|分类|是|[string]|xxx|
|data>>country|国家|是|[string]|美国|
|data>>seller_name|店铺名|是|[string]|8p1-US|
|data>>asin_url|asin地址|是|[string]|https://www.amazon.com/dp/B0B4WP8XXX|
|data>>pic_url|产品图片|是|[string]|https://xxxx/a8dbce2f2.jpg|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "2E9941CD-3A26-3550-52A3-F83F4D1977F1",
    "response_time": "2023-06-30 17:28:41",
    "data": [
    	{
            "id": 2,
            "order_hash": "b7ec98d3d3d11092b8838ef29508aa20",
            "sid": 101,
            "order_id": "112-6283972-5349000",
            "order_date": "2023-05-22",
            "return_date": "2023-05-24",
            "return_status": "Approved",
            "rma_id": "DjMbMZrvRRMA",
            "rma_id_provider": "Amazon",
            "label_type": "AmazonPrePaidLabel",
            "label_cost": "4.13",
            "currency_code": "USD",
            "return_carrier": "USPS",
            "tracking_id": "9202090339598309314960",
            "label_payer": "Customer",
            "a_to_z_claim": "N",
            "is_prime": "N",
            "asin": "B0B4WP8XXX",
            "seller_sku": "Hair-Ties-P0360",
            "item_name": "YiWu HENGFU.hi Heart Pearl Black Hair Ties - High Stretch Elastic Bands for Women and Girls, Double as Jewelry and Head Rope",
            "return_quantity": 1,
            "return_reason": "CR-UNWANTED_ITEM(客户退货-不想要的商品)",
            "in_policy": "Y",
            "return_type": "C-Returns",
            "resolution": "StandardRefund",
            "invoice_number": "",
            "return_delivery_date": "",
            "order_amount": "5.83",
            "order_quantity": 1,
            "safet_action_reason": "",
            "safet_claim_id": "",
            "safet_claim_state": "",
            "safet_claim_creation_time": "",
            "safet_claim_reimbursement_amount": "",
            "refunded_amount": "5.83",
            "sync_time": 1685260468,
            "rma_id_provider": "Amazon",
            "remark": "自动化备注",
            "tag_type_ids": [{
                "id": 60,
                "tag_name": "尺码问题",
                "tag_type": 2,
                "tag_color": "E76A5D",
                "tag_type_id": "2-60"
            }],
            "local_sku": "ZDH1688113470.6414766",
            "local_name": "自动化单品",
            "brand_title": "",
            "category_title_path": "",
            "country": "美国",
            "seller_name": "8p1-US",
            "asin_url": "https://www.amazon.com/dp/B0B4WP8XXX",
            "pic_url": "https://xxxx/a8dbce2f2.jpg"
    	}
    ],
    "total": 1
}
```
