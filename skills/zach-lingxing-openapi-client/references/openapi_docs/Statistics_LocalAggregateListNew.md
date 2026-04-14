# 库存报表-本地仓-新报表-汇总
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/inventory/center/openapi/storageReport/local/aggregate/list` | HTTPS | POST | 3 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|start_date|开始时间，格式：Y-m-d|是|[string]|2020-01-01|
|end_date|结束时间，格式：Y-m-d|是|[string]|2024-08-05|
|sys_wid|系统仓库id，多个用英文逗号分隔|否|[int]|1694,1688|

## 请求示例
```
{
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "sys_wid": "1694,1688"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]||
|data>>sys_wid|系统仓库id|是|[int]|1|
|data>>ware_house_name|仓库名称|是|[string]|仓库1|
|data>>product_count|商品数量|是|[number]|5935|
|data>>allocation_in_cost|调拨入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>allocation_in_count|调拨入库-数量|是|[number]| |
|data>>allocation_in_transit_cost|期末在途-成本（精度：2位小数点）|是|[number]|0.00|
|data>>allocation_in_transit_count|期末在途-数量|是|[number]| |
|data>>allocation_out_cost|调拨出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>allocation_out_count|调拨出库-数量|是|[number]| |
|data>>change_of_standard_in_cost|换标入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>change_of_standard_in_count|换标入库-数量|是|[number]| |
|data>>change_of_standard_out_cost|换标出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>change_of_standard_out_count|换标出库-数量|是|[number]| |
|data>>cost_adjustment|成本调整（精度：2位小数点）|是|[number]|0.00|
|data>>day_early_cost|期初库存-成本（精度：2位小数点）|是|[number]|0.00|
|data>>day_early_count|期初库存-数量|是|[number]| |
|data>>day_end_cost|期末库存-成本（精度：2位小数点）|是|[number]|0.00|
|data>>day_end_count|期末库存-数量|是|[number]| |
|data>>fba_out_cost|fba出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>fba_out_count|fba出库-数量|是|[number]| |
|data>>fbm_out_cost|fbm出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>fbm_out_count|fbm出库-数量|是|[number]| |
|data>>inventory_deficit_out_cost|盘亏出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>inventory_deficit_out_count|盘亏出库-数量|是|[number]| |
|data>>inventory_surplus_in_cost|盘盈入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>inventory_surplus_in_count|盘盈入库-数量|是|[number]| |
|data>>other_in_cost|其他入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>other_in_count|其他入库-数量|是|[number]| |
|data>>other_out_cost|其他出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>other_out_count|其他出库-数量|是|[number]| |
|data>>outsourcing_in_cost|委外入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>outsourcing_in_count|委外入库-数量|是|[number]| |
|data>>outsourcing_out_cost|委外出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>outsourcing_out_count|委外出库-数量|是|[number]| |
|data>>processing_in_cost|加工入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>processing_in_count|加工入库-数量|是|[number]| |
|data>>processing_out_cost|加工出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>processing_out_count|加工出库-数量|是|[number]| |
|data>>purchase_in_cost|采购入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>purchase_in_count|采购入库-数量|是|[number]| |
|data>>purchase_return_cost|退货出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>purchase_return_count|退货出库-数量|是|[number]| |
|data>>remove_in_cost|移除入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>remove_in_count|移除入库-数量|是|[number]| |
|data>>return_goods_in_cost|退货入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>return_goods_in_count|退货入库-数量|是|[number]| |
|data>>split_in_cost|拆分入库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>split_in_count|拆分入库-数量|是|[number]| |
|data>>split_out_cost|拆分出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>split_out_count|拆分出库-数量|是|[number]| |
|data>>wfs_out_cost|WFS出库-成本（精度：2位小数点）|是|[number]|0.00|
|data>>wfs_out_count|WFS出库-数量|是|[number]| |
|data>>gifts_in_cost|赠品入库-成本（精度：2位小数点）|是|[string]|0.00|
|data>>gifts_in_count|赠品入库-数量|是|[number]|0|
|data>>rotation_day_cost|周转天数-成本（精度：2位小数点）|是|[number]|0.00|
|data>>rotation_day_count|周转天数-数量（精度：2位小数点）|是|[number]|0.00|
|data>>rotation_rate_cost|周转率-成本（精度：4位小数点）|是|[number]|0.0000|
|data>>rotation_rate_count|周转率-数量（精度：4位小数点）|是|[number]|0.0000|
|data>>sales_ratio_cost|存销比-成本（精度：4位小数点）|是|[number]|0.0000|
|data>>sales_ratio_count|存销比-数量（精度：4位小数点）|是|[number]|0.0000|
|data>>sales_rate|动销率（精度：4位小数点）|是|[number]|0.0000|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details":[],
    "request_id": "BDF6F403-1998-7E7F-62C2-369C15FEE14D",
    "response_time": "2022-12-21 18:44:54"
    "data": [{
        "other_in_count": 0,
        "purchase_in_count": 0,
        "allocation_in_count": 0,
        "outsourcing_in_count": 0,
        "inventory_surplus_in_count": 0,
        "change_of_standard_in_count": 0,
        "processing_in_count": 0,
        "split_in_count": 0,
        "return_goods_in_count": 0,
        "remove_in_count": 0,
        "outsourcing_out_count": 0,
        "inventory_deficit_out_count": 0,
        "change_of_standard_out_count": 0,
        "processing_out_count": 0,
        "split_out_count": 0,
        "fba_out_count": 0,
        "fbm_out_count": 0,
        "purchase_return_count": 0,
        "allocation_out_count": 0,
        "other_out_count": 0,
        "wfs_out_count": 0,
        "gifts_in_cost": 0,
        "gifts_in_count": 0,
        "day_early_count": 119,
        "day_end_count": 119,
        "allocation_in_transit_count": 0,
        "other_in_cost": "0.00",
        "purchase_in_cost": "0.00",
        "allocation_in_cost": "0.00",
        "outsourcing_in_cost": "0.00",
        "inventory_surplus_in_cost": "0.00",
        "change_of_standard_in_cost": "0.00",
        "processing_in_cost": "0.00",
        "split_in_cost": "0.00",
        "return_goods_in_cost": "0.00",
        "remove_in_cost": "0.00",
        "outsourcing_out_cost": "0.00",
        "inventory_deficit_out_cost": "0.00",
        "change_of_standard_out_cost": "0.00",
        "processing_out_cost": "0.00",
        "split_out_cost": "0.00",
        "fba_out_cost": "0.00",
        "fbm_out_cost": "0.00",
        "purchase_return_cost": "0.00",
        "allocation_out_cost": "0.00",
        "other_out_cost": "0.00",
        "wfs_out_cost": "0.00",
        "day_early_cost": "0.00",
        "day_end_cost": "0.00",
        "allocation_in_transit_cost": "0.00",
        "cost_adjustment": "0.00",
        "rotation_day_count": "0.00",
        "rotation_rate_count": "0.0000",
        "sales_ratio_count": "0.0000",
        "rotation_day_cost": "0.00",
        "rotation_rate_cost": "0.0000",
        "sales_ratio_cost": "0.0000",
        "sys_wid": 4386,
        "ware_house_name": "1213",
        "product_count": 3,
        "sales_rate": "0.0000"
    }]
}
```
