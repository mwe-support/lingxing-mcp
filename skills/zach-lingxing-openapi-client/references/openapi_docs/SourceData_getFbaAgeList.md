# 查询亚马逊源报表—库龄表
查询 Manage Inventory Health 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/fbaStock/getFbaAgeList` | HTTPS | POST | 3 |

## 请求参数

| 参数名 | 说明                                          | 必填 | 类型     | 示例   |
| :----- | :-------------------------------------------- | :--- | :------- | ------ |
| sid    | 店铺id, 多个使用英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 是   | [string] |109|
| offset | 分页偏移量                                    | 否   | [int] |0|
| length | 分页长度，默认20                              | 否   | [int] |20|

## 请求示例
```
{
    "sid": 109,
    "offset": 0,
    "length": 20
}
```

## 返回结果
Json Object

| 参数名                                                    | 说明 | 必填 | 类型     | 示例   |
| :-------------------------------------------------------- | :--- | :--- | :------- | :----- |
| code                                                      |  状态码，0 成功    | 是   | [int]    |   0  |
| message                                                   |  消息提示   | 是   | [string] |        |
| error_details                                             |  错误信息    | 是   | [array]  |        |
| request_id                                                |  请求链路id |是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
| response_time                                             |  响应时间    | 是   | [string] |        |
| data                                                      |  响应数据    | 是   | [array]  |        |
| data>>list                                                |  数据列表    | 是   | [array]  |        |
| data>>list>>sid                                           |  店铺id    | 是   | [int]    |        |
| data>>list>>snapshot_date                                 |  生成报告的日期    | 是   | [string] |        |
| data>>list>>sku                                           |  您分配给所售商品的唯一编码，由字母和数字组成    | 是   | [string] |        |
| data>>list>>fnsku                                         |  亚马逊为存放在亚马逊运营中心并从亚马逊运营中心配送的商品分配的唯一编码，由字母和数字组成    | 是   | [string] |        |
| data>>list>>asin                                          |  亚马逊为通过亚马逊销售的商品分配的唯一编码，由 10 个字母或数字组成    | 是   | [string] |        |
| data>>list>>product_name                                  |  商品的名称    | 是   | [string] |        |
| data>>list>>condition                                     |  商品的状况(例如，新品或二手)    | 是   | [string] |        |
| data>>list>>available                                     |  可售(可售库存)数量    | 是   | [string] |        |
| data>>list>>pending_removal_quantity                      |  您请求退还或弃置的商品数量    | 是   | [string] |        |
| data>>list>>inv_age_0_to_90_days                          |  已在运营中心存放 0-90 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_91_to_180_days                        |  已在运营中心存放 91-180 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_181_to_270_days                       |  已在运营中心存放 181-270 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_271_to_365_days                       |  已在运营中心存放 271-365 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_365_plus_days                         |  已在运营中心存放超过 365 天的可售商品数量    | 是   | [string] |        |
| data>>list>>currency                                      |  用于支付预计长期仓储费的货币    | 是   | [string] |        |
| data>>list>>qty_to_be_charged_ltsf_6_mo                   |  截至下一收费日期，已在亚马逊运营中心存放 180 至 365 天且需支付 180 天长期仓储费的可售商品数量| 是   | [string] |        |
| data>>list>>qty_to_be_charged_ltsf_12_mo                  |  截至下一收费日期(每月 15 日)，已在运营中心存放超过 365 天的可售 商品数量    | 是   | [string] |        |
| data>>list>>projected_ltsf_6_mo                           |  在下一收费日期，已在运营中心存放 180 至 365 天的商品预计需要支付的长期仓储费    | 是   | [string] |        |
| data>>list>>projected_ltsf_12_mo                          |  截至下一收费日期(每月 15 日)，已在运营中心存放超过 365 天的商品的 预计长期仓储费       | 是   | [string] |        |
| data>>list>>estimated_ltsf_next_charge                    |  截至下一收费日期(每月 15 日)，在亚马逊运行中心存放超过365天的可售商品的数量预计的长期仓储费   | 是   | [string] |        |
| data>>list>>units_shipped_t7                              |  最近 7 天内已发货的商品数量    | 是   | [string] |        |
| data>>list>>units_shipped_t30                             |  最近 30 天内已发货的商品数量    | 是   | [string] |        |
| data>>list>>units_shipped_t60                             |  最近 60 天内已发货的商品数量    | 是   | [string] |        |
| data>>list>>units_shipped_t90                             |  最近 90 天内已发货的商品数量    | 是   | [string] |        |
| data>>list>>alert                                         |  当商品存在低流量或低转化率提醒时会显示，低流量表明只有少数潜在买家查看了该商品信息，低转化率表明潜在买家查看了商品信息但最后并未跟进购买商品    | 是   | [string] |        |
| data>>list>>your_price                                    |  您发布的商品价格    | 是   | [string] |        |
| data>>list>>sales_price                                   |  您的促销价格(如果您正在促销该商品)    | 是   | [string] |        |
| data>>list>>lowest_price_new_plus_shipping                |  此商品的新品在亚马逊商城的最低价格(含运费)    | 是   | [string] |        |
| data>>list>>lowest_price_used                             |  此商品的二手商品在亚马逊商城的最低价格(含运费)    | 是   | [string] |        |
| data>>list>>recommended_action                            |  建议您对库存执行的操作。建议的依据是您当前的买家需求，以及相对于不做任何操作，采取措施是否会降低您的成本    | 是   | [string] |        |
| data>>list>>healthy_inventory_level                       |  根据商品需求和您的成本，不属于冗余库存的库存数量。我们提供建议是为了帮助您达到这一库存水平    | 是   | [string] |        |
| data>>list>>recommended_sales_price                       |  有助于您根据当前库存设置来售出库存的建议促销价格。该值可能与最低价格或推荐报价价格不同。我们建议您在售出冗余库存之前维持该商品价格    | 是   | [string] |        |
| data>>list>>recommended_sale_duration_days                |  如果建议您开展促销活动，则该数值是有助于您售出冗余库存的预计促销持续天数    | 是   | [string] |        |
| data>>list>>recommended_removal_quantity                  |  可以移除从而避免产生仓储费的预计商品数量    | 是   | [string] |        |
| data>>list>>estimated_cost_savings_of_recommended_actions |  与不采取任何操作(需要为相应库存支付仓储费)相比，采取建议操作预计可以节约的成本    | 是   | [string] |        |
| data>>list>>sell_through                                  |  售出率为在过去 90 天内售出和已发货的商品数量除以此段时间内亚马逊 运营中心的平均可售库存量。追踪售出率可帮助您确定是否需要采取措施 来提高商品的流量或转化率    | 是   | [string] |        |
| data>>list>>item_volume                                   |  商品的体积，计算方法是将最长边、次长边和最短边的值相乘。这些测量值通常是指商品的长度、宽度和高度    | 是   | [string] |        |
| data>>list>>volume_unit_measurement                       |  商品体积的计量单位    | 是   | [string] |        |
| data>>list>>storage_type                                  |  可设置仓储限制的商品仓储类型分类    | 是   | [string] |        |
| data>>list>>storage_volume                                |  仓储容量等于此商品在亚马逊运营中心的总仓储使用量减去等待移除的商品的仓储使用量    | 是   | [string] |        |
| data>>list>>marketplace                                   |  商品所在的亚马逊商城    | 是   | [string] |        |
| data>>list>>product_group                                 |  区分图书和钟表或视频游戏等商品的独特商品分组    | 是   | [string] |        |
| data>>list>>sales_rank                                    |  商品的当前排名。销售排名值的正负变化是过去 7 天排名上升(正)或下 降(负)名次    | 是   | [string] |        |
| data>>list>>days_of_supply                                |  根据商品的预期需求估算的您当前库存能够持续供货的天数    | 是   | [string] |        |
| data>>list>>estimated_excess_quantity                     |  预计冗余商品数量是根据您当前的销售速度和买家需求预测得出的积压商品数量。保留积压商品并支付仓储费比通过降价售出或移除积压商品来降低库存数量的成本更高    | 是   | [string] |        |
| data>>list>>weeks_of_cover_t30                            |  过去 30 天现货库存平均数除以同期售出的商品数量除以 4 周。对于某一 商品，如果您在过去 30 天(4 周)内售出 400 件，在亚马逊运营中心还 有 100 件可售，那么您基于过去 30 天销量的可维持周数为 1    | 是   | [string] |        |
| data>>list>>weeks_of_cover_t90                            |  过去 90 天现货库存平均数除以同期售出的商品数量除以 12 周。对于某一 商品，如果您在过去 90 天(12 周)内售出 400 件，在亚马逊运营中心平 均还有 10 件可售，那么您基于过去 90 天销量的可维持周数为 3.33    | 是   | [string] |        |
| data>>list>>featuredoffer_price                           |  在商品详情页面上显示加入购物车按钮的商品    | 是   | [string] |        |
| data>>list>>sales_shipped_last_7_days                     |  最近 7 天的已发货商品销量    | 是   | [string] |        |
| data>>list>>sales_shipped_last_30_days                    |  最近 30 天的已发货商品销量    | 是   | [string] |        |
| data>>list>>sales_shipped_last_60_days                    |  最近 60 天的已发货商品销量    | 是   | [string] |        |
| data>>list>>sales_shipped_last_90_days                    |  最近 90 天的已发货商品销量    | 是   | [string] |        |
| data>>list>>inv_age_0_to_30_days                          |  已在运营中心存放 30 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_31_to_60_days                         |  已在运营中心存放 31-60 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_61_to_90_days                         |  已在运营中心存放 61-90 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_181_to_330_days                       |  已在运营中心存放 181-330 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>inv_age_331_to_365_days                       |  已在运营中心存放 331-365 天的可售商品数量    | 是   | [int]    |        |
| data>>list>>estimated_storage_cost_next_month             |  根据您当前的销售速度，从今天开始往后 30 天内所产生的预计仓储 费(月度仓储 + 长期仓储)。注意: 库存费用是基于您库存的最新每日快照中的数量得出，可能会 与您的实际库存数量不同    | 是   | [string] |        |
| data>>list>>inbound_quantity                              |  入库数量 = inbound-working + inbound-shipped + inbound receiving    | 是   | [string] |        |
| data>>list>>inbound_working                               |  处于“处理中”状态的货件数量    | 是   | [string] |        |
| data>>list>>inbound_shipped                               |  处于“已发货”状态的货件数量    | 是   | [string] |        |
| data>>list>>inbound_received                              |  处于“正在接收”状态的货件数量    | 是   | [string] |        |
| data>>list>>no_sale_last_6_months                         |  至少连续 6 个月未售出且在运营中心存放已超过 180 天的库存。如果您启 用可售库存自动移除服务，系统将在下一移除周期自动移除这些商品    | 是   | [string] |        |
| data>>total                                               |  总数   | 是   | [int]    | &nbsp; |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "1F08F267-6233-5A5A-A5B1-4CE7C78ED544",
    "response_time": "2024-08-06 16:15:15",
    "data": {
        "total": 4,
        "list": [
            {
                "sid": 109,
                "snapshot_date": "2023-06-28",
                "sku": "Black_ Head_Rope",
                "fnsku": "B09MT3989Q",
                "asin": "B09MT3989Q",
                "product_name": "Love Pearl Bottom Hair Circle Women's High Elastic Hair Binding Rope Jewelry Rubber Band Head Rope Black",
                "condition": "New",
                "available": 0,
                "pending_removal_quantity": 0,
                "inv_age_0_to_90_days": 0,
                "inv_age_91_to_180_days": 1,
                "inv_age_181_to_270_days": 0,
                "inv_age_271_to_365_days": 0,
                "inv_age_365_plus_days": 0,
                "currency": "USD",
                "qty_to_be_charged_ltsf_6_mo": 0,
                "qty_to_be_charged_ltsf_12_mo": 0,
                "projected_ltsf_6_mo": "",
                "estimated_ltsf_next_charge": "",
                "projected_ltsf_12_mo": "",
                "units_shipped_t7": 0,
                "units_shipped_t30": 0,
                "units_shipped_t60": 0,
                "units_shipped_t90": 0,
                "alert": "",
                "your_price": "",
                "sales_price": "",
                "lowest_price_new_plus_shipping": "-1.0",
                "lowest_price_used": "-1.0",
                "recommended_action": "",
                "healthy_inventory_level": 0,
                "recommended_sales_price": "0.00",
                "recommended_sale_duration_days": 0,
                "recommended_removal_quantity": 0,
                "estimated_cost_savings_of_recommended_actions": "0.000000",
                "sell_through": "0.0",
                "item_volume": "0.000000",
                "volume_unit_measurement": "",
                "storage_type": "Standard",
                "storage_volume": "",
                "marketplace": "US",
                "product_group": "",
                "sales_rank": "",
                "days_of_supply": "",
                "estimated_excess_quantity": "",
                "weeks_of_cover_t30": "",
                "weeks_of_cover_t90": "",
                "featuredoffer_price": "",
                "sales_shipped_last_7_days": "",
                "sales_shipped_last_30_days": "",
                "sales_shipped_last_60_days": "",
                "sales_shipped_last_90_days": "",
                "inv_age_0_to_30_days": 0,
                "inv_age_31_to_60_days": 0,
                "inv_age_61_to_90_days": 0,
                "inv_age_181_to_330_days": 0,
                "inv_age_331_to_365_days": 0,
                "inv_age_0_to_30_days_quantity": 0,
                "inv_age_31_to_60_days_quantity": 0,
                "inv_age_61_to_90_days_quantity": 0,
                "inv_age_91_to_180_days_quantity": 1,
                "inv_age_181_to_270_days_quantity": 0,
                "inv_age_271_to_330_days_quantity": 0,
                "inv_age_331_to_365_days_quantity": 0,
                "inv_age_365_plus_days_quantity": 0,
                "estimated_storage_cost_next_month": "",
                "inbound_quantity": "",
                "inbound_working": "",
                "inbound_shipped": "",
                "inbound_received": "",
                "no_sale_last_6_months": ""
            }
        ]
    },
    "total": 4
}
```