# 查询FBA成本计价流水

>支持查询成本中心FBA成本计价流水  

注意：
<br>
1.由于亚马逊库存分类账生成数据后5天内会发生变更，领星在获取数据的5天内会继续获取数据并覆盖更新历史版本，因此接口获取的5天内数据是有可能发生变更的。
2.business_types传参为1 - 期初库存-FBA上月结存时，change_other_amount、change_logistics_amount、change_purchase_amount、change_quantity字段不返回。

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/cost/center/api/cost/stream ` | HTTPS | POST | 10 |


## 请求参数

| 参数名            | 说明                                                         | 必填 | 类型     | 示例                |
| ----------------- | ------------------------------------------------------------ | ---- | -------- | ------------------- |
| wh_names          | 仓库名                                                        |否|[array]|["8P-US-2024美国仓"]|
| shop_names        | 店铺名                                                        |否|[array]|["8P-US-2024"]|
| skus              | sku                                                          |否|[array]|["LX-0035","00000000001","SKU9988"]|
| mskus             | msku                                                         |否|[array]|["HOLDER001","Pink_Head_Rope_1"]|
| disposition_types | 库存属性：<br>1 可用在途<br>2 可用<br>3 次品                      |否|[array]|[1,2,3]|
| business_types    | 出入库类型：<br>1 期初库存-FBA上月结存<br>10 调拨入库-FBA补货入库<br>11 调拨入库-FBA途损补回<br>12 调拨入库-FBA超签入库<br>13 调拨入库-FBA超签入库（close后）<br>14 调拨入库-FBA补货入库（无发货单）<br>20 调拨入库-FBA调仓入库<br>35 调拨入库-FBA发货在途入库<br>25 盘点入库-FBA盘点入库<br>30 FBA退货-FBA无源单销售退货<br>31 FBA退货-FBA有源单销售退货<br>200 销售出库-FBA补发货销售<br>201 销售出库-FBA多渠道销售订单<br>202 销售出库-FBA亚马逊销售订单<br>205 其他出库-FBA补货出库<br>220 盘点出库-FBA盘点出库<br>15 调拨出库-FBA调仓出库<br>215 调拨出库-FBA移除<br>225 调拨出库-FBA发货在途出库<br>226 调拨出库-FBA发货途损<br>227 调拨出库-后补发货单在途出库<br>5 调整单- FBA对账差异入库调整<br>210 调整单-FBA对账差异出库调整<br>400 调整单-尾差调整<br>420 调整单-负库存数量调整<br>405 调整单-期初成本录入|是|[array]|[1]|
| query_type        | 日期查询类型：<br>01 库存动作日期【对应成本计价详情页面单据日期，即在FBA仓库内发生各项库存动作的日期】<br>02 结算日期【仅销售、退货场景会存在结算日期，其他库存动作结算日期为空】|是|[string]|01|
| start_date        | 起始日期，Y-m-d，不允许跨月                               |是|[string]|2023-06-01|
| end_date          | 结束日期，Y-m-d，不允许跨月                               |是|[string]|2023-06-30|
| business_numbers  | 业务编号                                                     |否|[array]|["FBA176M2LL9C","FCInboundRoutingService-FTW1-GYR1-81d2e262-7a9b-459b-8878-2708f6f3e789"]|
| origin_accounts   | 源头单据号                                                   |否|[array]|["SP230413004(无源单取最近签收成本)，业务编号：FBA16V31K78D，流水编号：20220903J0001X"]|
| offset            | 分页偏移量，默认0                                             |否|[int]|0|
| length            | 分页长度，默认200条                                            |否|[int]|200|


## 请求示例
```
{
    "wh_names": [
        "8P-US-2024美国仓"
    ],
    "shop_names": [
        "8P-US-2024"
    ],
    "skus": [
        "LX-0035",
        "00000000001",
        "SKU9988"
    ],
    "mskus": [
        "HOLDER001",
        "Pink_Head_Rope_1"
    ],
    "disposition_types": [1,2,3],
    "business_types": [
        1
    ],
    "query_type": "01",
    "start_date": "2023-06-01",
    "end_date": "2023-06-30",
    "business_numbers": [
        "FBA176M2LL9C",
        "FCInboundRoutingService-FTW1-GYR1-81d2e262-7a9b-459b-8878-2708f6f3e789"
    ],
    "origin_accounts": [
        "SP230413004(无源单取最近签收成本)，业务编号：FBA16V31K78D，流水编号：20220903J0001X"
    ],
    "offset": 0,
    "length": 200
}
```

## 返回结果
Json Object

| 参数名                                      | 说明             | 必填 | 类型      | 示例                 |
| ------------------------------------------- | ---------------- | ---- | --------- | -------------------- |
| code                                        | 状态码，0 成功     | 是   | [int]  |                      |
| msg                                         | 响应信息         | 是   | [string]  |                      |
| success                                     | 操作是否成功     | 是   | [boolean] |                      |
| traceId                                     | 请求链路Id       | 是   | [string]  |                      |
| data                                        | 汇总数据         | 是   | [Object]  |                      |
| data>>total                                 | 总记录条数       | 是   | [number]  |                      |
| data>>size                                  | 每个数据页大小   | 是   | [number]  |                      |
| data>>current                               | 当前所在数据页   | 是   | [number]  |                      |
| data>>records                               | 分页数据列表     | 是   | [array]   |                      |
| data>>records>>stream_date                  | 库存动作日期     | 是   | [string]  | 2022-12-01           |
| data>>records>>settlement_date              | 结算日期         | 否   | [string]  | 2022-12-01           |
| data>>records>>source_data_time             | 数据源更新时间   | 否   | [string]  | 2022-12-28 00:13:21  |
| data>>records>>unique_key                   | 主键             | 否   | [string]  | 主键                 |
| data>>records>>data_version                 | 计算版本号       | 是   | [string]  | 1672156800661        |
| data>>records>>business_number              | 业务编号         | 否   | [string]  | FBA15F9VZ512         |
| data>>records>>origin_account               | 源头单据号       | 否   | [string]  | SP220210001          |
| data>>records>>sku                          | sku              | 是   | [string]  | 测试sku001           |
| data>>records>>msku                         | msku             | 是   | [string]  | 1160U1713            |
| data>>records>>wh_name                      | 仓库名称          | 是   | [string]  | xxxxxxx         |
| data>>records>>shop_name                    | 店铺名称         | 否   | [string]  | xxxxxxx          |
| data>>records>>disposition_type             | 库存属性         | 是   | [string]  | 可用在途             |
| data>>records>>business_type                | 出入库类型编码   | 是   | [string]  | 1                    |
| data>>records>>business_type_desc           | 出入库类型名称   | 是   | [string]  | 期初库存-FBA上月结存 |
| data>>records>>cost_source                  | 成本取值来源     | 是   | [string]  | 上月结存             |
| data>>records>>change_quantity              | 变动数量         | 是   | [number]  | 0                    |
| data>>records>>change_purchase_unit_price   | 变动采购单价     | 是   | [string]  | 0                    |
| data>>records>>change_purchase_amount       | 变动采购成本     | 是   | [string]  | 0                    |
| data>>records>>change_logistics_unit_price  | 变动头程单价     | 是   | [string]  | 0                    |
| data>>records>>change_logistics_amount      | 变动头程成本     | 是   | [string]  | 0                    |
| data>>records>>change_other_unit_price      | 变动其他单价     | 是   | [string]  | 0                    |
| data>>records>>change_other_amount          | 变动其他成本     | 是   | [string]  | 0                    |
| data>>records>>balance_quantity             | 结存数量         | 是   | [number]  | 70                   |
| data>>records>>balance_purchase_unit_price  | 结存采购成本单价 | 是   | [string]  | 5.5815               |
| data>>records>>balance_purchase_amount      | 结存采购成本     | 是   | [string]  | 390.71               |
| data>>records>>balance_logistics_unit_price | 结存头程成本单价 | 是   | [string]  | 20.0000              |
| data>>records>>balance_logistics_amount     | 结存头程成本     | 是   | [string]  | 1400.00              |
| data>>records>>balance_other_unit_price     | 结存其他成本单价 | 是   | [string]  | 2.4712               |
| data>>records>>balance_other_amount         | 结存其他成本     | 是   | [string]  | 172.98               |
| data>>records>>sales_platform               | 销售平台         | 否   | [string]  |                      |
| data>>records>>reason                       | 盘点原因         | 否   | [string]  |&nbsp;               |

## 返回成功示例
```
{
	"code": 0,
	"data": {
		"current": 0,
		"records": [
			{
				"balance_logistics_amount": "1.11",
				"balance_logistics_unit_price": "40.2469",
				"balance_other_amount": "1.11",
				"balance_other_unit_price": "40.2469",
				"balance_purchase_amount": "1.11",
				"balance_purchase_unit_price": "40.2469",
				"balance_quantity": 297,
				"business_number": "pock-Executor-BHX1-LCY2-1647210652366-627a54b1-37a9-4fbd-9e46-ffb58a3be20c",
				"business_type": "1",
				"business_type_desc": "期初库存-FBA上月结存",
				"change_logistics_amount": "1.11",
				"change_logistics_unit_price": "40.2469",
				"change_other_amount": "1.11",
				"change_other_unit_price": "40.2469",
				"change_purchase_amount": "1.11",
				"change_purchase_unit_price": "40.2469",
				"change_quantity": 297,
				"cost_source": "上月结存",
				"data_version": "1672053502119",
				"disposition_type": "可用",
				"msku": "1160U1152-A",
				"origin_account": "FBA15FN6XK4L",
				"reason": "原因",
				"sales_platform": "销售平台A",
				"settlement_date": "结算日期",
				"shop_name": "JHL Official-02",
				"sku": "sku003",
				"source_data_time": "2022-12-26 19:19:28",
				"streamDate": "2022-06-01",
				"unique_key": "null",
				"wh_name": "JHL Official-02"
			}
		],
		"size": 5,
		"total": 1
	},
	"msg": "操作成功",
	"success": true,
	"traceId": "320aba4f-6af1-4cac-aa0c-6b27bc77bae1.1673003238583"
}
```

## 返回失败示例
```
{
    "code": 1,
    "msg": "操作失败",
    "data": null,
    "traceId": "b2532fc7-9c1b-4b08-8d30-301b31b70562.1663226369188",
    "success": false
}
```
