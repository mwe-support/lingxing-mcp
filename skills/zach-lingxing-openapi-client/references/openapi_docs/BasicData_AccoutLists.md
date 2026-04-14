# 查询ERP用户信息列表
查询得到企业开启的全部ERP账号数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/account/lists` | HTTPS | GET | 1 |

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]| |
|data>>uid|用户id|是|[int]|1|
|data>>realname|姓名|是|[string]|超级管理员|
|data>>username|用户名|是|[string]|admin|
|data>>mobile|电话|是|[string]|15xxxxxxxx|
|data>>email|邮箱|是|[string]|15xxxxxxx4@qq.com|
|data>>login_num|登陆次数|是|[int]|146|
|data>>last_login_time|最近登录时间|是|[string]|2021-01-11 16:58:29|
|data>>last_login_ip|最近登录IP|是|[string]|127.0.0.1|
|data>>status|状态：0 禁用，1 正常|是|[int]|1|
|data>>create_time|创建时间|是|[string]|2018-01-01 00:00|
|data>>role|角色|是|[string]|测试角色,WMS权限角色|
|data>>seller|店铺权限|是|[string]|PM-US,ID-UK,ID-DE1-DE-DE,BA-IG-AU,STAN-US5555,ID-DE- IT,ID-DE133-NL,PM-CA,PM-MX|
|data>>is_master|是否为主账号：0 否，1 是|是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "BAC6212F-CCCD-546C-D6C7-998EB10B5F97",
    "response_time": "2024-07-17 11:29:26",
    "data": [
        {
            "uid": 1,
            "realname": "超级管理员",
            "username": "admin",
            "mobile": "15xxxxxxxx",
            "email": "15xxxxxxx4@qq.com",
            "login_num": 146
            "last_login_time": "-",
            "last_login_ip": "",
            "status": 0,
            "create_time": "-",
            "zid": 1,
            "role": "无法识别账户-角色组",
            "seller": "",
            "is_master": 2
        }
	],
    "total": 0
}
```

## 附加说明  
1. 唯一键：uid
2. 调用本接口将一次性全部返回企业已有的ERP账号信息
