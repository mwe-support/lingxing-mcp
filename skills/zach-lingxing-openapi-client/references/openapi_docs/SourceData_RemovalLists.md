# 查询亚马逊源报表-移除货件（旧）
>支持查询FBA移除货件报表数据  
>2022年8月1日后暂停更新此接口数据，获取之后的数据请使用 [查询亚马逊源报表-移除货件（新）](docs/SourceData/RemovalShipmentList)

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/fba_report/removalLists` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|start_date|开始时间，格式：Y-m-d，闭区间|是|[string]|2020-01-01|
|end_date|结束时间，格式：Y-m-d，开区间|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]| 0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sid|店铺id|是|[int]|2|
|data>>uuid|UUID|是|[string]|00340312891280010051|
|data>>request_timestamp|时间戳|是|[int]|1569808565|
|data>>request_date|创建时间|是|[string]|2019-09-30T01:56:05+00:00|
|data>>order_id|订单ID|是|[string]|930-GB-DE|
|data>>shipment_date|发货日期|是|[string]|2019-10-08T10:01:06+00:00|
|data>>sku|MSKU|是|[string]|DA12210B1|
|data>>fnsku|FNSKU|是|[string]|X0006NNFU0H|
|data>>disposition|disposition|是|[string]|Sellable|
|data>>shipped_quantity|发货量 |是|[number]|220|
|data>>carrier| 承运商|是|[string]|DRUDE|
|data>>tracking_number|物流跟踪号 |是|[string]|00340312891280010051|
|data>>shipment_status| 状态|是|[string]|  |
|data>>mid|站点ID|是|[number]|4|
|data>>seller_name|店铺名称|是|[string]|ID-DE-TU1-UK|
|data>>marketplace|站点名称|是|[string]|英国|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "37DC4E78-D303-8B49-E095-6496200F0B3F",
    "response_time": "2024-08-06 16:00:12",
    "data": [
        {
            "sid": 109,
            "uuid": "109|Black_ Head_Rope|9374889679010852492854",
            "uuid_num": 1,
            "request_timestamp": 1650017069,
            "request_date": "2022-04-15T03:04:29-07:00",
            "order_id": "8P_US_0415",
            "removal_order_type": "Return",
            "shipment_date": "2022-04-16T03:54:19-07:00",
            "sku": "Black_ Head_Rope",
            "fnsku": "B09MT3989Q",
            "disposition": "Sellable",
            "shipped_quantity": 1,
            "carrier": "USPS",
            "tracking_number": "9374889679010852492854",
            "shipment_status": "",
            "remarks": "",
            "gmt_modified": "2022-08-08 05:50:09",
            "v_uuid": "767039d7-eda4-45ed-bdf5-3d322dc6118e",
            "company_id": 90128554873982976,
            "mid": 1,
            "seller_name": "8P-US",
            "marketplace": "美国"
        }
    ],
    "total": 4
}
```