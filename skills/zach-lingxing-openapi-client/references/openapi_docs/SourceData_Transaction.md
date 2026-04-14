# 查询亚马逊源报表-交易明细
查询领星插件下载的 Transaction 报表数据
>本接口即将下线，建议使用[查询结算中心 - 交易明细](/docs/Finance/settlementTransactionList.md)

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/transaction` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|event_date|报表日期，格式：Y-m-d【每月３日后支持查询上月数据】|是|[string]|2020-06-07|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "event_date": "2020-06-07",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sid|店铺id|是|[int]|1|
|data>>is_to_b|是否为B2B订单：0 否【2c】，1 是|是|[int]|0|
|data>>report_date_month|client_task的月份|是|[string]|2019-03|
|data>>report_index|报表行索引|是|[int]| |
|data>>date_str|原本的日期字符串|是|[string]|1 Mar 2019 00:00:45 GMT+00:00|
|data>>date_locale|当地日期|是|[string]|2019-03-01|
|data>>date_iso|ISO时间|是|[string]|2019-03-01T00:00:45+00:00|
|data>>settlement_id|结算编号|是|[string]|11376876372|
|data>>type|类型：<br>1 ORDER<br>2 REFUND<br>3 ADJUSTMENT<br>4 A_TO_Z_GUARANTEE_CLAIM<br>5 CHARGEBACK_REFUND<br>6 FBA_INVENTORY_FEE<br>7 SERVICE_FEE<br>8 LIGHTNING_DEAL_FEE<br>9 TRANSFER<br>10 ORDER_RETROCHARGE<br>11 REFUND_RETROCHARGE<br>12 CHARGES_TO_CREDIT_CARD<br>13 FBA_CUSTOMER_RETURN_FEE<br>14 DEBT <br>15 NULL【其他类型】<br>16 FEE_ADJUSTMENT<br>17 LIQUIDATIONS<br>18 Shipping Services<br>19 Electronic Transactions<br>20 COD Transactions<br>21 Reimbursements<br>22 Tax Withheld<br>23 Liquidations Adjustments<br>24 PW Order Payment<br>25 PW Trial Shipment<br>26 Fulfilment Fee Refund<br>27 TBYB Order Payment<br>28 TBYB Trial Shipment<br> |是|[int]|1|
|data>>type_str|类型说明|是|[string]|  |
|data>>order_id|订单号|是|[string]|205-0598548-1768342|
|data>>sku|SKU|是|[string]|4H-3NL6-GL1I|
|data>>description|商品描述|是|[string]| |
|data>>quantity|商品数量|是|[number]|1|
|data>>marketplace|销售市场|是|[string]|amazon.co.uk|
|data>>fulfillment|发货方式|是|[string]|Amazon|
|data>>order_city|城市|是|[string]|MIDDLESBROUGH|
|data>>order_state|州|是|[string]|Cleveland|
|data>>order_postal|邮编|是|[string]|TS6 9JN|
|data>>product_sales|销售价格|是|[string]|12.4900|
|data>>product_sales_tax|销售税|是|[string]|  |
|data>>currency|币种|是|[string]|USD|
|data>>shipping_credits|运费|是|[string]|1.8700|
|data>>shipping_credits_tax|运费税（荷兰，瑞典，沙特，阿联酋无该税费）|否|[string]|  |
|data>>gift_wrap_credits|礼品包装费|是|[string]|0.0000|
|data>>gift_wrap_credits_tax|礼品包装税（荷兰，瑞典，沙特，阿联酋无该税费）|否|[string]|  |
|data>>promotional_rebates|促销返点|是|[string]|-1.8700|
|data>>promotional_rebates_tax|促销返点税（荷兰，瑞典，沙特，阿联酋无该税费）|否|[string]|  |
|data>>sales_tax_collected|销售税（仅荷兰，瑞典，沙特，阿联酋有该税费）|否|[string]|0.0000|
|data>>marketplace_facilitator_tax|市场税|是|[string]|0.0000|
|data>>selling_fees|平台费（佣金）|是|[string]|-2.2500|
|data>>fba_fees|FBA发货费|是|[string]|-2.1700|
|data>>other_transaction_fees|其他交易费|是|[string]|0.0000|
|data>>other|其他费|是|[string]|0.0000|
|data>>total|总计|是|[string]|10.5700|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "38AA9D9A-5936-FD62-9901-C415C1951111",
    "response_time": "2021-07-02 11:23:08",
    "data": [
        {
            "sid": 103,
            "is_to_b": 0,
            "report_date_month": "2021-05",
            "report_index": 736,
            "date_str": "May 31, 2021 11:56:23 AM PDT",
            "date_locale": "2021-05-31",
            "date_iso": "2021-05-31T11:56:23-07:00",
            "settlement_id": "142111161",
            "type": 1,
            "order_id": "113-1111111111111111-9121025",
            "sku": "200J",
            "description_str": "KOo",
            "quantity": 1,
            "marketplace": "amazon.com",
            "fulfillment": "Amazon",
            "order_city": "REDWOOD CITY",
            "order_state": "CA",
            "order_postal": "9401142",
            "product_sales": "19.9900",
            "currency": "USD",
            "shipping_credits": "0.0000",
            "shipping_credits_tax": "0.0000",
            "gift_wrap_credits": "0.0000",
            "gift_wrap_credits_tax": "0.0000",
            "promotional_rebates": "-10.0000",
            "promotional_rebates_tax": "0.0000",
            "sales_tax_collected": "0.0000",
            "marketplace_facilitator_tax": "-0.9700",
            "selling_fees": "-1.5000",
            "fba_fees": "-5.4200",
            "other_transaction_fees": "-0.7000",
            "other": "0.0000",
            "total": "2.3700",
            "description": "KORsy to",
            "type_str": "Order"
        },
        {
            "sid": 103,
            "is_to_b": 0,
            "report_date_month": "2021-05",
            "report_index": 741,
            "date_str": "May 31, 2021 2:00:44 PM PDT",
            "date_locale": "2021-05-31",
            "date_iso": "2021-05-31T14:00:44-07:00",
            "settlement_id": "1426581161",
            "type": 1,
            "order_id": "113-111111111111-5120241",
            "sku": "200J",
            "description_str": "KO",
            "quantity": 1,
            "marketplace": "amazon.com",
            "fulfillment": "Amazon",
            "order_city": "HOUSTON",
            "order_state": "TX",
            "order_postal": "77044-6581",
            "product_sales": "19.9900",
            "currency": "USD",
            "shipping_credits": "0.0000",
            "shipping_credits_tax": "0.0000",
            "gift_wrap_credits": "0.0000",
            "gift_wrap_credits_tax": "0.0000",
            "promotional_rebates": "0.0000",
            "promotional_rebates_tax": "0.0000",
            "sales_tax_collected": "0.0000",
            "marketplace_facilitator_tax": "-1.4500",
            "selling_fees": "-3.0000",
            "fba_fees": "-5.4200",
            "other_transaction_fees": "-1.4000",
            "other": "0.0000",
            "total": "10.1700",
            "description": "11111sy to",
            "type_str": "Order"
        }
    ],
    "total": 0
}
```
