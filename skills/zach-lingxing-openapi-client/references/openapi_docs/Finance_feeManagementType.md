# 查询费用类型列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/fee/management/open/feeManagement/otherFee/type` | HTTPS | POST | 1 |

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|msg|消息提示|是|[string]|操作成功|
|data|响应数据|是|[array]| |
|data>>id|费用类型id|是|[int]|1000014|
|data>>sort|排序|是|[int]|0|
|data>>name|费用名称|是|[string]|费用类型1|
|data>>fpoft_id|备用id|是|[string]|305250800313991680|

## 返回成功示例
```
{
    "code": 0,
    "msg": "操作成功",
    "data": [
        {
            "id": 1000014,
            "sort": 0,
            "name": "费用类型1",
            "fpoft_id": "305250800313991680"
        }
    ]
}
```
