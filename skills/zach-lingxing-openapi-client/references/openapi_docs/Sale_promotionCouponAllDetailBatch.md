# 查询优惠券详情+listing+订单(批量)

## 接口信息

| API Path                                             | 请求协议 | 请求方式 | [令牌桶容量]() |
| :--------------------------------------------------- | :------- | :------- | :------------- |
| `/promotionApi/open/promotion/couponAllDetailBatch` | HTTPS    | POST     | 1              |

## 请求参数

| 参数名                    | 说明                                    | 必填 | 类型     | 示例                                                         |
| :------------------------ | :-------------------------------------- | :--- | :------- | :----------------------------------------------------------- |
| itemList                  | 批量请求详情itemList个数最小为1最大为20 | 是   | [array]  | [{"promotionId":"bbdcdae5-57a1-4777-9ad6-3d901ea6fa74","storeId":"31","orderPageNum":1,"orderPageSize":20,"listingPageNum":2,"listingPageSize":1}] |
| itemList>>promotionId     | 活动id，唯一标识                        | 是   | [string] | bbdcdae5-57a1-4777-9ad6-3d901ea6fa74                         |
| itemList>>storeId         | 店铺id                                  | 是   | [string] | 31                                                           |
| itemList>>orderPageNum    | 活动订单分页页数,最小为1                | 是   | [number] | 1                                                            |
| itemList>>orderPageSize   | 活动订单分页大小,最小为1,最大为200      | 是   | [number] | 20                                                           |
| itemList>>listingPageNum  | 活动listing分页页数,最小为1             | 是   | [number] | 1                                                            |
| itemList>>listingPageSize | 活动listing分页大小,最小为1,最大为200   | 是   | [number] | 20                                                           |

## 请求示例

```
{
    "itemList": [
        {
            "promotionId": "2577860007635320832",
            "storeId": "32",
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

| 参数名                                              | 说明                                       | 必填 | 类型      | 示例                                                       |
| :-------------------------------------------------- | :----------------------------------------- | :--- | :-------- | :--------------------------------------------------------- |
| code                                                | 0成功                                      | 是   | [number]  | 1                                                          |
| message                                             |                                            | 是   | [string]  | 操作成功                                                   |
| error_details                                       |                                            | 否   | [array]   |                                                            |
| request_id                                          |                                            | 是   | [string]  |                                                            |
| response_time                                       | yyyy-MM-dd HH:mm:ss                        | 是   | [string]  |                                                            |
| total                                               |                                            | 是   | [int]     |                                                            |
| data                                                |                                            | 是   | [array]   |                                                            |
| data>>promotionId                                   | 活动id                                     | 是   | [string]  | bbdcdae5-57a1-4777-9ad6-3d901ea6fa74                       |
| data>>storeId                                       | 店铺id                                     | 是   | [string]  | A23VOKJ3KY8G48                                             |
| data>>coupon                                        | 优惠券信息                                 | 是   | [object]  |                                                            |
| data>>coupon>>promotionId                           | 活动id，唯一标识                           | 是   | [string]  | bbdcdae5-57a1-4777-9ad6-3d901ea6fa74                       |
| data>>coupon>>name                                  | 名称                                       | 是   | [string]  | 5%の割引 cj001                                             |
| data>>coupon>>storeId                               | 店铺ID                                     | 是   | [string]  | A23VOKJ3KY8G48                                             |
| data>>coupon>>storeName                             | 店铺名                                     | 是   | [string]  | 非凡-JP                                                    |
| data>>coupon>>regionName                            | 国家/地区名                                | 是   | [string]  | 日本                                                       |
| data>>coupon>>currencyIcon                          | 货币icon                                   | 是   | [string]  | JP¥                                                        |
| data>>coupon>>budget                                | 预算                                       | 是   | [string]  | JP¥10000.0                                                 |
| data>>coupon>>cost                                  | 支出                                       | 是   | [number]  | 0                                                          |
| data>>coupon>>discount                              | 折扣                                       | 是   | [number]  | 5                                                          |
| data>>coupon>>drawQuantity                          | 领取数                                     | 是   | [number]  | 0                                                          |
| data>>coupon>>exchangeQuantity                      | 兑换数                                     | 是   | [number]  | 0                                                          |
| data>>coupon>>exchangeRate                          | 兑换率                                     | 是   | [number]  | 0                                                          |
| data>>coupon>>status                                | 状态 0其他 1进行中 2已过期 3未开始 4已取消 | 是   | [number]  | 2                                                          |
| data>>coupon>>statusText                            | 状态说明                                   | 是   | [string]  | 已过期                                                     |
| data>>coupon>>originStatus                          | 促销活动平台状态                           | 是   | [string]  |                                                            |
| data>>coupon>>promotionType                         | 促销类型                                   | 是   | [number]  | 6                                                          |
| data>>coupon>>salesAmount                           | 活动总销售额                               | 是   | [number]  | 0                                                          |
| data>>coupon>>salesVolume                           | 活动总销量                                 | 是   | [number]  | 0                                                          |
| data>>coupon>>promotionStartTime                    | 活动开始时间                               | 是   | [string]  | 2024-07-18 00:00:00                                        |
| data>>coupon>>promotionEndTime                      | 活动结束时间                               | 是   | [string]  | 2024-09-18 00:00:00                                        |
| data>>listingPage                                   | 优惠券涉及的Listing信息                    | 是   | [object]  |                                                            |
| data>>listingPage>>total                            | 总数                                       | 是   | [number]  | 2                                                          |
| data>>listingPage>>size                             | 每页大小                                   | 是   | [number]  | 1                                                          |
| data>>listingPage>>pageCount                        | 总页数                                     | 是   | [number]  | 2                                                          |
| data>>listingPage>>current                          | 当前页数                                   | 是   | [number]  | 2                                                          |
| data>>listingPage>>currentSize                      | 当前页条数                                 | 是   | [number]  | 1                                                          |
| data>>listingPage>>records                          | 当前页数据                                 | 是   | [array]   |                                                            |
| data>>listingPage>>records>>storeId                 | 店铺id                                     | 是   | [string]  | 31                                                         |
| data>>listingPage>>records>>storeName               | 店铺名                                     | 是   | [string]  | 非凡-JP                                                    |
| data>>listingPage>>records>>regionName              | 国家/地区名                                | 是   | [string]  | 日本                                                       |
| data>>listingPage>>records>>currencyIcon            | 货币icon                                   | 是   | [string]  | JP¥                                                        |
| data>>listingPage>>records>>sellerSku               | seller_sku                                 | 是   | [string]  | 09-CJWX-DFQH                                               |
| data>>listingPage>>records>>asin                    | asin                                       | 是   | [string]  | B09SBF3H99                                                 |
| data>>listingPage>>records>>asinUrl                 | asin跳转亚马逊前台链接                     | 是   | [string]  | https://www.amazon.co.jp/dp/B09SBF3H99                     |
| data>>listingPage>>records>>smallImageUrl           | 商品缩略图                                 | 是   | [string]  | https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg |
| data>>listingPage>>records>>itemName                | 商品标题                                   | 是   | [string]  | シンプルなハート型ワックス編みカップルブレスレット (Red)   |
| data>>listingPage>>records>>coupon                  | 优惠券主要信息                             | 是   | [object]  |                                                            |
| data>>listingPage>>records>>coupon>>salesPrice      | 优惠价                                     | 是   | [number]  | 2889                                                       |
| data>>listingPage>>records>>coupon>>discountPrice   | 折后价                                     | 是   | [number]  | 0                                                          |
| data>>listingPage>>records>>coupon>>salesVolume     | 销量                                       | 是   | [number]  | 0                                                          |
| data>>listingPage>>records>>coupon>>salesAmount     | 销售额                                     | 是   | [number]  | 0                                                          |
| data>>listingPage>>hasNextPage                      | 是否有下一页                               | 是   | [boolean] | false                                                      |
| data>>listingPage>>hasPreviousPage                  | 是否有上一页                               | 是   | [boolean] | true                                                       |
| data>>orderPage                                     | 优惠券涉及的订单信息                       | 是   | [object]  |                                                            |
| data>>orderPage>>total                              | 总数                                       | 是   | [number]  | 1                                                          |
| data>>orderPage>>size                               | 每页大小                                   | 是   | [number]  | 20                                                         |
| data>>orderPage>>pageCount                          | 总页数                                     | 是   | [number]  | 1                                                          |
| data>>orderPage>>current                            | 当前页数                                   | 是   | [number]  | 1                                                          |
| data>>orderPage>>currentSize                        | 当前页条数                                 | 是   | [number]  | 1                                                          |
| data>>orderPage>>records                            | 当前页数据                                 | 是   | [array]   |                                                            |
| data>>orderPage>>records>>amazonOrderId             | 亚马逊订单号                               | 是   | [string]  | nnxn-397437                                                |
| data>>orderPage>>records>>storeId                   | 店铺id                                     | 是   | [string]  | 31                                                         |
| data>>orderPage>>records>>storeName                 | 店铺名                                     | 是   | [string]  | 非凡-JP                                                    |
| data>>orderPage>>records>>regionName                | 国家/地区名                                | 是   | [string]  | 日本                                                       |
| data>>orderPage>>records>>currencyIcon              | 货币icon                                   | 是   | [string]  | JP¥                                                        |
| data>>orderPage>>records>>orderItems                | 订单商品信息                               | 是   | [array]   |                                                            |
| data>>orderPage>>records>>orderItems>>sellerSku     | seller_sku                                 | 是   | [string]  | 09-CJWX-DFQH                                               |
| data>>orderPage>>records>>orderItems>>asin          | asin                                       | 是   | [string]  | B09SBF3H99                                                 |
| data>>orderPage>>records>>orderItems>>asinUrl       | asin跳转亚马逊前台链接                     | 是   | [string]  | https://www.amazon.co.jp/dp/B09SBF3H99                     |
| data>>orderPage>>records>>orderItems>>smallImageUrl | 商品缩略图                                 | 是   | [string]  | https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg |
| data>>orderPage>>records>>orderItems>>itemName      | 商品标题                                   | 是   | [string]  | シンプルなハート型ワックス編みカップルブレスレット (Red)   |
| data>>orderPage>>records>>orderItems>>localName     | 品名                                       | 是   | [string]  | KT7XL                                                      |
| data>>orderPage>>records>>orderItems>>localSku      | localSku                                   | 是   | [string]  | SKUKT7XL                                                   |
| data>>orderPage>>records>>orderItems>>promotionId   | 促销ID                                     | 是   | [string]  | bbdcdae5-57a1-4777-9ad6-3d901ea6fa74                       |
| data>>orderPage>>records>>purchaseDate              | 订购时间                                   | 是   | [string]  | 2022-06-30 00:00:00                                        |
| data>>orderPage>>records>>orderTotalAmount          | 订单总金额                                 | 是   | [number]  | 0                                                          |
| data>>orderPage>>records>>orderStatus               | 订单状态                                   | 是   | [string]  | CANCELLED                                                  |
| data>>orderPage>>hasNextPage                        | 是否有下一页                               | 是   | [boolean] | false                                                      |
| data>>orderPage>>hasPreviousPage                    | 是否有上一页                               | 是   | [boolean] | false                                                      |

## 返回成功示例

```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "",
    "response_time": "",
    "total": 0,
    "data": [{
        "promotionId": "bbdcdae5-57a1-4777-9ad6-3d901ea6fa74",
        "storeId": "A23VOKJ3KY8G48",
        "coupon": {
            "promotionId": "bbdcdae5-57a1-4777-9ad6-3d901ea6fa74",
            "name": "5%の割引 cj001",
            "storeId": "A23VOKJ3KY8G48",
            "storeName": "非凡-JP",
            "regionName": "日本",
            "currencyIcon": "JP¥",
            "budget": "JP¥10000.0",
            "cost": 0,
            "discount": 5,
            "drawQuantity": 0,
            "exchangeQuantity": 0,
            "exchangeRate": 0,
            "status": 2,
            "statusText": "已过期",
            "originStatus": "",
            "promotionType": 6,
            "salesAmount": 0,
            "salesVolume": 0,
            "promotionStartTime": "2024-07-18 00:00:00",
            "promotionEndTime": "2024-09-18 00:00:00"
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
                "sellerSku": "09-CJWX-DFQH",
                "asin": "B09SBF3H99",
                "asinUrl": "https://www.amazon.co.jp/dp/B09SBF3H99",
                "smallImageUrl": "https://m.media-amazon.com/images/I/51f8M9Z0O5L._SL75_.jpg",
                "itemName": "シンプルなハート型ワックス編みカップルブレスレット (Red)",
                "coupon": {
                    "salesPrice": 2889,
                    "discountPrice": 0,
                    "salesVolume": 0,
                    "salesAmount": 0
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
                "amazonOrderId": "nnxn-397437",
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
                    "promotionId": "bbdcdae5-57a1-4777-9ad6-3d901ea6fa74"
                }],
                "purchaseDate": "2022-06-30 00:00:00",
                "orderTotalAmount": 0,
                "orderStatus": "CANCELLED"
            }],
            "hasNextPage": false,
            "hasPreviousPage": false
        }
    }]
}
```