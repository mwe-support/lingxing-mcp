# 查询请款池-物流请款
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/requestFundsPool/logistics/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0| 否 | [int] | 0 |
|length|分页长度，默认20，上限200| 否 | [int] | 20 |
|search_field_time|时间搜索类型：<br />create_time  费用录入时间  <br />delivery_create_time  发货单创建时间 <br />shipment_time  发货时间 <br />close_time  付清时间|否|[string]| create_time |
|start_time|开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-23|
|end_time|结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|search_field|搜索类型：<br />order_sn  发货单号 <br />logistics_center_code  物流中心编码|否|[string]|order_sn|
|search_value|搜索值|否|[string]|SP240719005|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "search_field_time": "create_time",
    "start_time": "2024-07-23",
    "end_time": "2024-07-25",
    "search_field": "order_sn",
    "search_value": "SP240719005"
}
```

## 返回结果

Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ |  :------------ | :------------ |
| code | 状态码，0 成功  | 是   | [int]    | 0  |
| message  | 消息提示  | 是   | [string] | success |
| error_details  | 错误信息 | 是   | [array]  |  |
| request_id | 请求链路id  | 是   | [string] | 77ac259a67d5462594c83b80669b6eae.1692331008758 |
| response_time  | 响应时间 | 是   | [string] | 2023-08-18 11:56:49  |
| total  | 总数 | 是   | [int]    | 127 |
| data | 响应数据  | 是   | [array]  |   |
|data>>delivery_order_sn|发货单号|是|[string]|SP211123011|
|data>>source_type|来源类型：<br />1  发货单 <br />2  海外仓备货单|是|[int]|1|
|data>>pay_status|付款状态：<br />0  未申请  <br />1 已申请<br /> 2  部分付款 <br />3  已付清|是|[int]|1|
|data>>pay_status_text|付款状态文本|是|[string]|未申请|
|data>>receive_owner|收货仓库|是|[array]|["仓库11"]|
|data>>fee_type_text|费用类型文本|是|[string]|物流费用|
|data>>create_user|录入人名称|是|[string]| jack  |
|data>>create_time|录入时间|是|[string]|2021-11-23 15:22:20|
|data>>logistics_provider_id|物流商 ID|是|[string]|76|
|data>>logistics_provider_name|物流商名称|是|[string]|云途|
|data>>logistics_channel_name|物流方式名称|是|[string]|物流方式示例名字|
|data>>currency|币种|是|[string]|CNY|
|data>>currency_icon|币种符号|是|[string]|￥|
|data>>fee|费用金额|是|[string]|1.00|
|data>>discount|折扣金额|是|[string]|0.00|
|data>>payable_amount|应付金额|是|[string]|1.00|
|data>>paid_fee|已付金额|是|[string]|0.00|
|data>>unpaid_fee|未付金额|是|[string]|1.00|
|data>>apply_fee|申请中|是|[string]|0.00|
|data>>unapply_fee|未申请|是|[string]|1.00|
|data>>delivery_create_time|发货单创建时间|是|[string]|2022-09-17 14:51:55|
|data>>unpaid_request_funds| 未支付请款单 |是|[array]| |
|data>>unpaid_request_funds>>order_sn| 请款单单号 |是|[string]| RF220920007 |
|data>>unpaid_request_funds>>goods_value| 请款金额 |是|[string]| 50.00 |
|data>>unpaid_request_funds>>paid_fee| 已付金额 |是|[string]| 50.000000 |
|data>>unpaid_request_funds>>apply_user| 申请人 |是|[string]| 张军 |
|data>>unpaid_request_funds>>apply_time| 申请时间 |是|[string]| 2022-09-20 15:42:22 |
|data>>unpaid_request_funds>>status| 状态：<br />1 待付款<br />2 已完成<br />3 已作废<br />121 待审批<br />122 已驳回<br />124 已作废（审批流） |是|[int]| 2 |
|data>>unpaid_request_funds>>status_text| 状态说明 |是|[string]| 已完成 |
|data>>paid_request_funds| 已付清请款单 |是|[array]| |
|data>>paid_request_funds>>order_sn| 请款单单号 |是|[string]|RF220920007|
|data>>paid_request_funds>>goods_value| 请款金额 |是|[string]|50.00|
|data>>paid_request_funds>>paid_fee| 已付金额 |是|[string]|50.000000|
|data>>paid_request_funds>>apply_user| 申请人名称 |是|[string]|张军|
|data>>paid_request_funds>>apply_time| 申请时间 |是|[string]|2022-09-20 15:42:22|
|data>>paid_request_funds>>status| 状态：<br />1 待付款<br />2 已完成<br />3 已作废<br />121 待审批<br />122 已驳回<br />124 已作废（审批流） |是|[int]|2|
|data>>paid_request_funds>>status_text| 状态说明 |是|[string]|已完成|
|data>>shipment_ids| FBA 货件信息 |是|[array]| |
|data>>shipment_ids>>shipment_id| FBA 货件号 |是|[string]|FBA171VSN7N5|
|data>>shipment_ids>>inbound_shipment_item_mws_id| FBA 货件ID |是|[string]|47049|
|data>>provide_ids| 物流商单号 |是|[array]| ["1111"] |
|data>>shipment_date| 发货时间 |是|[string]| 1970-01-01 08:00:00 |
|data>>warehouse_list|发货仓库信息|是|[array]| |
|data>>warehouse_list>>rfpl_id|请款池单据 ID|是|[string]|301309165783843300|
|data>>warehouse_list>>wid|发货仓库 ID|是|[string]|48|
|data>>warehouse_list>>warehouse_name|发货仓库名称|是|[string]|新增仓库cXDt7dtWXy|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "b3411c55788d496ab3bb2eff93d95761.119.16966503960012927",
    "response_time": "2023-10-07 11:46:36",
    "data": [
        {
            "delivery_order_sn": "OWS220613001",
            "source_type": 2,
            "pay_status": 0,
            "pay_status_text": "未申请",
            "receive_owner": [
                "ffff-自建海外仓"
            ],
            "fee_type_text": "税费",
            "create_user": "zhangsan",
            "create_time": "2022-07-14 16:34:30",
            "logistics_provider_id": "1",
            "logistics_provider_name": "",
            "logistics_channel_name": "",
            "currency": "CNY",
            "currency_icon": "￥",
            "fee": "1.00",
            "discount": "0.00",
            "payable_amount": "1.00",
            "paid_fee": "0.00",
            "unpaid_fee": "1.00",
            "apply_fee": "0.00",
            "unapply_fee": "1.00",
            "delivery_create_time": "2022-06-13 18:02:33",
            "unpaid_request_funds": [],
            "paid_request_funds": [],
            "shipment_ids": [],
            "provide_ids": [],
            "shipment_date": "2022-06-13 18:02:52",
            "warehouse_list": [
                {
                    "rfpl_id": "301205149268918272",
                    "wid": "1",
                    "warehouse_name": "仓库1"
                }
            ]
        }
    ],
    "total": 50
}

```

