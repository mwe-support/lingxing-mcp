# 库存报表-海外仓-历史报表-明细
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sys_wid|系统仓库id，多个用英文逗号分隔|否|[int]|9|
|start_date|开始时间，格式：Y-m-d|是|[string]|2022-01-01|
|end_date|结束时间，格式：Y-m-d|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|是|[int]|0|
|length|每页条数，默认15|是|[int]|15|

## 请求示例
```
{
    "offset": 0,
    "length": 15,
    "start_date": "2022-01-01",
    "end_date": "2024-08-05",
    "sys_wid": "9"
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
|data|返回数据|是|[array]| |
|data>>sku|SKU|是|[string]|SKU-1|
|data>>api_sku|第三方SKU|是|[string]|ASVSDSA-1|
|data>>product_name|品名|是|[string]|手机|
|data>>fnsku|FNSKU|是|[string]|SDSADSV123|
|data>>seller_name|店铺|是|[string]|店铺1|
|data>>sys_wid|仓库id|是|[int]|23|
|data>>ware_house_name|仓库名称|是|[string]|仓库1|
|data>>category1|一级分类|是|[string]|分类1|
|data>>category2|二级分类|是|[string]|分类2|
|data>>category3|三级分类|是|[string]|分类3|
|data>>brand|品牌|是|[string]|某果|
|data>>attribute_text|库存属性|是|[string]|可售|
|data>>product_type|产品类型|是|[string]|辅料|
|data>>day_early_count|期初库存（数量）|是|[number]|2450424|
|data>>day_early_cost|期初库存（成本）|是|[number]|723024419.45|
|data>>api_day_early_count|第三方期初库存（数量）第三方只有数量|是|[number]| |
|data>>api_day_end_count|第三方期末库存（数量）第三方只有数量|是|[number]| |
|data>>purchase_in_count|采购入库（数量）|是|[number]|30|
|data>>purchase_in_cost|采购入库（成本）|是|[number]|22.50|
|data>>allocation_in_count|调拨入库（数量）|是|[number]| |
|data>>allocation_in_cost|调拨入库（成本）|是|[number]|0.00|
|data>>return_goods_in_count|退货入库（数量）|是|[number]| |
|data>>return_goods_in_cost|退货入库（成本）|是|[number]|0.00|
|data>>other_in_count|其他入库（数量）|是|[number]|1000|
|data>>other_in_cost|其他入库（成本）|是|[number]|0.00|
|data>>inventory_surplus_in_count|盘盈入库（数量）|是|[number]| |
|data>>inventory_surplus_in_cost|盘盈入库（成本）|是|[number]|0.00|
|data>>adjustment_count|库存调整（数量）|是|[number]| |
|data>>adjustment_cost|库存调整（成本）|是|[number]|0.00|
|data>>fba_out_count|FBA出库（数量）|是|[number]| |
|data>>fba_out_cost|FBA出库（成本）|是|[number]|0.00|
|data>>fbm_out_count|FBM出库（数量）|是|[number]| |
|data>>fbm_out_cost|FBM出库（成本）|是|[number]|0.00|
|data>>allocation_out_count|调拨出库（数量）|是|[number]| |
|data>>allocation_out_cost|调拨出库（成本）|是|[number]|0.00|
|data>>purchase_return_count|采购退货（数量）|是|[number]| |
|data>>purchase_return_cost|采购退货（成本）|是|[number]|0.00|
|data>>other_out_count|其他出库（数量）|是|[number]| |
|data>>other_out_cost|其他出库（成本）|是|[number]|0.00|
|data>>inventory_deficit_out_count|盘亏出库（数量）|是|[number]| |
|data>>inventory_deficit_out_cost|盘亏出库（成本）|是|[number]|0.00|
|data>>wfs_out_count|WFS出库（数量）|是|[number]| |
|data>>wfs_out_cost|WFS出库（成本）|是|[number]|0.00|
|data>>allocation_in_transit_count|期末在途（数量）|是|[number]|1|
|data>>allocation_in_transit_cost|期末在途（成本）|是|[number]|13.00|
|data>>day_end_count|期末库存（数量）|是|[number]|2451454|
|data>>day_end_cost|期末库存（成本）|是|[number]|723024441.95|
|data>>stocking_in_transit_count|期末在途（数量）|是|[number]| |
|data>>stocking_in_transit_cost|期末在途（成本）|是|[number]|0.00|
|data>>rotation_rate_count|库存周转率（数量）|是|[number]|0.0000|
|data>>rotation_rate_cost|库存周转率（成本）|是|[number]|0.0000|
|data>>rotation_day_count|库存周转天数（数量）|是|[number]| |
|data>>rotation_day_cost|库存周转天数（成本）|是|[number]| |
|data>>sales_ratio_count|存销比（数量）|是|[number]| |
|data>>sales_ratio_cost|存销比（成本）|是|[number]| |
|data>>cost_change_cost|成本补录（成本）|是|[number]|0.00|
|data>>sales_rate|动销率|是|[number]| |
|total|记录行数|是|[int]|510|


## 返回成功示例

```
{
    "code": 0,
    "message": "success",    
    "error_details": [],
    "request_id": "557581a380f4447b959d4adf777dfa09",
    "response_time": "2022-12-21 18:44:54"
    "request_id": "A42097F7-3400-BD9F-2A11-FED53ADD955A",
    "data": [{
        "id": 4387598,
        "product_id": 8,
        "ware_house_name": "西邮智仓 美国洛杉矶",
        "date_locale": "2022-10-15",
        "attribute": 1,
        "purchase_in_count": "0",
        "allocation_in_count": "0",
        "return_goods_in_count": "0",
        "pickout_in_count": "0",
        "other_in_count": "0",
        "adjustment_count": "0",
        "fba_out_count": "0",
        "fbm_out_count": "0",
        "allocation_out_count": "0",
        "purchase_return_count": "0",
        "other_out_count": "0",
        "cost_change_count": "0",
        "fnsku": "",
        "api_sku": "",
        "sku": "123713811-11",
        "product_name": "[演示数据]USB 壁式充电器 2.1A/5V 双端口 立方体电源适配器充电器插头充电块替换件",
        "is_combo": 0,
        "is_aux": 0,
        "api_day_early_count": 0,
        "api_day_end_count": 0,
        "uk": "39-8-0--1",
        "seller_id": "0",
        "inventory_surplus_in": "0",
        "wfs_out_count": "0",
        "bid": 1,
        "cid": 3,
        "different_count": -100,
        "global_tags": "",
        "seller_name": "",
        "brand": "",
        "category": "缺失的品牌\\缺失的品牌",
        "category1": "缺失的品牌",
        "category2": "缺失的品牌",
        "category3": "",
        "attribute_text": "可售",
        "day_early_count": 100,
        "day_end_count": 100,
        "product_type": "普通商品",
        "sys_wid": 39,
        "day_early_cost": 0,
        "purchase_in_cost": 0,
        "allocation_in_cost": 0,
        "other_in_cost": 0,
        "inventory_surplus_in_cost": 0,
        "return_goods_in_cost": 0,
        "pickout_in_cost": 0,
        "adjustment_cost": 0,
        "fba_out_cost": 0,
        "fbm_out_cost": 0,
        "other_out_cost": 0,
        "allocation_out_cost": 0,
        "purchase_return_cost": 0,
        "inventory_deficit_out_cost": 0,
        "cost_change_cost": 0,
        "wfs_out_cost": 0,
        "day_end_cost": 0,
        "rotation_rate_cost": 0,
        "rotation_day_cost": 0,
        "stocking_in_transit_cost": 0,
        "nventory_surplus_in_count": "0",
        "inventory_deficit_out_count": "0",
        "rotation_rate_count": "0.0000",
        "rotation_day_count": "0.00",
        "stocking_in_transit_counst": 0,
        "product_count": 0
    }],
    "total": 1
}
```
