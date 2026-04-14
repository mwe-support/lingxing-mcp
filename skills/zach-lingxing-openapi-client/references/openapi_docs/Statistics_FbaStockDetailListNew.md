# 库存报表-FBA-新版-明细
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/cost/center/openApi/fba/detail/query` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|是|[int]|0|
|length|分页长度，默认15，最大2100|是|[int]|15|
|start_date|开始日期，格式：Y-m|是|[string]|2020-01|
|end_date|结束日期，格式：Y-m|是|[string]|2024-08|
|seller_id|亚马逊店铺id ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|是|[array]|["AQ7DSXSNF6NDP","AJGRSY3EK14NJ"]|

## 请求示例
```
{
    "offset": 0,
    "length": 15,
    "start_date": "2020-01",
    "end_date": "2024-08",
    "seller_id": [
        "AQ7DSXSNF6NDP",
        "AJGRSY3EK14NJ"
    ]
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|msg|提示消息|是|[string]|操作成功|
|traceId|请求链路id|是|[string]|7248e68e-e304-46b7-8ee7-4094dd57b61c.1673358502644|
|data|响应数据|是|[object]| |
|data>>total|总数|是|[int]|22|
|data>>start_date|统计开始月份，格式：Y-m-d|是|[string]|2022-08-01|
|data>>end_date|统计结束月份，格式：Y-m-d|是|[string]|2022-08-31|
|data>>day_interval|时间区间相隔天数|是|[int]|31|
|data>>amount_type|计价类型：<br>0 成本计价<br> 1 固定值计价|是|[int]| |
|data>>row_data|明细数据|是|[array]| |
|data>>row_data>>seller_id|亚马逊店铺id|是|[string]|xxxxxxxxxxxxxxxx|
|data>>row_data>>sid|店铺id|是|[int]|1|
|data>>row_data>>wid|系统仓库id|是|[int]|2|
|data>>row_data>>ware_house_name|仓库名称|是|[string]|XinghaiDirect-1美国仓|
|data>>row_data>>start_count|期初库存-数量|是|[int]| |
|data>>row_data>>start_other_amount|期初库存-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>start_logistic_amount|期初库存-物流成本"<br>(精度：2位小数)|是|[string]|0.00|
|data>>row_data>>shipments_count|订单发货-数量|是|[int]| |
|data>>row_data>>shipments_other_amount|订单发货-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>shipments_logistic_amount|订单发货-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>whse_transfers_count|库房转运-数量|是|[int]| |
|data>>row_data>>whse_transfers_other_amount|库房转运-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>whse_transfers_logistic_amount|库房转运-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposed_count|弃置-数量|是|[int]| |
|data>>row_data>>disposed_other_amount|弃置-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposed_logistic_amount|弃置-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>found_count|已找到-数量|是|[int]| |
|data>>row_data>>found_other_amount|已找到-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>found_logistic_amount|已找到-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>lost_count|丢失-数量|是|[int]| |
|data>>row_data>>lost_other_amount|丢失-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>lost_logistic_amount|丢失-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>other_events_count|其他-数量|是|[int]| |
|data>>row_data>>other_events_other_amount|其他-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>other_events_logistic_amount|其他-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>receipts_count|货件补货-数量|是|[int]| |
|data>>row_data>>receipts_other_amount|货件补货-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>receipts_logistic_amount|货件补货-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>customer_returns_count|买家退货-数量|是|[int]| |
|data>>row_data>>customer_returns_other_amount|买家退货-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>customer_returns_logistic_amount|买家退货-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>vendor_returns_count|库存移除-数量|是|[int]| |
|data>>row_data>>vendor_returns_other_amount|库存移除-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>vendor_returns_logistic_amount|库存移除-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>difference_count|库存差异-数量|是|[int]| |
|data>>row_data>>difference_other_amount|库存差异-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>difference_logistic_amount|库存差异-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_count|期末库存-数量|是|[int]| |
|data>>row_data>>end_other_amount|期末库存-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_logistic_amount|期末库存-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>damaged_count|残损-数量|是|[int]| |
|data>>row_data>>damaged_other_amount|残损-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>damaged_logistic_amount|残损-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>partition_index|分区索引|是|[int]|10202201|
|data>>row_data>>end_on_way_count|期末在途-数量|是|[int]| |
|data>>row_data>>end_on_way_other_amount|期末在途-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_on_way_logistic_amount|期末在途-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>category_count|商品种类|是|[int]| |
|data>>row_data>>parent_node|是否父节点|是|[boolean]|true|
|data>>row_data>>inventory_turnover_rate|库存周转率<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>inventory_turnover_days|库存周转天数<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>start_total_amount|期初库存-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>shipments_total_amount|订单发货-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>whse_transfers_total_amount|库房转运-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>disposed_total_amount|弃置-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>found_total_amount|已找到-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>lost_total_amount|丢失-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>other_events_total_amount|其他-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>receipts_total_amount|货件补货-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>customer_returns_total_amount|订单退货-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>vendor_returns_total_amount|库存移除-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>difference_total_amount|库存差异-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_total_amount|期末库存-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>damaged_total_amount|已残损-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>end_on_way_total_amount|期末在途-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>stock_to_use_rate|存销比<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>adjustments_count|成本调整-数量|是|[int]| |
|data>>row_data>>adjustments_total_amount|成本调整-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>adjustments_logistic_amount|成本调整-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>adjustments_other_amount|成本调整-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>transferring_out_count|移仓在途-数量|是|[int]|1|
|data>>row_data>>transferring_out_total_amount|移仓在途-总成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>transferring_out_logistic_amount|移仓在途-物流成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>transferring_out_other_amount|移仓在途-商品成本<br>(精度：2位小数)|是|[number]|0.00|
|data>>row_data>>mid|站点id|是|[int]|1|
|data>>row_data>>parent_asin|父Asin|是|[string]|B07NL8PKF2|
|data>>row_data>>msku|msku|是|[string]|7501_x_h1856|
|data>>row_data>>asin|asin|是|[string]|B07NL8PKF2|
|data>>row_data>>disposition|库存属性：<br>sellable 可售<br>unsellable 不可售<br>all 全部|是|[string]|all|
|data>>row_data>>country_code|国家编码|是|[string]|US|
|data>>row_data>>fnsku|fnsku|是|[string]|X0023DBLEH|
|data>>row_data>>product_id|本地产品id|是|[int]|2|
|data>>row_data>>local_sku|本地产品sku|是|[string]|7501XH1856|
|data>>row_data>>local_name|本地产品名称|是|[string]|本地产品名称12|
|data>>row_data>>cid|商品分类id|是|[int]|12|
|data>>row_data>>product_category_name|产品分类名|是|[string]|产品分类名1|
|data>>row_data>>bid|品牌id|是|[int]|2|
|data>>row_data>>brand_name|品牌名称|是|[string]|品牌名称2|
|data>>row_data>>valuation_method|计价方法：<br>1 先进先出<br>2 移动加权<br>3 月末加权|是|[int]|1|
|data>>row_data>>child_data|返回字段与上级row_data一致|是|[array]|&nbsp;|

## 返回成功示例

```
{
    "code": 0,
    "msg": "操作成功",
    "traceId": "7248e68e-e304-46b7-8ee7-4094dd57b61c.1673358502644",
    "data": {
        "row_data": [
            {
                "sid": 6,
                "mid": 1,
                "wid": 19,
                "ware_house_name": "_xinghai_direct-1美国仓",
                "parent_asin": "_b07_n_l8_p_k_f2",
                "msku": "7501_x_h1856",
                "asin": "_b07_n_l8_p_k_f2",
                "disposition": "all",
                "seller_id": "_a1_r1_a_a_b_f0_f_m_f_l8",
                "country_code": "_u_s",
                "fnsku": "_x0023_d_b_l_e_h",
                "product_id": null,
                "local_sku": "",
                "local_name": "",
                "cid": null,
                "product_category_name": "",
                "bid": null,
                "brand_name": "",
                "valuation_method": null,
                "shipments_count": 0,
                "shipments_total_amount": "0.00",
                "shipments_logistic_amount": "0.00",
                "shipments_other_amount": "0.00",
                "whse_transfers_count": 0,
                "whse_transfers_total_amount": "0.00",
                "whse_transfers_logistic_amount": "0.00",
                "whse_transfers_other_amount": "0.00",
                "disposed_count": 0,
                "disposed_total_amount": "0.00",
                "disposed_logistic_amount": "0.00",
                "disposed_other_amount": "0.00",
                "found_count": 0,
                "found_total_amount": "0.00",
                "found_logistic_amount": "0.00",
                "found_other_amount": "0.00",
                "lost_count": 0,
                "lost_total_amount": "0.00",
                "lost_logistic_amount": "0.00",
                "lost_other_amount": "0.00",
                "other_events_count": 0,
                "other_events_total_amount": "0.00",
                "other_events_logistic_amount": "0.00",
                "other_events_other_amount": "0.00",
                "receipts_count": 0,
                "receipts_total_amount": "0.00",
                "receipts_logistic_amount": "0.00",
                "receipts_other_amount": "0.00",
                "customer_returns_count": 0,
                "customer_returns_total_amount": "0.00",
                "customer_returns_logistic_amount": "0.00",
                "customer_returns_other_amount": "0.00",
                "vendor_returns_count": -1,
                "vendor_returns_total_amount": "0.00",
                "vendor_returns_logistic_amount": "0.00",
                "vendor_returns_other_amount": "0.00",
                "difference_count": 0,
                "difference_total_amount": "0.00",
                "difference_logistic_amount": "0.00",
                "difference_other_amount": "0.00",
                "start_count": 1,
                "start_total_amount": "0.00",
                "start_logistic_amount": "0.00",
                "start_other_amount": "0.00",
                "end_count": 0,
                "end_total_amount": "0.00",
                "end_logistic_amount": "0.00",
                "end_other_amount": "0.00",
                "damaged_count": 0,
                "damaged_total_amount": "0.00",
                "damaged_logistic_amount": "0.00",
                "damaged_other_amount": "0.00",
                "end_on_way_count": 0,
                "end_on_way_total_amount": "0.00",
                "end_on_way_logistic_amount": "0.00",
                "end_on_way_other_amount": "0.00",
                "parent_node": true,                
                "inventory_turnover_rate": "0.00",
                "inventory_turnover_days": "0.00",
                "stock_to_use_rate": "0.00",
                "adjustments_count": 0,
                "adjustments_total_amount": "0.00",
                "adjustments_logistic_amount": "0.00",
                "adjustments_other_amount": "0.00",
                "transferring_out_count": 0,
                "transferring_out_total_amount": "0.00",
                "transferring_out_logistic_amount": "0.00",
                "transferring_out_other_amount": "0.00",
                "child_data": [
                    {
                        "sid": 6,
                        "mid": 1,
                        "wid": 19,
                        "ware_house_name": "_xinghai_direct-1美国仓",
                        "parent_asin": "_b07_n_l8_p_k_f2",
                        "msku": "7501_x_h1856",
                        "asin": "_b07_n_l8_p_k_f2",
                        "disposition": "unsellable",
                        "seller_id": "_a1_r1_a_a_b_f0_f_m_f_l8",
                        "country_code": "_u_s",
                        "fnsku": "_x0023_d_b_l_e_h",
                        "product_id": null,
                        "local_sku": "",
                        "local_name": "",
                        "cid": null,
                        "product_category_name": "",
                        "bid": null,
                        "brand_name": "",
                        "valuation_method": null,
                        "shipments_count": 0,
                        "shipments_total_amount": "0.00",
                        "shipments_logistic_amount": "0.00",
                        "shipments_other_amount": "0.00",
                        "whse_transfers_count": 0,
                        "whse_transfers_total_amount": "0.00",
                        "whse_transfers_logistic_amount": "0.00",
                        "whse_transfers_other_amount": "0.00",
                        "disposed_count": 0,
                        "disposed_total_amount": "0.00",
                        "disposed_logistic_amount": "0.00",
                        "disposed_other_amount": "0.00",
                        "found_count": 0,
                        "found_total_amount": "0.00",
                        "found_logistic_amount": "0.00",
                        "found_other_amount": "0.00",
                        "lost_count": 0,
                        "lost_total_amount": "0.00",
                        "lost_logistic_amount": "0.00",
                        "lost_other_amount": "0.00",
                        "other_events_count": 0,
                        "other_events_total_amount": "0.00",
                        "other_events_logistic_amount": "0.00",
                        "other_events_other_amount": "0.00",
                        "receipts_count": 0,
                        "receipts_total_amount": "0.00",
                        "receipts_logistic_amount": "0.00",
                        "receipts_other_amount": "0.00",
                        "customer_returns_count": 0,
                        "customer_returns_total_amount": "0.00",
                        "customer_returns_logistic_amount": "0.00",
                        "customer_returns_other_amount": "0.00",
                        "vendor_returns_count": -1,
                        "vendor_returns_total_amount": "0.00",
                        "vendor_returns_logistic_amount": "0.00",
                        "vendor_returns_other_amount": "0.00",
                        "difference_count": 0,
                        "difference_total_amount": "0.00",
                        "difference_logistic_amount": "0.00",
                        "difference_other_amount": "0.00",
                        "start_count": 1,
                        "start_total_amount": "0.00",
                        "start_logistic_amount": "0.00",
                        "start_other_amount": "0.00",
                        "end_count": 0,
                        "end_total_amount": "0.00",
                        "end_logistic_amount": "0.00",
                        "end_other_amount": "0.00",
                        "damaged_count": 0,
                        "damaged_total_amount": "0.00",
                        "damaged_logistic_amount": "0.00",
                        "damaged_other_amount": "0.00",
                        "end_on_way_count": 0,
                        "end_on_way_total_amount": "0.00",
                        "end_on_way_logistic_amount": "0.00",
                        "end_on_way_other_amount": "0.00",
                        "parent_node": false,
                        "child_data": [],
                        "inventory_turnover_rate": "0.00",
                        "inventory_turnover_days": "0.00",
                        "stock_to_use_rate": "0.00",
                        "adjustments_count": 0,
                        "adjustments_total_amount": "0.00",
                        "adjustments_logistic_amount": "0.00",
                        "adjustments_other_amount": "0.00",
                        "transferring_out_count": 0,
                        "transferring_out_total_amount": "0.00",
                        "transferring_out_logistic_amount": "0.00",
                        "transferring_out_other_amount": "0.00",
                    }
                ]
            }
        ],
        "start_date": "2022-08-01",
        "end_date": "2022-08-31",
        "day_interval": 31,
        "total": 1,
        "size": 1,
        "current": 1,
        "amount_type": 0
    }
}
```