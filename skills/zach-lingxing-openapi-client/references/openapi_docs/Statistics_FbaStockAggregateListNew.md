# 库存报表-FBA-新版-汇总
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/cost/center/openApi/fba/gather/query` | HTTPS | POST | 10 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|是|[int]|0|
|length|分页长度，默认为15|是|[int]|15|
|seller_id|亚马逊店铺id ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|是|[array]|["AQ7DSXSNF6NDP","AJGRSY3EK14NJ"]|
|start_date|统计起始月份，格式：Y-m|是|[string]|2022-01|
|end_date|统计结束月份，格式：Y-m|是|[string]|2024-08|

## 请求示例
```
{
    "offset": 0,
    "length": 15,
    "seller_id": [
        "AQ7DSXSNF6NDP",
        "AJGRSY3EK14NJ"
    ],
    "start_date": "2022-01",
    "end_date": "2024-08"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|msg|提示信息|是|[string]|操作成功|
|traceId|请求链路id|是|[string]|c3e060d3-aeed-4ef5-abe8-22258b1e2836.1673410807850|
|data|响应数据|是|[object]||
|data>>current|当前所在页|是|[int]|1|
|data>>size|单页数据行数|是|[int]|1|
|data>>total|总数|是|[int]|222|
|data>>end_date|统计结束月份，格式：Y-m-d|是|[string]|2022-08-31|
|data>>start_date|统计开始月份，格式：Y-m-d|是|[string]|2022-08-31|
|data>>amount_type|计价类型：0 成本计价，1 固定值计价|是|[int]|1|
|data>>day_interval|时间区间相隔天数|是|[int]|31|
|data>>row_data| |是|[array]||
|data>>row_data>>adjustments_count|成本调整-数量|是|[int]||
|data>>row_data>>adjustments_logistic_amount|成本调整-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>adjustments_other_amount|成本调整-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>adjustments_total_amount|成本调整-总成本|是|[number]|0.00|
|data>>row_data>>asin|asin|是|[string]|B07NL8PKF2|
|data>>row_data>>bid|品牌id|是|[int]||
|data>>row_data>>brand_name|品牌名称|是|[string]|品牌名称1|
|data>>row_data>>cid|分类id|是|[int]|12|
|data>>row_data>>country_code|国家编码|是|[string]|US|
|data>>row_data>>customer_returns_count|买家退货-数量|是|[int]||
|data>>row_data>>customer_returns_logistic_amount|买家退货-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>customer_returns_other_amount|买家退货-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>customer_returns_total_amount|买家退货-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>damaged_count|残损-数量|是|[int]||
|data>>row_data>>damaged_logistic_amount|残损-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>damaged_other_amount|残损-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>damaged_total_amount|残损-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>difference_count|库存差异-数量|是|[int]||
|data>>row_data>>difference_logistic_amount|库存差异-物流成本<br>(精度：2位小数)|是|[number]|4.55|
|data>>row_data>>difference_other_amount|库存差异-其他成本<br>(精度：2位小数)|是|[number]|1.33|
|data>>row_data>>difference_total_amount|库存差异-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposed_count|丢弃-数量|是|[int]||
|data>>row_data>>disposed_logistic_amount|丢弃-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposed_other_amount|丢弃-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposed_total_amount|丢弃-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposition|库存属性：<br>sellable 可售<br>unsellable 不可售<br> all 全部|是|[string]|all|
|data>>row_data>>end_count|期末库存-数量|是|[int]|1|
|data>>row_data>>end_logistic_amount|期末库存-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_on_way_count|期末在途-数量|是|[int]||
|data>>row_data>>end_on_way_logistic_amount|期末在途-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_on_way_other_amount|期末在途-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_on_way_total_amount|期末在途-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_other_amount|期末库存-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_total_amount|期末库存-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>fnsku|fnsku|是|[string]|X0023DBLEH|
|data>>row_data>>found_count|已找到-数量|是|[int]||
|data>>row_data>>found_logistic_amount|已找到-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>found_other_amount|已找到-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>found_total_amount|已找到-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>inventory_turnover_days|库存周转天数<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>inventory_turnover_rate|库存周转率<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>moving_pin_rate|动销率<br>(精度：2位小数)|是|[number]||
|data>>row_data>>local_name|本地产品名称|是|[string]|本地产品名称12|
|data>>row_data>>local_sku|本地产品Sku|是|[string]|7501XH1856|
|data>>row_data>>lost_count|丢失-数量|是|[int]||
|data>>row_data>>lost_logistic_amount|丢失-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>lost_other_amount|丢失-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>lost_total_amount|丢失-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>mid|站点id|是|[int]|4|
|data>>row_data>>msku|msku|是|[string]|7501XH1856|
|data>>row_data>>other_events_count|其他-数量|是|[int]||
|data>>row_data>>other_events_logistic_amount|其他-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>other_events_other_amount|其他-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>other_events_total_amount|其他-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>parent_asin|父Asin|是|[string]|B07NL8PKF2|
|data>>row_data>>parent_node|是否父节点|是|[string]|true|
|data>>row_data>>product_category_name|产品分类名|是|[string]|产品分类名1|
|data>>row_data>>product_id|产品id|是|[int]|2|
|data>>row_data>>receipts_count|货物补货-数量|是|[int]||
|data>>row_data>>receipts_logistic_amount|货物补货-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>receipts_other_amount|货物补货-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>receipts_total_amount|货物补货-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>shipments_count|订单发货-数量|是|[int]||
|data>>row_data>>shipments_logistic_amount|订单发货-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>shipments_other_amount|订单发货-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>shipments_total_amount|订单发货-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>sid|店铺id|是|[int]|3|
|data>>row_data>>seller_id|亚马逊店铺id|是|[string]|xxxxxxxxxxxxxxxx|
|data>>row_data>>start_count|期初库存-数量|是|[int]||
|data>>row_data>>start_logistic_amount|期初库存-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>start_other_amount|期初库存-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>start_total_amount|期初库存-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>stock_to_use_rate|存销比<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>valuation_method|计价方法:<br>1-先进先出 <br>2-移动加权 <br>3-月末加权|是|[int]|1|
|data>>row_data>>vendor_returns_count|库存移除-数量|是|[int]||
|data>>row_data>>vendor_returns_logistic_amount|库存移除-物流成本|是|[number]|0.00|
|data>>row_data>>vendor_returns_other_amount|库存移除-其他成本|是|[number]|0.00|
|data>>row_data>>vendor_returns_total_amount|库存移除-总成本|是|[number]|0.00|
|data>>row_data>>whse_transfers_logistic_amount|库房转运-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>whse_transfers_other_amount|库房转运-其他成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>whse_transfers_total_amount|库房转运-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>whse_transfers_count|库房转运-数量|是|[int]||
|data>>row_data>>wid|系统仓库id|是|[int]|123|
|data>>row_data>>ware_house_name|仓库名称|是|[string]|仓库名称213|
|data>>row_data>>child_data|返回字段与上级row_data一致|是|[array]|&nbsp;|

## 返回成功示例
```
{
    "code": 0,
    "msg": "操作成功",
    "traceId": "c3e060d3-aeed-4ef5-abe8-22258b1e2836.1673410807850",
    "data": {
        "row_data": [
            {
                "sid": 6,
                "wid": 19,
                "disposition": "all",
                "start_count": 4558,
                "start_other_amount": "0.00",
                "start_logistic_amount": "0.00",
                "shipments_count": -441,
                "shipments_other_amount": "0.00",
                "shipments_logistic_amount": "0.00",
                "whse_transfers_count": 162,
                "whse_transfers_other_amount": "0.00",
                "whse_transfers_logistic_amount": "0.00",
                "disposed_count": 0,
                "disposed_other_amount": "0.00",
                "disposed_logistic_amount": "0.00",
                "found_count": 1,
                "found_other_amount": "0.00",
                "found_logistic_amount": "0.00",
                "lost_count": -3,
                "lost_other_amount": "0.00",
                "lost_logistic_amount": "0.00",
                "other_events_count": 0,
                "other_events_other_amount": "0.00",
                "other_events_logistic_amount": "0.00",
                "receipts_count": 297,
                "receipts_other_amount": "0.00",
                "receipts_logistic_amount": "0.00",
                "customer_returns_count": 26,
                "customer_returns_other_amount": "0.00",
                "customer_returns_logistic_amount": "0.00",
                "vendor_returns_count": -16,
                "vendor_returns_other_amount": "0.00",
                "vendor_returns_logistic_amount": "0.00",
                "difference_count": -2,
                "difference_other_amount": "0.00",
                "difference_logistic_amount": "0.00",
                "end_count": 4580,
                "end_other_amount": "0.00",
                "end_logistic_amount": "0.00",
                "damaged_count": -2,
                "damaged_other_amount": "0.00",
                "damaged_logistic_amount": "0.00",
                "partition_index": null,
                "end_on_way_count": 0,
                "end_on_way_other_amount": "0.00",
                "end_on_way_logistic_amount": "0.00",
                "category_count": null,
                "parent_node": true,
                "child_data": [
                    {
                        "sid": 6,
                        "wid": 19,
                        "disposition": "sellable",
                        "start_count": 4519,
                        "start_other_amount": "0.00",
                        "start_logistic_amount": "0.00",
                        "shipments_count": -441,
                        "shipments_other_amount": "0.00",
                        "shipments_logistic_amount": "0.00",
                        "whse_transfers_count": 163,
                        "whse_transfers_other_amount": "0.00",
                        "whse_transfers_logistic_amount": "0.00",
                        "disposed_count": 0,
                        "disposed_other_amount": "0.00",
                        "disposed_logistic_amount": "0.00",
                        "found_count": 1,
                        "found_other_amount": "0.00",
                        "found_logistic_amount": "0.00",
                        "lost_count": -3,
                        "lost_other_amount": "0.00",
                        "lost_logistic_amount": "0.00",
                        "other_events_count": 0,
                        "other_events_other_amount": "0.00",
                        "other_events_logistic_amount": "0.00",
                        "receipts_count": 297,
                        "receipts_other_amount": "0.00",
                        "receipts_logistic_amount": "0.00",
                        "customer_returns_count": 9,
                        "customer_returns_other_amount": "0.00",
                        "customer_returns_logistic_amount": "0.00",
                        "vendor_returns_count": 0,
                        "vendor_returns_other_amount": "0.00",
                        "vendor_returns_logistic_amount": "0.00",
                        "difference_count": -2,
                        "difference_other_amount": "0.00",
                        "difference_logistic_amount": "0.00",
                        "end_count": 4541,
                        "end_other_amount": "0.00",
                        "end_logistic_amount": "0.00",
                        "damaged_count": -2,
                        "damaged_other_amount": "0.00",
                        "damaged_logistic_amount": "0.00",
                        "partition_index": null,
                        "end_on_way_count": 0,
                        "end_on_way_other_amount": "0.00",
                        "end_on_way_logistic_amount": "0.00",
                        "category_count": null,
                        "parent_node": false,
                        "child_data": [],
                        "inventory_turnover_rate": "0.10",
                        "inventory_turnover_days": "310.00",
                        "moving_pin_rate": null,
                        "start_total_amount": "0.00",
                        "shipments_total_amount": "0.00",
                        "whse_transfers_total_amount": "0.00",
                        "disposed_total_amount": "0.00",
                        "found_total_amount": "0.00",
                        "lost_total_amount": "0.00",
                        "other_events_total_amount": "0.00",
                        "receipts_total_amount": "0.00",
                        "customer_returns_total_amount": "0.00",
                        "vendor_returns_total_amount": "0.00",
                        "difference_total_amount": "0.00",
                        "end_total_amount": "0.00",
                        "damaged_total_amount": "0.00",
                        "end_on_way_total_amount": "0.00",
                        "stock_to_use_rate": "10.30",
                        "adjustments_count": 0,
                        "adjustments_total_amount": "0.00",
                        "adjustments_logistic_amount": "0.00",
                        "adjustments_other_amount": "0.00",
                        "ware_house_name": "_xinghai_direct-1美国仓"
                    }
                ],
                "inventory_turnover_rate": "0.10",
                "inventory_turnover_days": "310.00",
                "moving_pin_rate": null,
                "start_total_amount": "0.00",
                "shipments_total_amount": "0.00",
                "whse_transfers_total_amount": "0.00",
                "disposed_total_amount": "0.00",
                "found_total_amount": "0.00",
                "lost_total_amount": "0.00",
                "other_events_total_amount": "0.00",
                "receipts_total_amount": "0.00",
                "customer_returns_total_amount": "0.00",
                "vendor_returns_total_amount": "0.00",
                "difference_total_amount": "0.00",
                "end_total_amount": "0.00",
                "damaged_total_amount": "0.00",
                "end_on_way_total_amount": "0.00",
                "stock_to_use_rate": "10.39",
                "adjustments_count": 0,
                "adjustments_total_amount": "0.00",
                "adjustments_logistic_amount": "0.00",
                "adjustments_other_amount": "0.00",
                "ware_house_name": "_xinghai_direct-1美国仓"
            }
        ],
        "start_date": "2022-01-01",
        "end_date": "2022-01-31",
        "day_interval": 31,
        "total": 1,
        "size": 200,
        "current": 1,
        "amount_type": 0
    }
}
```