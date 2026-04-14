# 查询亚马逊Listing

### 唯一键说明：sid+seller_sku

支持根据亚马逊店铺查询【销售】>【Listing】模块数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws/listing` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明                                             | 必填 | 类型 | 示例 |
| :------------ |:-----------------------------------------------| :------------ | :------------ | :------------ |
|sid| 店铺id，多个使用英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[string]|1,16|
|is_pair| 是否配对：1 已配对，2 未配对                               |否|[int]|1|
|is_delete| 是否删除：0 未删除，1 已删除                               |否|[int]|0|
|pair_update_start_time| 【配对更新时间】的开始时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1 |否|[string]|2022-01-01 12:01:21|
|pair_update_end_time| 【配对更新时间】的结束时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1 |否|[string]|2022-10-01 12:01:21|
|listing_update_start_time| 【All Listing报表更新时间】的开始时间（此为零时区时间，格式Y-m-d H:i:s）          |否|[string]|2021-09-01 01:22:00|
|listing_update_end_time| 【All Listing报表更新时间】的结束时间（此为零时区时间，格式Y-m-d H:i:s）          |否|[string]|2022-10-01 11:22:00|
|search_field| 搜索支持字段：seller_sku、asin、sku                     |否|[string]|asin|
|search_value| 搜索值，上限10个                                      |否|[array]|["asin1","asin2"]|
|exact_search| 搜索模式：0 模糊搜索，1 精确搜索【默认值】                        |否|[int]|1|
|store_type| 商品类型，1-非低价商店 ，2-低价商店商品 |否|[int]|1|
|offset| 分页偏移量，默认0                                      |否|[int]|0|
|length| 分页长度，默认1000，上限1000                             |否|[int]|15|

## 请求示例
```
{
    "sid": "1,16",
    "is_pair": 1,
    "is_delete": 0,
    "pair_update_start_time": "2022-01-01 12:01:21",
    "pair_update_end_time": "2022-10-01 12:01:21",
    "listing_update_start_time": "2021-09-01 01:22:00",
    "listing_update_end_time": "2022-10-01 11:22:00",
    "search_field": "asin",
    "search_value": ["asin1", "asin2"],
    "exact_search": 1,
    "store_type": 1,
    "offset": 0,
    "length": 15
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|[]|
|request_id|请求链路id|是|[string]|83AAED7E-A5CF-6A09-6446-36F51AA3EEBA|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>listing_id|亚马逊定义的listing的id【可能为空】|是|[string]|xx|
|data>>sid|店铺id|是|[int]||
|data>>marketplace|国家|是|[string]|美国|
|data>>seller_sku|MSKU|是|[string]|xxxx|
|data>>fnsku|FNSKU|是|[string]|xxxx|
|data>>asin|ASIN|是|[string]|xxxxx|
|data>>parent_asin|父ASIN|是|[string]|xxx|
|data>>small_image_url|商品缩略图地址|是|[string]|https://xxx/xxx.gif|
|data>>status|状态：0 停售，1 在售|是|[int]|1|
|data>>is_delete|是否删除：0 否，1 是|是|[int]|0|
|data>>item_name|标题|是|[string]|xxxx|
|data>>local_sku|本地产品SKU|是|[string]|xxxx|
|data>>local_name|品名|是|[string]|product xxxx|
|data>>currency_code|币种|是|[string]|USD|
|data>>price|价格【不包含促销，运费，积分】|是|[string]|0.00|
|data>>landed_price|总价【包含了促销、运费、积分】|是|[string]|19.99|
|data>>listing_price|优惠价|是|[string]|19.99|
|data>>shipping|运费|是|[string]|0.00|
|data>>points|积分，日本站才有|是|[string]||
|data>>quantity|FBM库存|是|[int]|0|
|data>>afn_fulfillable_quantity|FBA可售|是|[int]|0|
|data>>afn_unsellable_quantity|FBA不可售|是|[int]|0|
|data>>reserved_fc_transfers|待调仓|是|[int]|0|
|data>>reserved_fc_processing|调仓中|是|[int]|0|
|data>>reserved_customerorders|待发货|是|[int]|0|
|data>>afn_inbound_shipped_quantity|在途|是|[int]|0|
|data>>afn_inbound_working_quantity|计划入库|是|[int]|0|
|data>>afn_inbound_receiving_quantity|入库中|是|[int]|0|
|data>>open_date|商品创建时间|是|[string]|2021-02-04 01:15:58 PST|
|data>>open_date_display|商品创建时间，格式：Y-m-d H:i:s+时区|是|[string]|2021-02-04 01:15:58 -08:00|
|data>>listing_update_date|All Listing报表更新时间 (注意：此为零时区时间)|是|[string]|2021-03-14 06:53:24|
|data>>seller_rank|排名|是|[int]|38214|
|data>>seller_brand|亚马逊品牌|是|[string]|38214|
|data>>seller_category|排名所属的类别(后续不再维护，改用seller_category_new)|是|[string]|Lighting|
|data>>review_num|评论条数|是|[int]|0|
|data>>last_star|星级评分|是|[string]|0|
|data>>fulfillment_channel_type|配送方式|是|[string]|FBM|
|data>>principal_info|负责人信息|是|[array]||
|data>>principal_info>>principal_uid|负责人用户id|是|[int]|xx|
|data>>principal_info>>principal_name|负责人姓名|是|[string]|xxx|
|data>>seller_category_new|排名所属的类别|是|[array]|["Beauty & Personal Care"]|
|data>>pair_update_time|配对更新时间 (注意：此为北京时间)|是|[string]|2022-02-23 18:10:45|
|data>>first_order_time|首单时间，格式：Y-m-d|是|[string]|2023-01-11|
|data>>on_sale_time|开售时间，格式：Y-m-d|是|[string]|2023-02-01|
|data>>store_type|商品类型，1-非低价商店 ，2-低价商店商品|是|[int]|1|
|data>>total_volume|销量-7天|是| [string] |100|
|data>>yesterday_volume| 销量-昨天 | 是   | [string] | 100|
| data>>fourteen_volume | 销量-14天| 是   | [string] |100|
| data>>thirty_volume | 销量-30天| 是   | [string] |100|
|data>>yesterday_amount|销售额-昨天|是|[String]|110.00|
|data>>seven_amount|销售额-7天|是|[String]|200.00|
|data>>fourteen_amount |销售额-14天|是|[String]|200.00|
|data>>thirty_amount|销售额-30天|是|[String]|300.00|
|data>>average_seven_volume|日均销量-7日|是|[string]|100|
|data>>average_fourteen_volume|日均销量-14日|是|[string]|100|
|data>>average_thirty_volume|日均销量-30日|是|[string]|100|
|data>>dimension_info|尺寸信息，没有尺寸信息时是空|是|[array]||
|data>>dimension_info>>item_height|商品高度|是|[string]|22.68|
|data>>dimension_info>>item_height_units_type|商品高度单位：<br>unkown未知单位<br>空字符串<br>inches(英寸复数,in)<br>inch(英寸单数,in)<br>centimeter(厘米,cm)<br>yard(码,yd)<br>veron(弗隆,fur)<br>foot(英尺,ft)|是|[string]|inch|
|data>>dimension_info>>item_length|商品长度|是|[string]|95.36|
|data>>dimension_info>>item_length_units_type|商品长度单位：<br>unkown未知单位<br>空字符串<br>inches(英寸复数,in)<br>inch(英寸单数,in)<br>centimeter(厘米,cm)<br>yard(码,yd)<br>veron(弗隆,fur)<br>foot(英尺,ft)|是|[string]|inch|
|data>>dimension_info>>item_width|商品宽度|是|[string]|20.55|
|data>>dimension_info>>item_width_units_type|商品宽度单位：<br>unkown未知单位<br>空字符串<br>inches(英寸复数,in)<br>inch(英寸单数,in)<br>centimeter(厘米,cm)<br>yard(码,yd)<br>veron(弗隆,fur)<br>foot(英尺,ft)|是|[string]|inch|
|data>>dimension_info>>item_weight|商品重量|是|[string]|5.41|
|data>>dimension_info>>item_weight_units_type|商品重量单位：<br>unkown未知单位<br>空字符串<br>pounds(ce(盎司,o磅,ib)<br>kg(千克,kg)<br>ounce(盎司,oz)<br>gram(克,g)<br>carat(克拉,ct)|是|[object]|unknown|
|data>>dimension_info>>package_height|包装高度|是|[string]|95.63|
|data>>dimension_info>>package_height_units_type|包装高度单位：<br>unkown未知单位<br>空字符串<br>inches(英寸复数,in)<br>inch(英寸单数,in)<br>centimeter(厘米,cm)<br>yard(码,yd)<br>veron(弗隆,fur)<br>foot(英尺,ft)|是|[string]|foot|
|data>>dimension_info>>package_length|包装长度|是|[string]|84.37|
|data>>dimension_info>>package_length_units_type|包装长度单位：<br>unkown未知单位<br>空字符串<br>inches(英寸复数,in)<br>inch(英寸单数,in)<br>centimeter(厘米,cm)<br>yard(码,yd)<br>veron(弗隆,fur)<br>foot(英尺,ft)|是|[string]||
|data>>dimension_info>>package_width|包装宽度|是|[string]|55.46|
|data>>dimension_info>>package_width_units_type|包装宽度单位：<br>unkown未知单位<br>空字符串<br>inches(英寸复数,in)<br>inch(英寸单数,in)<br>centimeter(厘米,cm)<br>yard(码,yd)<br>veron(弗隆,fur)<br>foot(英尺,ft)|是|[string]||
|data>>dimension_info>>package_weight|包装重量|是|[string]|11.74|
|data>>dimension_info>>package_weight_units_type|包装重量单位：<br>unkown未知单位<br>空字符串<br>pounds(ce(盎司,o磅,ib)<br>kg(千克,kg)<br>ounce(盎司,oz)<br>gram(克,g)<br>carat(克拉,ct)|是|[string]|pounds|
|data>>small_rank|小类排名信息|是|[array]||
|data>>small_rank>>category|小类名称|是|[string]|Laptop Stands|
|data>>small_rank>>rank|小类排名|是|[string]|223|
|data>>global_tags|全局标签|是|[array]||
|data>>global_tags>>globalTagId|全局标签ID|是|[string]|907204347399528686|
|data>>global_tags>>tagName|标签名称|是|[string]|TEST-005|
|data>>global_tags>>color|颜色|是|[string]|#3BB84C|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "83AAED7E-A5CF-6A09-6446-36F51AA3EEBA",
    "response_time": "2023-10-30 15:38:54",
    "total": 10,
    "data": [
            {
                "listing_id": "0623ZI1F5EF11",
                "seller_sku": "msku-1",
                "fnsku": "B085NPWXXX",
                "item_name": "xxxx ",
                "local_sku": "n2",
                "local_name": "组合2",
                "price": "11.10",
                "quantity": 11,
                "asin": "B0B4WP82XX",
                "parent_asin": "B0B4WP82XX",
                "small_image_url": "https://XXX/XXX.jpg",
                "status": 1,
                "is_delete": 0,
                "afn_fulfillable_quantity": 0,
                "reserved_fc_transfers": 0,
                "reserved_fc_processing": 0,
                "reserved_customerorders": 0,
                "afn_inbound_shipped_quantity": 0,
                "afn_unsellable_quantity": 0,
                "afn_inbound_working_quantity": 0,
                "afn_inbound_receiving_quantity": 0,
                "currency_code": "USD",
                "landed_price": "11.10",
                "listing_price": "11.10",
                "open_date": "2022-06-23 03:55:12 PDT",
                "listing_update_date": "2023-06-28 17:44:14",
                "seller_rank": 1112193,
                "seller_brand": "str",
                "seller_category": "[\"Beauty & Personal Care\"]",
                "review_num": 0,
                "last_star": "0.0",
                "fulfillment_channel_type": "FBM",
                "open_date_display": "2022-06-23 03:55:12 -07:00",
                "principal_info": [],
                "shipping": "0.00",
                "points": "0",
                "sid": 101,
                "store_type": 1,
                "total_volume": 100,
                "yesterday_volume": 100,
                "fourteen_volume": 100,
                "thirty_volume": 100,
                "yesterday_amount": "110.00",
                "seven_amount": "200.00",
                "thirty_amount": "300.00",
                "average_seven_volume": 100,
                "average_fourteen_volume": 100,
                "average_thirty_volume": 100
                "dimension_info": [
                    {
                        "item_height": "0.00",
                        "item_height_units_type": "",
                        "item_length": "0.00",
                        "item_length_units_type": "",
                        "item_width": "0.00",
                        "item_width_units_type": "",
                        "item_weight": "0.00",
                        "item_weight_units_type": "",
                        "package_height": "0.00",
                        "package_height_units_type": "",
                        "package_length": "0.00",
                        "package_length_units_type": "",
                        "package_width": "0.00",
                        "package_width_units_type": "",
                        "package_weight": "0.00",
                        "package_weight_units_type": ""
                    }
                ],
                "pair_update_time": "2023-10-30 15:25:51",
                "small_rank": [
                    {
                        "category": "Hair Elastics & Ties",
                        "rank": 13758
                    }
                ],
                "on_sale_time": "2023-10-04",
                "global_tags":[
                    {
                    "globalTagId": "907204347399528686",
                    "tagName": "TEST-005",
                    "color": "#3BB84C"
                    }
                ],
                "first_order_time": "",
                "marketplace": "美国",
                "seller_category_new": [
                    "Beauty & Personal Care"
                ]              
            }
        ]
}
```

## 返回失败示例
```
{
    "code": 102,
    "message": "参数不合法",
    "error_details": ["sid => sid 必须是数字"],
    "request_id": "7D4CD60C-7BAC-6E98-D182-DF241A110AC9",
    "response_time": "2021-11-08 18:09:02",
    "data": [],
    "total": 0
}
```

## 附加说明

1.  令牌桶容量是 1 ；要求在调用时，需要串行调用，需要在上一次请求返回数据后，下次请求才不会被限流。

**特别注意**：本接口按照 ( 账户 + path ) 维度进行限流, 一个账户下如存在多个appld, 本接口令牌桶容量是账号下所有appId共享的 ， 如果账号下所有appId调用总和超出令牌桶容量限制，将会导致限流。 建议同一账户下的不同 appId 错开调用时间。
