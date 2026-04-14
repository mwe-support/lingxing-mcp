# 查询发货单列表
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/storage/shipment/getInboundShipmentList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|search_value|搜索的值|否|[string]|123|
|search_field|搜索字段：<br>sku<br>shipment_sn 发货单号<br>shipment_id 货件单号|否|[string]|shipment_sn|
|sids|店铺id,多个时通过英文逗号分隔,如1,2,3，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[string]|8|
|mids|国家id,多个时通过英文逗号分隔,如1,2,3|否|[string]|1|
|wid|仓库id,多个时通过英文逗号分隔,如1,2,3|否|[string]|68125|
|logistics_type|物流方式id|否|[array]|[1]|
|status|发货单状态：<br>-1 : 待配货， <br>0：待发货，<br>1：已发货，<br>3：已作废，<br>4：已删除|否|[int]| |
|print_status|打印状态 0未打印 1 已打印|否|[string]|1|
|pick_status|拣货状态 0 未拣货 1已拣货|否|[string]|1|
|time_type|时间类型：<br> 3创建时间 (允许精确到时分秒)<br> 2创建时间<br> 1到货时间 <br> 0发货时间 <br>4更新时间 (允许精确到时分秒)|否|[int]|2|
|start_date|开始日期|否|[string]|2021-03-29|
|end_date|结束日期|否|[string]|2021-06-29|
|offset|偏移量=（currentPage -1）*length|是|[int]|0|
|length|长度|是|[int]|20|
|is_delete|是否删除：0 未删除【默认】 1 已删除 2 全部|否|[number]|0|
|senior_search_list|精准搜索|否|[array]||
|senior_search_list>>search_field|搜索字段：<br>sku<br>shipment_sn 发货单号<br>shipment_id 货件单号|是|[string]|"shipment_id"|
|senior_search_list>>search_value|搜索值|是|[array]|["1FBA194WNZDM9","1FBA194WD1DMJ"]|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/routing/storage/shipment/getInboundShipmentList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "search_value": "123",
    "search_field": "shipment_sn",
    "sids": "8",
    "mids": "1",
    "wid": "68125",
    "logistics_type": [1],
    "status": 0,
    "print_status": "1",
    "pick_status": "1",
    "time_type": 2,
    "start_date": "2021-03-29",
    "end_date": "2021-06-29",
    "offset": 0,
    "length": 20,
    "senior_search_list": [{
        "search_field": "shipment_id",
        "search_value": ["1FBA194WNZDM9", "1FBA194WD1DMJ"]
    }]
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[int]|0|
|message| |是|[string]|success|
|error_details| |是|[array]| |
|response_time| |是|[string]|2020-04-30 17:33:32|
|data| |是|[object]| |
|data>>list|发货单列表|是|[array]| |
|data>>list>>id|发货单id|是|[int]|25|
|data>>list>>shipment_sn|发货单号|是|[string]|SP180720003|
|data>>list>>status|发货单状态，<br>-1 : 待配货 <br>0：待发货，<br>1：已发货，<br>2：已完成，<br>3：已作废|是|[int]|0|
|data>>list>>shipment_time|发货时间|是|[string]| |
|data>>list>>wname|仓库名称|是|[string]|测试仓库|
|data>>list>>create_user|创建用户|是|[string]| |
|data>>list>>logistics_provider_id|物流商ID|是|[string]| |
|data>>list>>logistics_provider_name|物流商名称|是|[string]| |
|data>>list>>logistics_channel_name|物流渠道名称|是|[string]|鸿捷--HKUPS美国红单|
|data>>list>>expected_arrival_date|到货时间|是|[string]| |
|data>>list>>actual_shipment_time|实际发货时间（已废弃）|是|[string]| |
|data>>list>>etd_date|开船时间|是|[string]| |
|data>>list>>eta_date|预计到港时间|是|[string]| |
|data>>list>>delivery_date|实际妥投时间|是|[string]| |
|data>>list>>create_time|创建时间|是|[string]|2018-07-20|
|data>>list>>gmt_create|创建时间(精确到时分秒)|是|[string]|2018-07-20 15:14:18|
|data>>list>>is_pick|拣货状态 0 未拣货 1已拣货|是|[int]|1|
|data>>list>>is_print|是否打印 0-否,1-是|是|[int]|0|
|data>>list>>pick_time|拣货时间|是|[string]| |
|data>>list>>print_num|打印次数|是|[int]|0|
|data>>list>>head_fee_type|头程费分配方式，<br>0：按计费重；<br>1：按实重；<br>2：按体积重；<br>3：按SKU数量；<br>4：自定义；<br>5：按箱子体积|是|[int]|0|
|data>>list>>file_id|附件文件|是|[string]| |
|data>>list>>update_time|更新时间|是|[string]|2018-07-20 15:14:18|
|data>>list>>remark|备注|是|[string]| |
|data>>list>>wid|仓库ID|是|[int]|8|
|data>>list>>is_return_stock|是否恢复库存:0-否，1-是|是|[int]|0|
|data>>list>>pay_status|付款状态：<br>0：未申请，<br>1：已申请，<br>2：部分付款，<br>3：已付清，<br>4：无|否|[int]| |
|data>>list>>audit_status|审批状态：<br>121：待审核，<br>122：驳回，<br>123：通过，<br>124：作废|否|[int]| |
|data>>list>>shipment_user|发货人|否|[string]| |
|data>>list>>is_exist_declaration|是否关联报关单，0：否，1：是|否|[int]| |
|data>>list>>is_exist_clearance|是否关联清关单，0：否，1：是|否|[int]| |
|data>>list>>third_party_order_mode|下单模式，0：无，1：系统下单，2：手工下单|否|[int]| |
|data>>list>>third_party_order_status|第三方仓下单状态，待发货下才有：<br>1：未下单，<br>2：已下单，<br>3：异常，<br>4：已发货|否|[int]| |
|data>>list>>vat_code|店铺VAT税号|否|[string]| |
|data>>list>>method_id|运输方式ID|否|[string]| |
|data>>list>>method_name|运输方式名称|否|[string]| |
|data>>list>>is_custom_shipment_time|是否自定义发货时间，1：是，0：否|否|[int]| |
|data>>list>>logistics|物流轨迹列表|是|[array]| |
|data>>list>>logistics>>logistics_list_type|物流轨迹样式,<br>0:旧版,<br>1:新版|是|[int]|1|
|data>>list>>logistics>>replace_tracking_number|跟踪单号（旧版）|否|[string]|88803089941|
|data>>list>>logistics>>tracking_number|物流商号（旧版）|否|[string]|8880308989|
|data>>list>>logistics>>tracking_no|查询单号（新版）|否|[string]|ta1234567|
|data>>list>>logistics>>transport_type|运输类型（新版）编码：<br>1-快递,<br>2-海运,<br>3-空运,<br>4-其他|否|[int]|2|
|data>>list>>logistics>>transport_type_name|运输类型（新版）名称|否|[string]|海运|
|data>>list>>logistics>>order_type_code|单号类型（新版）编码：<br>1-订舱号,<br>2-提单号,<br>3-箱号,<br>4-其他,<br>5-跟踪单号,<br>6-航班号|否|[int]|4|
|data>>list>>logistics>>order_type_code_name|单号类型（新版）名称|否|[string]|其他|
|data>>list>>logistics>>shippers|承运商（新版）编码|否|[string]|emc|
|data>>list>>logistics>>shippers_name|承运商（新版）名称|否|[string]|长荣emc|
|data>>list>>logistics>>remark|轨迹备注（新版）|否|[string]|这里是备注字段|
|data>>list>>relate_list|关联货件列表|是|[array]| |
|data>>list>>relate_list>>mid|国家id|是|[int]|318|
|data>>list>>relate_list>>destination_fulfillment_center_id|物流中心编码|是|[string]|FTW1|
|data>>list>>relate_list>>quantity_shipped|申报量|是|[int]|190|
|data>>list>>relate_list>>id|明细id|是|[int]|1039|
|data>>list>>relate_list>>wname|仓库名称|是|[string]|测试仓库--吴萍|
|data>>list>>relate_list>>shipment_sn|发货单号|是|[string]|SP180720003|
|data>>list>>relate_list>>shipment_id|货件id|是|[string]|FBA15D9PQN10|
|data>>list>>relate_list>>shipment_status|货件状态|是|[string]| |
|data>>list>>relate_list>>wid|仓库id|是|[int]|8|
|data>>list>>relate_list>>pid|货件明细ID|是|[int]|318|
|data>>list>>relate_list>>sid|店铺id|是|[int]|8|
|data>>list>>relate_list>>sname|店铺名称|是|[string]|PM1：-test6-A0|
|data>>list>>relate_list>>num|发货数量|是|[int]|1|
|data>>list>>relate_list>>pic_url|图片url|是|[string]|http://ecx.images-amazon.com/images/I/31UvRfeNRPL._SL75_.jpg|
|data>>list>>relate_list>>packing_type|混装类型 <br>1混装,<br>2原装|是|[int]|1|
|data>>list>>relate_list>>fulfillment_network_sku|listing的fnsku|是|[string]|xxxx|
|data>>list>>relate_list>>sku|sku|是|[string]|10         1|
|data>>list>>relate_list>>fnsku|仓库fnsku|是|[string]| |
|data>>list>>relate_list>>msku|seller_sku|是|[string]|xxxx|
|data>>list>>relate_list>>nation|国家名称|是|[string]|美国|
|data>>list>>relate_list>>apply_num|关联货件量|是|[int]|1|
|data>>list>>relate_list>>product_id|商品id|是|[int]|19873|
|data>>list>>relate_list>>product_name|产品名称|是|[string]|林xxxx|
|data>>list>>relate_list>>asin|ASIN|是|[string]| |
|data>>list>>relate_list>>parent_asin|父ASIN|是|[string]| |
|data>>list>>relate_list>>remark|备注|是|[string]| |
|data>>list>>relate_list>>status|发货单状态，<br>-1 : 待配货 <br>0：待发货，<br>1：已发货，<br>3：已作废|是|[int]|0|
|data>>list>>relate_list>>is_combo|是否组合商品:<br>1-是,<br>0-否|是|[int]|1|
|data>>list>>relate_list>>create_by_mws|创建发货单途径：<br>1-货件,<br>0-发货计划|是|[int]|1|
|data>>list>>relate_list>>whb_code_list|仓位编码列表|是|[array]| |
|data>>list>>relate_list>>packing_type_name|包装名称|是|[string]|混装商品|
|data>>list>>relate_list>>product_valid_num|可用量|是|[int]|0|
|data>>list>>relate_list>>product_qc_num|待检量|是|[int]|0|
|data>>list>>relate_list>>shipment_order_list|关联关系列表|是|[array]| |
|data>>list>>relate_list>>shipment_order_list>>ispr_id|关联关系表ID|否|[int]| |
|data>>list>>relate_list>>shipment_order_list>>zid| |否|[int]| |
|data>>list>>relate_list>>shipment_order_list>>isp_id|发货计划表ID|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>isim_id|货件详情表ID|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>isil_id|发货单表ID|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>seq|发货计划批次号|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>shipment_plan_sn|发货计划单号|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>shipment_mws_sn|货件编号|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>shipment_list_sn|发货单号|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>shipment_plan_quantity|计划发货量|否|[int]| |
|data>>list>>relate_list>>shipment_order_list>>shipment_mws_quantity|货件关联量|否|[int]| |
|data>>list>>relate_list>>shipment_order_list>>shipment_list_quantity|发货单关联量|否|[int]| |
|data>>list>>relate_list>>shipment_order_list>>gmt_create|关联关系创建时间|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>gmt_modified|关联关系修改时间|否|[string]| |
|data>>list>>relate_list>>shipment_order_list>>company_id| |否|[int]| |
|data>>list>>relate_list>>shipment_order_list>>v_uuid| |否|[string]| |
|data>>list>>relate_list>>seqs|发货计划批次号（多个时使用,分隔）|否|[string]| |
|data>>list>>relate_list>>shipment_plan_quantity_total|发货计划发货量合计|否|[int]| |
|data>>list>>relate_list>>diff_num|差额|是|[int]|-1|
|data>>list>>relate_list>>sta_shipment_id|sta货件的shipmentId|是|[string]|sh8c22071a-b157-4847-aed6-c4adff747bxx|
|data>>list>>relate_list>>is_sta|是否sta货件，<br>1：是，<br>0：否|是|[string]| |
|data>>list>>relate_list>>sta_inbound_plan_id|sta货件所属的sta任务编号|是|[string]| |
|data>>list>>not_relate_list|未关联货件列表|是|[array]| |
|data>>list>>destination_fulfillment_center_id|物流中心编码|是|[string]|FTW1,BHX2,EUK5|
|data>>list>>status_name|状态名称|是|[string]|待发货|
|data>>list>>head_fee_type_name|头程分摊名称|是|[string]|按计费重|
|data>>list>>head_fee_type_name_new|新头程费分配名称方式： <br>0 产品-计费重（默认）<br> 1 产品-实重 <br>2 产品-体积重 <br>3 产品-数量<br> 4 自定义 <br>5 箱子-体积|是|[string]|产品-计费重|
|data>>list>>fileList|文件列表|是|[array]| |
|data>>list>>shipment_time_second|发货时间(精确到时分秒)|是|[string]|2023-10-23 18:23:40|
|data>>list>>is_delete|删除状态：0-未删除 1-已删除|是|[number]|0|
|data>>total| |是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "response_time": "2020-04-30 17:33:32",
    "data": {
        "list": [{
            "id": 25,
            "shipment_sn": "SP180720003",
            "status": 0,
            "shipment_time": "",
            "wname": "测试仓库",
            "create_user": "",
            "logistics_provider_id": "",
            "logistics_provider_name": "",
            "logistics_channel_name": "鸿捷--HKUPS美国红单",
            "expected_arrival_date": "",
            "actual_shipment_time": "",
            "etd_date": "",
            "eta_date": "",
            "delivery_date": "",
            "create_time": "2018-07-20",
            "gmt_create": "2018-07-20 15:14:18",
            "is_pick": 1,
            "is_print": 0,
            "pick_time": "",
            "print_num": 0,
            "head_fee_type": 0,
            "file_id": "",
            "update_time": "2018-07-20 15:14:18",
            "remark": "",
            "wid": 8,
            "is_return_stock": 0,
            "pay_status": 0,
            "audit_status": 0,
            "shipment_user": "",
            "is_exist_declaration": 0,
            "is_exist_clearance": 0,
            "third_party_order_mode": 0,
            "third_party_order_status": 0,
            "vat_code": "",
            "method_id": "",
            "method_name": "",
            "is_custom_shipment_time": 0,
            "logistics": [{
                "logistics_list_type": 1,
                "replace_tracking_number": "88803089941",
                "tracking_number": "8880308989",
                "tracking_no": "ta1234567",
                "transport_type": 2,
                "transport_type_name": "海运",
                "order_type_code": 4,
                "order_type_code_name": "其他",
                "shippers": "emc",
                "shippers_name": "长荣emc",
                "remark": "这里是备注字段"
            }],
            "relate_list": [{
                "mid": 318,
                "destination_fulfillment_center_id": "FTW1",
                "quantity_shipped": 190,
                "id": 1039,
                "wname": "测试仓库--吴萍",
                "shipment_sn": "SP180720003",
                "shipment_id": "FBA15D9PQN10",
                "shipment_status": "",
                "wid": 8,
                "pid": 318,
                "sid": 8,
                "sname": "PM1：-test6-A0",
                "num": 1,
                "pic_url": "http://ecx.images-amazon.com/images/I/31UvRfeNRPL._SL75_.jpg",
                "packing_type": 1,
                "fulfillment_network_sku": "xxxx",
                "sku": "10         1",
                "fnsku": "",
                "msku": "xxxx",
                "nation": "美国",
                "apply_num": 1,
                "product_id": 19873,
                "product_name": "林xxxx",
                "asin": "",
                "parent_asin": "",
                "remark": "",
                "status": 0,
                "is_combo": 1,
                "create_by_mws": 1,
                "whb_code_list": [],
                "packing_type_name": "混装商品",
                "product_valid_num": 0,
                "product_qc_num": 0,
                "shipment_order_list": [{
                    "ispr_id": 0,
                    "zid": 0,
                    "isp_id": "",
                    "isim_id": "",
                    "isil_id": "",
                    "seq": "",
                    "shipment_plan_sn": "",
                    "shipment_mws_sn": "",
                    "shipment_list_sn": "",
                    "shipment_plan_quantity": 0,
                    "shipment_mws_quantity": 0,
                    "shipment_list_quantity": 0,
                    "gmt_create": "",
                    "gmt_modified": "",
                    "company_id": 0,
                    "v_uuid": ""
                }],
                "seqs": "",
                "shipment_plan_quantity_total": 0,
                "diff_num": -1,
                "sta_shipment_id": "",
                "is_sta": "",
                "sta_inbound_plan_id": ""
            }],
            "not_relate_list": [],
            "destination_fulfillment_center_id": "FTW1,BHX2,EUK5",
            "status_name": "待发货",
            "head_fee_type_name": "按计费重",
            "head_fee_type_name_new": "产品-计费重",
            "fileList": [],
            "shipment_time_second": "2023-10-23 18:23:40",
            "is_delete": 0
        }],
        "total": 1
    }
}
```
