# 续约接口令牌 
给 access_token 延续有效期，每个refresh_token 只能使用一次

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/api/auth-server/oauth/refresh` | HTTPS | POST | 100 |

## 请求头
| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|Content-Type|是|请求内容类型|[string]|multipart/form-data|

## 请求参数

| 参数名  | 说明 | 必填 | 类型 |  示例  |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|appId|AppID，在ERP开放接口中获取|是|[string]|  |
|refreshToken|refreshToken，[获取接口令牌-token](docs/Authorization/GetToken) 接口对应字段【refresh_token】|是|[string]| &nbsp; |


## 返回结果
Json
Object

| 参数名  | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码|是|[int]|200|
|msg|消息提示|是|[string]|  |
|data|响应数据|是|[object]|  |
|data>>access_token|access_token|是|[string]|  |
|data>>refresh_token|refresh_token|是|[string]|  |
|data>>expires_in|access_token过期时间|是|[string]| &nbsp; |

## 返回成功示例

```
{
    "code": "200",
    "msg": "OK",
    "data": {
        "access_token": "8083150d-e4d9-4b09-a54e-b8c759532396",
        "refresh_token": "7bdbbaf8-495d-4f3a-b792-78747b86fb47",
        "expires_in": 7199
    }
}
```
