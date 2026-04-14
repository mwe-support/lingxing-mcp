# 查询商品折扣详情-列表-优惠卷

## 接口信息

| API Path                                   | 请求协议 | 请求方式 | [令牌桶容量]() |
| :----------------------------------------- | :------- | :------- | :------------- |
| `/basicOpen/promotion/listingDetailCoupon` | HTTPS    | POST     | 1              |

## 请求参数

| 参数名        | 说明                                                         | 必填 | 类型     | 示例         |
| :------------ | :----------------------------------------------------------- | :--- | :------- | :----------- |
| sellerSku     | seller_sku(msku)                                             | 是   | [string] | 7T-2COF-AV9I |
| promotionType | 促销类型                                                     | 否   | [array]  | []           |
| status        | 促销状态： 0 其他 1 进行中 2 已过期 3 未开始                 | 否   | [array]  | []           |
| storeId       | 店铺id                                                       | 是   | [string] | 43           |
| startTime     | 活动开始时间                                                 | 是   | [string] | 2024-09-10   |
| endTime       | 活动结束时间                                                 | 是   | [string] | 2024-09-12   |
| sortField     | 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） | 是   | [string] | startTime    |
| sortType      | 排序类型 asc desc                                            | 是   | [string] | desc         |
| pageNum       | 分页页码                                                     | 是   | [number] | 1            |
| pageSize      | 分页大小                                                     | 是   | [number] | 20           |

## 请求示例

```
{
   
    "sellerSku": "7T-2COF-AV9I",
    "promotionType": [],
    "status": [],
    "storeId": "43",
    "startTime": "2024-09-10",
    "endTime": "2024-09-12",
    "sortField": "startTime",
    "sortType": "desc",
    "pageNum": 1,
    "pageSize": 20
}
```

## 返回结果

Json Object

| 参数名                               | 说明                                                         | 必填 | 类型      | 示例                                           |
| :----------------------------------- | :----------------------------------------------------------- | :--- | :-------- | :--------------------------------------------- |
| code                                 | 状态码，0 成功                                               | 是   | [number]  | 0                                              |
| message                              | 消息提示                                                     | 是   | [string]  | success                                        |
| error_details                        | 错误信息                                                     | 是   | [array]   | []                                             |
| request_id                           | 请求链路id                                                   | 是   | [string]  | 9ed6f7bca84d4768a1c374ef8865e263.1752196903523 |
| response_time                        | 响应时间                                                     | 是   | [string]  | 2025-07-11 09:21:44                            |
| data                                 |                                                              | 是   | [object]  |                                                |
| data>>total                          | 总数                                                         | 是   | [number]  | 1                                              |
| data>>size                           |                                                              | 是   | [number]  | 20                                             |
| data>>pageCount                      |                                                              | 是   | [number]  | 1                                              |
| data>>current                        |                                                              | 是   | [number]  | 1                                              |
| data>>currentSize                    |                                                              | 是   | [number]  | 1                                              |
| data>>hasPreviousPage                |                                                              | 是   | [boolean] | false                                          |
| data>>hasNextPage                    |                                                              | 是   | [boolean] | false                                          |
| data>>records                        |                                                              | 是   | [array]   |                                                |
| data>>records>>promotionId           | 优惠券id                                                     | 是   | [string]  | aec82146-b1c3-46ed-b044-05d4b0e8baf5           |
| data>>records>>name                  | 优惠券名称                                                   | 是   | [string]  | Save 5% on asdfasdfa                           |
| data>>records>>storeId               | 店铺id                                                       | 是   | [string]  | 43                                             |
| data>>records>>storeName             | 店铺名                                                       | 是   | [string]  | uboss-US                                       |
| data>>records>>regionName            | 国家/地区                                                    | 是   | [string]  | 美国                                           |
| data>>records>>currencyIcon          | 货币icon                                                     | 是   | [string]  | $                                              |
| data>>records>>status                | 商品状态：1 active，2 draft，3 archived，4 deleted           | 是   | [number]  | 2                                              |
| data>>records>>needsAttention        | 状态                                                         | 是   | [boolean] | false                                          |
| data>>records>>statusText            | 状态                                                         | 是   | [string]  | 已过期                                         |
| data>>records>>originStatus          | 活动状态： ACTIVE 进行中 CANCELED 已取消 EXPIRED 已过期 RUNNING 生效中 NEEDS ACTION 需要注意 EXPIRING SOON 即将过期 SUBMITTED 已提交 FAILED 失败 | 是   | [string]  | EXPIRED                                        |
| data>>records>>originStatusText      | 活动状态                                                     | 是   | [string]  | 已过期                                         |
| data>>records>>discount              | 折扣                                                         | 是   | [string]  | 5.00%                                          |
| data>>records>>budget                | 预算                                                         | 是   | [string]  | $100                                           |
| data>>records>>cost                  | 支出                                                         | 是   | [number]  | 0                                              |
| data>>records>>drawQuantity          | 领取数                                                       | 是   | [number]  | 0                                              |
| data>>records>>exchangeQuantity      | 兑换数                                                       | 是   | [number]  | 0                                              |
| data>>records>>exchangeRate          | 兑换率                                                       | 是   | [number]  | 0                                              |
| data>>records>>salesAmount           | 活动总销售额                                                 | 是   | [number]  | 0                                              |
| data>>records>>salesAmountUsd        | 活动总销售额，换算成美元                                     | 是   | [number]  | 0                                              |
| data>>records>>salesVolume           | 活动总销量                                                   | 是   | [number]  | 0                                              |
| data>>records>>promotionStartTime    | 活动开始时间                                                 | 是   | [string]  | 2024-09-10 00:00:00                            |
| data>>records>>promotionStartTimeUtc | 活动开始时间UTC时间                                          | 是   | [null]    | null                                           |
| data>>records>>promotionEndTime      | 活动结束时间                                                 | 是   | [string]  | 2024-09-12 00:00:00                            |
| data>>records>>firstSyncTime         | 首次同步时间                                                 | 是   | [string]  | 2024-11-07 10:36:28                            |
| data>>records>>lastSyncTime          | 最后同步时间                                                 | 是   | [string]  | 2024-11-07 17:25:19                            |
| data>>records>>remark                | 备注                                                         | 是   | [string]  |                                                |
| total                                | 总数                                                         | 是   | [number]  | 1                                              |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "9ed6f7bca84d4768a1c374ef8865e263.1752196903523",
    "response_time": "2025-07-11 09:21:44",
    "data": {
        "total": 1,
        "size": 20,
        "pageCount": 1,
        "current": 1,
        "currentSize": 1,
        "hasPreviousPage": false,
        "hasNextPage": false,
        "records": [{
            "promotionId": "aec82146-b1c3-46ed-b044-05d4b0e8baf5",
            "name": "Save 5% on asdfasdfa",
            "storeId": "43",
            "storeName": "uboss-US",
            "regionName": "美国",
            "currencyIcon": "$",
            "status": 2,
            "needsAttention": false,
            "statusText": "已过期",
            "originStatus": "EXPIRED",
            "originStatusText": "已过期",
            "discount": "5.00%",
            "budget": "$100",
            "cost": 0,
            "drawQuantity": 0,
            "exchangeQuantity": 0,
            "exchangeRate": 0,
            "salesAmount": 0,
            "salesAmountUsd": 0,
            "salesVolume": 0,
            "promotionStartTime": "2024-09-10 00:00:00",
            "promotionStartTimeUtc": null,
            "promotionEndTime": "2024-09-12 00:00:00",
            "firstSyncTime": "2024-11-07 10:36:28",
            "lastSyncTime": "2024-11-07 17:25:19",
            "remark": ""
        }]
    },
    "total": 1
}
```