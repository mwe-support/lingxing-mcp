# 统计-查询退货分析
支持统计-查询退货分析

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/salesAnalysis/returnOrder/analysisLists` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| endDate | 结束日期，格式：yyyy-MM-dd，与startDate配合使用，最多支持366天范围 | <font color="red">是</font> | [string] | 2024-11-12 |
| length | 分页长度，每页数据条数 | <font color="red">是</font> | [int] | 20 |
| offset | 分页偏移量，当前页码 | <font color="red">是</font> | [int] | 0 |
| startDate | 开始日期，格式：yyyy-MM-dd，与endDate配合使用，最多支持366天范围 | <font color="red">是</font> | [string] | 2024-11-01 |
| asinType | 维度类型，枚举值：msku, asin, parentAsin, sku, spu（注意：不支持sid、country、category、band） | <font color="red">是</font> | [string] | msku |
| dateType | 时间类型，枚举值：0-退货时间, 1-下单时间 | <font color="red">是</font> | [int] | 0 |
| mids | 国家ID列表（mid） | 否 | [array] | [1,2,3] |
| principalUid | 负责人ID列表 | 否 | [array] | [1234567890,9876543210] |
| searchField | 搜索字段类型，枚举值：msku-MSKU, asin-ASIN, parentAsin-父ASIN, localSku-SKU, localName-品名, spu-SPU, spuName-款名 | 否 | [string] | msku |
| searchValue | 搜索值列表，与searchField配合使用 | 否 | [array] | ["TEST-SKU-001","TEST-SKU-002"] |
| sortField | 排序字段，枚举值：curReturnGoodsCount-退货量, returnGoodsCountRatio-退货量环比, curVolume-销量, curReturnGoodsVolumeRatio-退货率, returnGoodsVolumeRatioDiff-退货率环比差异 | 否 | [string] | curReturnGoodsCount |
| sortType | 排序类型，枚举值：ASC-升序, DESC-降序 | 否 | [string] | DESC |
| storeId | 店铺ID列表 | 否 | [array] | [123456789012345] |

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/salesAnalysis/returnOrder/analysisLists?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "endDate": "2024-11-12",
    "length": 20,
    "offset": 0,
    "startDate": "2024-11-01",
    "asinType": "msku",
    "dateType": 0,
    "mids": [1,2,3],
    "principalUid": [1234567890,9876543210],
    "searchField": "msku",
    "searchValue": ["TEST-SKU-001","TEST-SKU-002"],
    "sortField": "curReturnGoodsCount",
    "sortType": "DESC",
    "storeId": [123456789012345]
}'
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 响应码 | 是 | [int] |  |
| data | 返回数据 | 是 | [object] |  |
| data>>records | 退货分析记录列表 | 是 | [array] |  |
| data>>records>>asinsList | ASIN列表 | 是 | [array] |  |
| data>>records>>asinsList>>asin | ASIN，亚马逊标准识别号 | 是 | [string] | B08XYZ123AB |
| data>>records>>asinsList>>asinUrl | ASIN商品详情页URL地址 | 是 | [string] |  |
| data>>records>>curReturnGoodsCount | 当期退货量 | 是 | [int] | 30 |
| data>>records>>curReturnGoodsCountDistribution | 当期退货量分布明细（FBA/FBM） | 是 | [object] |  |
| data>>records>>curReturnGoodsCountDistribution>>fbaQuantity | FBA退货数量 | 是 | [int] | 25 |
| data>>records>>curReturnGoodsCountDistribution>>fbmQuantity | FBM退货数量 | 是 | [int] | 5 |
| data>>records>>curReturnGoodsItems | 当期退货订单数 | 是 | [int] | 20 |
| data>>records>>curReturnGoodsItemsDistribution | 当期退货订单数分布明细（FBA/FBM） | 是 | [object] |  |
| data>>records>>curReturnGoodsItemsDistribution>>fbaQuantity | FBA退货订单数 | 是 | [int] | 15 |
| data>>records>>curReturnGoodsItemsDistribution>>fbmQuantity | FBM退货订单数 | 是 | [int] | 5 |
| data>>records>>curReturnGoodsVolumeRatio | 当期退货率 | 是 | [string] | 5.00% |
| data>>records>>curVolume | 当期销量 | 是 | [int] | 600 |
| data>>records>>eventDate | 买家之声-后台更新时间，格式：yyyy-MM-dd，仅MSKU维度有此字段 | 否 | [string] | 2024-06-10 |
| data>>records>>fnskuInfoList | FNSKU信息列表 | 是 | [array] |  |
| data>>records>>fnskuInfoList>>fnsku | FNSKU，亚马逊物流SKU | 是 | [string] | X001ABC123 |
| data>>records>>fnskuInfoList>>msku | MSKU，卖家SKU | 是 | [string] | TEST-MSKU-001 |
| data>>records>>infoDTOList | 综合信息列表（包含商品、店铺、分类等详细信息） | 是 | [array] |  |
| data>>records>>infoDTOList>>asin | ASIN，亚马逊标准识别号 | 是 | [string] | B08XYZ123AB |
| data>>records>>infoDTOList>>asinUrl | ASIN商品详情页URL地址 | 是 | [string] | 3 |
| data>>records>>infoDTOList>>bid | 品牌ID | 是 | [long] | 9876543210 |
| data>>records>>infoDTOList>>brandTitle | 品牌标题 | 是 | [string] | MyBrand |
| data>>records>>infoDTOList>>categoryTitle | 商品分类标题 | 是 | [string] | 服装 |
| data>>records>>infoDTOList>>cid | 分类ID | 是 | [string] | 12345 |
| data>>records>>infoDTOList>>country | 国家代码 | 是 | [string] | US |
| data>>records>>infoDTOList>>fnsku | FNSKU，亚马逊物流SKU | 是 | [string] | X001ABC123 |
| data>>records>>infoDTOList>>fulfillmentChannel | 配送渠道，枚举值：FBA-亚马逊配送, FBM-卖家自配送 | 是 | [string] | FBA |
| data>>records>>infoDTOList>>localName | 本地商品名称，品名 | 是 | [string] | 男士圆领T恤 |
| data>>records>>infoDTOList>>localSku | 本地SKU | 是 | [string] | LOCAL-SKU-001 |
| data>>records>>infoDTOList>>msku | MSKU，卖家SKU | 是 | [string] | TEST-MSKU-001 |
| data>>records>>infoDTOList>>sellerName | 店铺名称 | 是 | [string] | MyAmazonStore |
| data>>records>>infoDTOList>>sid | 店铺ID | 是 | [long] | 1234567890 |
| data>>records>>infoDTOList>>smallImageUrl | 商品小图片URL地址 | 是 | [string] |g |
| data>>records>>infoDTOList>>spu | SPU编码 | 是 | [string] | SPU-2024-001 |
| data>>records>>infoDTOList>>spuName | SPU名称，款名 | 是 | [string] | 夏季T恤系列 |
| data>>records>>isParent | 是否为父ASIN | 是 | [string] | 1 |
| data>>records>>localSkuInfoList | 本地SKU信息列表 | 是 | [array] |  |
| data>>records>>localSkuInfoList>>localName | 本地商品名称，品名 | 是 | [string] | 男士圆领T恤 |
| data>>records>>localSkuInfoList>>localSku | 本地SKU | 是 | [string] | LOCAL-SKU-001 |
| data>>records>>mostCommonReturnReasonBucket | 买家之声-Top NCX Reason，最常见的不满意原因，仅MSKU维度有此字段 | 否 | [string] | 产品质量问题 |
| data>>records>>msku | MSKU，卖家SKU | 是 | [string] | TEST-MSKU-001 |
| data>>records>>ncxCount | 买家之声-不满意订单数，仅MSKU/ASIN/父ASIN维度有此字段 | 否 | [int] | 7 |
| data>>records>>ncxRate | 买家之声-不满意率，百分比格式，仅MSKU/ASIN/父ASIN维度有此字段 | 否 | [string] | 3.50% |
| data>>records>>orderCount | 买家之声-订单总数，仅MSKU/ASIN/父ASIN维度有此字段 | 否 | [int] | 200 |
| data>>records>>parentAsinsList | 父ASIN列表 | 是 | [array] | ["B08XYZABC1","B09ABCXYZ2"] |
| data>>records>>pcxHealth | 买家之声-满意度状况，枚举值：Good-良好, Fair-一般, Poor-差，仅MSKU维度有此字段 | 否 | [string] | Good |
| data>>records>>preReturnGoodsCount | 上期退货量 | 是 | [int] | 25 |
| data>>records>>preReturnGoodsItems | 上期退货订单数 | 是 | [int] | 15 |
| data>>records>>preReturnGoodsVolumeRatio | 上期退货率 | 是 | [string] | 5.00% |
| data>>records>>preVolume | 上期销量 | 是 | [int] | 500 |
| data>>records>>returnBadge | 退货标记，仅MSKU/ASIN/父ASIN维度有此字段 | 否 | [string] | 高退货率 |
| data>>records>>returnGoodsCountRatio | 退货量环比，相对于上期的增长率 | 是 | [string] | 20.00% |
| data>>records>>returnGoodsVolumeRatioDiff | 退货率环比差异，当期退货率与上期退货率的差值 | 是 | [string] | 1.50% |
| data>>records>>selFnskuSkuInfoList | 店铺FNSKU+SKU综合信息列表 | 是 | [array] |  |
| data>>records>>selFnskuSkuInfoList>>country | 国家代码 | 是 | [string] | US |
| data>>records>>selFnskuSkuInfoList>>fnsku | FNSKU，亚马逊物流SKU | 是 | [string] | X001ABC123 |
| data>>records>>selFnskuSkuInfoList>>localName | 本地商品名称，品名 | 是 | [string] | 男士圆领T恤 |
| data>>records>>selFnskuSkuInfoList>>localSku | 本地SKU | 是 | [string] | LOCAL-SKU-001 |
| data>>records>>selFnskuSkuInfoList>>msku | MSKU，卖家SKU | 是 | [string] | TEST-MSKU-001 |
| data>>records>>selFnskuSkuInfoList>>sellerName | 店铺名称 | 是 | [string] | MyAmazonStore |
| data>>records>>selFnskuSkuInfoList>>sid | 店铺ID | 是 | [long] | 1234567890 |
| data>>records>>selfnskuInfoList | 店铺FNSKU信息列表 | 是 | [array] |  |
| data>>records>>selfnskuInfoList>>country | 国家代码 | 是 | [string] | US |
| data>>records>>selfnskuInfoList>>fnsku | FNSKU，亚马逊物流SKU | 是 | [string] | X001ABC123 |
| data>>records>>selfnskuInfoList>>msku | MSKU，卖家SKU | 是 | [string] | TEST-MSKU-001 |
| data>>records>>selfnskuInfoList>>sellerName | 店铺名称 | 是 | [string] | MyAmazonStore |
| data>>records>>selfnskuInfoList>>sid | 店铺ID | 是 | [long] | 1234567890 |
| data>>records>>sellerInfoList | 店铺信息列表 | 是 | [array] |  |
| data>>records>>sellerInfoList>>country | 国家代码 | 是 | [string] | US |
| data>>records>>sellerInfoList>>sellerName | 店铺名称 | 是 | [string] | MyAmazonStore |
| data>>records>>sellerInfoList>>sid | 店铺ID | 是 | [long] | 1234567890 |
| data>>records>>sid | 店铺ID | 是 | [long] | 1234567890 |
| data>>records>>spuInfoList | SPU信息列表 | 是 | [array] |  |
| data>>records>>spuInfoList>>spu | SPU编码 | 是 | [string] | SPU-2024-001 |
| data>>records>>spuInfoList>>spuName | SPU名称，款名 | 是 | [string] | 夏季T恤系列 |
| data>>total | 总记录数 | 是 | [int] | 100 |
| error_details | 错误详情 | 是 | [array] |  |
| message | 提示信息 | 是 | [string] |  |
| request_id | 请求id | 是 | [string] |  |
| response_time | 响应时间 | 是 | [string] |  |
| total | 总记录数 | 是 | [int] |  |

## 返回成功示例
```
{
  "code": 0,
  "data": {
    "records": [
      {
        "asinsList": [
          {
            "asin": "B08XYZ123AB",
            "asinUrl": ""
          }
        ],
        "curReturnGoodsCount": 30,
        "curReturnGoodsCountDistribution": {
          "fbaQuantity": 25,
          "fbmQuantity": 5
        },
        "curReturnGoodsItems": 20,
        "curReturnGoodsItemsDistribution": {
          "fbaQuantity": 15,
          "fbmQuantity": 5
        },
        "curReturnGoodsVolumeRatio": "5.00%",
        "curVolume": 600,
        "eventDate": "2024-06-10",
        "fnskuInfoList": [
          {
            "fnsku": "X001ABC123",
            "msku": "TEST-MSKU-001"
          }
        ],
        "infoDTOList": [
          {
            "asin": "B08XYZ123AB",
            "asinUrl": "",
            "bid": 9876543210,
            "brandTitle": "MyBrand",
            "categoryTitle": "服装",
            "cid": "12345",
            "country": "US",
            "fnsku": "X001ABC123",
            "fulfillmentChannel": "FBA",
            "localName": "男士圆领T恤",
            "localSku": "LOCAL-SKU-001",
            "msku": "TEST-MSKU-001",
            "sellerName": "MyAmazonStore",
            "sid": 1234567890,
            "smallImageUrl": "",
            "spu": "SPU-2024-001",
            "spuName": "夏季T恤系列"
          }
        ],
        "isParent": "1",
        "localSkuInfoList": [
          {
            "localName": "男士圆领T恤",
            "localSku": "LOCAL-SKU-001"
          }
        ],
        "mostCommonReturnReasonBucket": "产品质量问题",
        "msku": "TEST-MSKU-001",
        "ncxCount": 7,
        "ncxRate": "3.50%",
        "orderCount": 200,
        "parentAsinsList": "[\"B08XYZABC1\",\"B09ABCXYZ2\"]",
        "pcxHealth": "Good",
        "preReturnGoodsCount": 25,
        "preReturnGoodsItems": 15,
        "preReturnGoodsVolumeRatio": "5.00%",
        "preVolume": 500,
        "returnBadge": "高退货率",
        "returnGoodsCountRatio": "20.00%",
        "returnGoodsVolumeRatioDiff": "1.50%",
        "selFnskuSkuInfoList": [
          {
            "country": "US",
            "fnsku": "X001ABC123",
            "localName": "男士圆领T恤",
            "localSku": "LOCAL-SKU-001",
            "msku": "TEST-MSKU-001",
            "sellerName": "MyAmazonStore",
            "sid": 1234567890
          }
        ],
        "selfnskuInfoList": [
          {
            "country": "US",
            "fnsku": "X001ABC123",
            "msku": "TEST-MSKU-001",
            "sellerName": "MyAmazonStore",
            "sid": 1234567890
          }
        ],
        "sellerInfoList": [
          {
            "country": "US",
            "sellerName": "MyAmazonStore",
            "sid": 1234567890
          }
        ],
        "sid": 1234567890,
        "spuInfoList": [
          {
            "spu": "SPU-2024-001",
            "spuName": "夏季T恤系列"
          }
        ]
      }
    ],
    "total": 100
  },
  "error_details": [],
  "message": "value",
  "request_id": "value",
  "response_time": "value",
  "total": 0
}
```
