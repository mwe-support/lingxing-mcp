# 查询买家之声列表

- MCP tool: `lingxing_voice_of_buyer`
- Official doc: `https://apidoc.lingxing.com/#/docs/Service/voiceOfBuyerList`
- API path: `POST /basicOpen/customerService/voiceOfBuyer/list`
- Token bucket capacity: `1`

## Purpose

查询买家之声列表，用于按店铺、配送方式、满意度、ASIN/MSKU/SKU 或退货标记筛选商品健康数据。

## Request Fields

| MCP arg | Official field | Type | Required | Notes |
|---|---|---|---|---|
| `sids` | `sids` | integer array | No | 店铺 sid 列表。 |
| `fulfillment_channel` | `fulfillment_channel` | string | No | `FBA` or `MFN`; `MFN` 对应 FBM。 |
| `pxc_health` | `pxc_health` | string array | No | `-1` 反馈不足, `0` 极差, `1` 不合格, `2` 一般, `3` 良好, `4` 极好。 |
| `search_field` | `search_field` | string | No | `asin`, `msku`, or `sku`. |
| `search_value` | `search_value` | string array | No | 配合 `search_field` 使用。 |
| `return_badge` | `return_badge` | string array | No | `Yes`, `No`, or `At_Risk`. |

The MCP tool automatically paginates with official `offset` / `length` fields and uses `length=200`, the documented maximum page size.

## Key Response Fields

| Field | Meaning |
|---|---|
| `sid`, `seller_name`, `country` | 店铺、店铺名、国家。 |
| `asin`, `asin_url`, `title` | ASIN、Amazon 链接和标题。 |
| `msku`, `sku`, `fnsku` | MSKU、本地 SKU 和 FNSKU。 |
| `fulfillment_channel` | 配送方式，`FBA` or `MFN`。 |
| `ncx_rate`, `ncx_count`, `order_count` | 不满意率、不满意订单数量、订单总数。 |
| `most_common_return_reason_bucket` | 主要退货原因。 |
| `event_date` | 买家之声上次更新日期。 |
| `pcx_health_text` | 满意度状况说明。 |
| `returnBadge`, `returnRate` | 退货标记、退货率。 |

