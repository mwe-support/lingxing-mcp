# 查询已有商品信息

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/listing/publish/openapi/amazon/product/search` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|store_id|store_id|是|[int]|34|
|skus|sku列表，最多20个|是|[array]|["0Z-WQSX-RMWR"]|


## 请求cURL示例
```bash
curl --location 'https://openapi.lingxing.com/listing/publish/openapi/amazon/product/search?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "store_id": 34,
    "skus": ["0Z-WQSX-RMWR"]
}'
```
## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，1为成功|是|[number]|1|
|msg|消息提示|是|[string]|成功|
|data|响应数据|是|[array]||
|data>>msku|msku|是|[string]|0Z-WQSX-RMWR|
|data>>info|商品信息|是|[object]| |
|request_id|请求链路id|是|[string]|b1b37efc-1eb8-11f1-b429-4ada51ecb306|

## 返回成功示例
```
{
  "code": 1,
  "msg": "成功",
  "data": [
    {
      "msku": "value",
      "info": {
        "summaries": [
          {
            "asin": "value",
            "conditionType": "new_new",
            "createdDate": "2023-07-27T02:53:03.969Z",
            "fnSku": "value",
            "itemName": "NP Phone Holder",
            "lastUpdatedDate": "2023-11-23T11:30:22.391Z",
            "mainImage": {
              "height": 500,
              "link": "value",
              "width": 500
            },
            "marketplaceId": "value",
            "productType": "PORTABLE_ELECTRONIC_DEVICE_STAND",
            "status": [
              "BUYABLE",
              "DISCOVERABLE"
            ]
          }
        ],
        "attributes": {
          "bullet_point": [
            {
              "language_tag": "en_US",
              "marketplace_id": "value",
              "value": "11111111112222222222233333333111111123668811323"
            }
          ],
          "condition_type": [
            {
              "marketplace_id": "value",
              "value": "new_new"
            }
          ],
          "fulfillment_availability": [
            {
              "fulfillment_channel_code": "DEFAULT",
              "lead_time_to_ship_max_days": 12,
              "quantity": 333
            }
          ],
          "generic_keyword": [
            {
              "language_tag": "en_US",
              "marketplace_id": "value",
              "value": "qwer23668811323"
            }
          ],
          "item_dimensions": [
            {
              "height": {
                "unit": "centimeters",
                "value": 5
              },
              "length": {
                "unit": "centimeters",
                "value": 10
              },
              "marketplace_id": "value",
              "width": {
                "unit": "centimeters",
                "value": 8
              }
            }
          ],
          "item_name": [
            {
              "language_tag": "en_US",
              "marketplace_id": "value",
              "value": "Women's Red Plaid A-Line Mini Skirt"
            }
          ],
          "item_package_dimensions": [
            {
              "height": {
                "unit": "centimeters",
                "value": 6
              },
              "length": {
                "unit": "centimeters",
                "value": 12
              },
              "marketplace_id": "value",
              "width": {
                "unit": "centimeters",
                "value": 9
              }
            }
          ],
          "item_package_weight": [
            {
              "marketplace_id": "value",
              "unit": "kilograms",
              "value": 0.2
            }
          ],
          "item_weight": [
            {
              "marketplace_id": "value",
              "unit": "kilograms",
              "value": 0.17
            }
          ],
          "list_price": [
            {
              "currency": "USD",
              "marketplace_id": "value",
              "value": 103
            }
          ],
          "main_product_image_locator": [
            {
              "marketplace_id": "value",
              "media_location": "value"
            }
          ],
          "merchant_shipping_group": [
            {
              "marketplace_id": "value",
              "value": "value"
            }
          ],
          "merchant_suggested_asin": [
            {
              "marketplace_id": "value",
              "value": "value"
            }
          ],
          "other_product_image_locator_1": [
            {
              "marketplace_id": "value",
              "media_location": "value"
            }
          ],
          "other_product_image_locator_2": [
            {
              "marketplace_id": "value",
              "media_location": "value"
            }
          ],
          "product_description": [
            {
              "language_tag": "en_US",
              "marketplace_id": "value",
              "value": "<p>4112323668811323</p>"
            }
          ],
          "product_site_launch_date": [
            {
              "marketplace_id": "value",
              "value": "2023-07-27T02:51:53.956Z"
            }
          ],
          "purchasable_offer": [
            {
              "audience": "ALL",
              "currency": "USD",
              "discounted_price": [
                {
                  "schedule": [
                    {
                      "end_at": "2025-06-05T07:00:00Z",
                      "start_at": "2025-06-04T07:00:00Z",
                      "value_with_tax": 12
                    }
                  ]
                }
              ],
              "end_at": {
                "value": null
              },
              "marketplace_id": "value",
              "our_price": [
                {
                  "schedule": [
                    {
                      "value_with_tax": 15.08
                    }
                  ]
                }
              ],
              "start_at": {
                "value": "2023-07-27T02:51:53.956Z"
              }
            },
            {
              "audience": "B2B",
              "currency": "USD",
              "marketplace_id": "value",
              "our_price": [
                {
                  "schedule": [
                    {
                      "value_with_tax": 68
                    }
                  ]
                }
              ],
              "quantity_discount_plan": [
                {
                  "schedule": [
                    {
                      "discount_type": "percent",
                      "levels": [
                        {
                          "lower_bound": 11,
                          "value": 12
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        "issues": [
          {
            "attributeNames": [
              "form_factor"
            ],
            "categories": [
              "MISSING_ATTRIBUTE"
            ],
            "code": "18448",
            "message": "value",
            "severity": "WARNING"
          },
          {
            "categories": [
              "INVALID_ATTRIBUTE"
            ],
            "code": "8541",
            "message": "value",
            "severity": "ERROR"
          }
        ],
        "offers": [
          {
            "audience": {
              "displayName": "Sell on Amazon",
              "value": "ALL"
            },
            "marketplaceId": "value",
            "offerType": "B2C",
            "price": {
              "amount": "15.08",
              "currency": "USD",
              "currencyCode": "USD"
            }
          },
          {
            "audience": {
              "displayName": "Amazon Business (B2B)",
              "value": "B2B"
            },
            "marketplaceId": "value",
            "offerType": "B2B",
            "price": {
              "amount": "68.0",
              "currency": "USD",
              "currencyCode": "USD"
            }
          }
        ],
        "fulfillmentAvailability": [
          {
            "fulfillmentChannelCode": "DEFAULT",
            "quantity": 333
          }
        ],
        "procurement": [],
        "relationships": [],
        "productTypes": [
          {
            "marketplaceId": "value",
            "productType": "PORTABLE_ELECTRONIC_DEVICE_STAND"
          }
        ]
      }
    }
  ],
  "request_id": "value"
}
```
