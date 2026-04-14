# 查询报表型数据明细-ASIN
支持查询FBA补货建议ASIN维度报表明细，可以获取模拟在途库存、在途模拟到达时间

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fbaSug/asin/getSourceList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|136|
|asin|ASIN|是|[string]|B0xxxxxxxx|
|type|数据类型：【默认1】<br>1 FBA可售<br>2 FBA在途<br>3 本地可用<br>4 待检量<br>5 待交付<br>6 采购计划<br>8 海外仓可用<br>9 海外仓在途|否|[string]|3|
|mode|补货建议模式：<br>0 普通模式<br>1 海外仓中转模式<br>不传默认取erp当前设置模式（在补货建议列表可切换）|否|[string]|1|

## 请求示例
```
{
    "sid": 136,
    "asin": "B0xxxxxxxx",
    "type": "3",
    "mode": "1"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[string]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|data|响应数据|是|[object]| |
|data>>mode|补货建议模式：<br>0 普通模式<br>1 海外仓中转模式|是|[string]|1|
|data>>source_list| |是|[array]|  |
|data>>source_list>>quantity|数量|是|[object]|25|
|data>>source_list>>type|数据类型：<br>1 FBA可售<br>2 FBA在途<br>3 本地可用<br>4 待检量<br>5 待交付<br>6 采购计划<br>8 海外仓可用<br>9 海外仓在途|是|[object]|6|
|data>>source_list>>amazon_sale_date|预计FBA可售时间|是|[string]|2021-07-06|
|data>>source_list>>remark|备注|是|[object]|  |
|data>>source_list>>remark>>msku|MSKU。type=1时返回|否|[string]|  |
|data>>source_list>>remark>>afn_fulfillable_quantity|FBA可售，type=1时|否|[string]|  |
|data>>source_list>>remark>>reserved_fc_transfers|待调仓，type=1时|否|[string]|  |
|data>>source_list>>remark>>reserved_fc_processing|调仓中，type=1时|否|[string]|  |
|data>>source_list>>remark>>shipment_id|货件单号，type=2时|否|[string]|  |
|data>>source_list>>remark>>warehouse_name|仓库名，type=3 或 type=8 或 type=9时|否|[string]|  |
|data>>source_list>>remark>>sku|SKU，type=3 或 type=8|否|[string]|  |
|data>>source_list>>remark>>fnsku|FNSKU，type=3 或 type=8|否|[string]|  |
|data>>source_list>>remark>>qc_sn|质检单号，type=4时|否|[string]|  |
|data>>source_list>>remark>>purchase_order_sn|采购单号，type=5时|否|[string]|  |
|data>>source_list>>remark>>plan_sn|采购计划编号，type=6时|否|[object]|PP210603016|
|data>>source_list>>remark>>overseas_order_no|海外仓备货单号，type=9时|否|[string]|  |
|data>>source_list>>remark>>logistics_name|物流方式，type=9时|否|[string]|  |
|data>>source_list>>remark>>deliver_time|发货时间，type=9时|否|[string]|  |
|data>>source_list>>expect_arrive_time|预计到货时间，仅type=5 或 type=9时|是|[string]|  |
|total|总数|是|[int]|0|


## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "B3A4ABBA-A31D-C81B-95E6-7D0FCF514C81",
    "response_time": "2021-11-11 17:50:45",
    "data": {
        "mode": "1",
        "source_list": [
            {
                "quantity": 10,
                "quantity_second": 0,
                "type": 6,
                "remark": {
                    "plan_sn": "PP211026009"
                },
                "amazon_sale_date": "2022-01-19",
                "expect_arrive_time": ""
            },
            {
                "quantity": 10,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO211106009"
                },
                "amazon_sale_date": "2022-01-15",
                "expect_arrive_time": ""
            },
            {
                "quantity": 20,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO211026015"
                },
                "amazon_sale_date": "2022-01-04",
                "expect_arrive_time": ""
            },
            {
                "quantity": 1,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO211021050"
                },
                "amazon_sale_date": "2021-12-30",
                "expect_arrive_time": ""
            },
            {
                "quantity": 23,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO211021035"
                },
                "amazon_sale_date": "2021-12-30",
                "expect_arrive_time": ""
            },
            {
                "quantity": 3,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO211021059"
                },
                "amazon_sale_date": "2021-12-23",
                "expect_arrive_time": "2021-10-03"
            },
            {
                "quantity": 10,
                "quantity_second": 0,
                "type": 3,
                "remark": {
                    "warehouse_name": "仓库1",
                    "sku": "SKUFAEB955",
                    "fnsku": "FND27C594"
                },
                "amazon_sale_date": "2021-12-20",
                "expect_arrive_time": ""
            },
            {
                "quantity": 2,
                "quantity_second": 0,
                "type": 3,
                "remark": {
                    "warehouse_name": "宝安第一仓",
                    "sku": "新版12",
                    "fnsku": ""
                },
                "amazon_sale_date": "2021-12-20",
                "expect_arrive_time": ""
            },
            {
                "quantity": 20,
                "quantity_second": 0,
                "type": 3,
                "remark": {
                    "warehouse_name": "仓库1",
                    "sku": "新版12",
                    "fnsku": ""
                },
                "amazon_sale_date": "2021-12-20",
                "expect_arrive_time": ""
            },
            {
                "quantity": 2,
                "quantity_second": 0,
                "type": 9,
                "remark": {
                    "overseas_order_no": "OWS211104002",
                    "warehouse_name": "仓库8",
                    "logistics_name": "",
                    "deliver_time": "2021-11-04 14:41:03"
                },
                "amazon_sale_date": "2021-12-14",
                "expect_arrive_time": ""
            },
            {
                "quantity": 10000,
                "quantity_second": 0,
                "type": 8,
                "remark": {
                    "warehouse_name": "仓库11",
                    "sku": "SKUFAEB955",
                    "fnsku": ""
                },
                "amazon_sale_date": "2021-12-10",
                "expect_arrive_time": ""
            },
            {
                "quantity": 9720,
                "quantity_second": 0,
                "type": 8,
                "remark": {
                    "warehouse_name": "仓库11",
                    "sku": "SKUFAEB955",
                    "fnsku": "FN477C98E"
                },
                "amazon_sale_date": "2021-12-10",
                "expect_arrive_time": ""
            },
            {
                "quantity": 21600,
                "quantity_second": 0,
                "type": 8,
                "remark": {
                    "warehouse_name": "仓库11",
                    "sku": "SKUFAEB955",
                    "fnsku": "FND27C594"
                },
                "amazon_sale_date": "2021-12-10",
                "expect_arrive_time": ""
            },
            {
                "quantity": 100,
                "quantity_second": 0,
                "type": 8,
                "remark": {
                    "warehouse_name": "西邮智仓 美国洛杉矶",
                    "sku": "SKUFAEB955",
                    "fnsku": ""
                },
                "amazon_sale_date": "2021-12-10",
                "expect_arrive_time": ""
            },
            {
                "quantity": 1,
                "quantity_second": 0,
                "type": 8,
                "remark": {
                    "warehouse_name": "哈哈哈",
                    "sku": "新版12",
                    "fnsku": ""
                },
                "amazon_sale_date": "2021-12-10",
                "expect_arrive_time": ""
            },
            {
                "quantity": 159300,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO210409003"
                },
                "amazon_sale_date": "2021-06-24",
                "expect_arrive_time": ""
            },
            {
                "quantity": 40010,
                "quantity_second": 0,
                "type": 5,
                "remark": {
                    "purchase_order_sn": "PO210413004"
                },
                "amazon_sale_date": "2021-06-24",
                "expect_arrive_time": ""
            }
        ]
    },
    "total": 0
}
```