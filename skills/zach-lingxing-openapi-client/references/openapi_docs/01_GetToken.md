# 获取 access-token和refresh-token

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/api/auth-server/oauth/access-token` | HTTPS | POST | 100 |

## 请求头
| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|Content-Type|是|请求内容类型|[string]|multipart/form-data|

## 请求参数

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|appId|AppID，在ERP开放接口菜单中获取|是|[string]|  |
|appSecret|AppSecret，在ERP开放接口菜单中获取|是|[string]| &nbsp; |

## 请求curl示例
```
curl --location 'https://openapi.lingxing.com/api/auth-server/oauth/access-token' \
--form 'appId="appId"' \
--form 'appSecret="appSecret"'
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码|是|[int]|200|
|msg|消息提示|是|[string]|  |
|data|响应数据|是|[object]|  |
|data>>access_token|access_token，请求令牌token|是|[string]|  |
|data>>refresh_token|refresh_token，可以使用它来给access_token延续有效期|是|[string]|  |
|data>>expires_in|access_token过期时间|是|[string]| &nbsp; |

## 返回成功示例

```
{
    "code": "200",
    "msg": "OK",
    "data": {
        "access_token": "4dcaa78e-b52d-4325-bc35-571021bb0787",
        "refresh_token": "da5b5047-e6d1-496c-ab4d-d5425a6a66e4",
        "expires_in": 7199
    }
}
```

## 返回失败示例

```
{
    "code": "2001001",
    "msg": "app not exist",
    "data": null
}
```
