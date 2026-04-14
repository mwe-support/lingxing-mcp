# 查询商品折扣详情-列表-秒杀

## 接口信息

| API Path                                    | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------------------------------------ | :------- | :------- | :----------------------------------------------------------- |
| `/basicOpen/promotion/listingDetailSecKill` | HTTPS    | POST     | 1                                                            |

## 请求参数

| 参数名        | 说明                                                         | 必填 | 类型     | 示例         |
| :------------ | :----------------------------------------------------------- | :--- | :------- | :----------- |
| sellerSku     | sellerSku                                                    | 是   | [string] | 09-CJWX-DFQH |
| promotionType | 促销类型                                                     | 否   | [array]  | []           |
| status        | 促销状态                                                     | 否   | [array]  | []           |
| storeId       | 店铺id                                                       | 是   | [string] | 31           |
| startTime     | 活动开始时间                                                 | 是   | [string] | 2021-06-21   |
| endTime       | 活动结束时间                                                 | 是   | [string] | 2021-06-28   |
| sortField     | 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） | 是   | [string] | startTime    |
| sortType      | 排序类型 asc desc                                            | 是   | [string] | desc         |
| pageNum       | 分页页码                                                     | 是   | [number] | 1            |
| pageSize      | 分页大小                                                     | 是   | [number] | 20           |

## 请求示例

```
{
    "sellerSku": "09-CJWX-DFQH",
    "promotionType": [],
    "status": [],
    "storeId": "31",
    "startTime": "2021-06-21",
    "endTime": "2021-06-28",
    "sortField": "startTime",
    "sortType": "desc",
    "pageNum": 1,
    "pageSize": 20
}
```

## 返回结果

Json Object

| 参数名                               | 说明                     | 必填 | 类型      | 示例                                           |
| :----------------------------------- | :----------------------- | :--- | :-------- | :--------------------------------------------- |
| code                                 | 消息提示                 | 是   | [number]  | 0                                              |
| message                              | 消息                     | 是   | [string]  | success                                        |
| error_details                        | 错误信息                 | 是   | [array]   | []                                             |
| request_id                           | 请求id                   | 是   | [string]  | 247d20a083f64e978b8281861dc53a9f.1752196813228 |
| response_time                        | 响应时间                 | 是   | [string]  | 2025-07-11 09:20:17                            |
| data                                 |                          | 是   | [object]  |                                                |
| data>>total                          |                          | 是   | [number]  | 1                                              |
| data>>size                           |                          | 是   | [number]  | 20                                             |
| data>>pageCount                      |                          | 是   | [number]  | 1                                              |
| data>>current                        |                          | 是   | [number]  | 1                                              |
| data>>currentSize                    |                          | 是   | [number]  | 1                                              |
| data>>hasNextPage                    |                          | 是   | [boolean] | false                                          |
| data>>hasPreviousPage                |                          | 是   | [boolean] | false                                          |
| data>>records                        |                          | 是   | [array]   |                                                |
| data>>records>>promotionId           | 活动id，唯一标识         | 是   | [string]  | 8189187e-c8c2-3bae-8f42-9ae8709fd6d8           |
| data>>records>>name                  | 秒杀标题                 | 是   | [string]  | Ciwete Stainless Steel Kitchen Cookware Set    |
| data>>records>>productQuantity       | 商品数量                 | 是   | [number]  | 2                                              |
| data>>records>>storeId               | 店铺id                   | 是   | [string]  | 31                                             |
| data>>records>>storeName             | 店铺名                   | 是   | [string]  | 非凡-JP                                        |
| data>>records>>regionName            | 国家/地区名              | 是   | [string]  | 日本                                           |
| data>>records>>currencyIcon          | 货币icon                 | 是   | [string]  | JP¥                                            |
| data>>records>>status                | 状态，系统内部状态（非促销活动状态）                     | 是   | [number]  | 0                                              |
| data>>records>>statusText            | 状态，系统内部状态（非促销活动状态）                        | 是   | [string]  | 其它                                           |
| data>>records>>originStatus          | 促销活动平台状态（与ERP中显示一致）        | 是   | [string]  | CANCELLED                                      |
| data>>records>>originStatusText      | 促销活动平台状态（与ERP中显示一致）        | 是   | [string]  | 已取消                                         |
| data>>records>>promotionType         | 秒杀类型                 | 是   | [number]  | 2                                              |
| data>>records>>promotionTypeText     | 秒杀类型                 | 是   | [string]  | Lightning Deal                                 |
| data>>records>>description           | 描述                     | 是   | [string]  | 秒杀-2021/03/10 2-19-52-682                    |
| data>>records>>seckillFee            | 秒杀费                   | 是   | [number]  | 0                                              |
| data>>records>>seckillFeeMin         | 最小秒杀费               | 是   | [number]  | 300                                            |
| data>>records>>seckillFeeMax         | 最大秒杀费               | 是   | [number]  | 500                                            |
| data>>records>>waived                | 该秒杀是否“已豁免”       | 是   | [boolean] | false                                          |
| data>>records>>salesAmount           | 活动总销售额             | 是   | [number]  | 0                                              |
| data>>records>>salesAmountUsd        | 活动总销售额，换算成美元 | 是   | [number]  | 0                                              |
| data>>records>>salesVolume           | 活动总销量               | 是   | [number]  | 0                                              |
| data>>records>>participateInventory  | 参与库存数               | 是   | [number]  | 19                                             |
| data>>records>>soldRate              | 售出率                   | 是   | [number]  | 0                                              |
| data>>records>>pageView              | 浏览量                   | 是   | [string]  | 0                                              |
| data>>records>>exchangeRate          | 转化率                   | 是   | [number]  | 0                                              |
| data>>records>>pcos                  | 费用除以销售额           | 是   | [number]  | 0                                              |
| data>>records>>promotionStartTime    | 活动开始时间             | 是   | [string]  | 2021-06-21 07:00:00                            |
| data>>records>>promotionStartTimeUtc | 活动开始时间UTC          | 是   | [null]    | null                                           |
| data>>records>>promotionEndTime      | 活动结束时间             | 是   | [string]  | 2021-06-28 06:59:00                            |
| data>>records>>firstSyncTime         | 首次同步时间             | 是   | [string]  | 2023-03-03 16:43:08                            |
| data>>records>>lastSyncTime          | 最后同步时间             | 是   | [string]  | 2023-03-03 16:43:08                            |
| data>>records>>remark                | 备注                     | 是   | [string]  |                                                |
| total                                | 总数                     | 是   | [number]  | 1                                              |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "247d20a083f64e978b8281861dc53a9f.1752196813228",
    "response_time": "2025-07-11 09:20:17",
    "data": {
        "total": 1,
        "size": 20,
        "pageCount": 1,
        "current": 1,
        "currentSize": 1,
        "hasNextPage": false,
        "hasPreviousPage": false,
        "records": [{
            "promotionId": "8189187e-c8c2-3bae-8f42-9ae8709fd6d8",
            "name": "Ciwete Stainless Steel Kitchen Cookware Set",
            "productQuantity": 2,
            "storeId": "31",
            "storeName": "非凡-JP",
            "regionName": "日本",
            "currencyIcon": "JP¥",
            "status": 0,
            "statusText": "其它",
            "originStatus": "CANCELLED",
            "originStatusText": "已取消",
            "promotionType": 2,
            "promotionTypeText": "Lightning Deal",
            "description": "秒杀-2021/03/10 2-19-52-682",
            "seckillFee": 0,
            "seckillFeeMin": 300,
            "seckillFeeMax": 500,
            "waived": false,
            "salesAmount": 0,
            "salesAmountUsd": 0,
            "salesVolume": 0,
            "participateInventory": 19,
            "soldRate": 0,
            "pageView": "0",
            "exchangeRate": 0,
            "pcos": 0,
            "promotionStartTime": "2021-06-21 07:00:00",
            "promotionStartTimeUtc": null,
            "promotionEndTime": "2021-06-28 06:59:00",
            "firstSyncTime": "2023-03-03 16:43:08",
            "lastSyncTime": "2023-03-03 16:43:08",
            "remark": ""
        }]
    },
    "total": 1
}
```

