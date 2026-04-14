# 查询产品表现

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/productPerformance/openApi/asinList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量|是|[int]|0|
|length|分页长度，最大10000|是|[int]|20|
|sort_field|排序字段，默认按volume排序，含义参考返回字段，只支持以下字段：<br>volume<br>order_items<br>amount<br>volume_chain_ratio<br>order_chain_ratio<br>amount_chain_ratio<br>b2b_volume<br>b2b_order_items<br>promotion_volume<br>promotion_amount<br>promotion_order_items<br>promotion_discount<br>avg_volume|是|[string]|volume|
|sort_type|排序方式：desc【降序】、asc【升序】，默认desc|是|[string]|desc|
|search_field|搜索字段，目前支持字段如下：<br>asin<br>parent_asin<br>msku<br>local_sku【sku】<br>item_name【标题】|否|[string]|asin|
|search_value|搜索值，最多批量搜索50个|否|[array]|["B085M7NH7K"]|
|mid|站点id|否|[int]|1|
|sid|店铺id，上限200 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】<br/>当单店铺查询时，传入字符串，示例："sid":"5608";<br/>当多店铺查询时，传入数组，示例："sid":[5609,5608]|是|[Object]|[1,109]|
|start_date|开始日期，筛选开始结束时间范围不能超过92天，双闭区间，格式：YYYY-MM-DD|是|[string]|2024-08-01|
|end_date|结束日期，筛选开始结束时间范围不能超过92天，双闭区间，格式：YYYY-MM-DD|是|[string]|2024-08-07|
|extend_search|表头筛选|否|[array]||
|extend_search>>field|筛选字段，对应返回字段的字段名，含义参考返回字段，只支持以下字段：<br>volume<br>order_items<br>amount<br>volume_chain_ratio<br>order_chain_ratio<br>amount_chain_ratio<br>b2b_volume<br>b2b_order_items<br>promotion_volume<br>promotion_amount<br>promotion_order_items<br>promotion_discount<br>avg_volume|否|[string]|volume|
|extend_search>>from_value|数值：<br>1、当exp为gt、lt、ge、le、eq 时，比较值填充至此字段；<br>2、当exp为range时，左区间值填充至此字段；|否|[int]|0|
|extend_search>>to_value|数值，仅当exp为range时，填充右区间值|否|[int]|1000|
|extend_search>>exp|可取值：range、gt、lt、ge、le、eq，其中range是闭区间|否|[string]|range|
|summary_field|汇总行维度，可取值为：<br>asin<br>parent_asin<br>msku<br>sku|是|[string]|asin|
|currency_code|货币类型，不传代表原币种，转换仅支持USD、CNY|否|[string]|CNY|
|is_recently_enum|是否仅查询活跃商品：<br>true 仅活跃【默认值】<br>false 全部商品|否|[boolean]|true|
|purchase_status|退货退款统计方式：<br>0 默认值，表示按退货退款的发生时间统计退货退款数据<br>1 表示按下单时间统计退货退款数据|否|[int]|0|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "sort_field": "volume",
    "sort_type": "desc",
    "search_field": "asin",
    "search_value": ["B085M7NH7K"],
    "mid": 1,
    "sid": [1,109],
    "start_date": "2024-08-01",
    "end_date": "2024-08-07",
    "extend_search": [
        {
            "field": "volume",
            "from_value": "0",
            "to_value": "1000",
            "exp": "range"
        }
    ],
    "summary_field": "asin",
    "currency_code": "CNY",
    "is_recently_enum": true,
    "purchase_status": 0
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|msg|提示信息|是|[string]|success|
|trace_id|请求链路id|是|[string]|success|
|data|响应数据|是|[object]| |
|data>>total|总数|是|[int]|1|
|data>>list|数据列表|是|[array]| |
|data>>list>>parent_asins|父asins信息|是|[array]||
|data>>list>>parent_asins>>amazon_url|亚马逊前台地址|是|[string]|https://www.amazon.com/dp/B49B3CCD9E|
|data>>list>>parent_asins>>parent_asin|父asin|是|[string]|B49B3CCD9E|
|data>>list>>parent_asins>>sid|parent_asin对应的店铺id|是|[int]|2|
|data>>list>>asins|asin列表|是|[array]||
|data>>list>>asins>>amazon_url|亚马逊前台地址|是|[string]|https://www.amazon.com/dp/BAE7F606CC|
|data>>list>>asins>>asin|asin名|是|[string]|BAE7F606CC|
|data>>list>>asins>>sid|asin对应的店铺id|是|[int]|2|
|data>>list>>price_list|价格列表|是|[array]||
|data>>list>>price_list>>local_name|品名|是|[string]|品名1|
|data>>list>>price_list>>local_sku|sku|是|[string]|SKU21b7132e785|
|data>>list>>price_list>>seller_sku|msku|是|[string]|MSKU8b88dc57b|
|data>>list>>price_list>>price|历史快照价格|是|[number]|8.99|
|data>>list>>price_list>>country|国家|是|[string]|美国|
|data>>list>>price_list>>seller_name|店铺名|是|[string]|店铺2|
|data>>list>>price_list>>is_eur|是否欧洲共享库存：0 否，1 是|是|[int]|0|
|data>>list>>price_list>>mid|站点ID|是|[int]|1|
|data>>list>>price_list>>sid|店铺id|是|[int]|2|
|data>>list>>price_list>>is_delete|是否删除：0 否，1 是|是|[int]|0|
|data>>list>>price_list>>volume|msku+sid对应的销量|是|[int]|7530|
|data>>list>>price_list>>product_pic_url|本地上传图片地址|是|[string]| |
|data>>list>>price_list>>small_image_url|msku缩略图地址|是|[string]| |
|data>>list>>price_list>>cid|分类ID|是|[int]|3|
|data>>list>>price_list>>source_rate|商品原币种汇率|是|[number]||
|data>>list>>price_list>>status|商品状态：<br>-1 未同步状态<br>1 active<br>0 inactive<br>2 incomplete|是|[int]|1|
|data>>list>>prev_cate_rank|上一次大类排名|是|[int]|39|
|data>>list>>item_name|标题|是|[string]|lingxing amazon product title 3EA49F959E|
|data>>list>>cate_rank|大类排名|是|[int]|55|
|data>>list>>small_cate_rank|小类排名|是|[array]||
|data>>list>>small_cate_rank>>category|类别|是|[string]|Hair Brushes|
|data>>list>>small_cate_rank>>prev_rank|上一次小类排名|是|[int]|1|
|data>>list>>small_cate_rank>>rank|排名|是|[int]|1|
|data>>list>>currency_icon|币种符号|是|[string]|$|
|data>>list>>seller_store_countries|店铺/国家|是|[array]||
|data>>list>>seller_store_countries>>seller_name|店铺名|是|[string]|店铺2|
|data>>list>>seller_store_countries>>country|国家|是|[string]|美国|
|data>>list>>categories|分类，字符串数组|是|[array]|["分类7"]|
|data>>list>>brands|品牌，字符串数组|是|[array]|["品牌2"]|
|data>>list>>principal_names|负责人|是|[array]|["负责人100086,负责人100088"]|
|data>>list>>developer_names|开发人|是|[array]|["开发人1"]|
|data>>list>>month_stock_sales_ratio|月库销比|是|[number]|18.97|
|data>>list>>volume|销量|是|[int]|7890|
|data>>list>>order_items|订单量|是|[int]|233|
|data>>list>>order_items_chain|环比订单量|是|[int]|233|
|data>>list>>amount|销售额|是|[number]|63240.03|
|data>>list>>volume_chain_ratio|销量环比|是|[number]|0.7758|
|data>>list>>volume_chain|环比销量|是|[int]|4333|
|data>>list>>amount_chain_ratio|销量额环比|是|[number]|0.7511|
|data>>list>>amount_chain|环比销量额|是|[number]|66.88|
|data>>list>>order_chain_ratio|订单量环比|是|[number]|0.7703|
|data>>list>>b2b_volume|B2B 销量|是|[int]|111|
|data>>list>>b2b_amount|B2B 销售额|是|[number]|357.38|
|data>>list>>b2b_order_items|B2B 订单量|是|[int]|47|
|data>>list>>gross_profit|结算毛利润|是|[number]|20777.37|
|data>>list>>predict_gross_profit|订单毛利润|是|[number]|-18212.26|
|data>>list>>gross_margin|结算毛利率|是|[number]|0.3326|
|data>>list>>predict_gross_margin|订单毛利率|是|[number]|-18212.26|
|data>>list>>roi|ROI|是|[number]|-0.3847|
|data>>list>>promotion_volume|促销销量|是|[int]|816|
|data>>list>>promotion_amount|促销销售额|是|[number]|6992.28|
|data>>list>>promotion_order_items|促销订单量|是|[int]|816|
|data>>list>>promotion_discount|促销折扣|是|[number]|1403.23|
|data>>list>>reviews_count|评论数|是|[int]|88962|
|data>>list>>return_count|退款量|是|[int]|110|
|data>>list>>return_rate|退款率|是|[number]|0.0139|
|data>>list>>afn_fulfillable_quantity|FBA可售|是|[int]|66489|
|data>>list>>afn_inbound_receiving_quantity|FBA入库中|是|[int]|111|
|data>>list>>afn_inbound_shipped_quantity|FBA在途|是|[int]|22|
|data>>list>>afn_inbound_working_quantity|FBA计划入库|是|[int]|33|
|data>>list>>afn_unsellable_quantity|FBA不可售|是|[int]|55|
|data>>list>>reserved_fc_processing|调仓中|是|[int]|22|
|data>>list>>reserved_fc_transfers|待调仓|是|[int]|55|
|data>>list>>fbm_quantity|FBM可售|是|[int]|11143|
|data>>list>>reserved_customerorders|待发货|是|[int]|222|
|data>>list>>stock_up_num|实际在途|是|[int]|222|
|data>>list>>clicks|点击量|是|[int]|32343|
|data>>list>>available_days|可售预估天数|是|[int]|444|
|data>>list>>fbm_available_days|fbm可售天数|是|[int]|223|
|data>>list>>avg_star|评分|是|[number]|4.6|
|data>>list>>prev_star|前一个评分|是|[number]|4.5|
|data>>list>>comment_rate|留评率|是|[number]|0.33|
|data>>list>>sessions|Sessions-Browser|是|[int]|6666|
|data>>list>>sessions_mobile|Sessions-Mobile|是|[int]|6666|
|data>>list>>sessions_total|Sessions-Total|是|[int]|6666|
|data>>list>>buy_box_percentage|Buybox|是|[number]|0.29|
|data>>list>>page_views|PV-Browser|是|[int]|3233|
|data>>list>>page_views_mobile|PV-Mobile|是|[int]|3233|
|data>>list>>page_views_total|PV-Total|是|[int]|3233|
|data>>list>>adv_rate|广告订单量占比|是|[number]|0.0399|
|data>>list>>ad_cvr|广告 CVR|是|[number]|1.0000|
|data>>list>>volume_cvr|销量 CVR|是|[number]|1.0000|
|data>>list>>cvr|CVR|是|[number]|0.0052|
|data>>list>>ctr|CTR,点击量/展示量|是|[number]|0.0165|
|data>>list>>acoas|广告花费/净销售额|是|[number]|0.3955|
|data>>list>>acos|广告花费/广告销售额|是|[number]|0.3255|
|data>>list>>has_oprator_log|是否有操作日志|是|[boolean]|true|
|data>>list>>return_goods_count|退货量|是|[int]|57|
|data>>list>>return_goods_rate|退货率|是|[number]|0.0072|
|data>>list>>cpc|cpc,花费/点击量|是|[number]|1.14|
|data>>list>>spend|广告花费【组成广告花费项目的总计】|是|[number]|1018.40|
|data>>list>>shared_cost_of_advertising|差异分摊|是|[number]|0.00|
|data>>list>>shared_ads_sb_cost|SB广告费|是|[number]|0.00|
|data>>list>>shared_ads_sbv_cost|SBV广告费|是|[number]|0.00|
|data>>list>>ads_sd_cost|SD广告费|是|[number]|0.00|
|data>>list>>ads_sp_cost|SP广告费|是|[number]|1018.40|
|data>>list>>roas|ROAS,广告销售额/广告花费|是|[number]|2.53|
|data>>list>>asoas|ASoAS,广告销售额/总销售额|是|[number]|0.0416|
|data>>list>>cpo|CPO,广告花费/广告订单量|是|[number]|3.31|
|data>>list>>cpm|CPM,广告花费/(1000*展示量)|是|[number]|5.89|
|data>>list>>ad_sales_amount|广告销售额|是|[number]|2575.03|
|data>>list>>ads_sp_sales|SP广告销售额|是|[number]|2575.03|
|data>>list>>ads_sd_sales|SD广告销售额|是|[number]|2575.03|
|data>>list>>shared_ads_sb_sales|SB广告销售额|是|[number]|2575.03|
|data>>list>>shared_ads_sbv_sales|SBV广告销售额|是|[number]|2575.03|
|data>>list>>ad_order_quantity|广告订单量|是|[int]|308|
|data>>list>>impressions|展示|是|[int]|172777|
|data>>list>>sids|店铺id|是|[array]|[2]|
|data>>list>>net_amount|净销售额|是|[number]|61836.80|
|data>>list>>small_image_url|页面所对应的缩略图地址,取自销量最高的msku的缩略图|是|[string]|https://xxx/xxx.png|
|data>>list>>ranking_update_time|排名更新时间【已废弃】|是|[string]|2017-12-01 10:25:50|
|data>>list>>avg_volume|平均销量|是|[number]|129.3|
|data>>list>>avg_custom_price|销售均价|是|[number]|7.84|
|data>>list>>icon_num|运营日志数量，用于前端判断是否存在运营日志数据|是|[int]|0|
|data>>list>>sku|sku【sku维度才有值】|是|[string]|sku-001|
|data>>list>>local_name|品名，【sku维度才有值】|是|[string]|品名222|
|data>>list>>spu_spu_names|spu数据|是|[array]||
|data>>list>>spu_spu_names>>spu|spu|是|[string]|yctest-spu|
|data>>list>>spu_spu_names>>spu_name|spu名称/款名|是|[string]|yc-test|
|data>>list>>attributes|属性，注意内部属性与属性值的分隔符是"\001：\001"，存在特殊隐藏字符|是|[array]||
|data>>list>>cg_price|采购成本，sku维度特有|是|[number]|22.33|
|data>>list>>whs_value|可用货值，sku维度特有|是|[number]|222.33|
|data>>list>>cg_price_currency_icon|采购成本，可用货值的币种符号|是|[string]|¥|
|data>>list>>local_quantity|本地可用，sku维度特有|是|[int]|22|
|data>>list>>oversea_quantity|海外仓可用，sku维度特有|是|[int]|33|
|data>>list>>inventory_sales_ratio|存销比，sku维度特有|是|[number]|0.0000|
|data>>list>>avg_landed_price|平均售价，sku维度特有|是|[number]|8.58|
|data>>list>>suppliers|供应商，sku维度特有|是|[array]|[“供应商a”]|
|data>>list>>model|型号，sku维度特有|是|[array]|["型号1"]|
|data>>list>>return_amount|退款金额|是|[double]|0.0|
|data>>list>>fbm_buyer_expenses | FBM买家运费 | 否 | [double] | 0.0 |
|data>>list>>points_number| 积分收入| 否 | [int] | 0 |
|data>>list>>product_create_time|product创建时间，sku维度特有|是|[string]|2017-12-01 10:25:50|
|data>>list>>ad_direct_sales_amount|直接成交销售额|是|[number]|2323.33|
|data>>list>>ad_direct_order_quantity|直接成交订单量|是|[int]|2333|
|data>>list>>rank_category|大类排名分类|是|[string]|Beauty & Personal Care|
|data>>list>>available_inventory|可用库存数据|否|[object]||
|data>>list>>available_inventory>>stock_up_num|实际在途|否|[string]|0|
|data>>list>>available_inventory>>available_inventory|可用库存总计 ，**注意：当且仅当界面有FBA公式配置（业务配置->仓库->FBA库存明细-可用库存计算方式，勾选FBA可售) 时返回**|否|[string]|66489|
|data>>list>>available_inventory>>afn_unsellable_quantity|FBA不可售|否|[string]|0|
|data>>list>>available_inventory>>afn_inbound_shipped_quantity|FBA在途|否|[string]|0|
|data>>list>>available_inventory>>afn_inbound_working_quantity|FBA计划入库|否|[string]|0|
|data>>list>>available_inventory>>afn_inbound_receiving_quantity|FBA入库中|否|[string]|0|
|data>>list>>available_inventory>>reserved_customerorders|待发货|否|[string]|0|
|data>>list>>available_inventory>>reserved_fc_processing|调仓中|否|[string]|0|
|data>>list>>available_inventory>>reserved_fc_transfers|待调仓|否|[string]|0|
|data>>list>>available_inventory>>fbm_quantity|fbm库存|否|[string]|0|
|data>>list>>available_inventory>>afn_fulfillable_quantity|FBA可售|否|[string]|66489|
|data>>list>>tag_set|Listing标签信息|是|[array]||
|data>>list>>tag_set>>global_tag_id|标签id|是|[string]|907311320790335784|
|data>>list>>tag_set>>tag_name|标签名|是|[string]|专用标签|
|data>>list>>tag_set>>color|标签颜色|是|[string]|#9C9CA0|
|data>>chain_start_date|环比时间|是|[string]|2021-04-01|
|data>>chain_end_date|环比时间|是|[string]|2021-05-31|
|data>>available_inventory_formula_zh|可用库存计算公式|是|[string]|FBA可售+FBM可售+待调仓+调仓中+待发货+入库中+计划入库+标发在途+不可售+实际在途|

## 返回成功示例
```
{
    "code": 0,
    "msg": "success",
    "trace_id": "bd1bdd39404d4f3d9fbeb1e1b51d597d.1723115595502",
    "data": {
        "total": 1,
        "list": [
            {
                "parent_asins": [
                    {
                        "amazon_url": "https://www.amazon.com/dp/B085M7NH7K",
                        "parent_asin": "B085M7NH7K",
                        "sid": "109"
                    }
                ],
                "asins": [
                    {
                        "amazon_url": "https://www.amazon.com/dp/B085M7NH7K",
                        "asin": "B085M7NH7K",
                        "sid": "109"
                    }
                ],
                "price_list": [
                    {
                        "country": "美国",
                        "is_eur": "0",
                        "local_sku": "Yajie003",
                        "mid": "1",
                        "local_name": "Yajie003",
                        "sid": "109",
                        "is_delete": "0",
                        "volume": "0",
                        "product_pic_url": "",
                        "small_image_url": "https://m.media-amazon.com/images/I/7196b5bK6PL._SL75_.jpg",
                        "seller_name": "篮球",
                        "price": "1349.00",
                        "seller_sku": "DEE-216",
                        "source_rate": 7.1,
                        "status": "0",
                        "cid": "0"
                    }
                ],
                "small_cate_rank": null,
                "item_name": "8P-SPEED Custom Car Floor Mats for Cadillac Coverage All Weather Protection Waterproof Non-Slip Leather Liner Set Wine",
                "sku": null,
                "local_name": null,
                "cate_rank": 0,
                "rank_category": null,
                "prev_cate_rank": 0,
                "currency_icon": "￥",
                "cg_price_currency_icon": "¥",
                "ranking_update_time": null,
                "seller_store_countries": [
                    {
                        "country": "美国",
                        "seller_name": "篮球"
                    }
                ],
                "categories": [],
                "brands": [],
                "principal_names": [
                    "超级管理员"
                ],
                "developer_names": [],
                "attributes": [],
                "month_stock_sales_ratio": null,
                "volume": 0,
                "b2b_volume": 0,
                "order_items": 0,
                "b2b_order_items": 0,
                "amount": "0.00",
                "b2b_amount": "0.00",
                "volume_chain_ratio": "0.0000",
                "amount_chain_ratio": "0.0000",
                "order_chain_ratio": "0.0000",
                "gross_profit": "0.00",
                "predict_gross_profit": "0.00",
                "gross_margin": "0.0000",
                "predict_gross_margin": "0.0000",
                "roi": "0.0000",
                "promotion_volume": 0,
                "promotion_amount": "0.00",
                "promotion_order_items": 0,
                "promotion_discount": "0.00",
                "reviews_count": 0,
                "return_count": 0,
                "return_rate": "0.0000",
                "afn_fulfillable_quantity": 0,
                "afn_inbound_receiving_quantity": 0,
                "afn_inbound_shipped_quantity": 0,
                "afn_inbound_working_quantity": 0,
                "afn_unsellable_quantity": 0,
                "reserved_fc_processing": 0,
                "reserved_fc_transfers": 0,
                "reserved_customerorders": 0,
                "fbm_quantity": 0,
                "stock_up_num": 0,
                "clicks": 0,
                "available_days": 0,
                "fbm_available_days": 0,
                "avg_star": "0.0",
                "prev_star": "0.0",
                "comment_rate": null,
                "sessions": 0,
                "sessions_mobile": 0,
                "sessions_total": 0,
                "buy_box_percentage": null,
                "page_views": 0,
                "page_views_mobile": 0,
                "page_views_total": 0,
                "ad_direct_order_quantity": 0,
                "ad_direct_sales_amount": "0.00",
                "adv_rate": "0.0000",
                "volume_cvr": "0.0000",
                "cvr": "0.0000",
                "ctr": "0.0000",
                "acoas": "0.0000",
                "acos": "0.0000",
                "has_oprator_log": null,
                "return_goods_count": 0,
                "return_goods_rate": "0.0000",
                "cpc": null,
                "spend": "0.00",
                "roas": "0.00",
                "asoas": "0.0000",
                "cpo": null,
                "cpm": null,
                "ad_sales_amount": "0.00",
                "ad_cvr": "0.0000",
                "ad_order_quantity": 0,
                "shared_cost_of_advertising": null,
                "shared_ads_sb_cost": "0.00",
                "shared_ads_sbv_cost": "0.00",
                "ads_sd_cost": "0.00",
                "ads_sp_cost": "0.00",
                "impressions": 0,
                "sids": [
                    109
                ],
                "net_amount": "0.00",
                "small_image_url": "https://m.media-amazon.com/images/I/7196b5bK6PL._SL75_.jpg",
                "available_inventory": {
                    "afn_fulfillable_quantity": 0,
                    "stock_up_num": 0,
                    "reserved_customerorders": 0,
                    "reserved_fc_transfers": 0,
                    "afn_inbound_receiving_quantity": 0,
                    "available_inventory": 0,
                    "reserved_fc_processing": 0,
                    "fbm_quantity": 0
                },
                "avg_custom_price": null,
                "avg_volume": "0.0",
                "icon_num": 0,
                "spu_spu_names": [
                    {
                        "spu_name": "",
                        "spu": ""
                    }
                ],
                "product_create_time": null,
                "cg_price": null,
                "whs_value": null,
                "local_quantity": null,
                "oversea_quantity": null,
                "inventory_sales_ratio": "0.0000",
                "avg_landed_price": "1349.00",
                "suppliers": [],
                "model": [],
                "return_amount": 0.0,
                "tag_set": [
                    {
                        "global_tag_id": "907414919208862908",
                        "tag_name": "这是ASIN标签",
                        "color": "#C309DB"
                    },
                    {
                        "global_tag_id": "907430960946815077",
                        "tag_name": "测试002",
                        "color": "#00B51E"
                    },
                    {
                        "global_tag_id": "907430960946815082",
                        "tag_name": "使用api创建005",
                        "color": "#9C9CA0"
                    }
                ],
                "currency_code": "CNY",
                "volume_chain": 0,
                "amount_chain": "0.00",
                "order_items_chain": 0,
                "pids": null
            }
        ],
        "chain_start_date": "2024-07-25",
        "chain_end_date": "2024-07-31",
        "available_inventory_formula_zh": "FBA可售+FBM可售+待调仓+调仓中+待发货+入库中+实际在途"
    }
}
```
## 附加说明
**限流算法说明**(需要同时满足才不会被限流)：<br/>
1）、令牌桶容量是1；要求在调用时，需要串行调用，需要在上一次请求返回数据后，下次请求才不会被限流<br/>
2）、如果上次请求传入的是一个店铺，则 需要在1）的基础上间隔1s；如果上次请求传入的是多个店铺，则需要间隔10s<br>
3）、summary_field为asin时，search_field不可为parent_asin。

**特别注意**：本接口按照 ( 账户 + path ) 维度进行限流, 一个账户下如存在多个appld, 本接口令牌桶容量是账号下所有appId共享的 ， 如果账号下所有appId调用总和超出令牌桶容量限制，将会导致限流。 建议同一账户下的不同 appId 错开调用时间。

**字段说明**
<br>PV-Total、PV-Mobile、PV-Browser字段需要在asin维度或父asin维度才有值



**唯一键说明**

asin维度：asin+sid

父asin维度：parent_asin+sid

msku维度：seller_sku+sid

sku维度：sku+sid
