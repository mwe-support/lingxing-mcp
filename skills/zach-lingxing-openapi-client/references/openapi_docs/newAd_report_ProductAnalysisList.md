# 出单时段分析（产品）
### 说明：msku的店铺订单等数据指标只是提供广告授权日期之后的统计结果，广告授权日期之前的暂未提供。
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ |:-----------------------------------------------------|
| `/basicOpen/adReport/productOrderAnalysis/list` | HTTPS | POST | 1                                                    |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|sid|是|[string]|17|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|sku|msku最多10个|是|[array]|["DEE-1020","PEE-7"]|
|start_date|开始日期，格式：Y-m-d|是|[string]|2024-09-03|
|end_date|结束日期，格式：Y-m-d|是|[string]|2024-09-16|
|group_type|时间维度<br>hourly 按小时<br>weekly 按周|是|[string]|weekly|
|sponsored_type|广告类型 <br>sp  <br>sd|否|[array]|["sd","sp"]|

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]| |
|request_id|请求链路id|是|[string]|f8411a4fc19148348c7499b3f619c811.1727251040129|
|response_time|响应时间|是|[string]|2024-09-25 15:57:20|
|data|响应数据|是|[object]| |
|data>>list| |是|[array]| |
|data>>list>>key|sub_total 汇总行 group_type= hourly 时对应小时  group_type =weekly 对应周|是|[string]|sub_total|
|data>>list>>store_orders|店铺订单|是|[string]|4934|
|data>>list>>store_orders_percent|店铺订单百分比|是|[string]|100|
|data>>list>>store_units|店铺销量|是|[string]|4934|
|data>>list>>store_units_percent|店铺销量百分比|是|[string]|100|
|data>>list>>store_sales|店铺销售额|是|[string]|14500.57|
|data>>list>>store_sales_percent|店铺销售额百分比|是|[string]|100|
|data>>list>>ad_orders|广告订单|是|[string]|4218|
|data>>list>>ad_orders_percent|广告订单百分比|是|[string]|100%|
|data>>list>>ad_sales|广告销售额|是|[string]|12175.52|
|data>>list>>ad_units|广告销量|是|[string]|4218|
|data>>list>>ad_units_percent|广告销量百分比|是|[string]|100%|
|data>>list>>spend|花费|是|[string]|4404.64|
|data>>list>>impressions|曝光|是|[string]|51991|
|data>>list>>clicks|点击|是|[string]|4684|
|data>>list>>ad_sales_percent|广告销售额百分比|是|[string]|100|
|data>>list>>spend_percent|花费百分比|是|[string]|100|
|data>>list>>acos|acos|是|[string]|36.18%|
|data>>list>>ad_spend_store_percent|广告花费占比|是|[string]|30.38|
|data>>list>>ad_order_store_percent|广告订单占比|是|[string]|85.49|
|data>>list>>as_sales_store_percent|广告销售额占比|是|[string]|83.97|
|data>>list>>ad_units_store_percent|广告销量占比|是|[string]|85.49|
|data>>list>>impression_percent|曝光百分比|是|[string]|100|
|data>>list>>clicks_percent|点击百分比|是|[string]|100|
|data>>list>>roas|roas|是|[string]|2.76|
|data>>list>>ctr|ctr|是|[string]|9.01%|
|data>>list>>cpc|cpc|是|[string]|0.94|
|data>>list>>cvr|cvr|是|[string]|90.05%|
|data>>list>>cpa|cpa|是|[string]|1.04|
|data>>list>>key_chart|group_type= hourly 对应小时的描述  <br>group_type =weekly 周的描述|是|[string]||
|data>>list>>key_table|group_type= hourly 对应小时的描述  <br>group_type =weekly 周的描述|是|[string]||
|total| |是|[int]|0|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/adReport/productOrderAnalysis/list?access_token=value&app_key=value&sign=value&timestamp=value' \
--header 'Content-Type: application/json' \
--data '{
    "sid": "1",
    "sku": ["DEE-1020","PEE-7"],
    "start_date": "2024-09-20",
    "end_date": "2024-09-26",
    "group_type": "hourly",
    "sponsored_type": ["sp"]
}'

```

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "c2d091a6ed6a4c78b558bda2816a4346.1727338836028",
    "response_time": "2024-09-26 16:20:36",
    "data": {
        "list": [
            {
                "key": "sub_total",
                "store_orders": "0",
                "store_orders_percent": "--",
                "store_units": "0",
                "store_units_percent": "--",
                "store_sales": "0",
                "store_sales_percent": "--",
                "ad_orders": "0",
                "ad_orders_percent": "--",
                "ad_sales": "0",
                "ad_units": "0",
                "ad_units_percent": "--",
                "spend": "0",
                "impressions": "0",
                "clicks": "0",
                "ad_sales_percent": "--",
                "spend_percent": "--",
                "acos": "--",
                "ad_spend_store_percent": "--",
                "ad_order_store_percent": "--",
                "as_sales_store_percent": "--",
                "ad_units_store_percent": "--",
                "impression_percent": "--",
                "clicks_percent": "--",
                "roas": "--",
                "ctr": "--",
                "cpc": "--",
                "cvr": "--",
                "cpa": "--",
                "key_chart": "汇总",
                "key_table": "汇总"
            }
        ]
    },
    "total": 0
}
```