# 查询退货分析

- MCP tool: lingxing_return_analysis
- Endpoint: /basicOpen/salesAnalysis/returnOrder/analysisLists
- Method: POST
- Source: 领星 API 文档 Statistics / ReturnOrderAnalysisLists
- Token bucket capacity: 1

## 用途

查询退货分析聚合数据，用于按 MSKU、ASIN、父 ASIN、SKU 或 SPU 等维度分析退货数量、退货件数、退货率、当前销量、退货原因和相关健康指标。

## MCP 参数

| 参数 | 必填 | 类型 | 说明 |
| --- | --- | --- | --- |
| startDate | 是 | string | 开始日期，格式 yyyy-MM-dd。与 endDate 的跨度最大 366 天。 |
| endDate | 是 | string | 结束日期，格式 yyyy-MM-dd。与 startDate 的跨度最大 366 天。 |
| asinType | 是 | string | 聚合维度。可选 msku、asin、parentAsin、sku、spu。接口不支持 sid、country、category、band。 |
| dateType | 是 | integer | 日期类型。0 表示退货时间，1 表示下单时间。 |
| mids | 否 | array integer | 国家 ID 列表。 |
| principalUid | 否 | array integer | 负责人 ID 列表。 |
| searchField | 否 | string | 搜索字段。可选 msku、asin、parentAsin、localSku、localName、spu、spuName。 |
| searchValue | 否 | array string | 搜索值列表，需要配合 searchField 使用。 |
| sortField | 否 | string | 排序字段。可选 curReturnGoodsCount、returnGoodsCountRatio、curVolume、curReturnGoodsVolumeRatio、returnGoodsVolumeRatioDiff。 |
| sortType | 否 | string | 排序方向。ASC 或 DESC。 |
| storeId | 否 | array integer | 店铺 ID 列表。 |

分页参数 offset 和 length 由 MCP 网关自动补充并合并分页结果。

## 主要返回字段

接口返回 data.records 和 data.total。常用字段包括 asinsList、curReturnGoodsCount、curReturnGoodsItems、curReturnGoodsVolumeRatio、curVolume、eventDate、fnskuInfoList、infoDTOList、isParent、localSkuInfoList、mostCommonReturnReasonBucket、msku、ncxCount、ncxRate、orderCount、parentAsinsList、pcxHealth、preReturnGoodsCount、preReturnGoodsItems、preReturnGoodsVolumeRatio、preVolume、returnBadge、returnGoodsCountRatio、returnGoodsVolumeRatioDiff、sellerInfoList、sid、spuInfoList。
