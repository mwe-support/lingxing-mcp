# 查询调价队列

## 接口信息

| API Path                                          | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------------------------------------------ | :------- | :------- | :----------------------------------------------------------- |
| `/basicOpen/module/adjustPrice/AdjustPriceManual` | HTTPS    | POST     | 1                                                            |

## 请求参数

| 参数名            | 说明                                                         | 必填 | 类型     | 示例                |
| :---------------- | :----------------------------------------------------------- | :--- | :------- | :------------------ |
| offset            | 偏移量                                                       | 是   | [number] | 0                   |
| length            | 页长度，上限500                                              | 是   | [number] | 20                  |
| sid               | 搜索店铺id                                                   | 否   | [array]  | [121]               |
| processing_status | 调价状态，支持多选，数组 1待调价 2调价中 3调价成功 4调价失败 5审批中 6已驳回 7已作废 | 否   | [array]  | [5]                 |
| time_type         | 搜索时间类型：1创建时间 2完成时间                            | 否   | [number] | 1                   |
| start_time        | 开始时间                                                     | 否   | [string] | 2024-01-18 00:00:00 |
| end_time          | 结束时间                                                     | 否   | [string] | 2024-01-18 23:59:59 |
| search_field      | 搜索字段：msku，asin                                         | 否   | [string] | asin                |
| search_value      | 搜索值，msku和asin支持多个搜索，数组                         | 否   | [array]  | ["B014I8SSD0"]      |
| tab_status        | tab状态栏  0全部 1待审批 2调价中 3成功 4失败 5已作废 默认0   | 否   | [number] | 0                   |

## 请求示例

```
{
    "offset": 0,
    "length": 20,
    "sid": [121],
    "processing_status": [5],
    "time_type": 1,
    "start_time": "2024-01-18 00:00:00",
    "end_time": "2024-01-18 23:59:59",
    "search_field": "asin",
    "search_value": ["B014I8SSD0"],
    "tab_status": 0
}
```

## 返回结果

Json Object

| 参数名                                                  | 说明                                           | 必填     | 类型                 | 示例                                                       |
| :------------------------------------------------------ | :--------------------------------------------- | :------- | :------------------- | :--------------------------------------------------------- |
| code                                                    | 消息提示                                       | 是       | [number]             | 0                                                          |
| message                                                 | 消息                                           | 是       | [string]             | success                                                    |
| error_details                                           | 错误信息                                       | 是       | [array]              | []                                                         |
| request_id                                              | 请求id                                         | 是       | [string]             | b1e354b1d6364018b4a32e200c9e1b13.1752205585066             |
| response_time                                           | 响应时间                                       | 是       | [string]             | 2025-07-11 11:46:28                                        |
| data                                                    | 数据                                           | 是       | [object]             |                                                            |
| data>>count                                             | 总记录数                                       | 是       | [number]             | 1                                                          |
| data>>list                                              | 数据列表                                       | 是       | [array]              | []                                                         |
| data>>list>>msku                                        | 亚马逊卖家sku                                  | 是       | [string]             | BPE-11-1                                                   |
| data>>list>>fnsku                                       | FNSKU                                          | 是       | [string]             |                                                            |
| data>>list>>asin                                        | ASIN                                           | 是       | [string]             | B014I8SSD0                                                 |
| data>>list>>sid                                         | 店铺id                                         | 是       | [number]             | 121                                                        |
| data>>list>>processing_status                           | 调价状态                                       | 是       | [number]             | 5                                                          |
| data>>list>>failure_reason                              | 调价失败原因，当处理状态为“调价失败”该字段有值 | 是       | [string]             |                                                            |
| data>>list>>finish_time                                 | 完成时间                                       | 是       | [string]             |                                                            |
| data>>list>>create_time                                 | 创建时间                                       | 是       | [string]             | 2024-01-18 10:00:07                                        |
| data>>list>>adjust_type                                 | 调价类型                                       | 是       | [number]             | 1                                                          |
| data>>list>>profit_estimate                             | 预估利润                                       | 是       | [object]             |                                                            |
| data>>list>>profit_estimate>>standard_price_profit      | 价格毛利润                                     | 是       | [null]               | null                                                       |
| data>>list>>profit_estimate>>standard_price_profit_rate | 价格毛利率                                     | 是       | [null]               | null                                                       |
| data>>list>>profit_estimate>>sale_price_profit          | 优惠价毛利润                                   | 是       | [string]             |                                                            |
| data>>list>>profit_estimate>>sale_price_profit_rate     | 优惠价毛利率                                   | 是       | [string]             |                                                            |
| data>>list>>profit_estimate>>currency_icon              | 币种符号                                       | 是       | [null]               | null                                                       |
| data>>list>>store_name                                  | 店铺名                                         | 是       | [string]             | feifan-US                                                  |
| data>>list>>marketplace                                 | 国家                                           | 是       | [string]             | 美国                                                       |
| data>>list>>create_user                                 | 创建人                                         | 是       | [string]             | 邹诗如                                                     |
| data>>list>>processing_status_text                      | 调价状态文字说明                               | 是       | [string]             | 审批中                                                     |
| data>>list>>adjust_before_obj                           | 调价前详情                                     | 是       | [object]             |                                                            |
| data>>list>>adjust_before_obj>>standard_price           | 价格                                           | 是       | [string]             | 199.87                                                     |
| data>>list>>adjust_before_obj>>sale_price               | 优惠价                                         | 是       | [string]             | 199.82                                                     |
| data>>list>>adjust_before_obj>>sale_time_range          | 优惠价生效期                                   | 是       | [string]             | 2025-06-19 至 2025-06-20                                   |
| data>>list>>adjust_before_obj>>icon                     | 币种符号                                       | 是       | [string]             | $                                                          |
| data>>list>>adjust_after_obj                            | 调价后详情                                     | 是       | [object]             |                                                            |
| data>>list>>adjust_after_obj>>standard_price            | 价格                                           | 是       | [string]             | 199.87                                                     |
| data>>list>>adjust_after_obj>>sale_price                | 优惠价                                         | 是       | [string]             | 199.82                                                     |
| data>>list>>adjust_after_obj>>sale_time_range           | 优惠价生效期                                   | 是       | [string]             | 2025-06-19 至 2025-06-20                                   |
| data>>list>>adjust_after_obj>>icon                      | 币种符号                                       | 是       | [string]             | $                                                          |
| data>>list>>adjust_range                                | 调价幅度                                       | 是       | [object]             |                                                            |
| data>>list>>adjust_range>>standard_price                | 价格幅度                                       | 是       | [string]             | 0.00                                                       |
| data>>list>>adjust_range>>sale_price                    | 优惠价幅度                                     | 是       | [string]             |                                                            |
| data>>list>>asin_url                                    | asin跳转亚马逊前台链接                         | 是       | [string]             | https://www.amazon.com/dp/B014I8SSD0                       |
| data>>list>>business_id                                 | 调价记录id                                     | 是       | [string]             | 403126332159950848                                         |
| data>>list>>can_audit                                   | 是否可以审批 1是 0不是                         | 是       | [number]             | 0                                                          |
| data>>list>>small_image_url                             | 商品缩略图地址                                 | 是       | [string]             | https://m.media-amazon.com/images/I/81Bxo64d2-L._SL75_.jpg |
| data>>list>>local_sku                                   | 本地产品SKU                                    | 是       | [string]             | automation-test-procurement-plan0                          |
| data>>list>>local_name                                  | 品名                                           | 是       | [string]             | 采购计划测试组合产品                                       |
| data>>list>>adjust_before                               | 调整前                                         | 是       | [array]              | ["价格：$199.87"]                                          |
| data>>list>>adjust_after                                | 调整后                                         | 是       | [array]              | ["价格：$199.87"]                                          |
| data>>list>>audit_info                                  | 审批信息，审批中                               | 审批驳回 | 审批作废时有数据返回 |                                                            |
| total                                                   | 总数                                           | 是       | [number]             | 1                                                          |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "b1e354b1d6364018b4a32e200c9e1b13.1752205585066",
    "response_time": "2025-07-11 11:46:28",
    "data": {
        "count": 1,
        "list": [{
            "msku": "BPE-11-1",
            "fnsku": "",
            "asin": "B014I8SSD0",
            "sid": 121,
            "processing_status": 5,
            "failure_reason": "",
            "finish_time": "",
            "create_time": "2024-01-18 10:00:07",
            "adjust_type": 1,
            "profit_estimate": {
                "standard_price_profit": null,
                "standard_price_profit_rate": null,
                "sale_price_profit": "",
                "sale_price_profit_rate": "",
                "currency_icon": null
            },
            "store_name": "feifan-US",
            "marketplace": "美国",
            "create_user": "邹诗如",
            "processing_status_text": "审批中",
            "adjust_before_obj": {
                "standard_price": "199.87",
                "sale_price": "199.82",
                "sale_time_range": "2025-06-19 至 2025-06-20",
                "icon": "$"
            },
            "adjust_after_obj": {
                "standard_price": "199.87",
                "sale_price": "199.82",
                "sale_time_range": "2025-06-19 至 2025-06-20",
                "icon": "$"
            },
            "adjust_range": {
                "standard_price": "0.00",
                "sale_price": ""
            },
            "asin_url": "https://www.amazon.com/dp/B014I8SSD0",
            "business_id": "403126332159950848",
            "can_audit": 0,
            "small_image_url": "https://m.media-amazon.com/images/I/81Bxo64d2-L._SL75_.jpg",
            "local_sku": "automation-test-procurement-plan0",
            "local_name": "采购计划测试组合产品",
            "adjust_before": ["价格：$199.87"],
            "adjust_after": ["价格：$199.87"],
            "audit_info": []
        }]
    },
    "total": 1
}
```

