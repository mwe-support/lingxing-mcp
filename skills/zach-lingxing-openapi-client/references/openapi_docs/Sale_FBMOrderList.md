# 查询亚马逊自发货订单列表
支持查询亚马逊FBM（自发货）订单列表，对应系统【销售】>【订单管理】模块数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/order/Order/getOrderList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|sid|店铺sid，用英文逗号分隔开 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[string]|22,34| 
|order_status|订单状态，多个用英文逗号分隔：<br>2 已发货<br>3 未付款<br>4 待审核<br>5 待发货<br>6 已取消|否|[string]|2,3| 
|page|页码数，默认1|否|[int]|1| 
|length|分页长度，默认100|否|[int]|100| 
|start_time|订购时间开始|否|[string]|2021-02-01 08:13:22 | 
|end_time|订购时间结束|否|[string]| 2021-02-05 08:13:22| 

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|操作成功|是|[string]|操作成功|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|052e20647c9c4622adb7576ae335211d.1687946868074|
|response_time|响应时间|是|[string]|2021-06-28 18:07:50|
|data|响应数据|是|[array]|  |
|data>>order_number|系统单号|是|[string]|103264677770103264677770 |
|data>>status|订单状态|是|[string]|待审核 |
|data>>order_from|订单类型|是|[string]|线上订单 |
|data>>country_code|目的国代码|是|[string]|JPJP |
|data>>purchase_time|订购时间|是|[string]|2021-01-31 23:47:492021-01-31 23:47:49 |
|data>>logistics_type_id|物流方式ID|是|[string]|物流方式ID|
|data>>logistics_provider_id|物流商ID|是|[string]|物流商ID|
|data>>platform_list|平台订单号|是|[array]|["113-5188133-2150656"]|
|data>>logistics_type_name|物流方式名称|是|[string]|联邮通优先挂号-带电 物流方式名称|
|data>>logistics_provider_name|物理商名称|是|[string]|4PX |
|data>>wid|发货仓库id|是|[int]|发货仓库id|
|data>>warehouse_name|发货仓库名称|是|[string]| OW-测试仓库 |
|data>>customer_comment|客服备注|是|[string]|qqqqqqqqqqqqqqqqqqq |
|total|总数|是|[int]|1 |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "C8491EBE-E2B0-86A1-9836-5A6CEF0CB1A8",
    "response_time": "2021-07-19 10:23:44",
    "data": [
        {
            "order_number": "103318489501696512",
            "status": "待发货",
            "order_from": "手工订单",
            "country_code": "US",
            "purchase_time": "2023-05-30 22:57:06",
            "logistics_type_id": "3295",
            "logistics_provider_id": "83",
            "platform_list": [
                543535
            ],
            "logistics_type_name": "HH",
            "logistics_provider_name": "HH",
            "wid": 130,
            "warehouse_name": "HH",
            "customer_comment": ""
        }
    ],
    "total": 38
}
```
