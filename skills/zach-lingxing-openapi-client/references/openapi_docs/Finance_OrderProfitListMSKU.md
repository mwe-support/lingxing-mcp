# 查询订单利润-MSKU
唯一键说明：sid+msku

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/mreport/OrderProfit` | HTTPS | POST | 1 |


## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限5000|否|[int]|20|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[113,115]|
|startDate|查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s|是|[string]|2023-02-01|
|endDate|查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s|是|[string]|2023-12-05|
|searchField|搜索值类型, 可选值:seller_sku,asin,local_name, local_sku|否|[string]|asin|
|searchValue|搜索的值|否|[array]|["B09"]|
|currencyCode|币种code【默认原币种】, 可选值：原币种,CNY,USD,EUR,JPY,AUD,CAD,MXN,GBP,INR,AED,SGD,SAR,BRL,SEK,PLN,TRY,HKD|否|[string]|CNY|


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/finance/mreport/OrderProfit?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "offset": 0,
    "length": 20,
    "sids": [113,115],
    "startDate": "2023-02-01",
    "endDate": "2023-12-05",
    "searchField": "asin",
    "searchValue": ["B09"],
    "currencyCode": "CNY"
}'
```

## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ |----|
|code|状态码，0：成功|是|[int]|    |
|message|消息提示|是|[string]|    |
|error_details|数据校验失败时的错误详情|是|[array]|    |
|request_id|请求链路id|是|[string]|    |
|response_time|响应时间|是|[string]|    |
|total| 总数|是|[int]|    |
|data|数据|是|[array]|    |
|data>>currency_code|币种|是|[string]|    |
|data>>currency_icon|币种符号|是|[string]|    |
|data>>gross_profit|毛利润|是|[string]|    |
|data>>gross_margin|毛利率|是|[string]|    |
|data>>avg_gross_profit|平均毛利润|是|[string]|    |
|data>>volume|销量|是|[number]|    |
|data>>replacement_quantity|补换货量|是|[number]|    |
|data>>multi_channel_volume|多渠道销量|是|[number]|    |
|data>>ad_sales_amount|广告销售额|是|[string]|    |
|data>>ad_volume|广告销量|是|[number]|    |
|data>>amount|销售额|是|[string]|    |
|data>>tax_amount|含税销售额|是|[string]|    |
|data>>refund_amount|退款金额|是|[string]|    |
|data>>refund_amount_rate|退款率|是|[string]|    |
|data>>shipping_cost|买家运费|是|[string]|    |
|data>>promotion_discount|促销折扣|是|[string]|    |
|data>>return_quantity|退货量|是|[number]|    |
|data>>return_rate|退货率|是|[string]|    |
|data>>selling_fee|平台费|是|[string]|    |
|data>>fulfillment_fee|fba发货费（包含亚马逊物流客户退货费）|是|[string]|    |
|data>>other_order_fee|其他订单费用|是|[string]|    |
|data>>spend|花费|是|[string]|    |
|data>>ads_sb_cost|sb花费|是|[string]|    |
|data>>ads_sbv_cost|sbv花费|是|[string]|    |
|data>>ads_sd_cost|sd花费|是|[string]|    |
|data>>ads_sp_cost|sp花费|是|[string]|    |
|data>>purchase_costs|采购成本|是|[string]|    |
|data>>avg_purchase_costs|采购均价|是|[string]|    |
|data>>logistics_costs|头程成本|是|[string]|    |
|data>>avg_logistics_costs|头程均价|是|[string]|    |
|data>>other_costs|其他成本|是|[string]|    |
|data>>avg_other_costs|其他均价|是|[string]|    |
|data>>total_costs|合计成本|是|[string]|    |
|data>>price_list|商品基础信息|是|[array]|    |
|data>>price_list>>principal_uids| |是|[string]|    |
|data>>price_list>>local_sku|sku |是|[string]|    |
|data>>price_list>>item_name|标题 |是|[string]|    |
|data>>price_list>>cate_title| |是|[string]|    |
|data>>price_list>>local_name| |是|[string]|    |
|data>>price_list>>sid| |是|[string]|    |
|data>>price_list>>is_delete| |是|[string]|    |
|data>>price_list>>brand_title| |是|[string]|    |
|data>>price_list>>volume| |是|[number]|    |
|data>>price_list>>small_main_image_url| |是|[string]|    |
|data>>price_list>>site_url| |是|[string]|    |
|data>>price_list>>parent_asin| |是|[string]|    |
|data>>price_list>>seller_sku| |是|[string]|    |
|data>>price_list>>asin| |是|[string]|    |
|data>>price_list>>status| |是|[string]|    |
|data>>is_parent|是否有子项|是|[boolean]|    |
|data>>small_image_url|图片链接|是|[string]|    |
|data>>parent_asins|父asin|是|[array]|    |
|data>>local_infos|本地商品信息|是|[array]|    |
|data>>local_infos>>local_sku| |是|[string]|    |
|data>>local_infos>>local_name| |是|[string]|    |
|data>>asins|asin|是|[array]|    |
|data>>asins>>asin_url| |是|[string]|    |
|data>>asins>>asin| |是|[string]|    |
|data>>sids|店铺id，在msku维度数组中只有一条数据|是|[array]|    |
|data>>item_name|品名|是|[string]|    |
|data>>categories|分类|是|[array]|    |
|data>>seller_store_countries|国家|是|[array]|    |
|data>>seller_store_countries>>country| |是|[string]|    |
|data>>seller_store_countries>>name| |是|[string]|    |
|data>>brands|品牌|是|[array]|    |
|data>>refund_quantity|退款量|是|[string]|    |
|data>>principal_names|listing负责人|是|[string]|    |
|data>>ad_sales_amount_sp|sp广告销售额|是|[double]|    |
|data>>ad_sales_amount_sd|sd广告销售额|是|[double]|    |
|data>>ad_sales_amount_sb|sb广告销售额|是|[double]|    |
|data>>ad_sales_amount_sbv|sbv广告销售额|是|[double]|    |
|data>>ad_volume_sp|sp广告销量|是|[long]|    |
|data>>ad_volume_sd|sd广告销量|是|[long]|    |
|data>>ad_volume_sb|sb广告销量|是|[long]|    |
|data>>ad_volume_sbv|sbv广告销量|是|[long]|    |
|data>>afn_volume|fba销量|是|[long]|    |
|data>>mfn_volume|fbm销量|是|[long]|    |
|data>>afn_amount|fba销售额|是|[double]|    |
|data>>mfn_amount|fbm销售额|是|[double]|    |
|data>>pm_discount|价格折扣|是|[double]|    |
|data>>sp_discount|配送折扣|是|[double]|    |
|data>>net_gross_margin|净毛利率|是|[string]| |
|data>>avg_volume|平均日销|是|[number]| |
|data>>net_amount|净销售额|是|[string]| |
|data>>avg_net_amount|平均售价|是|[string]| |
|data>>selling_fee_rate|平台费占比|是|[string]| |
|data>>fulfillment_fee_rate|FBA发货费占比|是|[string]| |
|data>>spend_rate|广告费率|是|[string]| |
|data>>total_stock_fee|仓储费|是|[string]| |
|data>>total_stock_fee_rate|仓储费占比|是|[string]| |
|data>>promotion_fee|推广费|是|[string]| |
|data>>shared_fba_international_inbound_fee|FBA国际物流运费|是|[string]| |
|data>>adjustments_fee|调整费|是|[string]| |
|data>>selling_other_fee|平台其他费|是|[string]| |
|data>>inventory_credit|FBA库存赔偿|是|[string]| |
|data>>shared_fba_inbound_convenience_fee|入库配置费|是|[string]| |
|data>>cost_of_points_granted|积分收入|是|[string]| |
|data>>shared_cost_of_advertising|差异分摊|是|[string]| |
|data>>total_other_granted|其它收入|是|[string]| |
|data>>shared_fba_liquidation_proceeds|清算收入|是|[string]| |
|data>>shared_fba_liquidation_proceeds_adjustments|清算调整|是|[string]| |
|data>>shared_amazon_shipping_reimbursement|亚马逊运费赔偿|是|[string]| |
|data>>shared_safe_t_reimbursement|Safe-T索赔|是|[string]| |
|data>>shared_netco_transaction|Netco交易|是|[string]| |
|data>>shared_reimbursements|赔偿收入|是|[string]| |
|data>>shared_clawbacks|追索收入|是|[string]| |
|data>>shared_commingling_vat_income|混合VAT收入|是|[string]| |
|data>>gift_wrap_credits|包装收入|是|[string]| |
|data>>a_to_z_guarantee_claims|买家交易保障索赔额|是|[string]| |
|data>>shared_others|其他|是|[string]| |
|data>>fba_storage_fee|月仓储费|是|[string]| |
|data>>shared_fba_storage_fee|月仓储费差异|是|[string]| |
|data>>long_term_storage_fee|长期仓储费|是|[string]| |
|data>>shared_long_term_storage_fee|长期仓储费差异|是|[string]| |
|data>>shared_storage_renewal_billing|库存续订费|是|[string]| |
|data>>shared_fba_disposal_fee|FBA销毁费|是|[string]| |
|data>>shared_fba_removal_fee|FBA移除费|是|[string]| |
|data>>shared_fba_inbound_transportation_program_fee|入仓手续费|是|[string]| |
|data>>shared_labeling_fee|标签费|是|[string]| |
|data>>shared_polybagging_fee|塑料包装费|是|[string]| |
|data>>shared_bubblewrap_fee|泡沫包装费|是|[string]| |
|data>>shared_taping_fee|胶带费|是|[string]| |
|data>>shared_awd_processing_fee|AWD处理费|是|[string]| |
|data>>shared_awd_transportation_fee|AWD运输费|是|[string]| |
|data>>shared_awd_storage_fee|AWD仓储费|是|[string]| |
|data>>shared_star_storage_fee|卫星仓仓储费|是|[string]| |
|data>>shared_fba_customer_return_fee|FBA退回卖家费|是|[string]| |
|data>>shared_fba_inbound_defect_fee|入库缺陷费|是|[string]| |
|data>>shared_fba_overage_fee|超量仓储费|是|[string]| |
|data>>shared_amazon_partnered_carrier_shipment_fee|合作承运费|是|[string]| |
|data>>shared_item_fee_adjustment|库存调整费用|是|[string]| |
|data>>shared_other_fba_inventory_fees|其他仓储费|是|[string]| |
|data>>fba_fulfillment_fee|fba（对应订单列表FBA发货费）|是|[string]| |
|data>>shared_fba_transaction_customer_return_fee|亚马逊物流客户退货费|是|[string]| |
|data>>off_site_promotion_fee|站外推广费|是|[string]| |


## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "574FB0B8-FD6E-8D29-91FD-295B55CF5398",
    "response_time": "2024-07-31 14:41:25",
    "data": [
        {
            "currency_code": "USD",
            "currency_icon": "$",
            "gross_profit": "0.00",
            "gross_margin": "0.0000",
            "avg_gross_profit": "0.00",
            "volume": 0,
            "replacement_quantity": 0,
            "multi_channel_volume": 0,
            "ad_sales_amount": "0.00",
            "ad_volume": 0,
            "amount": "0.00",
            "afn_amount": "",
            "mfn_amount": "",
            "tax_amount": "0.00",
            "refund_amount": "0.00",
            "refund_amount_rate": "0.00",
            "shipping_cost": "0.00",
            "promotion_discount": "0.00",
            "pm_discount": "",
            "sp_discount": "",
            "return_quantity": 0,
            "return_rate": "0.0000",
            "selling_fee": "0.00",
            "fulfillment_fee": "0.00",
            "other_order_fee": "0.00",
            "spend": "0.00",
            "ads_sb_cost": "0.00",
            "ads_sbv_cost": "0.00",
            "ads_sd_cost": "0.00",
            "ads_sp_cost": "0.00",
            "purchase_costs": "0.00",
            "avg_purchase_costs": "0.00",
            "logistics_costs": "0.00",
            "avg_logistics_costs": "0.00",
            "other_costs": "0.00",
            "avg_other_costs": "0.00",
            "total_costs": "0.00",
            "price_list": [
                {
                    "principal_uids": "10529123",
                    "local_sku": "4990a126a7b36350f4916c8f642fa811",
                    "item_name": "lingxing amazon product title A8442DB",
                    "cate_title": "分类5",
                    "local_name": "64fea5cf204b8d40d9b174d12d799a03",
                    "sid": "2",
                    "is_delete": "1",
                    "brand_title": "",
                    "volume": 0,
                    "small_main_image_url": "",
                    "site_url": "",
                    "parent_asin": "BFF23E679B",
                    "seller_sku": "5ebabc80e8d38aec1ee098fdc6bf99f9",
                    "asin": "BFF23E679B",
                    "status": "0"
                }
            ],
            "is_parent": false,
            "small_image_url": "",
            "parent_asins": [
                "BFF23E679B"
            ],
            "local_infos": [
                {
                    "local_sku": "4990a126a7b36350f4916c8f642fa811",
                    "local_name": "64fea5cf204b8d40d9b174d12d799a03"
                }
            ],
            "asins": [
                {
                    "asin_url": "",
                    "asin": "BFF23E679B"
                }
            ],
            "sids": [
                "2"
            ],
            "item_name": "",
            "categories": [
                "分类5"
            ],
            "seller_store_countries": [
                {
                    "country": "美国",
                    "name": ""
                }
            ],
            "brands": [

            ],
            "refund_quantity": "",
            "principal_names": "",
            "ad_sales_amount_sp": "",
            "ad_sales_amount_sd": "",
            "ad_sales_amount_sb": "",
            "ad_sales_amount_sbv": "",
            "ad_volume_sp": "",
            "ad_volume_sd": "",
            "ad_volume_sb": "",
            "ad_volume_sbv": "",
            "afn_volume": "",
            "mfn_volume": ""
        }
    ]
}
```



