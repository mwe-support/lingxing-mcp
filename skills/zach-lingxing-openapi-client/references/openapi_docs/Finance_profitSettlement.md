# 查询利润报表（旧）-结算明细

支持查询系统【财务】>【利润报表】>【结算明细】数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/finance/ProfitState/profitSettlement` | HTTPS | POST | 1 |

## 请求参数



| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[string]|1,2,3|
|start_date|结算开始时间筛选|是|[string]|2023-01-01|
|end_date|结算结束时间筛选|是|[string]|2023-01-30|
|currency_type|币种：<br>0原币种<br>1 CNY<br>2 USD<br>3 EUR<br>4 JPY<br>5 AUD<br>6 CAD<br>7 MXN<br>8 GBP<br>9 INR<br>10 AED<br>11 SGD<br>12 SAR<br>13 BRL<br>14 SEK<br>15 PLN<br>16 TRY|是|[int]|1|
|send_date_start|发货日期开始筛选时间，大于等于结算开始时间|否|[string]|2023-01-01|
|send_date_end|发货日期结束筛选时间，小于等于结算结束时间|否|[string]|2023-01-15|
|offset|分页偏移量|是|[int]|0|
|length|分页长度|是|[int]|20|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| |是|[int]|1|
|msg| |是|[string]|操作成功|
|total| |是|[int]|1762056|
|list| |是|[array]| |
|list>>sid|店铺id|是|[int]|1|
|list>>is_to_b|报告类型：B2C、B2B|是|[string]| B2C |
|list>>send_date|发货时间|是|[string]| |
|list>>date_locale|日期，年月日|是|[string]|2019-05-01|
|list>>date_month|月份，年月|是|[string]|2019-05|
|list>>type|交易类型|是|[number]|1|
|list>>type_str| |是|[string]|Order|
|list>>seller_name|店铺名|是|[string]|AZJKGHPUS|
|list>>order_id|订单号|是|[string]|111-3732700-8306627|
|list>>msku|msku|是|[string]|HPGEJKGBH081AB-USAE2|
|list>>description_str|描述|是|[string]|Bluetooth FM Transmitter for Car, Wireless Radio Transmitter Adapter with Power Off Function|
|list>>asin|asin|是|[string]|B07H2FSSSS|
|list>>icon|货币符号|是|[string]|$|
|list>>currency_code|货币简写|是|[string]|USD|
|list>>bid| |是|[number]|3|
|list>>cid| |是|[number]|3|
|list>>local_sku|sku|是|[string]|GEBH08JK1AB|
|list>>local_name|品名|是|[string]|蓝牙FM发射器|
|list>>settlement_id|交易编号|是|[string]|11778946301|
|list>>marketplace_fee|销售市场|是|[string]|amazon.com|
|list>>fulfillment|发货方式|是|[string]|Amazon|
|list>>quantity|数量|是|[number]|1|
|list>>product_sales|销售价格|是|[number]|17.99|
|list>>shipping_credits|运费|是|[number]| |
|list>>gift_wrap_credits|礼品包装费|是|[number]| |
|list>>promotional_rebates|促销返点|是|[number]| |
|list>>amazon_point_fee|积分|是|[number]| |
|list>>sales_tax_collected|销售税|是|[number]| |
|list>>marketplace_facilitator_tax|市场税|是|[number]| |
|list>>selling_fees|平台佣金|是|[number]|-2.7|
|list>>fba_fees|fba费用|是|[number]|-3.28|
|list>>other_transaction_fees|其他交易费|是|[number]| |
|list>>other|其他费|是|[number]| |
|list>>total|合计|是|[number]|12.01|
|list>>small_image_url|图片|是|[string]|http://ecx.images-amazon.com/images/I/41XalkKZHAL._SL75_.jpg|
|list>>asin_url|asin url|是|[string]|https://www.amazon.com/dp/B07H2FJKSS|
|list>>category_text|分类|是|[string]|音频转换|
|list>>product_brand_text|品牌|是|[string]|GE|
|list>>marketplace|站点|是|[string]|美国|
|list>>cg_price|采购成本|是|[string]| |
|list>>cg_transport_costs|头程成本|是|[string]|&nbsp;|



## 返回成功示例

```
{
    "code": 1,
    "msg": "操作成功",
    "total": 1762056,
    "list": [
        {
            "sid": 1,
            "msku": "HPGEBH081AB-USAE2",
            "is_to_b": 0,
            "date_locale": "2019-05-01",
            "date_month": "2019-05",
            "type": 1,
            "type_str": "Order",
            "order_id": "111-3732700-8306627",
            "description_str": "Bluetooth FM Transmitter for Car",
            "settlement_id": "11778946301",
            "marketplace_fee": "amazon.com",
            "fulfillment": "Amazon",
            "quantity": 1,
            "product_sales": 17.99,
            "shipping_credits": 0,
            "gift_wrap_credits": 0,
            "promotional_rebates": 0,
            "amazon_point_fee": 0,
            "sales_tax_collected": 0,
            "marketplace_facilitator_tax": 0,
            "selling_fees": -2.7,
            "fba_fees": -3.28,
            "other_transaction_fees": 0,
            "other": 0,
            "total": 12.01,
            "seller_name": "AZHPUS",
            "marketplace": "美国",
            "currency_code": "USD",
            "small_image_url": "http://ecx.images-amazon.com/images/I/41XalkKZHAL._SL75_.jpg",
            "asin_url": "https://www.amazon.com/dp/B07H2FY6SS",
            "asin": "B07H2FY6SS",
            "local_sku": "GEBH081AB",
            "local_name": "蓝牙FM发射器",
            "category_text": "音频转换",
            "product_brand_text": "GE",
            "icon": "$"
        }
    ]
}
```
