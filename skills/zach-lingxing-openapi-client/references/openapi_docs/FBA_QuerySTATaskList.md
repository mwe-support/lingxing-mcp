# 查询STA任务列表
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-plan/page` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|page|分页页码|是|[long]| |
|length|分页大小，上限200|是|[long]| |
|dateBegin|开始时间(北京时间)<br>备注:格式：YYYY-MM-DD<br>双闭区间|是|[string]| |
|dateEnd|结束时间(北京时间)<br>备注:格式：YYYY-MM-DD<br>双闭区间|是|[string]| |
|dateType|时间类型 1:创建 2更新|是|[int]| |
|planName|STA任务名称(模糊搜索)|否|[string]| |
|shipmentIdList|货件id或者货件单号(精确搜索)|否|[array]|["shd10e38ca-45e7-4a97-8512-780acf343f4b3"] |
|sids|领星店铺ID 列表，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)|否|[array]| |
|sortField| |否|[string]| |
|sortType| |否|[string]| |
|statusList|STA任务状态：<br>ACTIVE<br>VOIDED<br>SHIPPED<br>ERRORED |否|[array]|["ACTIVE","ERRORED"] |


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-plan/page?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "page": 1,
    "length": 10,
    "dateBegin": "2022-10-23",
    "dateEnd": "2022-11-21",
    "dateType": 2,
    "planName": "STA任务名称(模糊搜索)",
    "shipmentIdList": [""],
    "sids": [1],
    "statusList": ["ERRORED"]
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功|是|[int]|	0 |
|message|消息提示 |是|[string]|success |
|errorDetails|错误信息 |是|[array]| |
|requestId| 请求链路id|是|[string]| |
|responseTime|响应时间 |是|[string]| 2020-05-18 11:23:47|
|data| 响应数据|是|[object]| |
|data>>current| 当前页 |是|[long]| |
|data>>orders| 排序 |否|[array]| |
|data>>orders>>asc| 是否升序排列 |否|[boolean]| |
|data>>orders>>column| 排序列 |否|[string]| |
|data>>pages| 页数 |否|[long]| |
|data>>records| 记录行 |是|[array]| |
|data>>records>>gmtCreate|创建时间|是|[string]| |
|data>>records>>gmtModified|更新时间|是|[string]| |
|data>>records>>inboundPlanId|STA任务编号|是|[string]| |
|data>>records>>inboundPlanItemList|商品信息|是|[array]| |
|data>>records>>inboundPlanItemList>>asin|asin|是|[string]| |
|data>>records>>inboundPlanItemList>>fnsku|fnsku|是|[string]| |
|data>>records>>inboundPlanItemList>>msku|msku|是|[string]| |
|data>>records>>inboundPlanItemList>>parentAsin|父asin|是|[string]| |
|data>>records>>inboundPlanItemList>>productName|品名|是|[string]| |
|data>>records>>inboundPlanItemList>>quantity|申报量|是|[int]| |
|data>>records>>inboundPlanItemList>>sku|sku|是|[string]| |
|data>>records>>inboundPlanItemList>>title|标题|是|[string]| |
|data>>records>>inboundPlanItemList>>url|图片url|是|[string]| |
|data>>records>>planName|STA任务名称|是|[string]| |
|data>>records>>shipmentList|货件信息|是|[array]| |
|data>>records>>shipmentList>>shipmentId|货件id|是|[string]| |
|data>>records>>shipmentList>>shipmentConfirmationId|货件单号|是|[string]| |
|data>>records>>status|STA任务状态|是|[string]| |
|data>>records>>position_type|分仓方式，1-先装箱再分仓，2-先分仓再装箱|是|[int]|1|
|data>>records>>planCreateTime|计划创建时间|是|[string]|1|
|data>>records>>planUpdateTime|计划更新时间|是|[string]|1|
|data>>searchCount| |是|[boolean]| |
|data>>total| 总记录数 |是|[long]| ||


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": null,
    "requestId": "9810aa54fb474e89b291670773d641a5.1733217084822",
    "responseTime": "2024-12-03T17:11:24.822",
    "data": {
        "records": [{
            "inboundPlanId": "wf6d737569-f340-47d9-91cc-9936bf6211d7",
            "planName": "查询货件装箱详情",
            "gmtCreate": "2024-11-30 16:11",
            "gmtModified": "2024-11-30 16:13",
            "status": "ACTIVE",
            "shipmentList": [{
                "shipmentId": "sh689b63df-a66e-417b-8e6b-467a455f2cfd",
                "shipmentConfirmationId": "FBA18MKW1NY9"
            }, {
                "shipmentId": "shfb3190bd-b2d1-47f9-9988-5fbe466780a5",
                "shipmentConfirmationId": "FBA18ML13MY3"
            }],
            "inboundPlanItemList": [{
                "msku": "CN0002",
                "fnsku": "X00489S3FJ",
                "asin": "B0D3F2W56C",
                "parentAsin": "B0D3F2W56C",
                "productName": "随便spu-3",
                "sku": "asdkpasdk",
                "title": "Notes,Creative Cartoon,Students,Can Post It,Can Tear Messages N Times Paste",
                "url": "https://m.media-amazon.com/images/I/51YvC-1dvXL._SL75_.jpg",
                "quantity": 6
            }, {
                "msku": "20240122-GM",
                "fnsku": "X0047Z5K5Z",
                "asin": "B0CM59V6Y8",
                "parentAsin": "B0CPSY8HFP",
                "productName": "饭饭饭",
                "sku": "ggggasda",
                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky-GM",
                "url": "https://m.media-amazon.com/images/I/61-v2WaQOhL._SL75_.jpg",
                "quantity": 4
            }, {
                "msku": "STN0002",
                "fnsku": "X00489S34P",
                "asin": "B0D3F37ZPB",
                "parentAsin": "B0D3F37ZPB",
                "productName": "成本",
                "sku": "117009ZZ",
                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky",
                "url": "https://m.media-amazon.com/images/I/61FW9bR5rKL._SL75_.jpg",
                "quantity": 5
            }]
        }],
        "total": 1,
        "size": 10,
        "current": 1,
        "orders": [],
        "optimizeCountSql": true,
        "searchCount": true,
        "countId": null,
        "maxLimit": null,
        "pages": 1
    }
}
```