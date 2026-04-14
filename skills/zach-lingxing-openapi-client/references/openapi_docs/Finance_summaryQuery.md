# 查询库存分类账summary数据

支持查询亚马逊库存分类账summary数据，来源 GET_LEDGER_SUMMARY_VIEW_DATA

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/cost/center/ods/summary/query ` | HTTPS | POST | 10 |

## 请求参数

| 参数名      | 说明                                                       | 必填 | 类型     | 示例                                  |
| ----------- | ---------------------------------------------------------- | ---- | -------- | ------------------------------------- |
| sellerIds   | 亚马逊店铺id|是|[array]|["AN05PRUL7R796"]|
| queryType   | 查询维度：1 按月，2 按天|是|[int]|1|
| startDate   | 统计起始日期：月维度：Y-m ，天维度：Y-m-d，闭区间 |是|[string]|月维度:"2022-01"，天维度："2022-01-01"|
| endDate     | 统计结束日期：月维度：Y-m ，天维度：Y-m-d，闭区间  |是|[string]|月维度:"2022-01"，天维度："2022-01-01"|
| fnskus      | fnsku列表|否|[array]|["B085M7NH7S"]|
| asins       | asin列表|否|[array]|["B097MP26YP"]|
| mskus       | msku列表|否|[array]|["DA19037B1"]|
| disposition | 库存属性：01 SELLABLE，02 UNSELLABLE，03 ALL|否|[string]|"01"|
| locations   | 国家编码列表|否|[array]|"GB"|
| offset      | 分页偏移量，默认0|否|[int]|0|
| length      | 分页长度，默认20，上限1000|否|[int]|20|

## 请求示例
```
{
    "sellerIds": [
        "AN05PRUL7R796"
    ],
    "queryType": 1,
    "startDate": "2024-04",
    "endDate": "2024-06",
    "fnskus": [
        "B085M7NH7S"
    ],
    "asins": [
        "B097MP26YP"
    ],
    "mskus": [
        "DA19037B1"
    ],
    "disposition": "01",
    "location": "GB",
    "offset": 0,
    "length": 20
}
```

## 返回结果
Json Object

| 参数名                                    | 说明           | 必填 | 类型      | 示例                                  |
| ----------------------------------------- | -------------- | ---- | --------- | ------------------------------------- |
| code                                      | 状态码，1 成功   | 是   | [int]  |                                       |
| msg                                       | 响应信息       | 是   | [string]  |                                       |
| success                                   | 操作是否成功   | 是   | [boolean] |                                       |
| traceId                                   | 请求链路Id     | 是   | [string]  |                                       |
| data                                      | 汇总数据       | 是   | [Object]  |                                       |
| data>>total                               | 总记录条数     | 是   | [number]  |                                       |
| data>>size                                | 每个数据页大小 | 是   | [number]  |                                       |
| data>>current                             | 当前所在数据页 | 是   | [number]  |                                       |
| data>>records                             | 汇总数据列表   | 是   | [array]   |                                       |
| data>>records>>sellerId                   | 店铺Id         | 是   | [string]  |                                       |
| data>>records>>date                       | 数据日期       | 是   | [string]  | 月维度:"2022-01"，天维度:"2022-01-01" |
| data>>records>>fnsku                      | fnsku          | 是   | [string]  |                                       |
| data>>records>>msku                       | msku           | 是   | [string]  |                                       |
| data>>records>>title                      | 标题           | 否   | [string]  |                                       |
| data>>records>>disposition                | 库存属性       | 是   | [string]  | "01"                                  |
| data>>records>>dispositionDesc            | 库存属性描述   | 是   | [string]  | "SELLABLE"                            |
| data>>records>>startingWarehouseBalance   | 期初库存       | 是   | [number]  |                                       |
| data>>records>>inTransitBetweenWarehouses | 调拨在途       | 是   | [number]  |                                       |
| data>>records>>receipts                   | 签收           | 是   | [number]  |                                       |
| data>>records>>customerShipments          | 销售出库       | 是   | [number]  |                                       |
| data>>records>>customerReturns            | 销售退货       | 是   | [number]  |                                       |
| data>>records>>vendorReturns              | 移除           | 是   | [number]  |                                       |
| data>>records>>warehouseTransferInOrOut   | 调拨出入库     | 是   | [number]  |                                       |
| data>>records>>found                      | 找回           | 是   | [number]  |                                       |
| data>>records>>lost                       | 丢失           | 是   | [number]  |                                       |
| data>>records>>damaged                    | 损毁           | 是   | [number]  |                                       |
| data>>records>>disposed                   | 弃置           | 是   | [number]  |                                       |
| data>>records>>otherEvents                | 其他           | 是   | [number]  |                                       |
| data>>records>>endingWareHouseBalance     | 期末库存       | 是   | [number]  |                                       |
| data>>records>>unKnownEvents              | 未知           | 是   | [number]  |                                       |
| data>>records>>location                   | 国家编码       | 是   | [string]  | "GB"                                  |

## 返回成功示例

```
{
    "code":1,
    "msg":"操作成功",
    "data":{
        "records":[
            {
                "sellerId":"xxxxxxxxxxxxxxxx",
                "date":"2022-02",
                "fnsku":"X001HIDE4V",
                "asin":"B07YV8XB48",
                "msku":"1W-NDCE-8XGK-A",
                "title":"File Zipper Bags for School Office Household Travel Supplies (5 Colors)",
                "disposition":"01",
                "dispositionDesc":"SELLABLE",
                "startingWarehouseBalance":0,
                "inTransitBetweenWarehouses":0,
                "receipts":180,
                "customerShipments":-101,
                "customerReturns":0,
                "vendorReturns":0,
                "warehouseTransferInOrOut":0,
                "found":0,
                "lost":0,
                "damaged":0,
                "disposed":0,
                "otherEvents":0,
                "endingWareHouseBalance":79,
                "unKnownEvents":0,
                "location":"GB"
            }
        ],
        "total":95,
        "size":5,
        "current":1,
        "orders":[

        ],
        "optimizeCountSql":true,
        "hitCount":false,
        "countId":null,
        "maxLimit":null,
        "searchCount":true,
        "pages":19
    },
    "traceId":"7f7b2fd3-2831-495b-99db-6776438b6f8d.1663229370783",
    "success":true
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
