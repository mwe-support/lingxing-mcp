# 查询补货列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/restocking/analysis/getSummaryList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid_list|店铺id|否|[array]|["136","139"]|
|data_type|查询维度：1 asin，2 msku|是|[int]|1|
|asin_list|按传入的asin列表筛选数据|否|[array]|["B0xxxxxxxx"]|
|msku_list|按传入的msku列表筛选数据|否|[array]|["MSKUE457EF2"]|
|mode|补货建议模式：<br>0 普通模式<br>1 海外仓中转模式<br>【不传默认取erp当前设置模式（在补货建议列表可切换）】|否|[int]|0|
|listing_date_range|listing创建时间范围筛选：[开始日期，结束日期]，必须同时包含两个日期才生效|否|[array]|["2023-06-06","2024-07-13"]|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页条数，默认20，上限50|否|[int]|20|

## 请求示例
```
{
    "sid_list": ["136","139"],
    "data_type": 1,
    "asin_list": ["B0xxxxxxxx"],
    "mode": 0,
    "listing_opentime_list": [
        "2023-06-06",
        "2024-07-13"
    ],
    "offset": 0,
    "length": 20
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0成功|是|[int]|0|
|message|提示信息|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|DCF829F2-1054-08BC-7501-FBCF8BC614CA|
|response_time|响应时间|是|[string]|2023-04-24 17:29:54|
|total|总数|是|[int]|3|
|data|响应数据|是|[array]||
|data>>basic_info|基础数据|是|[object]||
|data>>basic_info>>data_type|数据类型：<br>1 asin，2 msku|是|[int]|2|
|data>>basic_info>>node_type|节点类型：<br>1 共享库存父行<br>2 共享库存子行<br>3 非共享库存<br>4 ASIN+国家汇总行|是|[int]|1|
|data>>basic_info>>sid|店铺id|是|[string]|9|
|data>>basic_info>>asin|ASIN|是|[string]|B0ABC83915|
|data>>basic_info>>msku_fnsku_list|相关msku和fnsku|是|[array]||
|data>>basic_info>>msku_fnsku_list>>msku|msku|是|[string]|msku3|
|data>>basic_info>>msku_fnsku_list>>fnsku|fnsku|是|[string]|fnsku2|
|data>>basic_info>>listing_opentime_list|listing创建时间|是|[array]|["2021-07-02 01:43:09 -07:00"]|
|data>>basic_info>>sync_time|数据更新时间|是|[string]|2023-04-24 16:48:02|
|data>>basic_info>>hash_id|唯一标识|是|[string]|6aff663b613960e61afc442dcde23aff|
|data>>amazon_quantity_info|亚马逊数量|是|[object]| |
|data>>amazon_quantity_info>>amazon_quantity_valid|FBA可售|是|[number]|0|
|data>>amazon_quantity_info>>amazon_quantity_shipping|FBA在途|是|[number]|0|
|data>>amazon_quantity_info>>amazon_quantity_shipping_plan|预计发货量|是|[number]|0|
|data>>amazon_quantity_info>>afn_fulfillable_quantity|FBA可售-可售|是|[number]|0|
|data>>amazon_quantity_info>>reserved_fc_transfers|FBA可售-待调仓|是|[number]|0|
|data>>amazon_quantity_info>>reserved_fc_processing|FBA可售-调仓中|是|[number]|0|
|data>>scm_quantity_info|供应链数量|是|[object]||
|data>>scm_quantity_info>>sc_quantity_local_valid|scm-本地仓可用|是|[number]|0|
|data>>scm_quantity_info>>sc_quantity_oversea_valid|scm-海外仓可用|是|[number]|0|
|data>>scm_quantity_info>>sc_quantity_oversea_shipping|scm-海外仓在途|是|[number]|0|
|data>>scm_quantity_info>>sc_quantity_local_qc|scm-待检待上架量|是|[number]|0|
|data>>scm_quantity_info>>sc_quantity_purchase_plan|scm-采购计划|是|[number]|50|
|data>>scm_quantity_info>>sc_quantity_purchase_shipping|scm-待交付|是|[number]|0|
|data>>scm_quantity_info>>sc_quantity_local_shipping|scm-本地仓在途|是|[number]|0|
|data>>sales_info|历史销量数据|是|[object]||
|data>>sales_info>>sales_avg_3|日均销量-3天|是|[number]|165|
|data>>sales_info>>sales_avg_7|日均销量-7天|是|[number]|165|
|data>>sales_info>>sales_avg_14|日均销量-14天|是|[number]|165|
|data>>sales_info>>sales_avg_30|日均销量-30天|是|[number]|165|
|data>>sales_info>>sales_avg_60|日均销量-60天|是|[number]|160.9|
|data>>sales_info>>sales_avg_90|日均销量-90天|是|[number]|153.6|
|data>>sales_info>>sales_total_3|总销量-3天|是|[number]|495|
|data>>sales_info>>sales_total_7|总销量-7天|是|[number]|1155|
|data>>sales_info>>sales_total_14|总销量-14天|是|[number]|2310|
|data>>sales_info>>sales_total_30|总销量-30天|是|[number]|4950|
|data>>sales_info>>sales_total_60|总销量-60天|是|[number]|9655|
|data>>sales_info>>sales_total_90|总销量-90天|是|[number]|13825|
|data>>suggest_info|建议数据|是|[object]||
|data>>suggest_info>>out_stock_flag|断货标记：0 不会断货，1 会断货|是|[int]|1|
|data>>suggest_info>>out_stock_date|断货日期（最早的）|是|[string]|2023-04-24|
|data>>suggest_info>>estimated_sale_quantity|预测销量|是|[number]|15711|
|data>>suggest_info>>estimated_sale_avg_quantity|预测日均销量|是|[number]|275.63|
|data>>suggest_info>>available_sale_days|预测可售天数|是|[number]|0|
|data>>suggest_info>>fba_available_sale_days|预测可售天数（只考虑FBA库存和FBA在途）|是|[number]|0|
|data>>suggest_info>>quantity_sug_purchase|建议采购量|是|[number]|15663|
|data>>suggest_info>>quantity_sug_local_to_oversea|建议本地发海外仓量|是|[number]|13508|
|data>>suggest_info>>quantity_sug_local_to_fba|建议本地发FBA量|是|[number]|0|
|data>>suggest_info>>quantity_sug_oversea_to_fba|建议海外仓发FBA量|是|[number]|6891|
|data>>suggest_info>>out_stock_date_purchase|断货时间：采购|是|[string]|2023-04-24|
|data>>suggest_info>>out_stock_date_local|断货时间：本地仓发货|是|[string]|2023-04-24|
|data>>suggest_info>>out_stock_date_oversea|断货时间：海外仓发货|是|[string]|2023-04-24|
|data>>suggest_info>>sug_date_purchase|建议采购日|是|[string]|2023-04-24|
|data>>suggest_info>>sug_date_send_local|建议本地仓发货日|是|[string]|2023-04-24|
|data>>suggest_info>>sug_date_send_oversea|建议海外仓发货日|是|[string]|2023-04-24|
|data>>suggest_info>>suggest_sm_list|多运输方式建议量|是|[array]| |
|data>>suggest_info>>suggest_sm_list>>sm_id|运输方式id|是|[string]|241250000631390720|
|data>>suggest_info>>suggest_sm_list>>name|运输方式名称|是|[string]|海派|
|data>>suggest_info>>suggest_sm_list>>quantity_sug_purchase|建议采购量|是|[number]|5300|
|data>>suggest_info>>suggest_sm_list>>quantity_sug_local_to_fba|建议本地发FBA量|是|[number]|4900|
|data>>suggest_info>>suggest_sm_list>>quantity_sug_local_to_oversea|建议本地发海外仓量|是|[number]|0|
|data>>ext_info|附加信息|是|[object]| |
|data>>ext_info>>restock_status|无需补货标识：0 需要补货，1 无需补货|是|[int]|0|
|data>>ext_info>>remark|备注|是|[string]||
|data>>ext_info>>star|是否关注：0 未关注，1 已关注|是|[int]|0|
|data>>ext_info>>need_flag|已弃用（原采、发标识）|是|[array]|[1,2]|
|data>>item_list|子项-结构同父项|是|[array]|&nbsp;|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "384AE0B2-1F40-990E-6E3F-857DDBC58BE9",
    "response_time": "2023-12-06 16:55:51",
    "data": [
        {
            "basic_info": {
                "hash_id": "0288f740df90c0d6e47ec50983d4d3cb",
                "data_type": 1,
                "node_type": 4,
                "sid": "119",
                "asin": "B0CM3B75YP",
                "msku_fnsku_list": [
                    {
                        "msku": "CN0001",
                        "fnsku": "X0040T7HJP"
                    }
                ],
                "listing_opentime_list": [
                    "2023-10-30 00:10:22 -07:00"
                ],
                "sync_time": "2023-12-06 16:30:36"
            },
            "amazon_quantity_info": {
                "amazon_quantity_valid": 0,
                "amazon_quantity_shipping": 20,
                "amazon_quantity_shipping_plan": 1201,
                "afn_fulfillable_quantity": 0,
                "reserved_fc_transfers": 0,
                "reserved_fc_processing": 0
            },
            "scm_quantity_info": {
                "sc_quantity_local_valid": 23,
                "sc_quantity_oversea_valid": 0,
                "sc_quantity_oversea_shipping": 0,
                "sc_quantity_local_qc": 0,
                "sc_quantity_purchase_plan": 0,
                "sc_quantity_purchase_shipping": 0,
                "sc_quantity_local_shipping": 0
            },
            "sales_info": {
                "sales_avg_3": 0,
                "sales_avg_7": 0,
                "sales_avg_14": 0,
                "sales_avg_30": 0,
                "sales_avg_60": 0,
                "sales_avg_90": 0,
                "sales_total_3": 0,
                "sales_total_7": 0,
                "sales_total_14": 0,
                "sales_total_30": 0,
                "sales_total_60": 0,
                "sales_total_90": 0
            },
            "suggest_info": {
                "out_stock_flag": 0,
                "out_stock_date": "",
                "estimated_sale_quantity": 0,
                "estimated_sale_avg_quantity": 0,
                "available_sale_days": 360,
                "fba_available_sale_days": 360,
                "quantity_sug_purchase": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_oversea_to_fba": 0,
                "out_stock_date_purchase": "",
                "out_stock_date_local": "",
                "out_stock_date_oversea": "",
                "sug_date_purchase": "",
                "sug_date_send_local": "",
                "sug_date_send_oversea": "",
                "suggest_sm_list": [
                    {
                        "sm_id": "241241710888379394",
                        "name": "空派",
                        "quantity_sug_purchase": 0,
                        "quantity_sug_local_to_fba": 0,
                        "quantity_sug_local_to_oversea": 0
                    },
                    {
                        "sm_id": "241384850192131072",
                        "name": "sr258",
                        "quantity_sug_purchase": 0,
                        "quantity_sug_local_to_fba": 0,
                        "quantity_sug_local_to_oversea": 0
                    }
                ]
            },
            "ext_info": {
                "restock_status": 0,
                "remark": "",
                "star": 0,
                "need_flag": []
            },
            "item_list": [
                {
                    "basic_info": {
                        "hash_id": "04158e9f9392e59f88ead19f374f5953",
                        "data_type": 1,
                        "node_type": 3,
                        "sid": "119",
                        "asin": "B0CM3B75YP",
                        "msku_fnsku_list": [
                            {
                                "msku": "CN0001",
                                "fnsku": "X0040T7HJP"
                            }
                        ],
                        "listing_opentime_list": [
                            "2023-10-30 00:10:22 -07:00"
                        ],
                        "sync_time": "2023-12-06 16:30:36"
                    },
                    "amazon_quantity_info": {
                        "amazon_quantity_valid": 0,
                        "amazon_quantity_shipping": 20,
                        "amazon_quantity_shipping_plan": 1201,
                        "afn_fulfillable_quantity": 0,
                        "reserved_fc_transfers": 0,
                        "reserved_fc_processing": 0
                    },
                    "scm_quantity_info": {
                        "sc_quantity_local_valid": 23,
                        "sc_quantity_oversea_valid": 0,
                        "sc_quantity_oversea_shipping": 0,
                        "sc_quantity_local_qc": 0,
                        "sc_quantity_purchase_plan": 0,
                        "sc_quantity_purchase_shipping": 0,
                        "sc_quantity_local_shipping": 0
                    },
                    "sales_info": {
                        "sales_avg_3": 0,
                        "sales_avg_7": 0,
                        "sales_avg_14": 0,
                        "sales_avg_30": 0,
                        "sales_avg_60": 0,
                        "sales_avg_90": 0,
                        "sales_total_3": 0,
                        "sales_total_7": 0,
                        "sales_total_14": 0,
                        "sales_total_30": 0,
                        "sales_total_60": 0,
                        "sales_total_90": 0
                    },
                    "suggest_info": {
                        "out_stock_flag": 0,
                        "out_stock_date": "",
                        "estimated_sale_quantity": 0,
                        "estimated_sale_avg_quantity": 0,
                        "available_sale_days": 360,
                        "fba_available_sale_days": 360,
                        "quantity_sug_purchase": 0,
                        "quantity_sug_local_to_oversea": 0,
                        "quantity_sug_local_to_fba": 0,
                        "quantity_sug_oversea_to_fba": 0,
                        "out_stock_date_purchase": "",
                        "out_stock_date_local": "",
                        "out_stock_date_oversea": "",
                        "sug_date_purchase": "",
                        "sug_date_send_local": "",
                        "sug_date_send_oversea": "",
                        "suggest_sm_list": [
                            {
                                "sm_id": "241241710888379394",
                                "name": "空派",
                                "quantity_sug_purchase": 0,
                                "quantity_sug_local_to_fba": 0,
                                "quantity_sug_local_to_oversea": 0
                            },
                            {
                                "sm_id": "241384850192131072",
                                "name": "sr258",
                                "quantity_sug_purchase": 0,
                                "quantity_sug_local_to_fba": 0,
                                "quantity_sug_local_to_oversea": 0
                            }
                        ]
                    },
                    "ext_info": {
                        "restock_status": 1,
                        "remark": "",
                        "star": 0,
                        "need_flag": []
                    },
                    "item_list": []
                }
            ]
        }
    ],
    "total": 5
}
```

## 附加说明
唯一键：hash_id