# SB分摊

## 接口信息

| API Path                                | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :-------------------------------------- | :------- | :------- | :----------------------------------------------------------- |
| `/pb/openapi/newad/sbDivideAsinReports` | HTTPS    | POST     | 1                                                            |

## 请求参数

| 参数名      | 说明                                                         | 必填 | 类型     | 示例         |
| ----------- | ------------------------------------------------------------ | ---- | -------- | ------------ |
| profile_id  | 店铺profile_id                                               | 是   | [int]    | 123456       |
| report_date | 报告日期                                                     | 是   | [string] | "2025-02-01" |
| offset      | 分页偏移量，默认0                                            | 否   | [int]    | 0            |
| length      | 分页长度，默认15                                             | 否   | [int]    | 1            |
| next_token  | 分页游标，上次分页结果中的next_token<br>(第一次分页无需填写，当next_token和offset同时存在时以next_token为主 | 否   | [string] | "MTAx"       |

## 请求示例

```
{
  "profile_id": 123456,
  "report_date": "2025-02-01",
  "offset": 0,
  "length": 15,
  "next_token": "MTAx"
}
```

## 返回结果

Json Object

| 参数名                 | 说明                                    | 必填 | 类型     | 示例                                     |
| ---------------------- | --------------------------------------- | ---- | -------- | ---------------------------------------- |
| code                   | 状态码，0 成功                          | 是   | [int]    | 0                                        |
| message                | 提示消息                                | 是   | [string] | "操作成功"                               |
| error_details          | 错误信息                                | 是   | [array]  | -                                        |
| request_id             | 请求链路id                              | 是   | [string] | "6bb694e1-3d25-4821-8db8-d55dc903f6ba"   |
| response_time          | 响应时间                                | 是   | [string] | "2023/2/17 9:59"                         |
| total                  | 总数                                    | 是   | [int]    | 1                                        |
| next_token             | 分页游标，填入下次请求中的next_token    | 是   | [string] | "ODAwMDAwMDAwMDAwMDAyNDE3"               |
| data                   | 响应数据                                | 是   | [array]  | -                                        |
| data>>report_date      | 报告日期                                | 是   | [number] | 800000000000137200                       |
| data>>profile_id       | profile_id                              | 是   | [number] | 800000000000137700                       |
| data>>campaign_id      | 广告活动id                              | 是   | [number] | 448868552891455                          |
| data>>department_id    | -                                       | 是   | [number] | 26                                       |
| data>>ad_group_id      | -                                       | 是   | [string] | "demo sb ads 2023-02-27 7db7"            |
| data>>transaction_uuid | 设置分摊的事务ID,用于追踪具体的分摊规则 | 是   | [string] | "enabled"                                |
| data>>asin             | -                                       | 是   | [number] | 1704643200000                            |
| data>>sku              | -                                       | 是   | [number] | 1704643200000                            |
| data>>impressions      | -                                       | 是   | [number] | 9000000000000013                         |
| data>>clicks           | 点击数                                  | 是   | [string] | "AD_STATUS_LIVE"                         |
| data>>spends           | 广告花费                                | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>orders           | 订单数                                  | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>sales            | 广告销售额                              | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>units_sold       | 销售件数                                | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>same_orders      | 直接订单数                              | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>same_sales       | 直接广告销售额                          | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>same_units_sold  | 直接销售件数                            | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>divide_asin_md5  | md5(ad_group_id, asin, sku)             | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |
| data>>percent          | 分摊比例                                | 是   | [array]  | ["B09MT9BKGH","B0BB389BKQ","B09MYZ614S"] |

## 返回成功示例

```
{
  "code": 0,
  "message": "操作成功",
  "error_details": [],
  "request_id": "6bb694e1-3d25-4821-8db8-d55dc903f6ba",
  "response_time": "2023/2/17 9:59",
  "total": 1,
  "next_token": "ODAwMDAwMDAwMDAwMDAyNDE3",
  "data": [
    {
      "report_date": 800000000000137200,
      "profile_id": 800000000000137700,
      "campaign_id": 448868552891455,
      "department_id": 26,
      "ad_group_id": "demo sb ads 2023-02-27 7db7",
      "transaction_uuid": "enabled",
      "asin": 1704643200000,
      "sku": 1704643200000,
      "impressions": 9000000000000013,
      "clicks": "AD_STATUS_LIVE",
      "spends": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "orders": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "sales": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "units_sold": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "same_orders": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "same_sales": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "same_units_sold": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "divide_asin_md5": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"],
      "percent": ["B09MT9BKGH", "B0BB389BKQ", "B09MYZ614S"]
    }
  ]
}
```

