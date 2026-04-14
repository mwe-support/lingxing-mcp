# 查询亚马逊源报表-移除订单（旧）
查询 Removal order detail report 报表
>支持查询FBA移除订单报表数据  
>2022年8月1日后暂停更新此接口数据，获取之后的数据请使用 [查询亚马逊源报表-移除订单（新）](docs/SourceData/RemovalOrderListNew)

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/removalOrders` | HTTPS | POST | 5 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|start_date|更新时间，左闭区间，格式：Y-m-d|是|[string]|2020-01-01|
|end_date|更新时间，右开区间，格式：Y-m-d格式|是|[string]|2024-08-05|
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

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>request_date|提交移除订单的日期|是|[string]|2019-05-22T11:53:00+00:00|
|data>>order_id|订单编号|是|[string]|vj5mbQz981|
|data>>order_type|移除订单类型（退货或弃置）|是|[string]|Disposal|
|data>>order_status|移除订单状态|是|[string]|  |
|data>>last_updated_date|订单最近更新的日期|是|[string]|2019-05-28T21:22:29+00:00|
|data>>sku|SKU|是|[string]|DA19037B91|
|data>>fnsku|FNSKU|是|[string]|X000NYD9RDX|
|data>>disposition|商品状况|是|[string]|Unsellable|
|data>>requested_quantity|移除订单中请求的此 FNSKU 的商品数量|是|[int]|1|
|data>>cancelled_quantity|取消数量|是|[int]| |
|data>>disposed_quantity|已处置数量|是|[int]|1|
|data>>shipped_quantity|已发货数量|是|[int]| |
|data>>in_process_quantity|处置中数量|是|[int]| |
|data>>removal_fee|移除费用|是|[string]|0.1000|
|data>>currency|币种|是|[string]|EUR|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "66B79749-7527-B8DF-49D4-3C7DFA349E39",
    "response_time": "2024-08-06 15:54:27",
    "data": [
        {
            "request_date": "2022-04-15T02:59:16-07:00",
            "order_id": "2204151CH2",
            "order_type": "Return",
            "order_status": "Cancelled",
            "last_updated_date": "2022-04-15T03:00:50-07:00",
            "sku": "Pink_Head_Rope",
            "fnsku": "B09MT9BKGH",
            "disposition": "Sellable",
            "requested_quantity": 2,
            "cancelled_quantity": 2,
            "disposed_quantity": 0,
            "shipped_quantity": 0,
            "in_process_quantity": 0,
            "removal_fee": "0.0000",
            "currency": ""
        }
    ],
    "total": 14
}
```