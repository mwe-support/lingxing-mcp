# 查询货件列表
支持查询FBA货件，对应系统【FBA】>【FBA货件】数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/fba_report/shipmentList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id，多个以英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[string]|11,22|
|start_date|货件创建开始日期，格式：Y-m-d，左闭右开|是|[string]|2019-07-12|
|end_date|货件创建截止日期，格式：Y-m-d，左闭右开|是|[string]|2019-07-13|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|100|
|shipment_id|货件单号，多个以英文逗号隔开，仅支持精确搜索|否|[string]||
|shipment_status|货件状态，多个以英文逗号分隔：<br>UNCONFIRMED<br>IN_TRANSIT<br>DELIVERED<br>CHECKED_IN<br>ABANDONED<br><br>DELETED<br>CLOSED<br>CANCELLED<br>WORKING<br>RECEIVING<br>SHIPPED<br>READY_TO_SHIP|否|[string]|DELETED|
|extra_date_field|根据start_extra_date和end_extra_date日期范围查询：<br>update 货件修改日期【默认值为update，目前只支持查询货件修改日期】|否|[string]|update|
|start_extra_date|开始日期，格式：Y-m-d，左闭右开|否|[string]|2022-07-14|
|end_extra_date|结束日期，格式：Y-m-d，左闭右开|否|[string]|2022-07-15|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/data/fba_report/shipmentList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "end_date": "2024-10-10",
    "offset": 0,
    "length": 100,
    "sid": "10",
    "start_date": "2024-04-01"
}'
```
## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|total|总数|是|[int]|1|
|data|响应数据|是|[object]| |
|data>>list|数据列表|是|[array]| |
|data>>list>>id|唯一记录id|是|[int]|10407|
|data>>list>>sid|店铺id|是|[int]|2|
|data>>list>>seller|店铺名称|是|[string]| |
|data>>list>>uid|创建人id|是|[int]| |
|data>>list>>username|创建人姓名|是|[string]| |
|data>>list>>shipment_id|亚马逊货件编号|是|[string]| |
|data>>list>>shipment_name|货件名称|是|[string]|FBA (13/08/2020, 02:58) - 1|
|data>>list>>sta_shipment_id|亚马逊货件id（sta货件时返回）	|是|[string]| |
|data>>list>>sta_inbound_plan_id|亚马逊货件编号（sta货件时返回）|是|[string]| |
|data>>list>>sta_plan_name|STA任务名称（sta货件时返回）|是|[string]| |
|data>>list>>is_closed|是否是已完成状态：0 进行中，1 已完成|是|[int]|1|
|data>>list>>shipment_status|状态：<br>WORKING：卖家已创建货件，但尚未发货<br>SHIPPED：承运人已取件<br>IN_TRANSIT：承运人已通知亚马逊配送中心，知晓货件的存在<br>DELIVERED：承运人已将货件配送至亚马逊配送中心<br>CHECK_IN：货件已在亚马逊配送中心的收货区域登记<br>RECEIVING：货件已到达亚马逊配送中心，但有部分商品尚未标记为已收到<br>CLOSED：货件已到达亚马逊配送中心，且所有商品已标记为已收到<br>CANCELLED：卖家在将货件发送至亚马逊配送中心后取消了货件<br>DELETE：卖家在将货件发送至亚马逊配送中心前取消了货件<br>ERROR：货件出错，但其并非亚马逊处理|是|[string]|CLOSED|
|data>>list>>gmt_modified|数据更新时间|是|[string]|2020-10-11 10:59|
|data>>list>>gmt_create|数据创建时间|是|[string]|2020-08-13 23:25|
|data>>list>>sync_time|同步时间【已废弃】|是|[string]|2020-10-11 10:59|
|data>>list>>destination_fulfillment_center_id|物流中心编码|是|[string]|BHX1|
|data>>list>>is_synchronous|是否erp创建：0 erp创建，1 亚马逊后台同步|是|[int]|1|
|data>>list>>is_uploaded_box|是否已上传装箱信息：0 未上传，1 已上传|是|[int]|0|
|data>>list>>is_sta|是否sta货件：0 否，1 是|是|[int]|0|
|data>>list>>shipping_mode|货件类型(GROUND_SMALL_PARCEL 小包裹快递（SPD）、FREIGHT_LTL 汽运零担（LTL）) |是|[string]||
|data>>list>>shipping_solution|承运人(USE_YOUR_OWN_CARRIER 其他承运人、AMAZON_PARTNERED_CARRIER 亚马逊合作承运人)|是|[string]||
|data>>list>>alpha_code|承运方式编码 |是|[string]||
|data>>list>>alpha_name|承运方式名称 |是|[string]||
|data>>list>>sta_shipment_date|发货日期 格式：yyyy-MM-dd|是|[string]||
|data>>list>>sta_delivery_start_date|送达时段-开始时间 格式：yyyy-MM-dd HH:mm:ss|是|[string]||
|data>>list>>sta_delivery_end_date|送达时段-结束时间 格式：yyyy-MM-dd HH:mm:ss|是|[string]||
|data>>list>>tracking_number_list|追踪编号（SPD类型货件时返回） |是|[array]||
|data>>list>>tracking_number_list>>box_id|箱号 |是|[string]||
|data>>list>>tracking_number_list>>tractracking_numberkingNumber|追踪编号 |是|[string]||
|data>>list>>bill_of_lading_number|提货单号（BOL） |是|[string]||
|data>>list>>freight_bill_number|跟踪编号（PRO） |是|[string]||
|data>>list>>item_list|子项数据|是|[array]| |
|data>>list>>item_list>>msku|MSKU|是|[string]| |
|data>>list>>item_list>>fnsku|FNSKU|是|[string]| |
|data>>list>>item_list>>sku|SKU|是|[string]| |
|data>>list>>item_list>>quantity_shipped|当前申报量|是|[int]|518|
|data>>list>>item_list>>init_quantity_shipped|货件初始申报量|是|[int]|518|
|data>>list>>item_list>>quantity_received|签收数量：亚马逊配送中心已接收的商品数量|是|[int]|511|
|data>>list>>item_list>>quantity_shipped_local|已发货数量（本地数据）|是|[int]| |
|data>>list>>item_list>>quantity_in_case|每个包装箱中的商品数量|是|[int]|37|
|data>>list>>item_list>>prep_details|预处理明细|是|[string]| |
|data>>list>>item_list>>prep_instruction|预处理操作：大多数为Labeling|是|[string]|Labeling|
|data>>list>>item_list>>prep_owner|预处理拥有者：AMAZON,SELLER,NONE；大多数为SELLER |是|[string]|AMAZON|
|data>>list>>item_list>>prep_label_owner|标签类型：AMAZON,SELLER,NONE	|是|[string]|AMAZON|
|data>>list>>item_list>>expiration|有效期 |是|[string]||
|data>>list>>item_list>>prep_owner|预处理拥有者：大多数为SELLER|是|[string]|SELLER|
|data>>list>>item_list>>release_date|生产日期|是|[string]| |
|data>>list>>item_list>>ware_house_storage_id|库存明细id|是|[int]| |
|data>>list>>item_list>>shipment_plan_list|关联的发货计划单号|是|[array]| |
|data>>list>>item_list>>shipment_plan_list>>shipment_plan_sn|发货计划单号|是|[string]| |
|data>>list>>working_time|WORKING时间|是|[string]|2023-04-24 11:35|
|data>>list>>shipped_time|SHIPPED时间|是|[string]|2023-04-24 17:35|
|data>>list>>receiving_time|RECEIVING时间|是|[string]|2023-04-24 17:35|
|data>>list>>closed_time|CLOSED时间|是|[string]|2023-04-24 17:35|
|data>>list>>reference_id|Reference ID|是|[string]|xxxxxx|
|data>>list>>ship_from_address|发货地址|是|[object]| |
|data>>list>>ship_from_address>>name|名称|是|[string]|测试发货名称|
|data>>list>>ship_from_address>>country_code|国家编码|是|[string]|CN|
|data>>list>>ship_from_address>>state_or_province_code|省(州)|是|[string]|广东省|
|data>>list>>ship_from_address>>city|城市|是|[string]|深圳|
|data>>list>>ship_from_address>>region|区|是|[string]| |
|data>>list>>ship_from_address>>address_line1|街道地址1|是|[string]|测试街道111|
|data>>list>>ship_from_address>>address_line2|街道地址2|是|[string]| |
|data>>list>>ship_from_address>>postal_code|邮编|是|[string]|rere2222|
|data>>list>>ship_from_address>>phone|联系电话|是|[string]|15966786622|
|data>>list>>ship_to_address|配送地址|是|[object]| |
|data>>list>>ship_to_address>>name|名称|是|[string]|FTW1名称|
|data>>list>>ship_to_address>>country_code|国家编码|是|[string]|AG|
|data>>list>>ship_to_address>>state_or_province_code|省(州)|是|[string]|省1|
|data>>list>>ship_to_address>>city|城市|是|[string]|城市1|
|data>>list>>ship_to_address>>region|区|是|[string]|区1|
|data>>list>>ship_to_address>>address_line1|街道地址1|是|[string]|地址1|
|data>>list>>ship_to_address>>address_line2|街道地址2|是|[string]|地址2|
|data>>list>>ship_to_address>>postal_code|邮编|是|[string]|123456|
|data>>list>>ship_to_address>>doorplate|门牌号|是|[string]|12|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "1859414A-17D8-7475-EA63-781ED827DA57",
    "response_time": "2024-12-18 15:29:35",
    "data": {
        "list": [
            {
                "id": 494,
                "sid": 10,
                "uid": 0,
                "shipment_id": "",
                "shipment_name": "",
                "is_closed": 1,
                "shipment_status": "CLOSED",
                "gmt_modified": "2024-11-30 12:00",
                "gmt_create": "2024-10-09 15:22",
                "sync_time": "",
                "destination_fulfillment_center_id": "",
                "username": "",
                "seller": "",
                "item_list": [
                    
                    {
                        "id": 147819,
                        "zid": 1,
                        "msku": "",
                        "fnsku": "",
                        "quantity_shipped": 18,
                        "init_quantity_shipped": 18,
                        "quantity_received": 18,
                        "quantity_shipped_local": 18,
                        "quantity_in_case": 0,
                        "prep_details": "",
                        "prep_instruction": "",
                        "prep_owner": "",
                        "release_date": "",
                        "ware_house_storage_id": 0,
                        "shipment_plan_list": [],
                        "sku": ""
                    }
                ],
                "is_synchronous": 1,
                "is_uploaded_box": 0,
                "working_time": "2024-10-09 15:22",
                "shipped_time": "",
                "receiving_time": "2024-10-26 19:24",
                "closed_time": "2024-11-28 04:11",
                "reference_id": "",
                "ship_from_address": {
                    "name": "",
                    "country_code": "",
                    "state_or_province_code": "",
                    "city": "",
                    "region": "",
                    "address_line1": "",
                    "address_line2": "",
                    "postal_code": "",
                    "phone": ""
                },
                "ship_to_address": {
                    "name": "",
                    "country_code": "",
                    "state_or_province_code": "",
                    "city": "",
                    "region": "",
                    "address_line1": "",
                    "address_line2": "",
                    "postal_code": "",
                    "doorplate": ""
                }
            }
        ]
    },
    "total": 1
}
```
