# 查询运营日志

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/operateManage/operateLog/list` | HTTPS | POST | 1 |

## 请求参数

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[array]|["109,136"]|
|search_field|搜索类型：<br />asin  ASIN<br />parent_asin  父ASIN<br />msku  MSKU|是|[string]|asin|
|search_value|搜索值|是|[string]|B085NNMFH7|
|date_type|时间类型：<br />1  日<br />2  周<br />3  月|是|[string]|1|
|start_date|开始时间，闭区间，格式：Y-m-d|是|[string]|2022-01-01|
|end_date|结束时间，闭区间，格式：Y-m-d|是|[string]|2024-08-05|

## 请求示例
```
{
    "sids": ["109,136"],
    "search_field": "asin",
    "search_value": "B085NNMFH7",
    "date_type": "1",
    "start_date": "2022-01-01",
    "end_date": "2024-08-05"
}
```

## 返回结果
Json Object

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|0|
|data|响应数据|是|[object]||
|data>>log_data|运营日志数据|是|[array]||
|data>>log_data>>type_name|类型名|是|[string]|运营手记|
|data>>log_data>>item_log_data|子项运营日志数据|是|[array]||
|data>>log_data>>item_log_data>>remark_id|备注id|是|[string]|373|
|data>>log_data>>item_log_data>>remark|备注|是|[string]|2222|
|data>>log_data>>item_log_data>>type_name|类型名|是|[string]|运营手记|
|data>>log_data>>item_log_data>>pic_url|图片地址|是|[string]|https://www.xxx.com/images/I/41Z.jpg|
|data>>log_data>>item_log_data>>gmt_modified|更新时间|是|[string]|2023-10-17 14:57:45|
|data>>log_data>>item_log_data>>uid|用户ID|是|[string]|10452291|
|data>>log_data>>item_log_data>>realname|备注操作人名称|是|[string]|tom|
|data>>log_data>>item_log_data>>sid|店铺ID|是|[string]|109|
|data>>log_data>>item_log_data>>date_type|时间维度：<br />1  日维度<br />2  周维度<br />3  月维度|是|[string]|1|
|data>>log_data>>item_log_data>>related_uids|艾特人id|是|[array]|["10379859"]|
|data>>small_cate_rank|小类数据|是|[array]||
|data>>small_cate_rank>>category|小类别名|是|[string]|computer|
|data>>small_cate_rank>>rank|小类排名|是|[string]|1|
|data>>rank_category|大类别名|是|[string]|egg|
|data>>cate_rank|大类排名|是|[string]|2|
|data>>r_date|日期|是|[string]|2023-10-1|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "2ce88d3d407341cc8f47dce84b1bacfa.1697596553077",
    "response_time": "2023-10-18 10:35:53",
    "data": [
        {
            "log_data": [
                {
                    "type_name": "运营手记",
                    "item_log_data": [
                        {
                            "remark_id": "372",
                            "remark": "HOLDER001",
                            "type_name": "运营手记",
                            "pic_url": null,
                            "gmt_modified": "2023-10-17 14:57:45",
                            "uid": "10452291",
                            "realname": "jack",
                            "sid": "109",
                            "date_type": "1",
                            "related_uids": null,
                            "rdate": "2023-10-01"
                        },
                        {
                            "remark_id": "373",
                            "remark": "two",
                            "type_name": "运营手记",
                            "pic_url": null,
                            "gmt_modified": "2023-10-17 19:12:38",
                            "uid": "10452291",
                            "realname": "jack",
                            "sid": "109",
                            "date_type": "1",
                            "related_uids": ["10379859"],
                            "rdate": "2023-10-01"
                        }
                    ]
                }
            ],
            "small_cate_rank": [],
            "cate_rank": "0",
            "rank_category": null,
            "r_date": "2023-10-01"
        } 
			],
    "total": 1
}
```