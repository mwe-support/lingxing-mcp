# 查询会员折扣or价格折扣详情+listing+订单(批量)

## 接口信息

| API Path                                                    | 请求协议 | 请求方式 | [令牌桶容量]() |
| :---------------------------------------------------------- | :------- | :------- | :------------- |
| `/promotionApi/open/promotion/primeDiscountAllDetailBatch` | HTTPS    | POST     | 1              |

## 请求参数

| 参数名                    | 说明                                    | 必填 | 类型     | 示例                                                         |
| :------------------------ | :-------------------------------------- | :--- | :------- | :----------------------------------------------------------- |
| itemList                  | 批量请求详情itemList个数最小为1最大为20 | 是   | [array]  | [{"promotionId":"2577860007635320832","storeId":"32","orderPageNum":1,"orderPageSize":20,"listingPageNum":2,"listingPageSize":1}] |
| itemList>>promotionId     | 活动id                                  | 是   | [string] | 2577860007635320832                                          |
| itemList>>storeId         | 店铺id                                  | 是   | [string] | 32                                                           |
| itemList>>orderPageNum    | 活动订单分页页数，最小为1               | 是   | [number] | 1                                                            |
| itemList>>orderPageSize   | 活动订单分页大小，最小为1，最大为200    | 是   | [number] | 20                                                           |
| itemList>>listingPageNum  | 活动listing分页页数，最小为1            | 是   | [number] | 1                                                            |
| itemList>>listingPageSize | 活动listing分页大小，最小为1，最大为200 | 是   | [number] | 20                                                           |

## 请求示例

```
{
    "itemList": [
        {
            "promotionId": "jgzk-123456",
            "storeId": "32",
            "orderPageNum": 1,
            "orderPageSize": 20,
            "listingPageNum": 1,
            "listingPageSize": 20
        }
    ]
}
```

## 返回结果

Json Object

| 参数名                                                      | 说明                                                       | 必填 | 类型      | 示例                                                         |
| :---------------------------------------------------------- | :--------------------------------------------------------- | :--- | :-------- | :----------------------------------------------------------- |
| code                                                        | 0成功                                                      | 是   | [number]  | 1                                                            |
| message                                                     |                                                            | 是   | [string]  | 操作成功                                                     |
| error_details                                               |                                                            | 否   | [array]   |                                                              |
| request_id                                                  |                                                            | 是   | [string]  |                                                              |
| response_time                                               |                                                            | 是   | [string]  |                                                              |
| total                                                       |                                                            | 是   | [int]     |                                                              |
| data                                                        |                                                            | 是   | [array]   | [{"promotionId":"2577860007635320832","storeId":"AJGRSY3EK14NJ","customerTarget":null,"primeDiscount":{"storeId":"AJGRSY3EK14NJ","storeName":"非凡-US","regionName":"美国","currencyIcon":"$","promotionId":"2577860007635320832","name":"11_14_17_13","status":2,"statusText":"已过期","originStatus":"ENDED","originStatusText":"已结束","customerTarget":null,"errorCount":"0","promotionStartTime":"2022-11-15 00:00:00","promotionEndTime":"2022-11-16 23:59:00","lastSyncTime":null,"pullDetailTaskId":null,"pullDetailStatus":null},"listingPage":{"total":2,"size":1,"pageCount":2,"current":2,"currentSize":1,"records":[{"storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","sellerSku":"31-250J-NKH6","asin":"B09SB1R9NB","asinUrl":"https://www.amazon.co.jp/dp/B09SB1R9NB","smallImageUrl":"https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg","itemName":"モース暗号ブレスレット","coupon":null,"secKIll":{"salesPrice":2660,"discountPrice":0,"discount":2660,"dealQuantity":""},"management":null,"primeDiscount":null}],"hasNextPage":false,"hasPreviousPage":true},"orderPage":{"total":1,"size":20,"pageCount":1,"current":1,"currentSize":1,"records":[{"amazonOrderId":"fasdfasdga13241-R","storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","orderItems":[{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"Percentage Off 2025/07/21 2-4-51-873"},{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be"}],"purchaseDate":"2022-05-07 00:00:00","orderTotalAmount":0,"orderStatus":"CANCELLED"}],"hasNextPage":false,"hasPreviousPage":false}}] |
| data>>promotionId                                           | 活动id                                                     | 是   | [string]  | 2577860007635320832                                          |
| data>>storeId                                               | 店铺id                                                     | 是   | [string]  | AJGRSY3EK14NJ                                                |
| data>>customerTarget                                        | 消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣 | 是   | [null]    | null                                                         |
| data>>primeDiscount                                         | 会员折扣or价格折扣信息                                     | 是   | [object]  |                                                              |
| data>>primeDiscount>>storeId                                | 店铺ID                                                     | 是   | [string]  | AJGRSY3EK14NJ                                                |
| data>>primeDiscount>>storeName                              | 店铺名                                                     | 是   | [string]  | 非凡-US                                                      |
| data>>primeDiscount>>regionName                             | 国家/地区名                                                | 是   | [string]  | 美国                                                         |
| data>>primeDiscount>>currencyIcon                           | 货币icon                                                   | 是   | [string]  | $                                                            |
| data>>primeDiscount>>promotionId                            | 活动id                                                     | 是   | [string]  | 2577860007635320832                                          |
| data>>primeDiscount>>name                                   | 名称                                                       | 是   | [string]  | 11_14_17_13                                                  |
| data>>primeDiscount>>status                                 | 状态 0其他 1进行中 2已过期 3未开始 4已取消                 | 是   | [number]  | 2                                                            |
| data>>primeDiscount>>statusText                             | 状态说明                                                   | 是   | [string]  | 已过期                                                       |
| data>>primeDiscount>>originStatus                           | 促销活动平台状态                                           | 是   | [string]  | ENDED                                                        |
| data>>primeDiscount>>customerTarget                         | 消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣 | 是   | [null]    | null                                                         |
| data>>primeDiscount>>errorCount                             | >0 则 需要注意                                             | 是   | [string]  | 0                                                            |
| data>>primeDiscount>>promotionStartTime                     | 活动开始时间                                               | 是   | [string]  | 2022-11-15 00:00:00                                          |
| data>>primeDiscount>>promotionEndTime                       | 活动结束时间                                               | 是   | [string]  | 2022-11-16 23:59:00                                          |
| data>>primeDiscount>>lastSyncTime                           | 最后同步时间                                               | 是   | [null]    | null                                                         |
| data>>primeDiscount>>pullDetailStatus                       | 获取详情状态 0=未获取（获取失败），1=获取中，2=获取成功    | 是   | [null]    | null                                                         |
| data>>listingPage                                           | 会员折扣or价格折扣涉及的Listing信息                        | 是   | [object]  |                                                              |
| data>>listingPage>>total                                    | 总数                                                       | 是   | [number]  | 2                                                            |
| data>>listingPage>>size                                     | 分页每页size                                               | 是   | [number]  | 1                                                            |
| data>>listingPage>>pageCount                                | 总页数                                                     | 是   | [number]  | 2                                                            |
| data>>listingPage>>current                                  | 当前页数                                                   | 是   | [number]  | 2                                                            |
| data>>listingPage>>currentSize                              | 当前页数据条数                                             | 是   | [number]  | 1                                                            |
| data>>listingPage>>records                                  |                                                            | 是   | [array]   | [{"storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","sellerSku":"31-250J-NKH6","asin":"B09SB1R9NB","asinUrl":"https://www.amazon.co.jp/dp/B09SB1R9NB","smallImageUrl":"https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg","itemName":"モース暗号ブレスレット","coupon":null,"secKIll":{"salesPrice":2660,"discountPrice":0,"discount":2660,"dealQuantity":""},"management":null,"primeDiscount":null}] |
| data>>listingPage>>records>>storeId                         | 店铺id                                                     | 是   | [string]  | 31                                                           |
| data>>listingPage>>records>>storeName                       | 店铺名                                                     | 是   | [string]  | 非凡-JP                                                      |
| data>>listingPage>>records>>regionName                      | 国家/地区名                                                | 是   | [string]  | 日本                                                         |
| data>>listingPage>>records>>currencyIcon                    | 货币icon                                                   | 是   | [string]  | JP¥                                                          |
| data>>listingPage>>records>>sellerSku                       | seller_sku                                                 | 是   | [string]  | 31-250J-NKH6                                                 |
| data>>listingPage>>records>>asin                            | asin                                                       | 是   | [string]  | B09SB1R9NB                                                   |
| data>>listingPage>>records>>asinUrl                         | asin跳转亚马逊前台链接                                     | 是   | [string]  | https://www.amazon.co.jp/dp/B09SB1R9NB                       |
| data>>listingPage>>records>>smallImageUrl                   | 商品缩略图                                                 | 是   | [string]  | https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg   |
| data>>listingPage>>records>>itemName                        | 商品标题                                                   | 是   | [string]  | モース暗号ブレスレット                                       |
| data>>listingPage>>records>>primeDiscount                   | 会员折扣or价格折扣基本信息                                 | 是   | [object]  | null                                                         |
| data>>listingPage>>records>>primeDiscount>>salesPrice       | 定价(listing优惠价)                                        | 是   | [number]  |                                                              |
| data>>listingPage>>records>>primeDiscount>>discountType     | 优惠类型 FIXED：固定折扣  PERCENT_OFF百分比折扣            | 是   | [string]  |                                                              |
| data>>listingPage>>records>>primeDiscount>>discountValue    | 会员折扣/价格折扣                                          | 是   | [number]  |                                                              |
| data>>listingPage>>records>>primeDiscount>>discountValueStr | 会员折扣/价格折扣 描述                                     | 是   | [string]  |                                                              |
| data>>listingPage>>records>>primeDiscount>>discountPrice    | 会员价/折扣价                                              | 是   | [number]  |                                                              |
| data>>listingPage>>records>>primeDiscount>>salesAmount      | 销售额                                                     | 是   | [number]  |                                                              |
| data>>listingPage>>records>>primeDiscount>>salesVolume      | 销量                                                       | 是   | [int]     |                                                              |
| data>>listingPage>>records>>primeDiscount>>pageView         | 浏览量                                                     | 是   | [long]    |                                                              |
| data>>listingPage>>records>>primeDiscount>>exchangeRate     | 转化率                                                     | 是   | [number]  |                                                              |
| data>>listingPage>>hasNextPage                              | 是否有下一页                                               | 是   | [boolean] | false                                                        |
| data>>listingPage>>hasPreviousPage                          | 是否有上一页                                               | 是   | [boolean] | true                                                         |
| data>>orderPage                                             | 会员折扣or价格折扣涉及的订单信息                           | 是   | [object]  |                                                              |
| data>>orderPage>>total                                      | 总数                                                       | 是   | [number]  | 1                                                            |
| data>>orderPage>>size                                       | 分页每页size                                               | 是   | [number]  | 20                                                           |
| data>>orderPage>>pageCount                                  | 总页数                                                     | 是   | [number]  | 1                                                            |
| data>>orderPage>>current                                    | 当前页数                                                   | 是   | [number]  | 1                                                            |
| data>>orderPage>>currentSize                                | 当前页数据条数                                             | 是   | [number]  | 1                                                            |
| data>>orderPage>>records                                    |                                                            | 是   | [array]   | [{"amazonOrderId":"fasdfasdga13241-R","storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","orderItems":[{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"Percentage Off 2025/07/21 2-4-51-873"},{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be"}],"purchaseDate":"2022-05-07 00:00:00","orderTotalAmount":0,"orderStatus":"CANCELLED"}] |
| data>>orderPage>>records>>amazonOrderId                     | 亚马逊订单号                                               | 是   | [string]  | fasdfasdga13241-R                                            |
| data>>orderPage>>records>>storeId                           | 店铺id                                                     | 是   | [string]  | 31                                                           |
| data>>orderPage>>records>>storeName                         | 店铺名                                                     | 是   | [string]  | 非凡-JP                                                      |
| data>>orderPage>>records>>regionName                        | 国家/地区名                                                | 是   | [string]  | 日本                                                         |
| data>>orderPage>>records>>currencyIcon                      | 货币icon                                                   | 是   | [string]  | JP¥                                                          |
| data>>orderPage>>records>>orderItems                        | 订单商品信息                                               | 是   | [array]   | [{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"Percentage Off 2025/07/21 2-4-51-873"},{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be"}] |
| data>>orderPage>>records>>orderItems>>sellerSku             | seller_sku                                                 | 是   | [string]  | 09-CJWX-DFQH                                                 |
| data>>orderPage>>records>>orderItems>>asin                  | asin                                                       | 是   | [string]  | B09SBF3H99                                                   |
| data>>orderPage>>records>>orderItems>>asinUrl               | asin跳转亚马逊前台链接                                     | 是   | [string]  | https://www.amazon.co.jp/dp/B09SBF3H99                       |
| data>>orderPage>>records>>orderItems>>smallImageUrl         | 商品缩略图                                                 | 是   | [string]  | https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg   |
| data>>orderPage>>records>>orderItems>>itemName              | 商品标题                                                   | 是   | [string]  | シンプルなハート型ワックス編みカップルブレスレット (Red)     |
| data>>orderPage>>records>>orderItems>>localName             | 品名                                                       | 是   | [string]  | KT7XL                                                        |
| data>>orderPage>>records>>orderItems>>localSku              | localSku                                                   | 是   | [string]  | SKUKT7XL                                                     |
| data>>orderPage>>records>>orderItems>>promotionId           | 促销ID                                                     | 是   | [string]  | Percentage Off 2025/07/21 2-4-51-873                         |
| data>>orderPage>>records>>purchaseDate                      | 订购时间                                                   | 是   | [string]  | 2022-05-07 00:00:00                                          |
| data>>orderPage>>records>>orderTotalAmount                  | 订单总金额                                                 | 是   | [number]  | 0                                                            |
| data>>orderPage>>records>>orderStatus                       | 订单状态                                                   | 是   | [string]  | CANCELLED                                                    |
| data>>orderPage>>hasNextPage                                | 是否有下一页                                               | 是   | [boolean] | false                                                        |
| data>>orderPage>>hasPreviousPage                            | 是否有上一页                                               | 是   | [boolean] | false                                                        |

## 返回成功示例

```
{
    "code": 1,
    "message": "操作成功",
    "error_details": [],
    "request_id": "",
    "response_time": "",
    "total": 0,
    "data": [{
        "promotionId": "2577860007635320832",
        "storeId": "AJGRSY3EK14NJ",
        "customerTarget": null,
        "primeDiscount": {
            "storeId": "AJGRSY3EK14NJ",
            "storeName": "非凡-US",
            "regionName": "美国",
            "currencyIcon": "$",
            "promotionId": "2577860007635320832",
            "name": "11_14_17_13",
            "status": 2,
            "statusText": "已过期",
            "originStatus": "ENDED",
            "customerTarget": null,
            "errorCount": "0",
            "promotionStartTime": "2022-11-15 00:00:00",
            "promotionEndTime": "2022-11-16 23:59:00",
            "lastSyncTime": null,
            "pullDetailStatus": null
        },
        "listingPage": {
            "total": 2,
            "size": 1,
            "pageCount": 2,
            "current": 2,
            "currentSize": 1,
            "records": [{
                "storeId": "31",
                "storeName": "非凡-JP",
                "regionName": "日本",
                "currencyIcon": "JP¥",
                "sellerSku": "31-250J-NKH6",
                "asin": "B09SB1R9NB",
                "asinUrl": "https://www.amazon.co.jp/dp/B09SB1R9NB",
                "smallImageUrl": "https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg",
                "itemName": "モース暗号ブレスレット",
                "primeDiscount": {
                    "salesPrice": 0,
                    "discountType": "",
                    "discountValue": 0,
                    "discountValueStr": "",
                    "discountPrice": 0,
                    "salesAmount": 0,
                    "salesVolume": 0,
                    "pageView": 0,
                    "exchangeRate": 0
                }
            }],
            "hasNextPage": false,
            "hasPreviousPage": true
        },
        "orderPage": {
            "total": 1,
            "size": 20,
            "pageCount": 1,
            "current": 1,
            "currentSize": 1,
            "records": [{
                "amazonOrderId": "fasdfasdga13241-R",
                "storeId": "31",
                "storeName": "非凡-JP",
                "regionName": "日本",
                "currencyIcon": "JP¥",
                "orderItems": [{
                    "sellerSku": "09-CJWX-DFQH",
                    "asin": "B09SBF3H99",
                    "asinUrl": "https://www.amazon.co.jp/dp/B09SBF3H99",
                    "smallImageUrl": "https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg",
                    "itemName": "シンプルなハート型ワックス編みカップルブレスレット (Red)",
                    "localName": "KT7XL",
                    "localSku": "SKUKT7XL",
                    "promotionId": "Percentage Off 2025/07/21 2-4-51-873"
                }],
                "purchaseDate": "2022-05-07 00:00:00",
                "orderTotalAmount": 0,
                "orderStatus": "CANCELLED"
            }],
            "hasNextPage": false,
            "hasPreviousPage": false
        }
    }]
}
```