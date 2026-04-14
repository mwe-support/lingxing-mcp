# 定制化附件下载接口
## 接口信息

| API Path                                 | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :--------------------------------------- | :------- | :------- | :----------------------------------------------------------- |
| /erp/sc/routing/customized/file/download | HTTPS    | POST     | 1                                                            |

## 请求参数

| 参数名  | 说明                                 | 必填 | 类型     | 示例      |
| :------ | :----------------------------------- | :--- | :------- | :-------- |
| file_id | 附件文件id(订单详情接口中附件id字段) | 是   | [string] | 123121211 |

## 请求示例

```
{
	"file_id":"123121211"
}
```



## 返回结果

Json Object

| 参数名          | 说明             | 必填 | 类型     | 示例                                     |
| :-------------- | :--------------- | :--- | :------- | :--------------------------------------- |
| code            | 状态码，0 成功   | 是   | [int]    | 0                                        |
| message         | 响应消息         | 是   | [string] | 操作成功                                 |
| error_details   | 错误信息         | 是   | [array]  |                                          |
| request_id      | 请求链路id       | 是   | [string] | 8DFEE1CA-EC9B-F401-5D41-9F95251D5D50     |
| response_time   | 响应时间         | 是   | [string] | 2020-09-21 15:48:58                      |
| data            | 数据             | 是   | [array]  |                                          |
| data>>file_name | 文件名           | 是   | [string] | d91bbb8d-da25-3941-51d5-9d4fe0d544ec.jpg |
| data>>mime_type | 文件类型         | 是   | [string] | image/png                                |
| data>>content   | 文件内容(base64) | 是   | [string] | /9j/4TT/lx61tQ/wrS8Vox28j/9k=            |



## 返回示例

```
{
  "code": 0,
  "message": "操作成功",
  "error_details": [],
  "request_id": "8DFEE1CA-EC9B-F401-5D41-9F95251D5D50",
  "response_time": "2020-09-21 15:48:58",
  "data": [
    {
      "file_name": "d91bbb8d-da25-3941-51d5-9d4fe0d544ec.jpg",
      "mime_type": "image/png",
      "content": "/9j/4TT/lx61tQ/wrS8Vox28j/9k="
    }
  ]
}
```
