# 查询发货结算报告
支持查询亚马逊发货与结算差异报告数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/cost/center/api/settlement/report ` | HTTPS | POST | 3 |

## 请求参数

| 参数名           | 说明  | 必填 | 类型     | 示例  |
| --------------- | ---------------- | ---- | -------- | ------ |
| amazonSellerIds | 亚马逊店铺id | 是   | [array]  | ["xxxxxxxxxxxxxxxx"] |
| sids            | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 是   | [array]  | [101,102] |
| timeType        | 时间类型：<br>01 下单时间<br>02 付款时间<br>03 发货时间<br>04 结算时间<br>05 转账时间<br>06 更新时间 | 是   | [string] |  01 |
| filterBeginDate | 开始日期，格式：Y-m-d，双闭区间| 是 | [string] | 2022-09-25 |
| filterEndDate   | 结束日期，格式：Y-m-d，双闭区间| 是 | [string] | 2022-09-25 |
| countryCodes    | 国家编码 | 否   | [array]  | UK |
| orderNumbers    | 订单编号   | 否   | [array]  |   |
| shipmentNumbers | 配送编号   | 否   | [array]  |   |
| customNumbers   | 自定义编号 | 否   | [array]  |   |
| mskus           | msku     | 否   | [array]  |   |
| skus            | sku      | 否   | [array]  |   |
| productNames    | 品名      | 否   | [array]  |   |
| trackCodes      | 物流追踪编码| 否  | [array] | ["QA0447985570"] |
| fulfillmentType | 配送方式【不传默认全部】：<br>  01 FBA| 否  | [string]  | 01   |
| offset          | 分页偏移量，默认0| 否 | [int]   | 0  |
| length          | 分页长度，默认20，上限1000| 否  | [int]  | 20   |

## 请求示例
```
{
    "amazonSellerIds": [
        "xxxxxxxxxxxxxxxx"
    ],
    "sids": [
        101,
        102
    ],
    "timetype": "01",
    "filterbegindate": "2023-05-01",
    "filterenddate": "2023-10-13",
    "countryCodes": [
        "UK"
    ],
    "orderNumbers": [
        "202-8957192-8477905"
    ],
    "shipmentNumbers": [
        "Dg2XV5wt5"
    ],
    "customNumbers": [
        "xxxxx"
    ],
    "mskus": [
        "msku-1"
    ],
    "skus": [
        "sku-1"
    ],
    "fulfillmentType": "01",
    "offset": 0,
    "length": 1
}
```

## 返回结果
Json Object

| 参数名                                  | 说明             | 必填 | 类型      | 示例 |
| :------------------------------------- | :--------------- | :---- | :--------- | :---- |
| code                                    | 状态码，1 成功   | 是   | [int]  |      |
| msg                                     | 响应信息        | 是   | [string]  |      |
| success                                 | 操作是否成功     | 是   | [boolean] |      |
| traceId                                 | 请求链路id       | 是   | [string]  |      |
| data                                    | 响应数据         | 是   | [Object]  |      |
| data>>total                             | 总数            | 是   | [int]  |      |
| data>>records                           | 记录列表        | 是   | [array]   |  |
| data>>records>>sellerId                 | 亚马逊店铺id     | 是   | [string]  | xxxxxxxxxxxxxxxx |
| data>>records>>sid                      | 店铺id         | 是   | [int]   | 101 |
| data>>records>>sellerName               | 店铺名称         | 是   | [string]  | JHL-Official-02 |
| data>>records>>countryCode              | 国家编码         | 是   | [string]  | UK |
| data>>records>>amazonOrderId            | 亚马逊订单id     | 是   | [string]  | 202-8957192-8477905 |
| data>>records>>shipmentItemId		      | 亚马逊包裹详情id  | 是   | [string]  |  |
| data>>records>>shipmentId               | 配送编号         | 是   | [string]  | Dg2XV5wt5|
| data>>records>>msku                     | msku            | 是   | [string]  | 19212H1033-A |
| data>>records>>localSku                 | sku             | 是   | [string]  | tuboshu111 |
| data>>records>>localName                | 品名             | 是   | [string]  | 土拨鼠数据线 |
| data>>records>>quantity                 | 数量             | 是   | [number]  |   1   |
| data>>records>>shipmentsDateLocale      | 发货时间         | 是   | [string]  | 2022-09-20 05:19:02 |
| data>>records>>financePostedDateLocale  | 结算时间         | 是   | [string]  | 2022-09-21 05:19:02 |
| data>>records>>settlementId             | 结算编号         | 是   | [string]  |      |
| data>>records>>daysBetweenShipAndFiance | 结算与发货间隔    | 是   | [string]  |00天00小时00分|
| data>>records>>fundTransferDateLocale   | 转账时间         | 是   | [string]  |      |
| data>>records>>fundTransferStatus       | 转账状态         | 是   | [string]  |Succeeded|
| data>>records>>processingStatus         | 结算状态         | 是   | [string]  | 已结算 |
| data>>records>>itemPrice                | 销售金额         | 是   | [number]  | 14.99 |
| data>>records>>itemTax                  | 销售税额         | 是   | [number]  | 3.00|
| data>>records>>shippingPrice            | 买家运费         | 是   | [number]  |      |
| data>>records>>shippingTax              | 买家运费税额     | 是   | [number]  |      |
| data>>records>>giftWrapPrice            | 礼品包装金额     | 是   | [number]  |      |
| data>>records>>giftWrapTax              | 礼品包装税额     | 是   | [number]  |      |
| data>>records>>itemPromotionDiscount    | 促销折扣（商品） | 是   | [number]  |      |
| data>>records>>shipPromotionDiscount    | 促销折扣（运费） | 是   | [number]  |      |
| data>>records>>currencyCode             | 币种           | 是   | [string]  |      |
| data>>records>>trackingNumber           | 物流追踪编号     | 是   | [string]  | QA0447985570 |
| data>>records>>salesChannel             | 销售渠道         | 是   | [string]  | Amazon.co.uk |
| data>>records>>merchantOrderId          | 自定义订单编号   | 是   | [string]  |      |
| data>>records>>brandName                | 品牌             | 是   | [string]  |  aplle |
| data>>records>>categoryName             | 分类             | 是   | [string]  | 耳机类 |
| data>>records>>listing                  | listing负责人    | 是   | [string]  | 张三,李四  |
| data>>records>>productDeveloper         | 开发负责人       | 是   | [string]  | duanfei001 |
| data>>records>>purchaseDateLocale       | 下单时间         | 是   | [string]  |2022-09-18 23:02:42|
| data>>records>>paymentsDateLocale       | 付款时间         | 是   | [string]  |2022-09-20 05:19:02|
| data>>records>>saleCountryName          | 销售国家         | 是   | [string]  | 英国 |
| data>>records>>region                   | 销售地区         | 是   | [string]  |      |
| data>>records>>shipCity                 | 销售城市         | 是   | [string]  |      |
| data>>records>>shipPostalCode           | 邮编             | 是   | [string]  |      |
| data>>records>>logisitcsMode            | 物流方式         | 是   | [string]  |  AMZN_UK |
| data>>records>>fulfillmentCenterId      | 运营中心         | 是   | [string]  | LCY2 |
| data>>records>>fulfillment              | 配送方式         | 是   | [string]  | FBA |
| data>>records>>gmtModified              | 更新时间         | 是   | [string]  | 2022-09-20 16:13:44 |

## 返回成功示例

```
{
    "code": 1,
    "msg": "操作成功",
    "data": {
        "records": [
            {
                "sellerId": "xxxxxxxxxxxxxxxx",
                "countryCode": "UK",
                "sellerName": "JHL | Official-02",
                "amazonOrderId": "202-8957192-8477905",
                "shipmentId": "Dg2XV5wt5",
                "msku": "19212H1033-A",
                "localSku": "tuboshu111",
                "localName": "土拨鼠数据线",
                "quantity": 1,
                "shipmentsDateLocale": "2022-09-20 05:19:02",
                "financePostedDateLocale": null,
                "settlementId": null,
                "daysBetweenShipAndFiance": "00天00小时00分",
                "fundTransferDateLocale": null,
                "fundTransferStatus": null,
                "processingStatus": "",
                "itemPrice": 14.99,
                "itemTax": 3.00,
                "shippingPrice": 0.00,
                "shippingTax": 0.00,
                "giftWrapPrice": 0.00,
                "giftWrapTax": 0.00,
                "itemPromotionDiscount": 0.00,
                "shipPromotionDiscount": 0.00,
                "currencyCode": "GBP",
                "trackingNumber": "QA0447985570",
                "salesChannel": "Amazon.co.uk",
                "merchantOrderId": "",
                "brandName": "aplle",
                "categoryName": "耳机类",
                "listing": "张三,李四",
                "productDeveloper": "duanfei001",
                "purchaseDateLocale": "2022-09-18 23:02:42",
                "paymentsDateLocale": "2022-09-20 05:19:02",
                "saleCountryName": "英国",
                "region": "--",
                "shipCity": "LONDON",
                "shipPostalCode": "W6 8DX",
                "logisitcsMode": "AMZN_UK",
                "fulfillmentCenterId": "LCY2",
                "fulfillment": "FBA",
                "gmtModified": "2022-09-20 16:13:44",
            }
        ],
        "total": 275
    },
    "traceId": "b47d6507-9ea1-4502-b477-7943f38c1ca2.1670570926191",
    "success": true
}
```

## 返回失败示例

```
{
    "code": 0,
    "msg": "操作失败",
    "data": null,
    "traceId": "b2532fc7-9c1b-4b08-8d30-301b31b70562.1663226369188",
    "success": false
}
```

