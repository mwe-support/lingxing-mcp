# 查询利润统计（旧）-MSKU
支持查询系统【统计】>【利润统计】中MSKU维度数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/finance/ProfitStatis/profitMsku` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|start_date|起始日期|是|[string]|2020-08-01|
|end_date|起始日期|是|[string]|2024-08-07|
|offset|分页偏移量|是|[int]|0|
|length|分页长度，上限200|是|[int]|200|
|sids|店铺id，通过逗号分隔可以多选，默认返回全部 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[string]|1,109|
|currency_type|币种，默认原币种<br>1 人民币-CNY<br>2 美元-USD<br>3 欧元-EUR<br>4 日元-JPY<br>5 澳元-AUD<br>6 加拿大元-CAD<br>7 墨西哥比索-MXN<br>8 英镑-GBP<br>9 印度卢比-INR<br>10 阿联酋迪拉姆-AED<br>11 新加坡元-SGD<br>12 沙特阿拉伯-SAR<br>13 巴西-BRL<br>14 瑞典-SEK<br>15 波兰-PLN<br>16 土耳其-TRY|否|[string]|2|
|sort_field|排序字段：asin|否|[string]|asin|
|sort_type|desc:倒序 <br> asc:顺序|否|[string]|desc|

## 请求示例
```
{
    "start_date": "2020-08-01",
    "end_date": "2024-08-07",
    "offset": 0,
    "length": 200,
    "sids": "1,109",
    "currency_type": "2",
    "sort_field": "asin",
    "sort_type": "desc"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|  |
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>msku|MSKU|是|[string]|  |
|data>>asin|Asin|是|[string]|  |
|data>>item_name|标题|是|[string]|  |
|data>>local_name|品名|是|[string]|  |
|data>>local_sku|SKU|是|[string]|  |
|data>>seller|店铺|是|[string]|  |
|data>>sid|店铺id|是|[int]|  |
|data>>marketplace|国家|是|[string]|  |
|data>>asin_name|负责人|是|[string]|  |
|data>>category_text|分类|是|[string]|  |
|data>>product_brand_text|品牌|是|[string]|  |
|data>>icon|币种-符号|是|[string]|  |
|data>>code|币种|是|[string]|  |
|data>>total_amount|销售额|是|[string]|  |
|data>>total_volume|销量|是|[number]|  |
|data>>replenishment_num|多渠道销量|是|[number]|  |
|data>>refund_num|退款量|是|[number]|  |
|data>>refund_amount|退款|是|[number]|  |
|data>>refund_rate|退款率|是|[string]|  |
|data>>channel_fee|发货费|是|[number]|  |
|data>>commission_amount|平台费|是|[number]|  |
|data>>promotion_amount|促销费|是|[number]|  |
|data>>order_quantity|广告订单量|是|[number]|  |
|data>>sales_amount|广告销售额|是|[number]|  |
|data>>total_spend|广告费|是|[number]|  |
|data>>total_cg_price|采购成本|是|[number]|  |
|data>>other_order_fee|测评费|是|[number]|  |
|data>>total_cg_transport_costs|头程费用|是|[number]|  |
|data>>gross_profit|毛利润|是|[number]|  |
|data>>profit_rate|毛利率|是|[string]|  |
|total|记录数|是|[int]| &nbsp; |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "F4CD40E1-7CB9-38DC-B196-5B17D375454E",
    "response_time": "2024-08-08 19:26:34",
    "data": [
        {
            "msku": "JJ002",
            "asin": "B0BBB14W7B",
            "item_name": "Super J Running Belt for Gym Workout Exercise Stable Sports Waist Bag Ultra Light Bounce Free",
            "local_name": "liyi-1",
            "local_sku": "liyi-1",
            "seller": "篮球 美国",
            "sid": "109",
            "marketplace": "美国",
            "asin_name": "超级管理员;林鸿基;刘瑞娟",
            "category_text": "服装",
            "product_brand_text": "LY",
            "icon": "$",
            "code": "USD",
            "total_amount": 0,
            "total_volume": "0",
            "replenishment_num": "2",
            "refund_num": "0",
            "refund_amount": 0,
            "refund_rate": "0.00%",
            "channel_fee": -9.6,
            "commission_amount": 0,
            "promotion_amount": 0,
            "order_quantity": "0",
            "sales_amount": 0,
            "total_spend": 0,
            "total_cg_price": 0,
            "other_order_fee": 0,
            "total_cg_transport_costs": 0,
            "gross_profit": -9.6,
            "profit_rate": "0.00%"
        },
        {
            "msku": "HOLDER001",
            "asin": "B0BB389BKQ",
            "item_name": "NP Phone Holder",
            "local_name": "",
            "local_sku": "",
            "seller": "篮球 美国",
            "sid": "109",
            "marketplace": "美国",
            "asin_name": "001-LXF;彭志帆;林鸿基;邱定楷",
            "category_text": "-",
            "product_brand_text": "",
            "icon": "$",
            "code": "USD",
            "total_amount": 0,
            "total_volume": "0",
            "replenishment_num": "2",
            "refund_num": "0",
            "refund_amount": 0,
            "refund_rate": "0.00%",
            "channel_fee": -10.15,
            "commission_amount": 0,
            "promotion_amount": 0,
            "order_quantity": "0",
            "sales_amount": 0,
            "total_spend": 0,
            "total_cg_price": -0.59,
            "other_order_fee": 0,
            "total_cg_transport_costs": -4.21,
            "gross_profit": -14.96,
            "profit_rate": "0.00%"
        }
    ],
    "total": 29
}
```
