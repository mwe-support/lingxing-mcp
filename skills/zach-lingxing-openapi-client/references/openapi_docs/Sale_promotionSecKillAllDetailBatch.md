# 查询秒杀详情+listing+订单(批量)

## 接口信息

| API Path                                              | 请求协议 | 请求方式 | [令牌桶容量]() |
| :---------------------------------------------------- | :------- | :------- | :------------- |
| `/promotionApi/open/promotion/secKillAllDetailBatch` | HTTPS    | POST     | 1              |

## 请求参数

| 参数名                    | 说明                                    | 必填 | 类型     | 示例                                                         |
| :------------------------ | :-------------------------------------- | :--- | :------- | :----------------------------------------------------------- |
| itemList                  | 批量请求详情itemList个数最小为1最大为20 | 是   | [array]  | [{"promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be","storeId":"31","orderPageNum":1,"orderPageSize":20,"listingPageNum":2,"listingPageSize":1}] |
| itemList>>promotionId     | 活动id                                  | 是   | [string] | 04e2ce6b-c5b6-4244-8100-68b6502d90be                         |
| itemList>>storeId         | 店铺id                                  | 是   | [string] | 31                                                           |
| itemList>>orderPageNum    | 活动订单分页页数，最小为1               | 是   | [number] | 1                                                            |
| itemList>>orderPageSize   | 活动订单分页大小，最小为1,最大为200     | 是   | [number] | 20                                                           |
| itemList>>listingPageNum  | 活动listing分页页数，最小为1            | 是   | [number] | 2                                                            |
| itemList>>listingPageSize | 活动listing分页大小，最小为1,最大为200  | 是   | [number] | 1                                                            |

## 请求示例

```
{
    "itemList": [
        {
            "promotionId": "04e2ce6b-c5b6-4244-8100-68b6502d90be",
            "storeId": "31",
            "orderPageNum": 1,  
            "orderPageSize": 20,
            "listingPageNum": 2,
            "listingPageSize": 1
        }
    ]
}
```

## 返回结果

Json Object

| 参数名                                              | 说明                                                         | 必填 | 类型      | 示例                                                         |
| :-------------------------------------------------- | :----------------------------------------------------------- | :--- | :-------- | :----------------------------------------------------------- |
| code                                                | 0成功                                                        | 是   | [number]  | 1                                                            |
| message                                             |                                                              | 是   | [string]  | 操作成功                                                     |
| error_details                                       |                                                              | 否   | [array]   |                                                              |
| request_id                                          |                                                              | 是   | [string]  |                                                              |
| response_time                                       | yyyy-MM-dd HH:mm:ss                                          | 是   | [string]  |                                                              |
| total                                               |                                                              | 是   | [int]     |                                                              |
| data                                                |                                                              | 是   | [array]   | [{"promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be","storeId":"A23VOKJ3KY8G48","secKill":{"storeId":"A23VOKJ3KY8G48","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be","name":"有数据的秒杀","status":2,"statusText":"已过期","originStatus":"ENDED","originStatusText":"已结束","promotionType":2,"promotionTypeText":"Lightning Deal","promotionStartTime":"2025-06-21 10:15:00","promotionEndTime":"2025-06-21 22:15:00","description":"有数据的秒杀","seckillFee":0,"seckillFeeMin":150,"seckillFeeMax":150,"waived":false,"salesAmount":312.38,"salesAmountUsd":null,"salesVolume":11,"soldRate":0.61,"pageView":"1422","exchangeRate":0.77,"pcos":0.48,"detailListings":null,"pullDetailTaskId":null,"pullDetailStatus":null},"listingPage":{"total":2,"size":1,"pageCount":2,"current":2,"currentSize":1,"records":[{"storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","sellerSku":"31-250J-NKH6","asin":"B09SB1R9NB","asinUrl":"https://www.amazon.co.jp/dp/B09SB1R9NB","smallImageUrl":"https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg","itemName":"モース暗号ブレスレット","coupon":null,"secKIll":{"salesPrice":2660,"discountPrice":0,"discount":2660,"dealQuantity":""},"management":null,"primeDiscount":null}],"hasNextPage":false,"hasPreviousPage":true},"orderPage":{"total":1,"size":20,"pageCount":1,"current":1,"currentSize":1,"records":[{"amazonOrderId":"fasdfasdga13241-R","storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","orderItems":[{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be"}],"purchaseDate":"2022-05-07 00:00:00","orderTotalAmount":0,"orderStatus":"CANCELLED"}],"hasNextPage":false,"hasPreviousPage":false}}] |
| data>>promotionId                                   | 活动id                                                       | 是   | [string]  | 04e2ce6b-c5b6-4244-8100-68b6502d90be                         |
| data>>storeId                                       | 店铺id                                                       | 是   | [string]  | A23VOKJ3KY8G48                                               |
| data>>secKill                                       | 秒杀信息                                                     | 是   | [object]  |                                                              |
| data>>secKill>>storeId                              | 店铺ID                                                       | 是   | [string]  | A23VOKJ3KY8G48                                               |
| data>>secKill>>storeName                            | 店铺名                                                       | 是   | [string]  | 非凡-JP                                                      |
| data>>secKill>>regionName                           | 国家/地区名                                                  | 是   | [string]  | 日本                                                         |
| data>>secKill>>currencyIcon                         | 货币icon                                                     | 是   | [string]  | JP¥                                                          |
| data>>secKill>>promotionId                          | 活动id                                                       | 是   | [string]  | 04e2ce6b-c5b6-4244-8100-68b6502d90be                         |
| data>>secKill>>name                                 | 名称                                                         | 是   | [string]  | 有数据的秒杀                                                 |
| data>>secKill>>status                               | 状态 0其他 1进行中 2已过期 3未开始 4已取消                   | 是   | [number]  | 2                                                            |
| data>>secKill>>statusText                           | 状态说明                                                     | 是   | [string]  | 已过期                                                       |
| data>>secKill>>originStatus                         | 促销活动平台状态                                             | 是   | [string]  | ENDED                                                        |
| data>>secKill>>promotionType                        | 活动类型 0未定义 1Best Deal 2Lightning Deal 3买一赠一 4购买折扣 5一口价 6折扣 7金额 8社媒促销 9金额 | 是   | [number]  | 2                                                            |
| data>>secKill>>promotionTypeText                    | 活动类型说明                                                 | 是   | [string]  | Lightning Deal                                               |
| data>>secKill>>promotionStartTime                   | 活动开始时间                                                 | 是   | [string]  | 2025-06-21 10:15:00                                          |
| data>>secKill>>promotionEndTime                     | 活动结束时间                                                 | 是   | [string]  | 2025-06-21 22:15:00                                          |
| data>>secKill>>description                          | 描述                                                         | 是   | [string]  | 有数据的秒杀                                                 |
| data>>secKill>>seckillFee                           | 秒杀费                                                       | 是   | [number]  | 0                                                            |
| data>>secKill>>seckillFeeMin                        | 秒杀费，最小值                                               | 是   | [number]  | 150                                                          |
| data>>secKill>>seckillFeeMax                        | 秒杀费，最大值                                               | 是   | [number]  | 150                                                          |
| data>>secKill>>waived                               | 是否已豁免                                                   | 是   | [boolean] | false                                                        |
| data>>secKill>>salesAmount                          | 活动总销售额                                                 | 是   | [number]  | 312.38                                                       |
| data>>secKill>>salesVolume                          | 活动总销量                                                   | 是   | [number]  | 11                                                           |
| data>>secKill>>soldRate                             | 售出率                                                       | 是   | [number]  | 0.61                                                         |
| data>>secKill>>pageView                             | 浏览量                                                       | 是   | [string]  | 1422                                                         |
| data>>secKill>>exchangeRate                         | 转化率                                                       | 是   | [number]  | 0.77                                                         |
| data>>secKill>>pcos                                 | pcos(费用除以销售额)                                         | 是   | [number]  | 0.48                                                         |
| data>>listingPage                                   | 秒杀涉及的Listing信息                                        | 是   | [object]  |                                                              |
| data>>listingPage>>total                            |                                                              | 是   | [number]  | 2                                                            |
| data>>listingPage>>size                             |                                                              | 是   | [number]  | 1                                                            |
| data>>listingPage>>pageCount                        |                                                              | 是   | [number]  | 2                                                            |
| data>>listingPage>>current                          |                                                              | 是   | [number]  | 2                                                            |
| data>>listingPage>>currentSize                      |                                                              | 是   | [number]  | 1                                                            |
| data>>listingPage>>records                          | 当前页数据                                                   | 是   | [array]   | [{"storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","sellerSku":"31-250J-NKH6","asin":"B09SB1R9NB","asinUrl":"https://www.amazon.co.jp/dp/B09SB1R9NB","smallImageUrl":"https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg","itemName":"モース暗号ブレスレット","coupon":null,"secKIll":{"salesPrice":2660,"discountPrice":0,"discount":2660,"dealQuantity":""},"management":null,"primeDiscount":null}] |
| data>>listingPage>>records>>storeId                 | 店铺id                                                       | 是   | [string]  | 31                                                           |
| data>>listingPage>>records>>storeName               | 店铺名                                                       | 是   | [string]  | 非凡-JP                                                      |
| data>>listingPage>>records>>regionName              | 国家/地区名                                                  | 是   | [string]  | 日本                                                         |
| data>>listingPage>>records>>currencyIcon            | 货币icon                                                     | 是   | [string]  | JP¥                                                          |
| data>>listingPage>>records>>sellerSku               | seller_sku                                                   | 是   | [string]  | 31-250J-NKH6                                                 |
| data>>listingPage>>records>>asin                    | asin                                                         | 是   | [string]  | B09SB1R9NB                                                   |
| data>>listingPage>>records>>asinUrl                 | asin跳转亚马逊前台链接                                       | 是   | [string]  | https://www.amazon.co.jp/dp/B09SB1R9NB                       |
| data>>listingPage>>records>>smallImageUrl           | 商品缩略图                                                   | 是   | [string]  | https://m.media-amazon.com/images/I/71SLxt+OS8L._SL75_.jpg   |
| data>>listingPage>>records>>itemName                | 商品标题                                                     | 是   | [string]  | モース暗号ブレスレット                                       |
| data>>listingPage>>records>>secKIll                 | 秒杀基本信息                                                 | 是   | [object]  |                                                              |
| data>>listingPage>>records>>secKIll>>salesPrice     | 优惠价                                                       | 是   | [number]  | 2660                                                         |
| data>>listingPage>>records>>secKIll>>discountPrice  | 秒杀价                                                       | 是   | [number]  | 0                                                            |
| data>>listingPage>>records>>secKIll>>discount       | 每件商品折扣                                                 | 是   | [number]  | 2660                                                         |
| data>>listingPage>>records>>secKIll>>dealQuantity   | 秒杀库存数量                                                 | 是   | [string]  |                                                              |
| data>>listingPage>>hasNextPage                      |                                                              | 是   | [boolean] | false                                                        |
| data>>listingPage>>hasPreviousPage                  |                                                              | 是   | [boolean] | true                                                         |
| data>>orderPage                                     | 秒杀涉及的订单信息                                           | 是   | [object]  |                                                              |
| data>>orderPage>>total                              |                                                              | 是   | [number]  | 1                                                            |
| data>>orderPage>>size                               |                                                              | 是   | [number]  | 20                                                           |
| data>>orderPage>>pageCount                          |                                                              | 是   | [number]  | 1                                                            |
| data>>orderPage>>current                            |                                                              | 是   | [number]  | 1                                                            |
| data>>orderPage>>currentSize                        |                                                              | 是   | [number]  | 1                                                            |
| data>>orderPage>>records                            | 当前页数据                                                   | 是   | [array]   | [{"amazonOrderId":"fasdfasdga13241-R","storeId":"31","storeName":"非凡-JP","regionName":"日本","currencyIcon":"JP¥","orderItems":[{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be"}],"purchaseDate":"2022-05-07 00:00:00","orderTotalAmount":0,"orderStatus":"CANCELLED"}] |
| data>>orderPage>>records>>amazonOrderId             | 亚马逊订单号                                                 | 是   | [string]  | fasdfasdga13241-R                                            |
| data>>orderPage>>records>>storeId                   | 店铺id                                                       | 是   | [string]  | 31                                                           |
| data>>orderPage>>records>>storeName                 | 店铺名                                                       | 是   | [string]  | 非凡-JP                                                      |
| data>>orderPage>>records>>regionName                | 国家/地区名                                                  | 是   | [string]  | 日本                                                         |
| data>>orderPage>>records>>currencyIcon              | 货币icon                                                     | 是   | [string]  | JP¥                                                          |
| data>>orderPage>>records>>orderItems                | 订单商品信息                                                 | 是   | [array]   | [{"sellerSku":"09-CJWX-DFQH","asin":"B09SBF3H99","asinUrl":"https://www.amazon.co.jp/dp/B09SBF3H99","smallImageUrl":"https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg","itemName":"シンプルなハート型ワックス編みカップルブレスレット (Red)","localName":"KT7XL","localSku":"SKUKT7XL","promotionId":"04e2ce6b-c5b6-4244-8100-68b6502d90be"}] |
| data>>orderPage>>records>>orderItems>>sellerSku     | seller_sku                                                   | 是   | [string]  | 09-CJWX-DFQH                                                 |
| data>>orderPage>>records>>orderItems>>asin          | asin                                                         | 是   | [string]  | B09SBF3H99                                                   |
| data>>orderPage>>records>>orderItems>>asinUrl       | asin跳转亚马逊前台链接                                       | 是   | [string]  | https://www.amazon.co.jp/dp/B09SBF3H99                       |
| data>>orderPage>>records>>orderItems>>smallImageUrl | 商品缩略图                                                   | 是   | [string]  | https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg   |
| data>>orderPage>>records>>orderItems>>itemName      | 商品标题                                                     | 是   | [string]  | シンプルなハート型ワックス編みカップルブレスレット (Red)     |
| data>>orderPage>>records>>orderItems>>localName     | 品名                                                         | 是   | [string]  | KT7XL                                                        |
| data>>orderPage>>records>>orderItems>>localSku      | localSku                                                     | 是   | [string]  | SKUKT7XL                                                     |
| data>>orderPage>>records>>orderItems>>promotionId   | 促销ID                                                       | 是   | [string]  | 04e2ce6b-c5b6-4244-8100-68b6502d90be                         |
| data>>orderPage>>records>>purchaseDate              | 订购时间                                                     | 是   | [string]  | 2022-05-07 00:00:00                                          |
| data>>orderPage>>records>>orderTotalAmount          | 订单总金额                                                   | 是   | [number]  | 0                                                            |
| data>>orderPage>>records>>orderStatus               | 订单状态                                                     | 是   | [string]  | CANCELLED                                                    |
| data>>orderPage>>hasNextPage                        |                                                              | 是   | [boolean] | false                                                        |
| data>>orderPage>>hasPreviousPage                    |                                                              | 是   | [boolean] | false                                                        |



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
        "promotionId": "04e2ce6b-c5b6-4244-8100-68b6502d90be",
        "storeId": "A23VOKJ3KY8G48",
        "secKill": {
            "storeId": "A23VOKJ3KY8G48",
            "storeName": "非凡-JP",
            "regionName": "日本",
            "currencyIcon": "JP¥",
            "promotionId": "04e2ce6b-c5b6-4244-8100-68b6502d90be",
            "name": "有数据的秒杀",
            "status": 2,
            "statusText": "已过期",
            "originStatus": "ENDED",
            "promotionType": 2,
            "promotionTypeText": "Lightning Deal",
            "promotionStartTime": "2025-06-21 10:15:00",
            "promotionEndTime": "2025-06-21 22:15:00",
            "description": "有数据的秒杀",
            "seckillFee": 0,
            "seckillFeeMin": 150,
            "seckillFeeMax": 150,
            "waived": false,
            "salesAmount": 312.38,
            "salesVolume": 11,
            "soldRate": 0.61,
            "pageView": "1422",
            "exchangeRate": 0.77,
            "pcos": 0.48
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
                "secKIll": {
                    "salesPrice": 2660,
                    "discountPrice": 0,
                    "discount": 2660,
                    "dealQuantity": ""
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
                    "promotionId": "04e2ce6b-c5b6-4244-8100-68b6502d90be"
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