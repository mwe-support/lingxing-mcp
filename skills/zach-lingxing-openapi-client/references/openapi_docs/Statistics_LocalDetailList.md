# 库存报表-本地仓-历史报表-明细
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sys_wid|系统仓库id，多个用英文逗号分隔|否|[int]|1|
|start_date|开始时间，格式：Y-m-d|是|[string]|2022-01-01|
|end_date|结束时间，格式：Y-m-d|是|[string]|2022-08-05|
|offset|分页偏移量，默认0|是|[int]|0|
|length|分页长度，默认15|是|[int]|15|

## 请求示例
```
{
    "start_date": "2022-01-01",
    "end_date": "2022-08-05",
    "offset": 0,
    "length": 15,
    "sys_wid": "1"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码， 0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]| |
|data>>spu|SPU|是|[string]|1|
|data>>spu_name|款名|是|[string]|手机|
|data>>sku|SKU|是|[string]|SSS|
|data>>product_name|品名|是|[string]|商品名|
|data>>fnsku|FNSKU|是|[string]|XASSV21321|
|data>>sku_attribute|属性|是|[string]|红色|
|data>>seller_name|店铺|是|[string]|店铺231|
|data>>sys_wid|仓库id|是|[int]|32|
|data>>ware_house_name|仓库名称|是|[string]|仓库1|
|data>>category1|一级分类|是|[string]|手机1|
|data>>category2|二级分类|是|[string]|手机2|
|data>>category3|三级分类|是|[string]|手机3|
|data>>brand|品牌|是|[string]|某为|
|data>>attribute_text|库存属性|是|[string]|全部|
|data>>product_type|产品类型|是|[string]|辅料|
|data>>day_early_count|期初库存（数量）|是|[number]|2450424|
|data>>day_early_cost|期初库存（成本）|是|[number]|723024419.45|
|data>>purchase_in_count|采购入库（数量）|是|[number]|30|
|data>>purchase_in_cost|采购入库（成本）|是|[number]|22.50|
|data>>allocation_in_count|调拨入库（数量）|是|[number]| |
|data>>allocation_in_cost|调拨入库（成本）|是|[number]|0.00|
|data>>return_goods_in_count|退货入库（数量）|是|[number]|2|
|data>>return_goods_in_cost|退货入库（成本）|是|[number]|0.00|
|data>>other_in_count|其他入库（数量）|是|[number]|1000|
|data>>other_in_cost|其他入库（成本）|是|[number]|0.00|
|data>>inventory_surplus_in_count|盘盈入库（数量）|是|[number]|2|
|data>>inventory_surplus_in_cost|盘盈入库（成本）|是|[number]|0.00|
|data>>adjustment_count|库存调整（数量）|是|[number]| |
|data>>adjustment_cost|库存调整（成本）|是|[number]|0.00|
|data>>fba_out_count|FBA出库（数量）|是|[number]|2|
|data>>fba_out_cost|FBA出库（成本）|是|[number]|0.00|
|data>>fbm_out_count|FBM出库（数量）|是|[number]|3|
|data>>fbm_out_cost|FBM出库（成本）|是|[number]|0.00|
|data>>allocation_out_count|调拨出库（数量）|是|[number]|2|
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
|data>>rotation_rate_count|库存周转率（数量）|是|[number]| |
|data>>rotation_rate_cost|库存周转率（成本）|是|[number]|0.0000|
|data>>rotation_day_count|库存周转天数（数量）|是|[number]| |
|data>>rotation_day_cost|库存周转天数（成本）|是|[number]| |
|data>>sales_ratio_count|存销比（数量）|是|[number]| |
|data>>sales_ratio_cost|存销比（成本）|是|[number]| |
|data>>cost_change_cost|成本补录（成本）|是|[number]|0.00|
|data>>sales_rate|动销率|是|[number]| |
|total|总数|是|[int]|1|


## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details":[],
    "request_id": "BDF6F403-1998-7E7F-62C2-369C15FEE14D",
    "response_time": "2022-12-21 18:44:54"
    "data": [{
        "spu_name": "",
        "sku": "1544220",
        "product_name": "kmkm",
        "fnsku": "",
        "sku_attribute": "",
        "seller_name": "",
        "category1": "",
        "category2": "",
        "category3": "",
        "brand": "",
        "attribute_text": "可售",
        "product_type": "普通商品",
        "sys_wid": "3879",
        "ware_house_name": "dabing-test",
        "day_early_count": 1,
        "day_early_cost": "",
        "purchase_in_count": 0,
        "purchase_in_cost": "",
        "allocation_in_count": 0,
        "allocation_in_cost": "",
        "return_goods_in_count": 0,
        "return_goods_in_cost": "",
        "other_in_count": 0,
        "other_in_cost": "",
        "inventory_surplus_in_count": 0,
        "inventory_surplus_in_cost": "",
        "adjustment_count": 0,
        "adjustment_cost": "",
        "fba_out_count": 0,
        "fba_out_cost": "",
        "fbm_out_count": 0,
        "fbm_out_cost": "",
        "allocation_out_count": 0,
        "allocation_out_cost": "",
        "purchase_return_count": 0,
        "purchase_return_cost": "",
        "other_out_count": 0,
        "other_out_cost": "",
        "inventory_deficit_out_count": 0,
        "inventory_deficit_out_cost": "",
        "wfs_out_count": 0,
        "wfs_out_cost": "",
        "allocation_in_transit_count": 0,
        "allocation_in_transit_cost": "",
        "day_end_count": 1,
        "day_end_cost": "",
        "rotation_rate_count": "0.0000",
        "rotation_rate_cost": "",
        "rotation_day_count": 0,
        "rotation_day_cost": "",
        "sales_ratio_count": 0,
        "sales_ratio_cost": "",
        "cost_change_cost": 0
    }],
    "total": 1
}
```

