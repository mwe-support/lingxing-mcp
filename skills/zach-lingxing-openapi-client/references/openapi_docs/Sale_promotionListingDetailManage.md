# 查询商品折扣详情-列表-管理促销

## 接口信息

| API Path                                   | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :----------------------------------------- | :------- | :------- | :----------------------------------------------------------- |
| `/basicOpen/promotion/listingDetailManage` | HTTPS    | POST     | 1                                                            |

## 请求参数

| 参数名        | 说明                                                         | 必填 | 类型     | 示例         |
| :------------ | :----------------------------------------------------------- | :--- | :------- | :----------- |
| sellerSku     | seller_sku(msku)                                             | 是   | [string] | 31-250J-NKH6 |
| promotionType | 促销类型                                                     | 否   | [array]  | []           |
| status        | 促销状态                                                     | 否   | [array]  | []           |
| storeId       | 店铺id                                                       | 是   | [string] | 132          |
| startTime     | 活动开始时间                                                 | 是   | [string] | 2023-01-01   |
| endTime       | 活动结束时间                                                 | 是   | [string] | 2023-01-31   |
| sortField     | 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） | 是   | [string] | startTime    |
| sortType      | 排序类型 asc desc                                            | 是   | [string] | desc         |
| pageNum       | 分页页码                                                     | 是   | [number] | 1            |
| pageSize      | 分页大小                                                     | 是   | [number] | 20           |

## 请求示例

```
{

    "sellerSku": "31-250J-NKH6",
    "promotionType": [],
    "status": [],
    "storeId": "132",
    "startTime": "2023-01-01",
    "endTime": "2023-01-31",
    "sortField": "startTime",
    "sortType": "desc",
    "pageNum": 1,
    "pageSize": 20
}
```

## 返回结果

Json Object

| 参数名                                 | 说明                         | 必填 | 类型      | 示例                                           |
| :------------------------------------- | :--------------------------- | :--- | :-------- | :--------------------------------------------- |
| code                                   | 消息提示                     | 是   | [number]  | 0                                              |
| message                                | 消息                         | 是   | [string]  | success                                        |
| error_details                          | 错误信息                     | 是   | [array]   | []                                             |
| request_id                             | 请求id                       | 是   | [string]  | c6ed840963a24d3e9805ca03b269f51b.1752205194893 |
| response_time                          | 响应时间                     | 是   | [string]  | 2025-07-11 11:40:01                            |
| data                                   |                              | 是   | [object]  |                                                |
| data>>total                            |                              | 是   | [number]  | 1                                              |
| data>>size                             |                              | 是   | [number]  | 20                                             |
| data>>pageCount                        |                              | 是   | [number]  | 1                                              |
| data>>current                          |                              | 是   | [number]  | 1                                              |
| data>>currentSize                      |                              | 是   | [number]  | 1                                              |
| data>>hasNextPage                      |                              | 是   | [boolean] | false                                          |
| data>>hasPreviousPage                  |                              | 是   | [boolean] | false                                          |
| data>>records                          |                              | 是   | [array]   |                                                |
| data>>records>>promotionId             | 活动id，唯一标识             | 是   | [string]  | VPC-6-14498719 Coupon                          |
| data>>records>>name                    | 名称-内部描述                | 是   | [string]  |                                                |
| data>>records>>trackingId              | 追踪编码                     | 是   | [string]  | VPC-6-14498719 Coupon                          |
| data>>records>>storeId                 | 店铺id                       | 是   | [string]  | 132                                            |
| data>>records>>storeName               | 店铺名                       | 是   | [string]  | feifan-JP1                                     |
| data>>records>>regionName              | 国家/地区名                  | 是   | [string]  | 日本                                           |
| data>>records>>currencyIcon            | 货币icon                     | 是   | [string]  | JP¥                                            |
| data>>records>>status                  | 状态                         | 是   | [number]  | 2                                              |
| data>>records>>statusText              | 状态                         | 是   | [string]  | 已过期                                         |
| data>>records>>originStatus            | 促销活动平台状态             | 是   | [string]  | EXPIRED                                        |
| data>>records>>originStatusText        | 促销活动平台状态             | 是   | [string]  | 已过期                                         |
| data>>records>>promotionType           | 促销类型                     | 是   | [number]  | 0                                              |
| data>>records>>promotionTypeText       | 促销类型                     | 是   | [string]  | 未定义类型                                     |
| data>>records>>promotionCode           | 优惠码                       | 是   | [string]  |                                                |
| data>>records>>promotionCodeType       | 优惠码类型，1优先型，2无限型 | 是   | [null]    | null                                           |
| data>>records>>salesAmount             | 活动总销售额                 | 是   | [number]  | 0                                              |
| data>>records>>salesAmountUsd          | 活动总销售额，换算成美元     | 是   | [number]  | 0                                              |
| data>>records>>salesVolume             | 活动总销量                   | 是   | [number]  | 0                                              |
| data>>records>>participateCondition    | 参与条件                     | 是   | [string]  |                                                |
| data>>records>>participateConditionNum | 参与条件数值                 | 是   | [number]  | 0                                              |
| data>>records>>buyerGets               | 买家获得                     | 是   | [string]  |                                                |
| data>>records>>buyerGetsNum            | 买家获得值                   | 是   | [number]  | 0                                              |
| data>>records>>purchaseProduct         | 需购买商品                   | 是   | [string]  |                                                |
| data>>records>>discountProduct         | 优惠商品                     | 是   | [string]  |                                                |
| data>>records>>excludeProduct          | 排除商品                     | 是   | [string]  |                                                |
| data>>records>>exchangeLimit           | 是否限制兑换，1是0否         | 是   | [number]  | 0                                              |
| data>>records>>promotionStartTime      | 活动开始时间                 | 是   | [string]  | 2023-01-02 00:00:00                            |
| data>>records>>promotionStartTimeUtc   | 活动开始时间Utc              | 是   | [null]    | null                                           |
| data>>records>>promotionEndTime        | 活动结束时间                 | 是   | [string]  | 2023-01-03 23:59:00                            |
| data>>records>>firstSyncTime           | 首次同步时间                 | 是   | [string]  | 2023-03-06 18:15:41                            |
| data>>records>>lastSyncTime            | 最后同步时间                 | 是   | [string]  | 2024-01-09 14:13:20                            |
| data>>records>>remark                  | 备注                         | 是   | [string]  |                                                |
| total                                  |                              | 是   | [number]  | 1                                              |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "c6ed840963a24d3e9805ca03b269f51b.1752205194893",
    "response_time": "2025-07-11 11:40:01",
    "data": {
        "total": 1,
        "size": 20,
        "pageCount": 1,
        "current": 1,
        "currentSize": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "records": [{
            "promotionId": "VPC-6-14498719 Coupon",
            "name": "",
            "trackingId": "VPC-6-14498719 Coupon",
            "storeId": "132",
            "storeName": "feifan-JP1",
            "regionName": "日本",
            "currencyIcon": "JP¥",
            "status": 2,
            "statusText": "已过期",
            "originStatus": "EXPIRED",
            "originStatusText": "已过期",
            "promotionType": 0,
            "promotionTypeText": "未定义类型",
            "promotionCode": "",
            "promotionCodeType": null,
            "salesAmount": 0,
            "salesAmountUsd": 0,
            "salesVolume": 0,
            "participateCondition": "",
            "participateConditionNum": 0,
            "buyerGets": "",
            "buyerGetsNum": 0,
            "purchaseProduct": "",
            "discountProduct": "",
            "excludeProduct": "",
            "exchangeLimit": 0,
            "promotionStartTime": "2023-01-02 00:00:00",
            "promotionStartTimeUtc": null,
            "promotionEndTime": "2023-01-03 23:59:00",
            "firstSyncTime": "2023-03-06 18:15:41",
            "lastSyncTime": "2024-01-09 14:13:20",
            "remark": ""
        }]
    },
    "total": 1
}
```

