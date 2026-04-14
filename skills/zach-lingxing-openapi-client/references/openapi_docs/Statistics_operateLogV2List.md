# 查询运营日志(新)
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/operateManage/operateLog/list/v2` | HTTPS | POST   | 1 |

## 请求参数
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认为20|否|[number]|0|
|length|分页长度，默认为200|否|[number]|40|
|sids|店铺列表|否|[array]|["123"]|
|mids|国家列表|否|[array]|["1","2"]|
|start_date|开始时间，格式：yyyy-mm-dd|是|[string]|2023-10-01|
|end_date|结束时间，格式：yyyy-mm-dd|是|[string]|2023-10-31|
|search_field|搜索条件：<br>asin ASIN<br>parent_asin 父ASIN<br>msku MSKU【默认】|否|[string]|msku|
|search_value|搜索值|否|[array]|["1234123"]|
|summary_type|日志维度：<br>asin ASIN<br>parent_asin 父ASIN<br>msku MSKU|是|[string]|asin|

## 请求示例
```
{
    "offset": 0,
    "length": 40,
    "sids": [
        "123"
    ],
    "mids": [
        "1",
        "2"
    ],
    "start_date": "2023-10-01",
    "end_date": "2023-10-31",
    "search_field": "msku",
    "search_value": [
        "1234123"
    ],
    "summary_type": "asin"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[number]|0|
|message|提示信息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|c94201a63d0c45ee9bb07cc6d6e4a260.1732604778665|
|response_time|响应时间|是|[string]|2024-11-26 15:06:20|
|data|响应数据|是|[object]| |
|data>>data|响应数据|是|[array]| |
|data>>data>>product_info|商品信息|是|[object]| |
|data>>data>>product_info>>small_image_url|图片|是|[string]|https://image.distributetop.com/lingxing-erp/90128554873982976/20220919/56e5d1a9fd38411a98e5cc7e503efb4a.jpg|
|data>>data>>product_info>>asin|ASIN|是|[string]|B0BB389BKQ|
|data>>data>>product_info>>parent_asins|父ASIN|是|[array]|["B0BB389BKQ"]|
|data>>data>>product_info>>seller_skus|MSKU|是|[array]|["HOLDER001"]|
|data>>data>>product_info>>seller_info| |是|[array]| |
|data>>data>>product_info>>seller_info>>seller_name|店铺|是|[string]|篮球|
|data>>data>>product_info>>seller_info>>marketplace|国家|是|[string]|美国|
|data>>data>>product_info>>local_infos| |是|[array]| |
|data>>data>>product_info>>local_infos>>local_name|品名|是|[string]|布料-khf|
|data>>data>>product_info>>local_infos>>local_sku|SKU|是|[string]|bl-khf|
|data>>data>>log_data|手动日志|是|[object]| |
|data>>data>>log_data>>2023-10-20| |是|[object]| |
|data>>data>>log_data>>2023-10-20>>log_data| |是|[object]| |
|data>>data>>log_data>>2023-10-20>>log_data>>start_date|日志时间|是|[string]|2024-10-21|
|data>>data>>log_data>>2023-10-20>>log_data>>type_name|日志类型|是|[string]|广告|
|data>>data>>log_data>>2023-10-20>>log_data>>remark|日志内容|是|[string]|1|
|data>>data>>auto_log_data|自动日志|是|[object]| |
|data>>data>>auto_log_data>>2023-10-20| |是|[object]| |
|data>>data>>auto_log_data>>2023-10-20>>log_data| |是|[array]| |
|data>>data>>auto_log_data>>2023-10-20>>log_data>>start_date|日志时间|是|[string]|2023-10-20|
|data>>data>>auto_log_data>>2023-10-20>>log_data>>type_name|日志类型|是|[string]|广告|
|data>>data>>auto_log_data>>2023-10-20>>log_data>>remark|日志内容|是|[string]|【广告活动】修改0608|
|total| |是|[number]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "c94201a63d0c45ee9bb07cc6d6e4a260.1732604778665",
    "response_time": "2024-11-26 15:06:20",
    "data": {
        "data": [
            {
                "product_info": {
                    "small_image_url": "https://image.distributetop.com/lingxing-erp/90128554873982976/20220919/56e5d1a9fd38411a98e5cc7e503efb4a.jpg",
                    "asin": "B0BB389BKQ",
                    "parent_asins": [
                        "B0BB389BKQ"
                    ],
                    "seller_skus": [
                        "HOLDER001"
                    ],
                    "seller_info": [
                        {
                            "seller_name": "篮球",
                            "marketplace": "美国"
                        }
                    ],
                    "local_infos": [
                        {
                            "local_name": "布料-khf",
                            "local_sku": "bl-khf"
                        }
                    ]
                },
                "log_data": {
                    "2023-10-20": {
                        "log_data": null
                    },
                    "2023-10-21": {
                        "log_data": null
                    }
                },
                "auto_log_data": {
                    "2023-10-24": {
                        "log_data": [
                            {
                                "start_date": "2023-10-24",
                                "type_name": "广告",
                                "remark": "【广告活动】新增FGH43394RU-手动-关键词-BROAD-关键词-2023-08-10-18:31:47-勿归档 复制 18点20分；修改0608"
                            },
                            {
                                "start_date": "2023-10-24",
                                "type_name": "广告",
                                "remark": "【广告组】新增FGH43394RU-手动-关键词-BROAD-关键词-2023-08-10-18:31:47-勿归档；"
                            },
                            {
                                "start_date": "2023-10-24",
                                "type_name": "广告",
                                "remark": "【广告】新加广告MSKU：HOLDER001；"
                            },
                            {
                                "start_date": "2023-10-24",
                                "type_name": "广告",
                                "remark": "【投放】新建1个；"
                            },
                            {
                                "start_date": "2023-10-24",
                                "type_name": "广告",
                                "remark": "【否定投放】新建1个，"
                            }
                        ]
                    },
                    "2023-10-29": {
                        "log_data": [
                            {
                                "start_date": "2023-10-29",
                                "type_name": "广告",
                                "remark": "【广告活动】修改0608"
                            },
                            {
                                "start_date": "2023-10-29",
                                "type_name": "广告",
                                "remark": "【投放】修改36个；"
                            }
                        ]
                    }
                }
            }
        ]
    },
    "total": 1
}
```