# 查询退款量（旧）
>支持查询ASIN或父ASIN的退款量和退款量数据，对应系统【统计】>【利润统计（旧版）】退款数据  
>注意：旧版-利润统计已经下线，新版-利润统计的增量数据不会在此接口返回

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/finance/Refund/profitMonthRefund` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 |必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|asin_type|1 asin <br>2 父asin|是|[string]|1|
|offset|分页偏移量|是|[int]| 0|
|length|分页条数，上限200|是|[int]|200|
|start_date|起始日期|是|[string]|2020-01-01|
|end_date|结束日期|是|[string]|2024-08-05|
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|sort_field|排序字段：asin|否|[string]|asin|
|sort_type|desc 倒序<br>asc 顺序|否|[string]|desc| 

## 请求示例
```
{
    "offset": 0,
    "length": 200,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "asin_type": "1",
    "sid": 109,
    "sort_field": "asin",
    "sort_type": "desc"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data| |是|[object]|  |
|data>>total|总数|是|[int]|2|
|data>>list|明细|是|[array]|  |
|data>>list>>asin_type|1:asin <br>2:父asin|是|[int]|1|
|data>>list>>asin|asin|是|[string]|XXXX1|
|data>>list>>parent_asin|父asin<br>asin_type=2的时候会返回|否|[string]|  |
|data>>list>>refund_num|退款量|是|[string]|27|
|data>>list>>refund_rate|退款率|是|[string]|2.05%|

## 返回成功示例


```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "689584F6-8D7F-19F7-B11A-2AC55FA36B81",
    "response_time": "2021-05-10 21:07:17",
    "data": {
        "total": 2,
        "list": [
            {
                "asin_type": 1,
                "asin": "XXXX1",
                "refund_num": "27",
                "refund_rate": "2.05%"
            },
            {
                "asin_type": 1,
                "asin": "XXXX2",
                "refund_num": "0",
                "refund_rate": "0.00%"
            }
        ]
    }
}


// asin_type = 2
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "E8BA08C6-EFE7-EE31-8870-7FDFC1EF6C89",
    "response_time": "2021-05-10 21:07:17",
    "data": {
        "total": 2,
        "list": [
            {
                "asin_type": 2,
                "asin": "AAAAA1;AAAAA2;AAAAA3",
                "parent_asin": "AAAAA",
                "refund_num": "34",
                "refund_rate": "1.77%"
            },
            {
                "asin_type": 2,
                "asin": "AAAAA1;AAAAA2;AAAAA4",
                "parent_asin": "AAAAA",
                "refund_num": "27",
                "refund_rate": "2.05%"
            }
        ]
    }
}

```

