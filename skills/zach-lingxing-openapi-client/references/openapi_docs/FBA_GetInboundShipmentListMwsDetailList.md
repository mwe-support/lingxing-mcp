# 批量查询发货单详情
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|shipment_sn_arr|发货单号数组，上限50|是|[array]|["SP230601024"]|
| return_deleted | 是否返回已删除数据: false-否(默认)，true-是 |否|[boolean]|false|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "shipment_sn_arr": ["SP230601024"]
}'
```

## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|8A221558-5272-0032-DBF0-C9CAD7353A9E|
|response_time|响应时间|是|[string]|2022-03-09 11:41:17|
|data|响应数据|是|[array]| |
|data>>id|发货单ID|是|[int]|6413|
|data>>tracking_id|物流追踪(运单)ID|是|[int]|0|
|data>>shipment_sn|发货单号|是|[string]|SP220302002|
|data>>status|发货单状态，<br>-1 : 待配货 <br>0：待发货，<br>1：已发货，<br>3：已作废，<br>4：已删除|是|[int]|-1|
|data>>shipment_time|发货时间|是|[string]|2023-03-14 15:48:51|
|data>>wid|仓库ID|是|[int]|1|
|data>>gmt_modified|修改时间|是|[string]|2022-03-02 11:10:51|
|data>>gmt_create|创建时间|是|[string]|2022-03-02 11:10:49|
|data>>remark|备注|是|[string]| |
|data>>creator_uid|创建人UID|是|[int]|129067|
|data>>opt_uid|最后操作人UID|是|[int]|129067|
|data>>msku_count|种类数|是|[int]|1|
|data>>quantity_total|发货总量|是|[int]|0|
|data>>logistics_channel_id|渠道商ID|是|[int]|0|
|data>>confirm_uid|确认人UID|是|[int]|0|
|data>>shipment_uid|发货人UID|是|[int]|0|
|data>>confirm_time|确认时间(时间戳格式)|是|[int]|0|
|data>>expected_arrival_date|预计到货日期|是|[string]| |
|data>>is_related|1=关联；0=不关联|是|[int]|0|
|data>>is_whb_checked|1=自动选择仓位扣减；<br>0=不选择仓位扣减|是|[int]|0|
|data>>head_fee_type|头程费分配方式：<br> 0 产品-计费重（默认）<br> 1 产品-实重<br> 2 产品-体积重 <br>3 产品-数量<br> 4 自定义 <br>5 箱子-体积|是|[int]|0|
|data>>is_points_behind|是否分抛计算(0:否,1:是)|是|[int]|1|
|data>>points_behind_coeffient|分抛系数(0-100)|是|[int]|1|
|data>>is_return_stock|是否恢复库存，<br>0=否，<br>1=是|是|[int]|0|
|data>>ware_house_bak_name|仓库名称(作为被删仓库的备用值)|是|[string]|xxx|
|data>>is_print|是否打印拣货单<br>（0：未打印，1：已打印）|是|[int]|0|
|data>>print_num|打印次数|是|[int]|0|
|data>>is_pick|是否拣货<br>（0：未拣货，1:已拣货）|是|[int]|0|
|data>>pick_time|完成拣货时间|是|[string]|2022-05-06|
|data>>print_time|最后一次打印时间|是|[int]|1677229505|
|data>>etd_date|开船时间|是|[string]|2022-05-06|
|data>>eta_date|预计到港时间|是|[string]|2022-05-06|
|data>>delivery_date|实际妥投时间|是|[string]|2022-05-06|
|data>>order_logistics_status|订单物流状态|是|[string]|2022-05-06|
|data>>shipment_user|发货人|是|[string]|xxx|
|data>>wname|仓库名称|是|[string]|仓库1|
|data>>create_user|创建人|是|[string]|超级管理员|
|data>>file_id|附件文件|是|[string]|1|
|data>>actual_shipment_time|实际发货时间|是|[string]|2023-03-14|
|data>>logistics_channel_name|物流渠道名称|是|[string]|xxxx|
|data>>is_delete|0-未删除|是|[int]|0|
|data>>destination_fulfillment_center_id|物流中心编码|是|[string]|xasf|
|data>>cancel_time|作废时间(时间戳格式)|是|[int]|0|
|data>>logistics_provider_id|物流商ID|是|[int]|0|
|data>>logistics_provider_name|物流商名称|是|[string]|0|
|data>>transportation_cost_status|物流费用填写状态，<br>1：全部填写，<br>2：部分填写，<br>3：全未填写|是|[int]|3|
|data>>other_cost_status|其他费用填写状态<br>，1：全部填写，<br>2：部分填写，<br>3：全未填写|是|[int]|3|
|data>>pay_status|付款状态<br>0：未申请，<br>1：已申请，<br>2：部分付款，<br>3：已付清，<br>4：无|是|[int]|4|
|data>>predicted_transportation_cost_status|预估物流费用填写状态，<br>1：全部填写，<br>2：部分填写，<br>3：全未填写|是|[int]|3|
|data>>predicted_other_cost_status|预估其他费用填写状态，<br>1：全部填写，<br>2：部分填写，<br>3：全未填写|是|[int]|3|
|data>>audit_status|审批状态，<br>121：待审核，<br>122：驳回，<br>123：通过，<br>124：作废|是|[int]|0|
|data>>stash_shipment_uid|暂存发货人UID（审批流专用）|是|[int]|0|
|data>>stash_shipment_time|暂存发货时间（审批流专用）|是|[int]|0|
|data>>is_relate_aux|是否关联辅料，<br>0：否，<br>1：是|是|[int]|1|
|data>>items|商品列表|是|[array]| |
|data>>items>>id|商品明细ID|是|[int]|40288|
|data>>items>>pid|货件明细ID|是|[int]|0|
|data>>items>>inbound_shipment_list_id|发货单ID|是|[int]|6413|
|data>>items>>box_num|箱数|是|[int]|0|
|data>>items>>num|发货数量|是|[int]|1|
|data>>items>>wid|仓库ID|是|[int]|1|
|data>>items>>ware_house_storage_id|已作废字段|是|[int]|0|
|data>>items>>product_id|本地商品ID|是|[int]|3322|
|data>>items>>sku|SKU|是|[string]|测试组合商品sku|
|data>>items>>fnsku|仓库FNSKU|是|[string]|FN24B265B|
|data>>items>>status|状态|是|[int]|-1|
|data>>items>>shipment_time|发货时间|是|[int]|0|
|data>>items>>aux_cost|辅料费用|是|[string]|0.0000|
|data>>items>>fba_stock_cost|fba库存费用|是|[string]|0.0000|
|data>>items>>fee_cost|仓库费用|是|[string]|0.0000|
|data>>items>>stock_cost|仓库发货成本价|是|[string]|0.0000|
|data>>items>>tax_amount|税费值|是|[string]|0.00|
|data>>items>>tax_currency|税费币种|是|[string]|USD|
|data>>items>>create_time| |是|[int]|0|
|data>>items>>update_time| |是|[int]|0|
|data>>items>>gmt_modified|更新时间|是|[string]|2022-03-02 11:10:51|
|data>>items>>gmt_create|创建时间|是|[string]|2022-03-02 11:10:51|
|data>>items>>cost_weight|每个商品对应的计费重(体积重)|是|[string]|0.0000|
|data>>items>>total_transport_cost|总费用(商品的运费和税费之和)|是|[string]|0.0000|
|data>>items>>cg_package_length|包装规格（CM）长|是|[string]|0.00|
|data>>items>>cg_package_width|包装规格（CM）宽|是|[string]|0.00|
|data>>items>>cg_package_height|包装规格（CM）高|是|[string]|0.00|
|data>>items>>cg_product_gross_weight|商品毛重（G）|是|[string]|0.00|
|data>>items>>calculate_tax_amount|税费值(人民币)|是|[string]|0.0000|
|data>>items>>product_name|商品名称|是|[string]|测试组合商品品名|
|data>>items>>whb_code|仓位编码列表|是|[array]| |
|data>>items>>sname|店铺名称|是|[string]|店铺7|
|data>>items>>nation|店铺所在国家|是|[string]|日本|
|data>>items>>cg_product_net_weight|商品净重（G）|是|[string]|0.00|
|data>>items>>total_nw|总净重（G）|是|[string]|0.00|
|data>>items>>total_gw|总毛重（G）|是|[string]|0.00|
|data>>items>>shipment_plan_quantity|计划发货量|是|[int]|1|
|data>>items>>apply_num|申报量|是|[int]|0|
|data>>items>>remark|备注|是|[string]| |
|data>>items>>isp_id|发货计划id|是|[int]|514|
|data>>items>>is_combo|组合商品：0-否，1-是|是|[int]|1|
|data>>items>>create_by_mws|货件生成发货单: 0-否，1-是|是|[int]|0|
|data>>items>>cg_box_width|箱子宽度(CM)宽|是|[string]|0.00|
|data>>items>>cg_box_height|箱子宽度(CM)高|是|[string]|0.00|
|data>>items>>cg_box_weight|单箱重量（KG）|是|[string]|0.00|
|data>>items>>cg_box_net_weight|单箱净重（KG）|是|[string]|0.00|
|data>>items>>cg_box_gross_weight|单箱毛重（KG）|是|[string]|0.00|
|data>>items>>cg_box_length|箱子宽度(CM)长|是|[string]|0.00|
|data>>items>>cbm|CBM|是|[string]|0.00|
|data>>items>>product_mws_id|在线商品ID|是|[int]|3396|
|data>>items>>volume_weight|体积重|是|[string]|0.00|
|data>>items>>quantity_in_case|单箱数量|是|[int]|0|
|data>>items>>pic_url|图片URL|是|[string]||
|data>>items>>packing_type|混装类型：1：原装，2：原装|是|[int]|1|
|data>>items>>shipment_id|货件编号|是|[string]| |
|data>>items>>sid|店铺ID|是|[int]|7|
|data>>items>>wname|仓库名|是|[string]|仓库1|
|data>>items>>fulfillment_network_sku|listing的fnsku|是|[string]|FN24B265B|
|data>>items>>shipment_sn|发货单号|是|[string]|SP220302002|
|data>>items>>msku|seller_sku|是|[string]|MSKU00B2BEA|
|data>>items>>transport_cost|每个商品对应的头程价格|是|[string]|0.0000|
|data>>items>>diff_num|差额|是|[int]|0|
|data>>items>>mid|店铺所在国家ID|是|[null]| |
|data>>items>>shipment_order_sn|发货计划单号|是|[string]|R220124024|
|data>>items>>calculate_transportation_cost|运费（人民币）|是|[string]|0.0000|
|data>>items>>calculate_other_cost|其他费用(人民币)|是|[string]|0.0000|
|data>>items>>calculate_predicted_transportation_cost|预估运费（人民币）|是|[string]|0.000000|
|data>>items>>calculate_predicted_other_cost|预估其他费用(人民币)|是|[string]|0.000000|
|data>>items>>predicted_transport_cost|预估每个商品对应的头程价格|是|[string]|0.000000|
|data>>items>>predicted_total_transport_cost|预估总费用(预估物流费用和税费之和)|是|[string]|0.000000|
|data>>items>>destination_fulfillment_center_id|物流中心编码|是|[null]| |
|data>>items>>quantity_shipped|货件申报量|是|[int]|0|
|data>>items>>is_delete| |是|[null]| |
|data>>items>>shipment_status|货件状态|是|[null]| |
|data>>items>>quantity_receive|待到货量|是|[string]|0|
|data>>items>>is_relate_mws|关联货件：0-否，1-是|是|[int]|0|
|data>>items>>product_qc_num|待检量|是|[int]|0|
|data>>items>>product_valid_num|可用量|是|[int]|1|
|data>>items>>sku_box_key|产品装箱唯一键，发货单内唯一，可用于关联箱子信息|是|[string]|xxxxxxxxxxx|
|data>>items>>storage_list| |是|[array]| |
|data>>items>>storage_list>>fnsku|fnsku|是|[string]|fnakusdfa|
|data>>items>>storage_list>>wid|仓库ID|是|[int]|1|
|data>>items>>storage_list>>product_id|产品ID|是|[int]|3322|
|data>>items>>storage_list>>storage_hash_id|MD5(wid + '_' + product_id + '_' + fnsku)|是|[string]|3f98aeab2261ad638e63df0fc4a8e60d|
|data>>items>>storage_list>>product_valid_num|可用量|是|[int]|0|
|data>>items>>storage_list>>product_qc_num|待检量|是|[int]|0|
|data>>items>>storage_list>>quantity_receive|签收量|是|[string]|0|
|data>>items>>shipment_order_list| |是|[array]| |
|data>>items>>shipment_order_list>>ispr_id|关联关系表ID|是|[int]|25078|
|data>>items>>shipment_order_list>>isp_id|发货计划表ID|是|[int]|514|
|data>>items>>shipment_order_list>>isim_id|货件详情表ID|是|[int]|0|
|data>>items>>shipment_order_list>>isil_id|发货单表ID|是|[int]|6413|
|data>>items>>shipment_order_list>>isilm_id|发货单详情表ID|是|[int]|40288|
|data>>items>>shipment_order_list>>shipment_plan_sn|发货计划单号|是|[string]|R220124024|
|data>>items>>shipment_order_list>>shipment_mws_sn|货件编号|是|[string]|xxxxxxxxxx|
|data>>items>>shipment_order_list>>shipment_list_sn|发货单号|是|[string]|SP220302002|
|data>>items>>shipment_order_list>>shipment_plan_quantity|计划发货量|是|[int]|1|
|data>>items>>shipment_order_list>>shipment_mws_quantity|货件关联量|是|[int]|0|
|data>>items>>shipment_order_list>>shipment_list_quantity|发货单关联量|是|[int]|1|
|data>>items>>shipment_order_list>>gmt_create|创建时间|是|[string]|2022-03-02 11:10:51|
|data>>items>>shipment_order_list>>gmt_modified|修改时间|是|[string]|2022-03-02 11:10:51|
|data>>items>>shipment_order_list>>quantity_shipped|货件申报量|是|[null]|1|
|data>>items>>shipment_ids| |是|[array]| |
|data>>items>>shipment_ids>>quantity_shipped|建单数量|是|[string]|1|
|data>>items>>shipment_ids>>init_quantity_shipped|货件初始申报量|是|[string]|1|
|data>>items>>shipment_ids>>quantity|发货单发货量|是|[string]|1|
|data>>items>>shipment_ids>>id|自增ID|是|[string]|1|
|data>>items>>shipment_ids>>shipment_id|货件编号|是|[string]|xxxxxxxxx|
|data>>items>>cost_source|实际费用|是|[string]|实际费用|
|data>>items>>whb_code_list|仓位编码列表|是|[array]| |
|data>>items>>son_storage_arr|组合商品列表|否|[array]| |
|data>>items>>son_storage_arr>>product_id|产品id|是|[int]|3063|
|data>>items>>son_storage_arr>>product_image|产品图片|是|[string]||
|data>>items>>son_storage_arr>>pic_url|产品图片|是|[string]||
|data>>items>>son_storage_arr>>sku|SKU|是|[string]|SKU868EBEC|
|data>>items>>son_storage_arr>>product_name|品名|是|[string]|[演示数据]4K UHD 内存卡带适配器|
|data>>items>>son_storage_arr>>quantity|组合产品数量|是|[int]|1|
|data>>items>>son_storage_arr>>product_valid_num|可用量|是|[int]|0|
|data>>items>>son_storage_arr>>product_qc_num|待检量|是|[int]|0|
|data>>items>>son_storage_arr>>product_pending_num|待到货量|是|[int]|0|
|data>>items>>max_product_valid_num|组合商品最大可用量|否|[int]|1|
|data>>items>>sta_shipment_id|sta的shipmentId|是|[string]| |
|data>>items>>is_sta|是否sta货件，1：是，0：否|是|[string]| |
|data>>items>>sta_inbound_plan_id|sta任务编号|是|[string]| |
|data>>logistics|物流信息列表（旧版物流信息）|是|[array]| |
|data>>logistics>>id|物流信息ID（旧版物流信息）|是|[int]|1407|
|data>>logistics>>inbound_shipment_list_mws_id|发货单ID（旧版物流信息）|是|[int]|5528|
|data>>logistics>>gmt_modified|修改时间（旧版物流信息）|是|[string]|2021-12-23 14:48:42|
|data>>logistics>>gmt_create|创建时间（旧版物流信息）|是|[string]|2021-10-29 14:13:26|
|data>>logistics>>tracking_number|物流商号（旧版物流信息）|是|[string]|物流商单号123|
|data>>logistics>>replace_tracking_number|跟踪单号（旧版物流信息）|是|[string]|跟踪号123|
|data>>logistics>>transportation_cost|实际物流费用（旧版物流信息）|是|[string]|100.00|
|data>>logistics>>other_cost|实际其他费用（旧版物流信息）|是|[string]|100.00|
|data>>logistics>>transportation_currency|实际物流费用币种（旧版物流信息）|是|[string]|CNY|
|data>>logistics>>other_currency|实际其他费用币种（旧版物流信息）|是|[string]|USD|
|data>>logistics>>other_cost_remark|实际其他费用备注（旧版物流信息）|是|[string]|我是一个备注|
|data>>logistics>>predicted_transportation_cost|预估物流费用（旧版物流信息）|是|[string]|100.00|
|data>>logistics>>predicted_transportation_currency|预估物流费用币种（旧版物流信息）|是|[string]|CNY|
|data>>logistics>>predicted_other_cost|预估其他费用（旧版物流信息）|是|[string]|0.00|
|data>>logistics>>predicted_other_currency|预估其他费用币种（旧版物流信息）|是|[string]|CNY|
|data>>logistics>>predicted_other_cost_remark|预估其他费用备注（旧版物流信息）|是|[string]| |
|data>>auxs|辅料列表|是|[array]| |
|data>>auxs>>isialm_id|辅料自增ID|是|[int]|149|
|data>>auxs>>aux_id|辅料产品ID|是|[int]|5455|
|data>>auxs>>pid|货件明细ID|是|[int]|0|
|data>>auxs>>num|商品发货数量|是|[int]|0|
|data>>auxs>>aux_sku|辅料SKU|是|[string]|7989879wewe|
|data>>auxs>>aux_name|辅料名称|是|[string]|广告纸|
|data>>auxs>>shipment_sn|发货单号|是|[string]|SP220302002|
|data>>auxs>>shipment_plan_sn|发货计划单号|是|[string]|xxxxxxx|
|data>>auxs>>shipment_id|货件编号|是|[string]|xxxxxxxx|
|data>>auxs>>inbound_shipment_list_id|发货计划ID|是|[int]|6413|
|data>>auxs>>cg_price|辅料单位成本|是|[string]|11.0000|
|data>>auxs>>cg_total_price|辅料总成本|是|[string]|11.0000|
|data>>auxs>>cg_product_net_weight|辅料净重|是|[string]|71.76|
|data>>auxs>>cg_product_length|箱子规格(CM)长|是|[string]|75.38|
|data>>auxs>>remark|备注|是|[string]| |
|data>>auxs>>cg_product_width|箱子规格(CM)宽|是|[string]|40.46|
|data>>auxs>>cg_product_height|箱子规格(CM)高|是|[string]|47.91|
|data>>auxs>>relation_product_msku|关联MSKU|是|[string]|MSKU00B2BEA|
|data>>auxs>>relation_type|1关联商品,2关联整单|是|[int]|1|
|data>>auxs>>relation_product_sku|关联SKU|是|[string]| |
|data>>auxs>>relation_product_fnsku|关联FNSKU|是|[string]|FN24B265B|
|data>>auxs>>aux_num|关联数量|是|[int]|1|
|data>>auxs>>relation_product_id|关联产品ID|是|[int]|3322|
|data>>auxs>>relation_isilm_id|关联发货单ID|是|[int]|0|
|data>>auxs>>update_uid|修改人UID|是|[int]|0|
|data>>auxs>>update_user|修改人|是|[string]|xxx|
|data>>auxs>>create_user|创建人|是|[string]|xxxx|
|data>>auxs>>create_uid|创建人UID|是|[int]|129067|
|data>>auxs>>aux_head_fee_type|辅料分摊类型<br> 1:按sku分摊,<br>2:实重分摊,<br>3:按体积重分摊,<br>:按计费重分摊|是|[int]|3|
|data>>auxs>>is_points_behind|是否分抛计算(0:否,1:是)|是|[int]|1|
|data>>auxs>>points_behind_coeffient|分抛系数(0-100)|是|[int]|1|
|data>>auxs>>create_time| |是|[int]|1646190650|
|data>>auxs>>update_time| |是|[int]|0|
|data>>auxs>>gmt_create|创建时间|是|[string]|2022-03-02 11:10:51|
|data>>auxs>>gmt_modified|修改时间|是|[string]|2022-03-02 11:10:51|
|data>>principals|权限人列表|是|[array]| |
|data>>principals>>isp_id|主键ID|是|[string]|250157647881658368|
|data>>principals>>shipment_sn|发货单号|是|[string]|SP220302002|
|data>>principals>>isil_id|发货单ID|是|[int]|6413|
|data>>principals>>principal_uid|权限人UID|是|[int]|129067|
|data>>principals>>operate_user|操作人|是|[string]|施振锋|
|data>>principals>>operate_uid|操作人UID|是|[int]|129067|
|data>>principals>>principal_user|权限人|是|[string]|施振锋|
|data>>principals>>gmt_modified|修改时间|是|[string]|2022-03-02 11:10:52|
|data>>principals>>gmt_create|创建时间|是|[string]|2022-03-02 11:10:52|
|data>>msg| |是|[string]|xxx|
|data>>status_name|状态名称|是|[string]|待配货|
|data>>last_update_time|最后修改日期|是|[string]|2022-03-02 11:10:49|
|data>>head_fee_type_name|头程费用名称|是|[string]|按计费重|
|data>>fileList|附件列表|是|[array]| |
|data>>box_type|装箱类型：<br>SINGLE-每箱只允许一款SKU，<br>MULTIPLE-每箱允许多款SKU|是|[string]|MULTIPLE|
|data>>box_remark|装箱备注|是|[string]|多个SKU装箱|
|data>>logistics_list_type|物流信息版本0旧版1新版|是|[object]|0|
|data>>head_logistics_list|新版物流信息列表(logistics_list_type = 1时才有意义)|是|[array]| |
|data>>head_logistics_list>>track_list|轨迹信息|否|[array]| |
|data>>head_logistics_list>>track_list>>tracking_no|查询单号|是|[string]|xxxxxx|
|data>>head_logistics_list>>track_list>>transport_type|运输类型 ：1快递；2海运；3空运；4其他；|是|[string]|1|
|data>>head_logistics_list>>track_list>>transport_type_name|运输类型 名称|是|[string]|快递|
|data>>head_logistics_list>>track_list>>order_type_code_name|单号类型 名称|是|[string]|5|
|data>>head_logistics_list>>track_list>>order_type_code|单号类型：<br>1.订舱号；<br>2.提单号；<br>3.箱号；<br>4.其他；<br>5跟踪单号；<br>6航班号<br> （注意：与运输类型有联动） 当transport_type=1只能传 5.跟踪单号 <br> 当transport_type=2只能传<br> 1.订舱号<br> 2.提单号<br>3.箱号 <br>4.其他<br> transport_type=3只能传 <br>2.提单号 <br>6.航班号<br> 当transport_type=4只能传 空|是|[string]|跟踪单号|
|data>>head_logistics_list>>track_list>>shippers_name|承运商 名称|是|[string]|xxx|
|data>>head_logistics_list>>track_list>>shippers|承运商|是|[string]|xxx|
|data>>head_logistics_list>>track_list>>remark|备注|否|[string]|xxxx|
|data>>head_logistics_list>>estimate_expenses_list|费用数组-预估费用数组|是|[object]| |
|data>>head_logistics_list>>estimate_expenses_list>>price|单价|是|[string]|1|
|data>>head_logistics_list>>estimate_expenses_list>>price_currency|单价币种|是|[string]|CNY|
|data>>head_logistics_list>>estimate_expenses_list>>logistics_fee|物流费用|是|[string]|1|
|data>>head_logistics_list>>estimate_expenses_list>>logistics_fee_currency|物流费用币种|是|[string]|CNY|
|data>>head_logistics_list>>estimate_expenses_list>>chargeable_weight|计费重|是|[string]|1|
|data>>head_logistics_list>>estimate_expenses_list>>total_fee|费用合计|是|[string]|1|
|data>>head_logistics_list>>estimate_expenses_list>>total_fee_currency|费用合计币种|是|[string]|CNY|
|data>>head_logistics_list>>estimate_expenses_list>>logistics_fee_gmt_create|物流费用-创建时间|是|[string]| |
|data>>head_logistics_list>>estimate_expenses_list>>logistics_fee_gmt_modified|物流费用-更新时间|是|[string]| |
|data>>head_logistics_list>>estimate_expenses_list>>tax_fee_gmt_create|税费-创建时间|是|[string]| |
|data>>head_logistics_list>>estimate_expenses_list>>tax_fee_gmt_modified|税费-更新时间|是|[string]| |
|data>>head_logistics_list>>estimate_expenses_list>>other_fee_arr|其他费数组|是|[array]| |
|data>>head_logistics_list>>estimate_expenses_list>>other_fee_arr>>fee_type_id|其他费ID|是|[string]|111111|
|data>>head_logistics_list>>estimate_expenses_list>>other_fee_arr>>name|其他费名称|是|[string]|xxxxxx|
|data>>head_logistics_list>>estimate_expenses_list>>other_fee_arr>>other_amount|其他费费用|是|[float]|1.00|
|data>>head_logistics_list>>estimate_expenses_list>>other_fee_arr>>other_currency|其他费币种|是|[string]|CNY|
|data>>head_logistics_list>>estimate_expenses_list>>other_fee_arr>>logistics_provider_id|多物流商费用的物流商ID|是|[string]|111111|
|data>>head_logistics_list>>actual_expenses_list|费用明细-实际费用数组 (参考estimate_expenses_list)|是|[object]| |
|data>>head_logistics_list>>actual_expenses_list>>price|单价|是|[object]|1|
|data>>head_logistics_list>>actual_expenses_list>>price_currency|单价币种|是|[string]|CNY|
|data>>head_logistics_list>>actual_expenses_list>>logistics_fee|物流费用|是|[string]|1|
|data>>head_logistics_list>>actual_expenses_list>>logistics_fee_currency|物流费用币种|是|[string]|CNY|
|data>>head_logistics_list>>actual_expenses_list>>chargeable_weight|计费重（kg）|是|[string]|1|
|data>>head_logistics_list>>actual_expenses_list>>total_fee|费用合计|是|[string]|1|
|data>>head_logistics_list>>actual_expenses_list>>total_fee_currency|费用合计币种|是|[string]|CNY|
|data>>head_logistics_list>>actual_expenses_list>>tax_fee|实际税费|是|[string]|1|
|data>>head_logistics_list>>actual_expenses_list>>tax_fee_currency|实际税费币种|是|[string]|CNY|
|data>>head_logistics_list>>actual_expenses_list>>other_fee_arr|其他费数组|是|[array]| |
|data>>head_logistics_list>>actual_expenses_list>>other_fee_arr>>fee_type_id|其他费ID|是|[string]|12312312321312312|
|data>>head_logistics_list>>actual_expenses_list>>other_fee_arr>>name|其他费名称|是|[string]|xxxxx|
|data>>head_logistics_list>>actual_expenses_list>>other_fee_arr>>other_amount|其他费费用|是|[string]|1|
|data>>head_logistics_list>>actual_expenses_list>>other_fee_arr>>other_currency|其他费币种|是|[string]|CNY|
|data>>head_logistics_list>>actual_expenses_list>>other_fee_arr>>logistics_provider_id|多物流商费用的物流商ID|是|[string]|111111|
|data>>box_list|箱规列表，每个子项代表一个箱规|否|[array]| |
|data>>box_list>>box_num|箱子数|是|[string]|3|
|data>>box_list>>cg_box_length|箱子长|是|[string]|20|
|data>>box_list>>cg_box_width|箱子宽|是|[string]|30|
|data>>box_list>>cg_box_height|箱子高|是|[string]|40|
|data>>box_list>>cg_box_weight|箱子重|是|[string]|1.33|
|data>>box_list>>box_range|箱子范围|是|[string]|1-4|
|data>>box_list>>box_codes|自定义箱号,通过\n分隔|是|[string]| |
|data>>box_list>>box_skus|箱子内包含的SKU信息，SINGLE类型装箱，只会有一个子项，MULTIPLE类型装箱，可能会有多个子项|是|[array]| |
|data>>box_list>>box_skus>>sku_box_key|产品装箱唯一键，可通过此键关联产品|是|[string]|63BB81CF-0650-45C9-5BDB-26B58E13565F|
|data>>box_list>>box_skus>>sku|SKU|是|[string]|0530-1|
|data>>box_list>>box_skus>>shipment_id|货件编号|是|[string]|FBA16XNMN3N4|
|data>>box_list>>box_skus>>seller_name|店铺名|是|[string]|8P-SPEED|
|data>>box_list>>box_skus>>msku|MSKU|是|[string]|Black_ Head_Rope|
|data>>box_list>>box_skus>>fnsku|FNSKU|是|[string]|B09MT3989Q|
|data>>box_list>>box_skus>>product_name|品名|是|[string]|新的商品|
|data>>box_list>>box_skus>>quantity_in_case|单箱数量|是|[string]|32|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "request_id": "17265BB1-88CE-8DE4-12D4-022C161EC3F3",
    "error_details": "",
    "data": [{
        "id": 8163,
        "tracking_id": 0,
        "shipment_sn": "SP230213001",
        "status": 0,
        "shipment_time": "",
        "wid": 1,
        "gmt_modified": "2023-02-24 17:04:26",
        "gmt_create": "2023-02-13 15:51:02",
        "remark": "duo111",
        "creator_uid": 287,
        "opt_uid": 287,
        "msku_count": 1,
        "quantity_total": 1,
        "logistics_channel_id": 1722,
        "confirm_uid": 0,
        "shipment_uid": 0,
        "confirm_time": 0,
        "expected_arrival_date": "2023-02-13",
        "is_related": 0,
        "is_whb_checked": 0,
        "head_fee_type": 1,
        "is_return_stock": 0,
        "ware_house_bak_name": "",
        "is_print": 0,
        "print_num": 0,
        "is_pick": 0,
        "pick_time": "1973-12-22",
        "print_time": 125415524,
        "etd_date": "",
        "eta_date": "",
        "delivery_date": "",
        "order_logistics_status": "",
        "shipment_user": "",
        "wname": "仓库1",
        "create_user": "冯权",
        "file_id": "",
        "actual_shipment_time": "",
        "logistics_channel_name": "Beatles-5",
        "is_delete": 0,
        "destination_fulfillment_center_id": "FWA4",
        "cancel_time": 0,
        "logistics_provider_id": "15",
        "logistics_provider_name": "未定义1",
        "transportation_cost_status": 3,
        "other_cost_status": 3,
        "pay_status": 4,
        "predicted_transportation_cost_status": 1,
        "predicted_other_cost_status": 3,
        "audit_status": 0,
        "stash_shipment_uid": 0,
        "stash_shipment_time": 0,
        "is_relate_aux": 0,
        "is_exist_declaration": 1,
        "is_exist_clearance": 0,
        "is_points_behind": 0,
        "points_behind_coeffient": 0,
        "v_uuid": "287BCD46-21DF-FC0F-BB12-E3837B59EB16",
        "third_party_order_mode": 0,
        "third_party_logistics_wp_code": "",
        "third_party_order_status": 0,
        "third_party_order_status_code": "",
        "third_party_order_sn": "",
        "third_party_order_exception_reason": "",
        "is_change_label": 0,
        "label_replacement_option": 0,
        "is_signature": 0,
        "age_detection": 0,
        "is_insurance": 0,
        "insurance_value": "0.00",
        "lift_gate": 0,
        "is_relate_head_logistics": 1,
        "ware_operation_type": 0,
        "other_ware_operation": 0,
        "inventory_type": 0,
        "order_cod_currency": "",
        "is_split_prediction": 0,
        "stash_audit_users": "",
        "pick_num": 0,
        "vat_code": "",
        "head_fee_status": 0,
        "is_custom_cost": 0,
        "method_id": "241242581740101632",
        "method_name": "海派",
        "logistics_way_id": 241266354975649792,
        "scheme_id": 1722,
        "packing_task_sn": "",
        "estimated_shipment_date": "",
        "logistics_estimated_day": 0,
        "volume_parameter": 5000,
        "cost_source": 1,
        "is_custom_shipment_time": 0,
        "return_stock_type": 0,
        "cancel_reason": "",
        "is_auto_adjust": 0,
        "items": [{
            "id": 42115,
            "pid": 47042,
            "inbound_shipment_list_id": 8163,
            "box_num": 1,
            "num": 1,
            "pick_num": 0,
            "wid": 1,
            "ware_house_storage_id": 0,
            "product_id": 2117179,
            "sku": "0530-1",
            "fnsku": "XXXXXXXX",
            "seller_id": "16",
            "status": 0,
            "shipment_time": 0,
            "aux_cost": "0.0000",
            "fba_stock_cost": "0.0000",
            "fee_cost": "0.0000",
            "stock_cost": "0.0000",
            "tax_amount": "0.00",
            "tax_currency": "USD",
            "create_time": 0,
            "update_time": 0,
            "gmt_modified": "2023-02-13 15:51:05",
            "gmt_create": "2023-02-13 15:51:03",
            "cost_weight": "0.0000",
            "total_transport_cost": "0.000000",
            "cg_package_length": "56.00",
            "cg_package_width": "23.00",
            "cg_package_height": "123.00",
            "cg_product_gross_weight": "0.00",
            "calculate_tax_amount": "0.0000",
            "product_name": "新的商品",
            "whb_code": [],
            "sname": "8P-SPEED",
            "nation": "美国",
            "cg_product_net_weight": "0.00",
            "total_nw": "0.00",
            "total_gw": "0.00",
            "shipment_plan_quantity": 0,
            "apply_num": 1,
            "remark": "",
            "isp_id": 0,
            "is_combo": 0,
            "create_by_mws": 1,
            "cg_box_width": "125.00",
            "cg_box_height": "468.00",
            "cg_box_weight": "0.00",
            "cg_box_net_weight": "0.00",
            "cg_box_gross_weight": "0.00",
            "cg_box_length": "94.00",
            "cbm": "5.50",
            "product_mws_id": 10000864,
            "asin": "B09MT3989Q",
            "parent_asin": "B09MT3989Q",
            "volume_weight": "5499000.00",
            "quantity_in_case": 567,
            "pic_url": "https://image.distributetop.com/lingxing-erp/90124993550340096/20220907/1caa2240295640fb88cd131154b0517f.jpg",
            "packing_type": 1,
            "shipment_id": "FBA170YCSMQX",
            "sid": 16,
            "wname": "仓库1",
            "fulfillment_network_sku": "XXXXX",
            "shipment_sn": "SP230213001",
            "msku": "XXXXX",
            "transport_cost": "0.0000",
            "diff_num": -1,
            "mid": 1,
            "shipment_order_sn": "",
            "calculate_transportation_cost": "0.0000",
            "calculate_other_cost": "0.0000",
            "calculate_predicted_transportation_cost": "0.000000",
            "calculate_predicted_other_cost": "0.000000",
            "predicted_transport_cost": "0.0000",
            "predicted_total_transport_cost": "0.000000",
            "custom_stock_cost": "0.0000",
            "custom_aux_cost": "0.0000",
            "seller_name": "8P-SPEED",
            "tax_unit": "0.0000",
            "outbound_head_cost_unit": "0.0000",
            "purchase_price_unit": "0.0000",
            "outbound_cost_unit": "0.0000",
            "v_uuid": "4E62DEAD-F0FF-7C4A-F1A1-0E66878626BD",
            "gmt_migrate": "1970-01-01 00:00:00",
            "third_party_product_name": "",
            "third_party_product_code": "",
            "match_num": 0,
            "third_party_order_quantity": 0,
            "product_declared_value": "0.00",
            "label_replacement_qty": 0,
            "hs_code": "",
            "box_no": "",
            "box_pu_number": 0,
            "for_finance_cost": "0.000000",
            "label_file_id": 0,
            "sku_box_key": "bae70c58-3123-4fd8-b7db-40a8aaa23800",
            "custom_purchase_price_unit": "0.0000",
            "custom_outbound_cost_unit": "0.0000",
            "custom_outbound_head_cost_unit": "0.0000",
            "custom_fba_inbound_cost_unit": "0.0000",
            "list_item_volume_proportion": "0.000000",
            "destination_fulfillment_center_id": "FWA4",
            "quantity_shipped": 3,
            "is_delete": 0,
            "shipment_status": "WORKING",
            "warehouse_items": [{
                "inbound_shipment_item_list_mws_id": 42115,
                "isilmi_id": "0",
                "out_num": 0,
                "product_id": 2117179,
                "product_valid_num": 0,
                "seller_id": "",
                "seller_name": "",
                "storage_list": [],
                "storage_seller": [],
                "valid_storage_arr": [],
                "warehouse_fnsku": "",
                "whb_code": [],
                "wid": 0,
                "wname": ""
            }],
            "is_lock": 0,
            "lock_status": 1,
            "quantity_receive": 0,
            "is_relate_mws": 1,
            "product_qc_num": 0,
            "product_valid_num": 0,
            "storage_list": [],
            "shipment_order_list": [{
                "ispr_id": 33492,
                "isp_id": 0,
                "isim_id": 47042,
                "isil_id": 8163,
                "isilm_id": 42115,
                "shipment_plan_sn": "",
                "shipment_mws_sn": "FBA170YCSMQX",
                "shipment_list_sn": "SP230213001",
                "shipment_plan_quantity": 0,
                "shipment_mws_quantity": 3,
                "shipment_list_quantity": 1,
                "gmt_create": "2023-02-13 15:51:03",
                "gmt_modified": "2023-02-13 15:51:03",
                "v_uuid": "E96B64B8-5746-6FBB-2C65-E1D2553ED0D3",
                "quantity_shipped": 3,
                "seq": null
            }],
            "shipment_ids": [{
                "quantity_shipped": 5,
                "init_quantity_shipped": 3,
                "quantity": 1,
                "id": 47042,
                "shipment_id": "FBA170YCSMQX"
            }],
            "cost_source": "预估费用",
            "whb_code_list": [{
                "whb_code": "T-1-1",
                "whb_type": 5,
                "product_num": 1,
                "product_id": 2117179,
                "sku": "0530-1",
                "fnsku": "XXXXXXXX",
                "whb_code_name": "T-1-1"
            }],
            "valid_storage_arr": [{
                "whb_code": "T-1-1",
                "whb_type": 5,
                "product_num": 1,
                "product_id": 2117179,
                "sku": "0530-1",
                "fnsku": "XXXXXXXX",
                "whb_code_name": "T-1-1"
            }],
            "seqs": "",
            "asin_url": "https://www.amazon.com/dp/B09MT3989Q",
            "label_file_list": [],
            "all_out_num": 0
        }],
        "auxs": [],
        "principals": [{
            "isp_id": "250280871997517824",
            "shipment_sn": "",
            "isil_id": 8163,
            "principal_uid": 129164,
            "operate_user": "冯权",
            "operate_uid": 287,
            "principal_user": "陈育杰",
            "gmt_modified": "2023-02-13 15:51:05",
            "gmt_create": "2023-02-13 15:51:05",
            "v_uuid": "E9B3DEE0-05AF-9607-A983-B051D981E3FF"
        }],
        "declarations": [{
            "inbound_shipment_list_mws_id": 8163,
            "order_sn": "CD20230222003"
        }],
        "clearances": [],
        "third_party_order_file_list": [],
        "box_type": "SINGLE",
        "box_remark": "",
        "msg": "",
        "can_edit_logistics": 1,
        "disable_currency": {
            "transportation_cost": [],
            "other_cost": [],
            "tax_cost": []
        },
        "current_month": 1,
        "is_close_account_month": 0,
        "status_name": "待发货",
        "last_update_time": "2023-02-13 15:50:49",
        "head_fee_type_name": "按实重",
        "fileList": [],
        "box_list": [{
            "box_num": 1,
            "cg_box_length": "94.00",
            "cg_box_width": "125.00",
            "cg_box_height": "468.00",
            "cg_box_weight": "0.00",
            "box_range": "",
            "box_codes": "",
            "box_skus": [{
                "sku_box_key": "bae70c58-3123-4fd8-b7db-40a8aaa23800",
                "sku": "0530-1",
                "shipment_id": "FBA170YCSMQX",
                "seller_name": "8P-SPEED",
                "msku": "XXXXX",
                "fnsku": "XXXXXXXXX",
                "product_name": "新的商品",
                "quantity_in_case": 567
            }]
        }],
        "head_logistics_list": {
            "logistics_list_type": 0,
            "track_list": [{
                "tracking_no": "b",
                "transport_type": 1,
                "transport_type_name": "快递",
                "shippers_name": "",
                "shippers": "",
                "remark": "a",
                "order_type_code": 5,
                "order_type_code_name": "跟踪单号"
            }],
            "estimate_expenses_list": {
                "fee_type": 1,
                "logistics_fee": "2233.00",
                "price": 0,
                "price_currency": "CNY",
                "billing_way": 2,
                "chargeable_weight": "1099.80",
                "logistics_fee_currency": "CNY",
                "total_fee": "2233.00",
                "total_fee_currency": "CNY",
                "remark": "预估其他费用：￥0.00,实际其他费用：￥0.00,备注：；",
                "other_fee_arr": [{
                        "fee_type_id": "241259697847279616",
                        "name": "22",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241249750098461184",
                        "name": "自定义2",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241192037543649792",
                        "name": "5",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241192037528822272",
                        "name": "4",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241171895434473472",
                        "name": "哈哈哈4",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241170444310777856",
                        "name": "哈哈哈333",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241170444085714944",
                        "name": "黑五专用费",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241170442348691456",
                        "name": "哈哈哈12299",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "0",
                        "name": "其他费用",
                        "other_amount": "0.00",
                        "other_currency": ""
                    }
                ]
            },
            "actual_expenses_list": {
                "fee_type": 2,
                "logistics_fee": "0.00",
                "price": 0,
                "price_currency": "CNY",
                "billing_way": 2,
                "chargeable_weight": 0,
                "logistics_fee_currency": "",
                "total_fee": "0.00",
                "total_fee_currency": "CNY",
                "remark": "预估其他费用：￥0.00,实际其他费用：￥0.00,备注：；",
                "other_fee_arr": [{
                        "fee_type_id": "241259697847279616",
                        "name": "22",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241249750098461184",
                        "name": "自定义2",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241192037543649792",
                        "name": "5",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241192037528822272",
                        "name": "4",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241171895434473472",
                        "name": "哈哈哈4",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241170444310777856",
                        "name": "哈哈哈333",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241170444085714944",
                        "name": "黑五专用费",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "241170442348691456",
                        "name": "哈哈哈12299",
                        "other_amount": "0.00",
                        "other_currency": "CNY"
                    },
                    {
                        "fee_type_id": "0",
                        "name": "其他费用",
                        "other_amount": "0.00",
                        "other_currency": ""
                    }
                ]
            }
        },
        "logistics_list_type": 0,
        "logistics": [{
            "predicted_transportation_cost": "2233.00",
            "predicted_transportation_currency": "CNY",
            "other_cost_remark": "",
            "tracking_number": "a",
            "replace_tracking_number": "b",
            "predicted_other_cost": "0.00",
            "predicted_other_currency": "CNY",
            "transportation_cost": "0.00",
            "transportation_currency": "CNY",
            "other_cost": "0.00",
            "other_currency": "CNY"
        }]
    }]
}
```
