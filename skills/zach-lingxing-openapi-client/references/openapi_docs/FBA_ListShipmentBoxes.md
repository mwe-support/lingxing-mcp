# 查询货件装箱信息
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-shipment/listShipmentBoxes` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|shipmentIdList|货件id|是|[array]| ["shd10e38ca-45e7-4a97-8512-780acf343f4b3"]|
|sid|亚马逊店铺sid，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-shipment/listShipmentBoxes?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
    "shipmentIdList": "货件id",
    "sid": 1
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功|是|[int]|	0 |
|message|消息提示 |是|[string]|success |
|errorDetails|错误信息 |是|[array]| |
|requestId| 请求链路id|是|[string]| |
|responseTime|响应时间 |是|[string]| 2020-05-18 11:23:47|
|data| 响应数据|是|[object]| |
|data>>inboundPlanId|STA任务编号|是|[string]| |
|data>>shipmentList|货件装箱信息|是|[array]| |
|data>>shipmentList>>palletList|托帕明细|是|[array]| |
|data>>shipmentList>>palletList>>height|托帕高度|是|[number]| |
|data>>shipmentList>>palletList>>length|托帕长度|是|[number]| |
|data>>shipmentList>>palletList>>lengthUnit|长度单位(IN-英制,CM-公制)|是|[string]| |
|data>>shipmentList>>palletList>>quantity|托帕数量|是|[int]| |
|data>>shipmentList>>palletList>>stackability|是是可堆叠|是|[string]| |
|data>>shipmentList>>palletList>>weight|托帕重量|是|[number]| |
|data>>shipmentList>>palletList>>weightUnit|重量单位（LB-磅，KG-千克）|是|[string]| |
|data>>shipmentList>>palletList>>width|托帕宽度|是|[number]| |
|data>>shipmentList>>shipmentId|货件id|是|[string]| |
|data>>shipmentList>>shipmentPackingList|装箱明细|是|[array]| |
|data>>shipmentList>>shipmentPackingList>>boxId|箱子id|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>height|箱子高度|是|[number]| |
|data>>shipmentList>>shipmentPackingList>>length|箱子长度|是|[number]| |
|data>>shipmentList>>shipmentPackingList>>lengthUnit|长度单位：含IN、CM|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>packageId|包裹id|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList|商品明细|是|[array]| |
|data>>shipmentList>>shipmentPackingList>>productList>>asin|asin|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>expiration|有效期|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>fnsku|fnsku|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>labelOwner|标签类型（AMAZON,SELLER,NONE）|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>msku|msku|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>parentAsin|父asin|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>prepOwner|预处理提供方（AMAZON,SELLER,NONE）|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>productName|品名|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>quantityInBox|单箱数量|是|[int]| |
|data>>shipmentList>>shipmentPackingList>>productList>>sku|sku|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>title|标题|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>productList>>url|图片url|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>total|商品总数量|是|[int]| |
|data>>shipmentList>>shipmentPackingList>>weight|箱子重量|是|[number]| |
|data>>shipmentList>>shipmentPackingList>>weightUnit|重量单位：含LB、KG|是|[string]| |
|data>>shipmentList>>shipmentPackingList>>width|箱子宽度|是|[number]| ||
|data>>shipmentList>>shipmentPackingList>>box_name|箱名<br>先装箱再分仓时box_name格式为【Px-By】，表示包装x组第y箱； <br>先分仓再装箱时box_name格式为【货件单号-Bx】，表示货件第x箱|是|[string]|先装箱再分仓时：P1-B1 <br>先分仓再装箱时：FBA18QJFDCWJ - B11 ||


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": null,
    "requestId": "4848b0c49fa64012a381c81bdf826d30.1733129764446",
    "responseTime": "2024-12-02T16:56:04.446",
    "data": {
        "inboundPlanId": "wf99cc1a5d-b08d-4237-8419-bd63ce084f7d",
        "shipmentList": [
            {
                "shipmentId": "sh58020432-5479-48f7-b730-5786820eed44",
                "shipmentPackingList": [
                    {
                        "localBoxId": "1",
                        "packageId": null,
                        "boxId": null,
                        "total": 1,
                        "weight": 12.320000,
                        "weightUnit": "KG",
                        "length": 12.000000,
                        "width": 3.000000,
                        "height": 4.000000,
                        "lengthUnit": "CM",
                        "productList": [
                            {
                                "msku": "20240122-GM",
                                "fnsku": "X0047Z5K5Z",
                                "asin": "B0CM59V6Y8",
                                "parentAsin": "B0CPSY8HFP",
                                "productName": "饭饭饭",
                                "sku": "ggggasda",
                                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky-GM",
                                "url": "https://m.media-amazon.com/images/I/61-v2WaQOhL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            }
                        ]
                    },
                    {
                        "localBoxId": "2",
                        "packageId": null,
                        "boxId": null,
                        "total": 1,
                        "weight": 5.330000,
                        "weightUnit": "KG",
                        "length": 2.000000,
                        "width": 13.000000,
                        "height": 4.000000,
                        "lengthUnit": "CM",
                        "productList": [
                            {
                                "msku": "CN0002",
                                "fnsku": "X00489S3FJ",
                                "asin": "B0D3F2W56C",
                                "parentAsin": "B0D3F2W56C",
                                "productName": "随便spu-3",
                                "sku": "asdkpasdk",
                                "title": "Notes,Creative Cartoon,Students,Can Post It,Can Tear Messages N Times Paste",
                                "url": "https://m.media-amazon.com/images/I/51YvC-1dvXL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            }
                        ]
                    },
                    {
                        "localBoxId": "3",
                        "packageId": null,
                        "boxId": null,
                        "total": 1,
                        "weight": 5.330000,
                        "weightUnit": "KG",
                        "length": 2.000000,
                        "width": 13.000000,
                        "height": 4.000000,
                        "lengthUnit": "CM",
                        "productList": [
                            {
                                "msku": "CN0002",
                                "fnsku": "X00489S3FJ",
                                "asin": "B0D3F2W56C",
                                "parentAsin": "B0D3F2W56C",
                                "productName": "随便spu-3",
                                "sku": "asdkpasdk",
                                "title": "Notes,Creative Cartoon,Students,Can Post It,Can Tear Messages N Times Paste",
                                "url": "https://m.media-amazon.com/images/I/51YvC-1dvXL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            }
                        ]
                    },
                    {
                        "localBoxId": "4",
                        "packageId": null,
                        "boxId": null,
                        "total": 2,
                        "weight": 7.550000,
                        "weightUnit": "KG",
                        "length": 2.990000,
                        "width": 3.220000,
                        "height": 4.330000,
                        "lengthUnit": "CM",
                        "productList": [
                            {
                                "msku": "STN0002",
                                "fnsku": "X00489S34P",
                                "asin": "B0D3F37ZPB",
                                "parentAsin": "B0D3F37ZPB",
                                "productName": "成本",
                                "sku": "117009ZZ",
                                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky",
                                "url": "https://m.media-amazon.com/images/I/61FW9bR5rKL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 2,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            }
                        ]
                    }
                ],
                "palletList": []
            },
            {
                "shipmentId": "sh3c90571c-5655-44cc-a18f-3d7479623816",
                "shipmentPackingList": [
                    {
                        "localBoxId": "1",
                        "packageId": null,
                        "boxId": null,
                        "total": 3,
                        "weight": 12.330000,
                        "weightUnit": "KG",
                        "length": 12.220000,
                        "width": 5.660000,
                        "height": 7.550000,
                        "lengthUnit": "CM",
                        "productList": [
                            {
                                "msku": "20240122-GM",
                                "fnsku": "X0047Z5K5Z",
                                "asin": "B0CM59V6Y8",
                                "parentAsin": "B0CPSY8HFP",
                                "productName": "饭饭饭",
                                "sku": "ggggasda",
                                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky-GM",
                                "url": "https://m.media-amazon.com/images/I/61-v2WaQOhL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            },
                            {
                                "msku": "CN0002",
                                "fnsku": "X00489S3FJ",
                                "asin": "B0D3F2W56C",
                                "parentAsin": "B0D3F2W56C",
                                "productName": "随便spu-3",
                                "sku": "asdkpasdk",
                                "title": "Notes,Creative Cartoon,Students,Can Post It,Can Tear Messages N Times Paste",
                                "url": "https://m.media-amazon.com/images/I/51YvC-1dvXL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            },
                            {
                                "msku": "STN0002",
                                "fnsku": "X00489S34P",
                                "asin": "B0D3F37ZPB",
                                "parentAsin": "B0D3F37ZPB",
                                "productName": "成本",
                                "sku": "117009ZZ",
                                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky",
                                "url": "https://m.media-amazon.com/images/I/61FW9bR5rKL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            }
                        ]
                    },
                    {
                        "localBoxId": "2",
                        "packageId": null,
                        "boxId": null,
                        "total": 2,
                        "weight": 8.360000,
                        "weightUnit": "KG",
                        "length": 4.220000,
                        "width": 5.330000,
                        "height": 1.220000,
                        "lengthUnit": "CM",
                        "productList": [
                            {
                                "msku": "20240122-GM",
                                "fnsku": "X0047Z5K5Z",
                                "asin": "B0CM59V6Y8",
                                "parentAsin": "B0CPSY8HFP",
                                "productName": "饭饭饭",
                                "sku": "ggggasda",
                                "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky-GM",
                                "url": "https://m.media-amazon.com/images/I/61-v2WaQOhL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            },
                            {
                                "msku": "CN0002",
                                "fnsku": "X00489S3FJ",
                                "asin": "B0D3F2W56C",
                                "parentAsin": "B0D3F2W56C",
                                "productName": "随便spu-3",
                                "sku": "asdkpasdk",
                                "title": "Notes,Creative Cartoon,Students,Can Post It,Can Tear Messages N Times Paste",
                                "url": "https://m.media-amazon.com/images/I/51YvC-1dvXL._SL75_.jpg",
                                "expiration": "2025-11-01",
                                "quantityInBox": 1,
                                "prepOwner": "SELLER",
                                "labelOwner": "SELLER"
                            }
                        ]
                    }
                ],
                "palletList": [
                    {
                        "weight": 13,
                        "weightUnit": "LB",
                        "length": 12,
                        "width": 9,
                        "height": 5,
                        "lengthUnit": "IN",
                        "quantity": 3,
                        "stackability": "STACKABLE"
                    }
                ]
            }
        ]
    }
}
```

