# 查询商品折扣详情-列表-会员折扣

## 接口信息

| API Path                                          | 请求协议 | 请求方式 | [令牌桶容量]() |
| :------------------------------------------------ | :------- | :------- | :------------- |
| `/basicOpen/promotion/listingDetailPrimeDiscount` | HTTPS    | POST     | 1              |

## 请求参数

| 参数名        | 说明                                                         | 必填 | 类型     | 示例          |
| :------------ | :----------------------------------------------------------- | :--- | :------- | :------------ |
| sellerSku     | seller_sku(msku)                                             | 是   | [string] | a_test_sku_x3 |
| promotionType | 促销类型                                                     | 否   | [array]  | []            |
| status        | 促销状态                                                     | 否   | [array]  | []            |
| storeId       | 店铺id                                                       | 是   | [string] | 43            |
| startTime     | 活动开始时间                                                 | 是   | [string] | 2025-01-07    |
| endTime       | 活动结束时间                                                 | 是   | [string] | 2025-03-17    |
| sortField     | 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） | 是   | [string] | startTime     |
| sortType      | 排序类型 asc desc                                            | 是   | [string] | desc          |
| pageNum       | 分页页码                                                     | 是   | [number] | 1             |
| pageSize      | 分页大小                                                     | 是   | [number] | 20            |

## 请求示例

```
{
    "sellerSku": "a_test_sku_x3",
    "promotionType": [],
    "status": [],
    "storeId": "43",
    "startTime": "2025-01-07",
    "endTime": "2025-03-17",
    "sortField": "startTime",
    "sortType": "desc",
    "pageNum": 1,
    "pageSize": 20
}
```

## 返回结果

Json Object

| 参数名                               | 说明                                                       | 必填 | 类型      | 示例                                           |
| :----------------------------------- | :--------------------------------------------------------- | :--- | :-------- | :--------------------------------------------- |
| code                                 | 消息提示                                                   | 是   | [number]  | 0                                              |
| message                              | 消息                                                       | 是   | [string]  | success                                        |
| error_details                        | 错误信息                                                   | 是   | [array]   | []                                             |
| request_id                           | 请求id                                                     | 是   | [string]  | fe02741c80d3418bb2ebebaacd2a4728.1752196754425 |
| response_time                        | 响应时间                                                   | 是   | [string]  | 2025-07-11 09:19:20                            |
| data                                 | 消息提示                                                   | 是   | [object]  |                                                |
| data>>total                          |                                                            | 是   | [number]  | 3                                              |
| data>>size                           |                                                            | 是   | [number]  | 20                                             |
| data>>pageCount                      |                                                            | 是   | [number]  | 1                                              |
| data>>current                        |                                                            | 是   | [number]  | 1                                              |
| data>>currentSize                    |                                                            | 是   | [number]  | 3                                              |
| data>>hasNextPage                    |                                                            | 是   | [boolean] | false                                          |
| data>>hasPreviousPage                |                                                            | 是   | [boolean] | false                                          |
| data>>records                        |                                                            | 是   | [array]   |                                                |
| data>>records>>promotionId           | 活动id，唯一标识                                           | 是   | [string]  | 0be5992b-cad8-4c9a-b104-c3980ecdf691           |
| data>>records>>customerTarget        | 消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣 | 是   | [string]  | PRIME_EXCLUSIVE                                |
| data>>records>>name                  | 折扣名称                                                   | 是   | [string]  | 会员折扣测试-固定折扣                          |
| data>>records>>storeId               | 店铺id                                                     | 是   | [string]  | 43                                             |
| data>>records>>storeName             | 店铺名                                                     | 是   | [string]  | uboss-US                                       |
| data>>records>>regionName            | 国家/地区名                                                | 是   | [string]  | 美国                                           |
| data>>records>>currencyIcon          | 货币icon                                                   | 是   | [string]  | $                                              |
| data>>records>>status                | 状态                                                       | 是   | [number]  | 1                                              |
| data>>records>>statusText            | 状态                                                       | 是   | [string]  | 进行中                                         |
| data>>records>>errorCount            | errorCount>0时 ，代表“需要注意”状态                        | 是   | [string]  | 0                                              |
| data>>records>>originStatus          | 促销活动平台状态                                           | 是   | [string]  | RUNNING                                        |
| data>>records>>originStatusText      | 促销活动平台状态                                           | 是   | [string]  | 生效中                                         |
| data>>records>>productQuantity       | 商品数量                                                   | 是   | [number]  | 0                                              |
| data>>records>>promotionStartTime    | 活动开始时间（productQuantity）                            | 是   | [string]  | 2025-01-07 00:30:32                            |
| data>>records>>promotionStartTimeUtc | 活动开始时间UTC                                            | 是   | [null]    | null                                           |
| data>>records>>promotionEndTime      | 活动结束时间                                               | 是   | [string]  | 2025-03-17 00:30:32                            |
| data>>records>>salesVolume           | 活动总销量                                                 | 是   | [number]  | 2                                              |
| data>>records>>salesAmount           | 活动总销售额                                               | 是   | [number]  | 21                                             |
| data>>records>>salesAmountUsd        | 活动总销售额，换算成美元                                   | 是   | [number]  | 21                                             |
| data>>records>>pageView              | 浏览量                                                     | 是   | [string]  | 200                                            |
| data>>records>>exchangeRate          | 转化率                                                     | 是   | [number]  | 1                                              |
| data>>records>>firstSyncTime         | 首次同步时间                                               | 是   | [string]  | 2025-02-28 16:16:59                            |
| data>>records>>lastSyncTime          | 最后同步时间                                               | 是   | [string]  | 2025-02-28 16:16:59                            |
| data>>records>>remark                | 备注                                                       | 是   | [string]  | 假数据                                         |
| total                                | 总数                                                       | 是   | [number]  | 3                                              |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "fe02741c80d3418bb2ebebaacd2a4728.1752196754425",
    "response_time": "2025-07-11 09:19:20",
    "data": {
        "total": 3,
        "size": 20,
        "pageCount": 1,
        "current": 1,
        "currentSize": 3,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "records": [
            {
                "promotionId": "0be5992b-cad8-4c9a-b104-c3980ecdf691",
                "customerTarget": "PRIME_EXCLUSIVE",
                "name": "会员折扣测试-固定折扣",
                "storeId": "43",
                "storeName": "uboss-US",
                "regionName": "美国",
                "currencyIcon": "$",
                "status": 1,
                "statusText": "进行中",
                "errorCount": "0",
                "originStatus": "RUNNING",
                "originStatusText": "生效中",
                "productQuantity": 0,
                "promotionStartTime": "2025-01-07 00:30:32",
                "promotionStartTimeUtc": null,
                "promotionEndTime": "2025-03-17 00:30:32",
                "salesVolume": 2,
                "salesAmount": 21,
                "salesAmountUsd": 21,
                "pageView": "200",
                "exchangeRate": 1,
                "firstSyncTime": "2025-02-28 16:16:59",
                "lastSyncTime": "2025-02-28 16:16:59",
                "remark": "假数据"
            },
            {
                "promotionId": "0be5992b-cad8-4c9a-b104-c3980ecdf692",
                "customerTarget": "PRIME_EXCLUSIVE",
                "name": "会员折扣测试-百分比折扣",
                "storeId": "43",
                "storeName": "uboss-US",
                "regionName": "美国",
                "currencyIcon": "$",
                "status": 1,
                "statusText": "进行中",
                "errorCount": "0",
                "originStatus": "RUNNING",
                "originStatusText": "生效中",
                "productQuantity": 0,
                "promotionStartTime": "2025-01-07 00:30:32",
                "promotionStartTimeUtc": null,
                "promotionEndTime": "2025-03-17 00:30:32",
                "salesVolume": 1,
                "salesAmount": 28,
                "salesAmountUsd": 28,
                "pageView": "100",
                "exchangeRate": 1,
                "firstSyncTime": "2025-02-28 16:16:59",
                "lastSyncTime": "2025-02-28 16:16:59",
                "remark": "假数据"
            },
            {
                "promotionId": "0be5992b-cad8-4c9a-b104-c3980ecdf693",
                "customerTarget": "ALL CUSTOMERS",
                "name": "价格折扣测试-固定折扣",
                "storeId": "43",
                "storeName": "uboss-US",
                "regionName": "美国",
                "currencyIcon": "$",
                "status": 1,
                "statusText": "进行中",
                "errorCount": "0",
                "originStatus": "RUNNING",
                "originStatusText": "生效中",
                "productQuantity": 0,
                "promotionStartTime": "2025-01-07 00:30:32",
                "promotionStartTimeUtc": null,
                "promotionEndTime": "2025-03-17 00:30:32",
                "salesVolume": 2,
                "salesAmount": 21,
                "salesAmountUsd": 21,
                "pageView": "200",
                "exchangeRate": 1,
                "firstSyncTime": "2025-02-28 16:16:59",
                "lastSyncTime": "2025-02-28 16:16:59",
                "remark": "假数据"
            }
        ]
    },
    "total": 3
}
```