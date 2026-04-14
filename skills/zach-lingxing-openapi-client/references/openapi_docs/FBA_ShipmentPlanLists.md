# 查询FBA发货计划
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/fba_report/shipmentPlanLists` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sids|店铺ids，12,13组成，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[string]| |
|wid|仓库id|否|[string]| |
|packing_type|包装类型2原装 1混装|否|[string]| |
|search_field_time|查找时间字段(gmt_create-创建时间,estimated_delivery_time-计划发货时间)，不传该字段默认为gmt_create|否|[string]|gmt_create|
|search_field|查找字段  order_sn发货计划单号|否|[string]|create_user|
|search_value|查找值|否|[string]| |
|status|状态|否|[string]| |
|mids|国家id|否|[string]| |
|offset|偏移量 0 偏移量 (currentPage -1) * length|否|[int]|0|
|length|长度 默认20|否|[int]|20|
|start_date|开始日期 如:2021-09-07|否|[string]| |
|end_date|结束日期 如:2021-09-08|否|[string]| |


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/data/fba_report/shipmentPlanLists?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "sids": "",
    "wid": "",
    "packing_type": "",
    "search_field_time": "gmt_create",
    "search_field": "create_user",
    "search_value": "",
    "status": "",
    "mids": "",
    "offset": 0,
    "length": 20,
    "start_date": "",
    "end_date": ""
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|错误码 0成功|是|[int]|1|
|message|消息|是|[string]|请求成功|
|request_id|请求id|是|[string]|936D6C3B-D4FE-0F89-9328-FA1D0DF6813B|
|data|发货计划组列表|是|[array]| |
|data>>ispg_id|发货计划组id|是|[int]|181|
|data>>create_time|创建时间|是|[string]|2021-09-27 10:27:46|
|data>>seq|批次号|是|[string]|RP210927003|
|data>>remark|创建时间|是|[string]| |
|data>>create_user|创建用户|是|[string]|吴姗珊|
|data>>custom_fields|自定义字段|是|[array]| |
|data>>custom_fields>>id|字段ID|是|[string]| |
|data>>custom_fields>>name|字段名|是|[string]| |
|data>>custom_fields>>val_text|字段值|是|[string]| |
|data>>list|子项目列表|是|[array]| |
|data>>list>>ispg_id|发货计划组父ID|是|[int]|181|
|data>>list>>isp_id|发货计划id|是|[int]|426|
|data>>list>>logistics_channel_id|物流ID|是|[int]|0|
|data>>list>>custom_fields|自定义字段|是|[array]| |
|data>>list>>custom_fields>>id|字段ID|是|[string]| |
|data>>list>>custom_fields>>name|字段名|是|[string]| |
|data>>list>>custom_fields>>val_text|字段值|是|[string]| |
|data>>list>>fnsku|fnsku|是|[string]|X000XF6OGV|
|data>>list>>msku|seller_sku|是|[string]||
|data>>list>>wid|仓库id|是|[int]|68200|
|data>>list>>wname|仓库名称|是|[string]|012.10|
|data>>list>>sid|店铺id|是|[int]|1206|
|data>>list>>create_time|创建时间|是|[string]|2021-09-27 10:27:46|
|data>>list>>status|状态：<br>-5、已驳回，<br>0、待审核，<br>5、待处理，<br>10、已处理|是|[int]|10|
|data>>list>>packing_type|包装类型 2原装 1混装|是|[int]|1|
|data>>list>>shipment_time|计划发货时间|是|[string]| |
|data>>list>>shipment_plan_quantity|计划发货量|是|[int]|2000|
|data>>list>>seq|批次号|是|[string]|RP210927003|
|data>>list>>logistics_name|物流名称|是|[string]| |
|data>>list>>quantity_in_case|单箱数量|是|[int]|2000|
|data>>list>>box_num|箱数|是|[int]|1|
|data>>list>>is_relate_mws|是否关联货件|是|[int]|1|
|data>>list>>is_relate_list|是否关联发货单|是|[int]|1|
|data>>list>>remark|备注|是|[string]| |
|data>>list>>print_num|打印次数|是|[int]|0|
|data>>list>>create_user|创建用户|是|[string]|吴姗珊|
|data>>list>>small_image_url|商品图片|是|[string]||
|data>>list>>order_sn|计划发货单号|是|[string]|R210927006|
|data>>list>>product_name|产品名称|是|[string]|辅料管理5|
|data>>list>>product_id|产品id|是|[int]|89981|
|data>>list>>sku|sku|是|[string]|辅料管理5|
|data>>list>>pic_url|商品图片|是|[string]||
|data>>list>>is_combo|是否组合商品|是|[int]|0|
|data>>list>>cg_package_length|包装长(CM,2位小数)|是|[string]| |
|data>>list>>cg_package_height|包装高(CM,2位小数)|是|[string]| |
|data>>list>>cg_package_width|包装宽(CM,2位小数)|是|[string]| |
|data>>list>>cg_box_length|箱子长(CM,2位小数)|是|[string]| |
|data>>list>>cg_box_width|箱子宽(CM,2位小数)|是|[string]| |
|data>>list>>cg_box_height|箱子高(CM,2位小数)|是|[string]| |
|data>>list>>cg_box_weight|单箱重量(KG,2位小数)|是|[string]| |
|data>>list>>cg_box_net_weight|单箱净重(KG,2位小数)|是|[string]| |
|data>>list>>cg_box_gross_weight|单箱毛重(KG,2位小数)|是|[string]| |
|data>>list>>is_urgent|是否加急（0-否，1-是）|是|[int]| |
|data>>list>>storage_list|库存列表|是|[array]| |
|data>>list>>storage_list>>product_id|商品id|是|[int]|89981|
|data>>list>>storage_list>>product_valid_num|库存可用量|是|[int]|6000|
|data>>list>>storage_list>>product_qc_num|待检量|是|[int]|0|
|data>>list>>storage_list>>quantity_receive|待收货量|是|[int]|0|
|data>>list>>mws_relate|发货单关联|是|[array]| |
|data>>list>>mws_relate>>isim_id|关联货件id|是|[int]|11039|
|data>>list>>mws_relate>>isil_id|关联发货单id|是|[int]|1034|
|data>>list>>mws_relate>>isilm_id|关联发货单明细id|是|[int]|3495|
|data>>list>>mws_relate>>shipment_plan_sn|关联发货计划单号|是|[string]|R210927006|
|data>>list>>mws_relate>>shipment_mws_sn|关联货件单号|是|[string]|FBA15CS95XDX|
|data>>list>>mws_relate>>shipment_list_sn|关联发货单单号|是|[string]|SP210927003|
|data>>list>>mws_relate>>shipment_plan_quantity|关联发货计划数量|是|[int]|2000|
|data>>list>>mws_relate>>shipment_mws_quantity|关联货件数量|是|[int]|2000|
|data>>list>>mws_relate>>shipment_list_quantity|关联发货单数量|是|[int]|2000|
|data>>list>>mws_relate>>is_sta|是否sta货件，1：是，0：否|是|[string]| |
|data>>list>>mws_relate>>sta_shipment_id|sta的shipmentId|是|[string]| |
|data>>list>>mws_relate>>sta_inbound_plan_id|sta任务编号|是|[string]| |
|data>>list>>status_name|状态名称|是|[string]|已处理|
|data>>list>>packing_type_name|包装类型名称|是|[string]|混装|
|data>>list>>diff_num|差额|是|[int]|4000|
|data>>list>>sname|店铺|是|[string]|AK-quanqiu-JP-test7-JP|
|data>>list>>nation|国家|是|[string]|日本|
|data>>list>>lock_status|锁定状态：1-未锁定 2-已锁定 3-已使用|是|[int]|1|
|total|发货计划量总数|是|[int]|179|
|error_details|错误信息|是|[array]| |
|response_time|响应时间|是|[string]| |


## 返回成功示例
```
{
    "code": 0,
    "message": "请求成功",
    "require_id": "936D6C3B-D4FE-0F89-9328-FA1D0DF6813B",
    "data": [
      {
        "ispg_id": 181,
        "create_time": "2021-09-27 10:27:46",
        "seq": "RP210927003",
        "remark": "",
        "create_user": "吴姗珊",
        "custom_fields": [{
            "id": "",
            "name": "",
            "val_text": ""
        }],
        "list": [{
            "ispg_id": 181,
            "isp_id": 426,
            "logistics_channel_id": 0,
            "custom_fields": [{
                "id": "",
                "name": "",
                "val_text": ""
            }],
            "fnsku": "X000XF6OGV",
            "msku": "",
            "wid": 68200,
            "wname": "012.10",
            "sid": 1206,
            "create_time": "2021-09-27 10:27:46",
            "status": 10,
            "packing_type": 1,
            "shipment_time": "",
            "shipment_plan_quantity": 2000,
            "seq": "RP210927003",
            "logistics_name": "",
            "quantity_in_case": 2000,
            "box_num": 1,
            "is_relate_mws": 1,
            "is_relate_list": 1,
            "remark": "",
            "print_num": 0,
            "create_user": "吴姗珊",
            "small_image_url": "",
            "order_sn": "R210927006",
            "product_name": "辅料管理5",
            "product_id": 89981,
            "sku": "辅料管理5",
            "pic_url": "",
            "is_combo": 0,
            "cg_package_length": "",
            "cg_package_height": "",
            "cg_package_width": "",
            "cg_box_length": "",
            "cg_box_width": "",
            "cg_box_height": "",
            "cg_box_weight": "",
            "cg_box_net_weight": "",
            "cg_box_gross_weight": "",
            "is_urgent": 0,
            "storage_list": [{
                "product_id": 89981,
                "product_valid_num": 6000,
                "product_qc_num": 0,
                "quantity_receive": 0
            }],
            "mws_relate": [{
                "isim_id": 11039,
                "isil_id": 1034,
                "isilm_id": 3495,
                "shipment_plan_sn": "R210927006",
                "shipment_mws_sn": "FBA15CS95XDX",
                "shipment_list_sn": "SP210927003",
                "shipment_plan_quantity": 2000,
                "shipment_mws_quantity": 2000,
                "shipment_list_quantity": 2000,
                "is_sta": "",
                "sta_shipment_id": "",
                "sta_inbound_plan_id": ""
            }],
            "status_name": "已处理",
            "packing_type_name": "混装",
            "diff_num": 4000,
            "sname": "AK-quanqiu-JP-test7-JP",
            "nation": "日本",
            "lock_status": 1
        }]
    }],
    "total": 179
    "error_details": [],
    "response_time": ""
}
```