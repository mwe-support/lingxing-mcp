# 查询亚马逊源报表-移除订单（新）
查询 Reports-Fulfillment-Removal Order Detail 报表
> 报表为seller_id维度，按sid请求会返回对应seller_id下所有移除订单数据，同一个seller_id授权的店铺任取一个sid请求报表数据即可

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/data/order/removalOrderListNew` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
|------|---------|------------|------------|--------|
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|start_date|查询时间【更新时间】，左闭区间,格式：Y-m-d|是|[string]|2020-01-01|
|end_date|查询时间【更新时间】，右开区间,格式：Y-m-d|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|
|search_field_time|搜索时间类型：【默认 last_updated_date】<br>last_updated_date 更新时间<br>request_date 创建时间|是|[string]|last_updated_date|

## 请求示例
```
{
    "sid": 109,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "search_field_time": "last_updated_date",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
|------|---------|------------|------------|--------|
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|EBF82D68-51E2-9993-517B-19F2D10A40A5|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]||
|data>>seller_id|亚马逊店铺id|是|[string]|A1MQMW3JWPNXXX|
|data>>sid|店铺id【为0代表未确定订单店铺】|是|[int]|101|
|data>>region|地区|是|[string]|na|
|data>>request_date|订单日期|是|[string]|2023-04-21T00:48:17-07:00|
|data>>order_id|订单号|是|[string]|222113|
|data>>order_type|订单类型|是|[string]|Return|
|data>>order_status|订单状态|是|[string]|Completed|
|data>>last_updated_date|更新时间|是|[string]|2023-04-25T08:02:19-07:00|
|data>>sku|msku|是|[string]|a-111|
|data>>fnsku|fnsku|是|[string]|B09MT3989X|
|data>>disposition|库存属性|是|[string]|Sellable|
|data>>requested_quantity|请求数量|是|[number]|2|
|data>>cancelled_quantity|取消数量|是|[number]|2|
|data>>disposed_quantity|已处置数量|是|[number]|0|
|data>>shipped_quantity|已发货数量|是|[number]|0|
|data>>in_process_quantity|处置中数量|是|[number]|0|
|data>>removal_fee|移除费用|是|[string]|0.0000|
|data>>currency|币种|是|[string]||
|data>>address_detail|配送地址|是|[string]|1234a,36003,Autauga Autaugaville66666,AL,美国|
|data>>country_code|国家编码|是|[string]||
|data>>local_sku|sku|是|[string]||
|data>>local_name|品名|是|[string]||
|total|总数|是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "B86AF260-2D3E-7C9C-777E-7B1DC54FE4AA",
    "response_time": "2023-05-31 13:02:42",
    "data": [{
        "seller_id": "A1MQMW3JWPNXXX",
	    "sid":101,
        "region": "na",
        "request_date": "2023-04-21T00:48:17-07:00",
        "order_id": "222113",
        "order_type": "Return",
        "order_status": "Completed",
        "last_updated_date": "2023-04-25T08:02:19-07:00",
        "sku": "a-111",
        "fnsku": "B09MT3989X",
        "disposition": "Sellable",
        "requested_quantity": 2,
        "cancelled_quantity": 2,
        "disposed_quantity": 0,
        "shipped_quantity": 0,
        "in_process_quantity": 0,
        "removal_fee": "0.0000",
        "currency": "",
        "address_detail": "1234aa,36003,Autauga Autaugaville66666,AL,美国"
    }],
    "total": 1
}
```
