# 查询利润报表（旧） - MSKU
支持查询系统【财务】>【利润报表】中MSKU维度统计数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/finance/ProfitState/profitMsku` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|是|[int]|0|
|length|分页长度，默认20|是|[int]|20|
|currency_type|币种 : <br>1 CNY <br>2 USD <br>3 EUR<br> 4 JPY<br> 5 AUD<br> 6 CAD <br>7 MXN <br>8 GBP<br> 9 INR <br>10 AED<br> 11 SGD <br>12 SAR <br>13 BRL <br>14 SEK <br>15 PLN <br>16 TRY|是|[int]| 1 |
|sids|店铺id，多个使用英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[string]|1,2,3,4,5,6|
|month|月份|是|[string]|2021-05|

## 返回结果

Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码， 0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|total|总数|是|[int]|2|
|fifo_type|类型：0 固定值，1 先进先出 |是|[int]|1|
|is_closing_data|是否结账数据：0否，1是|是|[int]|0|
|data|响应数据|是|[array]|  |
|data>>date|请求时间|是|[string]|2021-07-07 18:01:58|
|data>>date_locale|年月|是|[string]|2021-05|
|data>>other_fee_goods|商品其他费|是|[number]|1.55|
|data>>other_fee_seller|店铺其他费|是|[number]|0.19|
|data>>sid|店铺id|是|[int]|1|
|data>>msku|MSKU值|是|[string]|JX-MPNS-QNHN|
|data>>asin|ASIN|是|[string]|B07H2PWWWW|
|data>>currency_code|原币种，如：USD|是|[string]|USD|
|data>>sales_total|销售额|是|[number]| |
|data>>refund|销售退款|是|[number]| |
|data>>sales_total_amz_fba|FBA销售额|是|[number]| |
|data>>sales_total_amz_fbm|FBM销售额|是|[number]| |
|data>>ads_total_sales_amount|广告销售额|是|[number]| |
|data>>sales_total_quantity|销量|是|[string]| |
|data>>sales_total_amz_fba_quantity|FBA销量|是|[string]| |
|data>>sales_total_amz_fbm_quantity|FBM销量|是|[string]| |
|data>>ads_sd_order_quantity|SD广告销量|是|[string]| |
|data>>ads_quantity|广告销量|是|[string]| |
|data>>reship_quantity|亚马逊补发量|是|[string]| |
|data>>ads_order_quantity|SP广告销量|是|[string]| |
|data>>income_fba_fee|FBA买家运费|是|[number]| |
|data>>income_fba_amz_fee|亚马逊FBA发货费|是|[number]| |
|data>>shared_report_inventory_difference_fee|仓储费差异分摊|是|[number]| |
|data>>income_fba_mc_fee|多渠道订单运费|是|[number]| |
|data>>income_fbm_amz_fee|FBM买家运费|是|[number]| |
|data>>promotion|促销折扣|是|[number]| |
|data>>adjustment_total|FBA库存赔偿|是|[number]| |
|data>>adjustment|库存调整补偿金额|是|[number]| |
|data>>shared_income_adjustment|费用分摊|是|[number]| |
|data>>liquidations|清算|是|[string]|0.0000000000|
|data>>fba_adjustment_quantity|FBA库存赔偿量|是|[string]| |
|data>>adjustment_quantity|MSKU库存赔偿量|是|[string]| |
|data>>refund_quantity|退款量|是|[string]| |
|data>>refund_quantity_rate|退货率|是|[string]|0%|
|data>>return_total_sellable_quantity|退货量|是|[string]| |
|data>>return_sellable_quantity|退货可售|是|[string]| |
|data>>return_unsellable_quantity|退货不可售|是|[string]| |
|data>>refund_rate|退款率|是|[string]|0%|
|data>>expense_fba_fee|售出订单|是|[number]| |
|data>>selling_fee_order_fba|售出订单平台费|是|[number]| |
|data>>expence_fba_amz_fee|售出订单FBA发货费|是|[number]| |
|data>>order_other_fee_order|售出订单其他费|是|[number]| |
|data>>expence_fbm_amz_fee|售出订单FBM发货费|是|[number]| |
|data>>expense_fba_mc_fee|多渠道FBA发货费|是|[number]| |
|data>>return_order|退款订单|是|[number]| |
|data>>selling_fee_refund|退款订单平台费|是|[number]| |
|data>>expence_fba_fee_refund|退款订单发货费|是|[number]| |
|data>>order_other_fee_refund|退款订单其他费|是|[number]| |
|data>>ads_total_fee|广告费|是|[number]| |
|data>>ads_fee|SP广告费|是|[number]| |
|data>>ads_sbv_fee|SBV广告费分摊|是|[number]| |
|data>>ads_sd_fee|SD广告费|是|[number]| |
|data>>ads_sb_fee|SB广告费分摊|是|[number]| |
|data>>shared_ads_fee|广告费差异分摊|是|[number]| |
|data>>total_coupon|优惠券总和|是|[number]| |
|data>>total_ld|秒杀费总和|是|[number]| |
|data>>early_reviewer_program_fee|早期评论者计划|是|[number]| |
|data>>total_promotion_fee|推广费|是|[number]| |
|data>>fba_inventory_fee|FBA仓储费|是|[number]| |
|data>>month_storage_inventory_fee|月仓储费|是|[number]| |
|data>>longterm_storage_inventory_fee|长期仓储费|是|[number]| |
|data>>fba_other_inventory_fee|FBA其他仓储服务费|是|[number]| |
|data>>disposal_quantity|销毁量|是|[string]| |
|data>>disposal_fee|销毁费|是|[number]| |
|data>>removal_quantity|移除量|是|[string]| |
|data>>removal_fee|移除费|是|[number]| |
|data>>service_subscription_fee|订阅费|是|[number]| |
|data>>customer_return_fee|退货入仓费|是|[number]| |
|data>>fba_amazon_partnered_carrier_shipment_fee|合作承运费|是|[number]| |
|data>>fba_inventory_placement_service_fee|合仓费|是|[number]| |
|data>>shared_amz_inventory_fee|FBA仓储服务其他费分摊|是|[number]| |
|data>>amz_adjustment_total|库存调整费|是|[number]| |
|data>>amz_adjustment|库存调整费|是|[number]| |
|data>>shared_expence_adjustment|其他调整费分摊|是|[number]| |
|data>>selling_other_fee|平台其他费|是|[number]| |
|data>>platform_other_fee|其他费分摊|是|[number]| |
|data>>sale_tax|销售税|是|[number]| |
|data>>total_cg_price|采购成本|是|[number]| |
|data>>total_cg_transport_costs|头程费用|是|[number]| |
|data>>custom_order_fee|测评费|是|[number]| |
|data>>gross_profit|毛利润|是|[number]|1.74|
|data>>profit_rate|毛利率|是|[string]|0%|
|data>>shipping_label_fee_order|售出订单运输标签费|是|[number]| |
|data>>transaction_inventory_storage_overage_fee|超量仓储费|是|[number]| |
|data>>fba_international_freight_fee|FBA物流国际货运费|是|[number]| |
|data>>hidden_tax_fee|隐藏税|是|[number]| |
|data>>product_sales_tax|商品销售税|是|[number]| |
|data>>shipping_credits_tax|运费税|是|[number]| |
|data>>gift_wrap_credits_tax|礼品包装税|是|[number]| |
|data>>promotional_rebates_tax|促销折扣税|是|[number]| |
|data>>tax_marketplace|市场税|是|[number]| |
|data>>low_value_goods_tax|低价值税|是|[number]| |
|data>>tax_collection_withholding_total|亚马逊代收代扣|是|[number]| |
|data>>income_tax_withheld|预扣所得税|是|[number]| |
|data>>cash_on_delivery|货到付款（COD）|是|[number]| |
|data>>tcs_cgst|印度站税费|是|[number]| |
|data>>tcs_sgst|印度站税费|是|[number]| |
|data>>tcs_igst|印度站税费|是|[number]| |
|data>>small_image_url|缩略图|是|[string]|  |
|data>>asin_url|ASIN链接|是|[string]|https://www.amazon.com/dp/B07H2PWWWW|
|data>>category_text|分类名|是|[string]|  |
|data>>product_brand_text|品牌名|是|[string]|  |
|data>>item_name|品名|是|[string]|Pencil Case with 2 Compartments|
|data>>local_sku|本地SKU|是|[string]|1596786|
|data>>local_name|本地商品名|是|[string]|=C135+A135|
|data>>asin_name|负责人|是|[string]|  |
|data>>seller_name|店铺名|是|[string]|PM-MX-MX|
|data>>marketplace|国家|是|[string]|美国|
|data>>icon|货币符号|是|[string]|$|
|data>>other_fee_goods_detail|商品其他费详情|是|[array]|  |
|data>>other_fee_goods_detail>>sid|店铺id|是|[string]|1|
|data>>other_fee_goods_detail>>other_fee_type_id|费用类型ID|是|[number]|1087|
|data>>other_fee_goods_detail>>name|费用名称|是|[string]|555|
|data>>other_fee_goods_detail>>other_fee|金额|是|[number]|1.55|
|data>>other_fee_seller_detail|店铺其他费详情|是|[array]|  |
|data>>other_fee_seller_detail>>sid|店铺id|是|[string]|1|
|data>>other_fee_seller_detail>>other_fee_type_id|费用类型ID|是|[number]|1096|
|data>>other_fee_seller_detail>>name|费用名称|是|[string]|其他费1|
|data>>other_fee_seller_detail>>other_fee|金额|是|[number]|0.12|

**详细说明**：

> 注意：利润报表msku维度返回数据会区分批次成本模式和固定值模式，不同的模式返回的字段不一样。以上字段为公共字段，批次成本模式和固定值模式都会返回，下面的字段为批次成本模式和固定值模式单独返回的。注意： 返回的字段fifo_type（类型，0：固定值；1：先进先出；）即代表当前模式

**批次成本模式：（1）采购成本：**fifo_cg_price             -&gt;    FBA订单发货fifo_fbm_cg_price     -&gt;    FBM订单发货fifo_refund_cg_price -&gt;    买家退货fifo_adjustment_cg_price   -&gt;  库存调整fifo_remove_cg_price  -&gt;  库存移除fifo_difference_cg_price -&gt; 库存差异fba_catch_cg_price  -&gt;  FBA补货差异  

**(2) 头程费用：**fifo_cg_transport_costs  -&gt; FBA售出商品fifo_fbm_costs  -&gt;  FBM售出商品fifo_adjustment_costs -&gt; 库存调整fifo_remove_costs -&gt;  库存移除fifo_difference_costs -&gt; 库存差异fifo_refund_costs  -&gt;  买家退货fba_catch_costs -&gt; FBA补货差异    

**固定值模式**：**（1）采购成本：**sales_cg_price  -&gt; FBA售出商品sales_total_amz_fba_quantity -&gt; FBA售出商品 - 数量expense_cg_price -&gt; 多渠道订单商品sales_total_mc_fba_quantity -&gt; 多渠道订单商品-数量disposal_cg_price -&gt; 销毁商品disposal_quantity -&gt; 销毁商品-数量fba_cg_price -&gt; FBA库存赔偿fba_adjustment_quantity -&gt;  FBA库存赔偿-数量sales_reship_cg_price  -&gt; 补发货商品reship_quantity -&gt; 补发货商品-数量  
**(2) 头程费用：**sales_cg_transport_costs-&gt;FBA售出商品sales_total_amz_fba_quantity -&gt; FBA售出商品-数量expense_cg_transport_costs -&gt; 多渠道订单商品sales_total_mc_fba_quantity -&gt; 多渠道订单商品-数量disposal_cg_transport_costs -&gt; 销毁商品disposal_quantity -&gt; 销毁商品-数量fba_cg_transport_costs-&gt;FBA库存赔偿fba_adjustment_quantity -&gt; FBA库存赔偿-数量sales_reship_cg_transport_costs-&gt;补发货商品reship_quantity -&gt; 补发货商品-数量