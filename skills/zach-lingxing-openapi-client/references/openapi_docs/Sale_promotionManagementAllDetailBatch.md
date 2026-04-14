# 查询管理促销详情+listing+订单(批量)

## 接口信息

| API Path                                                 | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------------------------------------------------- | :------- | :------- | :----------------------------------------------------------- |
| `/promotionApi/open/promotion/managementAllDetailBatch` | HTTPS    | POST     | 1                                                            |

## 请求参数

| 参数名                    | 说明                                    | 必填 | 类型     | 示例 |
| :------------------------ | :-------------------------------------- | :--- | :------- | :--- |
| itemList                  | 批量请求详情itemList个数最小为1最大为20 | 是   | [array]  |      |
| itemList>>promotionId     | 活动id                                  | 是   | [string] |      |
| itemList>>storeId         | 店铺id                                  | 是   | [string] |      |
| itemList>>orderPageNum    | 活动订单分页页数，最小1                 | 是   | [number] |      |
| itemList>>orderPageSize   | 活动订单分页大小，最小为1，最大为200    | 是   | [number] |      |
| itemList>>listingPageNum  | 活动listing分页页数，最小1              | 是   | [number] |      |
| itemList>>listingPageSize | 活动listing分页大小，最小为1，最大为200 | 是   | [number] |      ||

## 请求示例

```
{
  "itemList": [
    {
      "promotionId": "PROMO123456",
      "storeId": "STORE789",
      "orderPageNum": 1,
      "orderPageSize": 50,
      "listingPageNum": 1,
      "listingPageSize": 100
    },
    {
      "promotionId": "PROMO654321",
      "storeId": "STORE987",
      "orderPageNum": 2,
      "orderPageSize": 100,
      "listingPageNum": 1,
      "listingPageSize": 200
    }
  ]
}
```

## 返回结果

Json Object

| 参数名                                                | 说明                                                         | 必填 | 类型      | 示例                                                         |
| :---------------------------------------------------- | :----------------------------------------------------------- | :--- | :-------- | :----------------------------------------------------------- |
| code                                                  | 0成功                                                        | 是   | [number]  | 0                                                            |
| message                                               |                                                              | 是   | [string]  |                                                              |
| error_details                                         |                                                              | 否   | [array]   |                                                              |
| request_id                                            |                                                              | 是   | [string]  |                                                              |
| response_time                                         | yyyy-MM-dd HH:mm:ss                                          | 是   | [string]  |                                                              |
| total                                                 |                                                              | 是   | [int]     |                                                              |
| data                                                  |                                                              | 是   | [array]   | [{"listingPage":{"current":0,"currentSize":0,"hasNextPage":true,"hasPreviousPage":true,"pageCount":0,"records":[{"asin":"","asinUrl":"","coupon":{"dealQuantity":"","discount":0,"discountPrice":0,"salesPrice":0},"currencyIcon":"","itemName":"","management":{"discountPrice":0,"salesAmount":0,"salesPrice":0,"salesVolume":0},"primeDiscount":{"discountPrice":0,"discountType":"","discountValue":0,"discountValueStr":"","exchangeRate":0,"pageView":0,"salesAmount":0,"salesPrice":0,"salesVolume":0},"regionName":"","secKIll":{"dealQuantity":"","discount":0,"discountPrice":0,"salesPrice":0},"sellerSku":"","smallImageUrl":"","storeId":0,"storeName":""}],"size":0,"total":0},"management":{"buyerGets":"","currencyIcon":"","detailListings":[{"asin":"","discountPrice":0,"itemName":"","salesAmount":0,"salesPrice":0,"salesVolume":0,"sellerSku":"","smallImageUrl":""}],"detailOrders":[{"asin":"","asinUrl":"","itemName":"","localName":"","localSku":"","promotionId":"","sellerSku":"","smallImageUrl":""}],"discountProduct":"","displayOnDetailPage":0,"exchangeLimit":0,"excludeProduct":"","name":"","originStatus":"","originStatusText":"","participateCondition":"","promotionCode":"","promotionEndTime":"","promotionId":"","promotionPageLink":"","promotionStartTime":"","promotionType":0,"promotionTypeText":"","pullDetailStatus":0,"pullDetailTaskId":"","purchaseProduct":"","regionName":"","salesAmount":0,"salesAmountUsd":0,"salesVolume":0,"status":0,"statusText":"","storeId":"","storeName":"","trackingId":""},"orderPage":{"current":0,"currentSize":0,"hasNextPage":true,"hasPreviousPage":true,"pageCount":0,"records":[{"amazonOrderId":"","currencyIcon":"","orderItems":[{"asin":"","asinUrl":"","itemName":"","localName":"","localSku":"","promotionId":"","sellerSku":"","smallImageUrl":""}],"orderStatus":"","orderTotalAmount":0,"purchaseDate":"","regionName":"","storeId":0,"storeName":""}],"size":0,"total":0},"promotionId":"","storeId":""}] |
| data>>promotionId                                     | 活动id                                                       | 是   | [string]  |                                                              |
| data>>storeId                                         | 店铺id                                                       | 是   | [string]  |                                                              |
| data>>management                                      | 管理促销信息                                                 | 是   | [object]  |                                                              |
| data>>management>>storeId                             | 店铺ID                                                       | 是   | [string]  |                                                              |
| data>>management>>storeName                           | 店铺名称                                                     | 是   | [string]  |                                                              |
| data>>management>>regionName                          | 国家/地区名                                                  | 是   | [string]  |                                                              |
| data>>management>>currencyIcon                        | 货币icon                                                     | 是   | [string]  |                                                              |
| data>>management>>promotionId                         | 活动id                                                       | 是   | [string]  |                                                              |
| data>>management>>name                                | 名称                                                         | 是   | [string]  |                                                              |
| data>>management>>status                              | 状态 0其他 1进行中 2已过期 3未开始 4已取消                   | 是   | [number]  | 0                                                            |
| data>>management>>statusText                          | 状态说明                                                     | 是   | [string]  |                                                              |
| data>>management>>originStatus                        | 促销活动平台状态                                             | 是   | [string]  |                                                              |
| data>>management>>promotionType                       | 活动类型 0未定义 1Best Deal 2Lightning Deal 3买一赠一 4购买折扣 5一口价 6折扣 7金额 8社媒促销 9金额 | 是   | [number]  | 0                                                            |
| data>>management>>promotionTypeText                   | 活动类型说明                                                 | 是   | [string]  |                                                              |
| data>>management>>promotionStartTime                  | 活动开始时间                                                 | 是   | [string]  |                                                              |
| data>>management>>promotionEndTime                    | 活动结束时间                                                 | 是   | [string]  |                                                              |
| data>>management>>promotionCode                       | 优惠码                                                       | 是   | [string]  |                                                              |
| data>>management>>exchangeLimit                       | 是否限制兑换，1是0否                                         | 是   | [number]  | 0                                                            |
| data>>management>>participateCondition                | 兑换限制条件                                                 | 是   | [string]  |                                                              |
| data>>management>>buyerGets                           | 买家获得                                                     | 是   | [string]  |                                                              |
| data>>management>>purchaseProduct                     | 需购买商品                                                   | 是   | [string]  |                                                              |
| data>>management>>discountProduct                     | 优惠商品                                                     | 是   | [string]  |                                                              |
| data>>management>>excludeProduct                      | 排除商品                                                     | 是   | [string]  |                                                              |
| data>>management>>trackingId                          | 追踪编码                                                     | 是   | [string]  |                                                              |
| data>>management>>displayOnDetailPage                 | 是否显示在详情页，1是0否                                     | 是   | [number]  |                                                              |
| data>>management>>salesAmount                         | 活动总销售额                                                 | 是   | [number]  | 0                                                            |
| data>>management>>salesVolume                         | 活动总销量                                                   | 是   | [number]  | 0                                                            |
| data>>management>>promotionPageLink                   | 营销页面链接                                                 | 是   | [string]  |                                                              |
| data>>listingPage                                     | 管理促销涉及的Listing信息                                    | 是   | [object]  |                                                              |
| data>>listingPage>>current                            |                                                              | 是   | [number]  | 0                                                            |
| data>>listingPage>>currentSize                        |                                                              | 是   | [number]  | 0                                                            |
| data>>listingPage>>hasNextPage                        |                                                              | 是   | [boolean] | true                                                         |
| data>>listingPage>>hasPreviousPage                    |                                                              | 是   | [boolean] | true                                                         |
| data>>listingPage>>pageCount                          |                                                              | 是   | [number]  | 0                                                            |
| data>>listingPage>>records                            |                                                              | 是   | [array]   | [{"asin":"","asinUrl":"","coupon":{"dealQuantity":"","discount":0,"discountPrice":0,"salesPrice":0},"currencyIcon":"","itemName":"","management":{"discountPrice":0,"salesAmount":0,"salesPrice":0,"salesVolume":0},"primeDiscount":{"discountPrice":0,"discountType":"","discountValue":0,"discountValueStr":"","exchangeRate":0,"pageView":0,"salesAmount":0,"salesPrice":0,"salesVolume":0},"regionName":"","secKIll":{"dealQuantity":"","discount":0,"discountPrice":0,"salesPrice":0},"sellerSku":"","smallImageUrl":"","storeId":0,"storeName":""}] |
| data>>listingPage>>records>>asin                      | asin                                                         | 是   | [string]  |                                                              |
| data>>listingPage>>records>>asinUrl                   | asin跳转亚马逊前台链接                                       | 是   | [string]  |                                                              |
| data>>listingPage>>records>>currencyIcon              | 货币icon                                                     | 是   | [string]  |                                                              |
| data>>listingPage>>records>>itemName                  | 商品标题                                                     | 是   | [string]  |                                                              |
| data>>listingPage>>records>>management                | 管理促销基本信息                                             | 是   | [object]  |                                                              |
| data>>listingPage>>records>>management>>discountPrice | 折后价                                                       | 是   | [number]  | 0                                                            |
| data>>listingPage>>records>>management>>salesAmount   | 销售额                                                       | 是   | [number]  | 0                                                            |
| data>>listingPage>>records>>management>>salesPrice    | 优惠价                                                       | 是   | [number]  | 0                                                            |
| data>>listingPage>>records>>management>>salesVolume   | 销量                                                         | 是   | [number]  | 0                                                            |
| data>>listingPage>>records>>regionName                | 国家/地区名                                                  | 是   | [string]  |                                                              |
| data>>listingPage>>records>>sellerSku                 | seller_sku                                                   | 是   | [string]  |                                                              |
| data>>listingPage>>records>>smallImageUrl             | 商品缩略图                                                   | 是   | [string]  |                                                              |
| data>>listingPage>>records>>storeId                   | 店铺id                                                       | 是   | [number]  | 0                                                            |
| data>>listingPage>>records>>storeName                 | 店铺名                                                       | 是   | [string]  |                                                              |
| data>>listingPage>>size                               |                                                              | 是   | [number]  | 0                                                            |
| data>>listingPage>>total                              |                                                              | 是   | [number]  | 0                                                            |
| data>>orderPage                                       | 管理促销涉及的订单信息                                       | 是   | [object]  |                                                              |
| data>>orderPage>>current                              |                                                              | 是   | [number]  | 0                                                            |
| data>>orderPage>>currentSize                          |                                                              | 是   | [number]  | 0                                                            |
| data>>orderPage>>hasNextPage                          |                                                              | 是   | [boolean] | true                                                         |
| data>>orderPage>>hasPreviousPage                      |                                                              | 是   | [boolean] | true                                                         |
| data>>orderPage>>pageCount                            |                                                              | 是   | [number]  | 0                                                            |
| data>>orderPage>>records                              |                                                              | 是   | [array]   | [{"amazonOrderId":"","currencyIcon":"","orderItems":[{"asin":"","asinUrl":"","itemName":"","localName":"","localSku":"","promotionId":"","sellerSku":"","smallImageUrl":""}],"orderStatus":"","orderTotalAmount":0,"purchaseDate":"","regionName":"","storeId":0,"storeName":""}] |
| data>>orderPage>>records>>amazonOrderId               | 亚马逊订单号                                                 | 是   | [string]  |                                                              |
| data>>orderPage>>records>>currencyIcon                | 货币icon                                                     | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems                  | 订单商品信息                                                 | 是   | [array]   | [{"asin":"","asinUrl":"","itemName":"","localName":"","localSku":"","promotionId":"","sellerSku":"","smallImageUrl":""}] |
| data>>orderPage>>records>>orderItems>>asin            | asin                                                         | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>asinUrl         | asin跳转亚马逊前台链接                                       | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>itemName        | 商品标题                                                     | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>localName       | 品名                                                         | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>localSku        | localSku                                                     | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>promotionId     | 促销ID                                                       | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>sellerSku       | seller_sku                                                   | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderItems>>smallImageUrl   | 商品缩略图                                                   | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderStatus                 | 订单状态                                                     | 是   | [string]  |                                                              |
| data>>orderPage>>records>>orderTotalAmount            | 订单总金额                                                   | 是   | [number]  | 0                                                            |
| data>>orderPage>>records>>purchaseDate                | 订购时间                                                     | 是   | [string]  |                                                              |
| data>>orderPage>>records>>regionName                  | 国家/地区名                                                  | 是   | [string]  |                                                              |
| data>>orderPage>>records>>storeId                     | 店铺id                                                       | 是   | [number]  | 0                                                            |
| data>>orderPage>>records>>storeName                   | 店铺名                                                       | 是   | [string]  |                                                              |
| data>>orderPage>>size                                 |                                                              | 是   | [number]  | 0                                                            |
| data>>orderPage>>total                                |                                                              | 是   | [number]  | 0                                                            |

## 返回成功示例

```
{
  "code": 0,
  "message": "success",
  "error_details": [],
  "request_id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
  "response_time": "2023-05-15 14:30:45",
  "total": 1,
  "data": [
    {
      "promotionId": "PROMO123456",
      "storeId": "STORE789",
      "management": {
        "storeId": "STORE789",
        "storeName": "BestSeller Store",
        "regionName": "United States",
        "currencyIcon": "$",
        "promotionId": "PROMO123456",
        "name": "Summer Sale 2023",
        "status": 1,
        "statusText": "进行中",
        "originStatus": "ACTIVE",
        "promotionType": 4,
        "promotionTypeText": "购买折扣",
        "promotionStartTime": "2023-05-01 00:00:00",
        "promotionEndTime": "2023-05-31 23:59:59",
        "promotionCode": "SUMMER20",
        "exchangeLimit": 1,
        "participateCondition": "Buy 2 items",
        "buyerGets": "20% off",
        "purchaseProduct": "All eligible items",
        "discountProduct": "Selected items",
        "excludeProduct": "Clearance items",
        "trackingId": "TRACK789",
        "displayOnDetailPage": 1,
        "salesAmount": 1250.50,
        "salesVolume": 45,
        "promotionPageLink": "https://www.amazon.com/promos/PROMO123456"
      },
      "listingPage": {
        "current": 1,
        "currentSize": 2,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "pageCount": 1,
        "records": [
          {
            "asin": "B08N5KWB9H",
            "asinUrl": "https://www.amazon.com/dp/B08N5KWB9H",
            "currencyIcon": "$",
            "itemName": "Wireless Bluetooth Headphones",
            "management": {
              "discountPrice": 59.99,
              "salesAmount": 1199.80,
              "salesPrice": 59.99,
              "salesVolume": 20
            },
            "regionName": "United States",
            "sellerSku": "WH-2023-BLUE",
            "smallImageUrl": "https://m.media-amazon.com/images/I/71+6m.jpg",
            "storeId": 789,
            "storeName": "BestSeller Store"
          },
          {
            "asin": "B07PGL2ZKV",
            "asinUrl": "https://www.amazon.com/dp/B07PGL2ZKV",
            "currencyIcon": "$",
            "itemName": "Portable Charger 10000mAh",
            "management": {
              "discountPrice": 25.99,
              "salesAmount": 50.70,
              "salesPrice": 25.99,
              "salesVolume": 2
            },
            "regionName": "United States",
            "sellerSku": "PC-2023-BLK",
            "smallImageUrl": "https://m.media-amazon.com/images/I/61+9m.jpg",
            "storeId": 789,
            "storeName": "BestSeller Store"
          }
        ],
        "size": 10,
        "total": 2
      },
      "orderPage": {
        "current": 1,
        "currentSize": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "pageCount": 1,
        "records": [
          {
            "amazonOrderId": "112-1234567-8901234",
            "currencyIcon": "$",
            "orderItems": [
              {
                "asin": "B08N5KWB9H",
                "asinUrl": "https://www.amazon.com/dp/B08N5KWB9H",
                "itemName": "Wireless Bluetooth Headphones",
                "localName": "蓝牙无线耳机",
                "localSku": "LOCAL-BT-001",
                "promotionId": "PROMO123456",
                "sellerSku": "WH-2023-BLUE",
                "smallImageUrl": "https://m.media-amazon.com/images/I/71+6m.jpg"
              }
            ],
            "orderStatus": "Shipped",
            "orderTotalAmount": 119.98,
            "purchaseDate": "2023-05-10 15:30:22",
            "regionName": "United States",
            "storeId": 789,
            "storeName": "BestSeller Store"
          }
        ],
        "size": 10,
        "total": 1
      }
    }
  ]
}
```

