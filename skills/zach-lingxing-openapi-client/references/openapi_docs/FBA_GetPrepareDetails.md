# 获取商品预处理信息

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/amzStaServer/openapi/inbound-packing/getPrepDetails` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明                      | 必填 | 类型     | 示例       |
| :----- | :------------------------ | :--- | :------- | :--------- |
| sid    | sid店铺id                 | 是   | [number] | 50         |
| msku   | 商品MSKU: 最多不超过100个 | 是   | [array]  | ["CN0001"] |

## 请求cURL示例

```
curl --location --request POST 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-packing/getPrepDetails?app_key=value&access_token=value&timestamp=value&sign=value' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sid":119,
    "msku":["7T-2COF-AV9I"]
}'
```

## 返回结果

| 参数名             | 说明                           | 必填 | 类型     | 示例                                                   |
| :----------------- | :----------------------------- | :--- | :------- | :----------------------------------------------------- |
| code               | 响应状态码                     | 是   | [number] | 0                                                      |
| message            | 业务提示信息                   | 是   | [string] | 操作成功                                               |
| errorDetails       | 错误详细信息                   | 是   | [null]   |                                                        |
| requestId          | 请求追踪ID                     | 是   | [string] | f44f1ac942e8440e9584e05d20923f9f.215.17404636353283729 |
| responseTime       | 服务端响应时间                 | 是   | [string] | 2025-02-25T14:07:16.258                                |
| data               |                                | 是   | [array]  |                                                        |
| data>>sid          | 亚马逊店铺sid                  | 是   | [string] | 50                                                     |
| data>>msku         | msku                           | 是   | [string] | CN0001                                                 |
| data>>prepOwner    | 预处理方式                     | 是   | [string] | SELLER                                                 |
| data>>labelOwner   | 标签方式                       | 是   | [string] | SELLER                                                 |
| data>>prepCategory | 预处理分类，具体见附加说明     | 是   | [string] | TEXTILE                                                |
| data>>prepTypes    | 预处理类型集合，具体见附加说明 | 是   | [array]  | ["ITEM_LABELING","ITEM_POLYBAGGING"]                   |

## 返回成功示例

```
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": null,
    "requestId": "dadf4732e5b543b4bc26cc5438140122.1740989522601",
    "responseTime": "2025-03-03T16:12:03.775",
    "data": [
        {
            "sid": "119",
            "msku": "7T-2COF-AV9I",
            "prepOwner": "NONE",
            "labelOwner": "NONE",
            "prepCategory": "NONE",
            "prepTypes": null
        }
    ]
}
```

## 附加说明

1、`prepCategory`字段说明：

预处理分类：

ADULT-成人：对应的预处理类型通常为无需预处理[ITEM_NO_PREP]

HANGER-悬挂在衣架上的服装：对应的预处理类型通常为聚乙烯塑料袋包装、取下衣架[ITEM_RMOVHANG, ITEM_POLYBAGGING]

TEXTILE-服装、面料、毛绒玩具和纺织品：对应的预处理类型通常为聚乙烯塑料袋包装[ITEM_POLYBAGGING]

BABY-母婴用品：对应的预处理类型通常为无需预处理[ITEM_NO_PREP]

FRAGILE-易碎品：对应的预处理类型通常为气泡膜包装、贴标签[ITEM_BUBBLEWRAP, ITEM_LABELING]

LIQUID-液体（未存放在玻璃容器中）：对应的预处理类型通常为无需预处理[ITEM_NO_PREP]

PERFORATED-打孔包装：对应的预处理类型通常为聚乙烯塑料袋包装、窒息警告[ITEM_POLYBAGGING, ITEM_SUFFOSTK]

GRANULAR-粉末、球状或颗粒状物品：对应的预处理类型通常为聚乙烯塑料袋包装、窒息警告[ITEM_POLYBAGGING, ITEM_SUFFOSTK]

SHARP-尖利物品：对应的预处理类型通常为气泡膜包装、贴标签[ITEM_BUBBLEWRAP, ITEM_LABELING]

SMALL-小号：对应的预处理类型通常为聚乙烯塑料袋包装、贴标签[ITEM_POLYBAGGING, ITEM_LABELING]

SET-套装销售：对应的预处理类型通常为气泡膜包装、贴标签、套装创建[ITEM_BUBBLEWRAP, ITEM_SETCREAT, ITEM_LABELING]

NONE-无需进行预处理：对应的预处理类型通常为无需预处理[ITEM_NO_PREP]

UNKNOWN-未设置：表示未设置预处理类型。该值仅用于查询，不可作为入参。

FC_PROVIDED-由亚马逊确定：表示由亚马逊Fulfillment Center确定预处理类型。该值仅用于查询，不可作为入参。

2、`prepTypes`字段说明

预处理操作类型

ITEM_NO_PREP-无需预处理：商品不需要任何预处理

ITEM_POLYBAGGING-聚乙烯塑料袋包装：将商品放在透明袋中，以防破损、落尘或泄漏。包装袋必须印有窒息警告，必须密封（如果不是自粘袋）。商品也可以使用收缩包装。

ITEM_BUBBLEWRAP-气泡膜包装：如果商品本身不具有保护性包装，请将每件商品都用保护性气泡膜包装或者缠裹起来，也可以将商品放在保护性套箱或气泡袋中（气泡袋必须有窒息警告）。确保包装严密且完全覆盖裸露的边缘。

ITEM_LABELING-贴标签：必须在商品上应用FNSKU标签。

ITEM_SUFFOSTK-窒息警告：开口12厘米或更大的塑料袋（平放时测量）必须有窒息警告。此警告必须印在袋子上或作为标签附加。

ITEM_RMOVHANG-取下衣架：商品不能使用衣架发货。

ITEM_SETCREAT-套装创建：成套销售的商品必须在包装上贴上套装标签。例如，“套装销售”、“准备发货”或“套装勿拆”。单件商品上的条形码不得朝外，否则应予以遮盖。

ITEM_BLACK_SHRINKWRAP-不透明袋包装：将商品放入黑色或不透明的包装袋中，包装袋必须印有窒息警告，必须封紧（如果不是自粘袋）。

ITEM_SIOC-原包装发货：商品以原始产品包装发货。

ITEM_HANG_GARMENT-悬挂衣服：取下衣架，然后将商品放入透明袋中，以防损坏或落尘。商品也可以使用收缩包装。

ITEM_SETSTK-套装销售：套装产品必须在包装上标明为套装。在子套装产品上添加一个标签，清楚地说明产品必须作为整体单位接受和销售。例如，如果一套六个独特的玩具车作为整体单位销售，每辆车的包装必须表明它是套装的一部分

ITEM_TAPING-胶带固定：表示需要用胶带固定。

ITEM_BOXING-装箱：对于锋利物品、易碎物品、危险液体和黑胶唱片，可能需要装箱。对于超过4.5公斤的物品，请使用双壁瓦楞箱。

ITEM_BLANKSTK-空白贴纸：商品需要一个空白贴纸来遮盖无法被另一个贴纸覆盖的不良条形码

ITEM_CAP_SEALING-二次密封：为了防止泄漏，产品需要有以下类型的二次密封：感应密封、安全环、夹子、热收缩塑料袋或装箱。

ITEM_DEBUNDLE-拆包：需要拆开标有单独销售的一组商品。