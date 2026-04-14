# 查询库存分类账detail数据

>支持查询亚马逊库存分类账detail数据，来源 GET_LEDGER_DETAIL_VIEW_DATA  
>注意：由于亚马逊库存分类账生成数据后5天内会发生变更，领星在获取数据的5天内会继续获取数据并覆盖更新历史版本，因此接口获取的5天内数据是有可能发生变更的

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/cost/center/ods/detail/query ` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |  
| sellerIds   |亚马逊店铺id|是|[array]|["AN05PRUL7R796"]|
| startDate   |统计起始日期 Y-m-d 闭区间|是|[string]|2024-03-02|
| endDate     |统计结束日期 Y-m-d 闭区间|是|[string]|2024-06-1|
| fnskus      |fnsku列表|否|[array]|["B085M7NH7S"]|
| asins       |asin列表|否|[array]|["B097MP26YP"]|
| mskus       |msku列表|否|[array]|["DA19037B1"]|
| eventTypes  |事件类型，支持传多值：<br>01 Shipments<br>02 CustomerReturns<br>03 WhseTransfers<br>04 Receipts<br>05 VendorReturns<br>06 Adjustments|否|[array]|["01","02"]|
| referenceId |引用id，支持模糊搜索|否|[string]||
| disposition |库存类型：<br>01 SELLABLE<br>02 UNSELLABLE<br>03 ALL|否|[string]|01|
| locations   |国家编码列表|否|[array]|GB|
| offset      |分页偏移量，默认0|否|[int]|0|
| length      |分页长度，默认20，上限1000|否|[int]|20|

## 请求示例
```
{
    "sellerIds": [
        "AN05PRUL7R796"
    ],
    "startDate": "2024-03-02",
    "endDate": "2024-06-1",
    "fnskus": [
        "B085M7NH7S"
    ],
    "asins": [
        "B097MP26YP"
    ],
    "mskus": [
        "DA19037B1"
    ],
    "eventTypes": [
        "01",
        "02"
    ],
    "disposition": "01",
    "location": "GB",
    "offset": 0,
    "length": 20
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
| code                             | 状态码，1 成功  | 是   | [int]  |   1          |
| msg                              | 响应信息       | 是   | [string]  |              |
| success                          | 操作是否成功   | 是   | [boolean] |              |
| traceId                          | 请求链路id     | 是   | [string]  |              |
| data                             | 明细数据       | 是   | [object]  |              |
| data>>total                      | 总记录条数     | 是   | [number]  |              |
| data>>size                       | 每个数据页大小 | 是   | [number]  |              |
| data>>current                    | 当前所在数据页 | 是   | [number]  |              |
| data>>records                    | 明细数据列表   | 是   | [array]   |              |
| data>>records>>sellerId          | 亚马逊店铺id   | 是   | [string]  |              |
| data>>records>>date              | 数据日期       | 是   | [string]  | 2022-04-01 |
| data>>records>>fnsku             | fnsku          | 是   | [string]  |              |
| data>>records>>asin              | asin           | 是   | [string]  |              |
| data>>records>>msku              | msku           | 是   | [string]  |              |
| data>>records>>title             | 标题           | 否   | [string]  |              |
| data>>records>>eventType         | 事件类型       | 是   | [string]  | 01         |
| data>>records>>eventTypeDesc     | 事件类型描述   | 是   | [string]  | Shipments  |
| data>>records>>referenceId       | 货物id         | 否   | [string]  |              |
| data>>records>>quantity          | 数量           | 是   | [number]  |              |
| data>>records>>fulfillmentCenter | 储存库存的履行中心 | 是   | [string]  |              |
| data>>records>>disposition       | 库存属性       | 是   | [string]  | 01         |
| data>>records>>dispositionDesc   | 库存属性描述   | 是   | [string]  | SELLABLE   |
| data>>records>>reason           | 原因           | 否   | [string]  |              |
| data>>records>>location          | 国家           | 是   | [string]  | GB         |
| data>>records>>uniqueMd5Idx      | 和uniqueMd5联合作为唯一键，uniqueMd5Idx是标识uniqueMd5的index       | 是   | [string]  |bc4f83291d4fda71272fc586b81c3240|
| data>>records>>uniqueMd5         | 和uniqueMd5Idx联合作为唯一键          | 是   | [string]  |0|

## 返回成功示例
```
{
    "code": 1,
    "msg": "操作成功",
    "data": {
        "records": [
            {
                "sellerId": "xxxxxxxxxxxxxxxx",
                "date": "2022-04-01",
                "fnsku": "X0010DNT2F",
                "asin": "B07Q3PV8SR",
                "msku": "1300U1207",
                "title": "HEETA Scalp Massager [Soft& Convenient] Shampoo Brush with Silicone Bristles for Wet and Dry Hair",
                "eventType": "01",
                "eventTypeDesc": "Shipments",
                "referenceId": "41247588491302",
                "quantity": -1,
                "fulfillmentCenter": "EUK5",
                "disposition": "01",
                "dispositionDesc": "SELLABLE",
                "reason": "",
                "location": "GB",
                "uniqueMd5Idx": "bc4f83291d4fda71272fc586b81c3240",
                "uniqueMd5": "0",
            }
        ],
        "total": 12673,
        "size": 20,
        "current": 1,
        "orders": [],
        "optimizeCountSql": true,
        "hitCount": false,
        "countId": null,
        "maxLimit": null,
        "searchCount": true,
        "pages": 634
    },
    "traceId": "b2532fc7-9c1b-4b08-8d30-301b31b70562.1663226369188",
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