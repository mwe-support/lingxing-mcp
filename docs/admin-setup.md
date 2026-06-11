# 管理员执行清单

这份文档是给实施人、超级管理员和服务器管理员看的。  
目标很简单：把领星 MCP 的访问链路先跑通。

默认目标人群是：

- 技术型卖家
- AI 协作用户
- 需要给团队共享领星数据的实施人

---

## 你需要准备什么

至少要有这三类权限或资源：

1. **领星超级管理员**
   - 用来操作开放接口、白名单和 API 账号
2. **一台固定出口云服务器**
   - 用来承接团队共享模式的 HTTP gateway
3. **本地客户端**
   - 用来做健康检查和最终接入

---

## 固定 checklist

真正落地时，你可以按这三段来执行：

1. **领星侧**
   - 超级管理员登录
   - `设置 -> 业务配置 -> 基础 -> 开放接口`
   - 添加白名单 IP
   - 添加 API 账号
   - 获取 `APP ID / AppSecret`
2. **腾讯云侧**
   - 购买 `CVM`
   - 推荐 `2核4G + Ubuntu 22.04 + EIP`
3. **服务器侧**
   - 配置环境变量
   - 启动 gateway
   - 初始化 tokens
   - 做 `healthz / smoke_check`

---

## 第 1 步：在领星后台开通开放接口

请使用 **超级管理员账号** 登录领星后台，然后进入：

`设置 -> 业务配置 -> 基础 -> 开放接口`

你需要完成：

1. 添加固定出口服务器的 IP 白名单
2. 添加 API 账号
3. 记录 `APP ID`
4. 记录 `AppSecret`

### 建议做法

- 如果你只是先跑通整条链路，可以先给较宽的只读权限
- 验证通过后，再按实际需求收缩权限

---

## 第 2 步：准备固定出口服务器

推荐默认值：

- 腾讯云 `CVM`
- `2核4G`
- `Ubuntu 22.04 LTS`
- 基础带宽即可
- 长期团队共享建议绑定 `EIP`

如果你还没买服务器，直接看：

- [tencent-cloud-buying-guide.md](./tencent-cloud-buying-guide.md)

---

## 第 3 步：在服务器上准备运行环境

通常至少要准备：

- `LINGXING_APP_ID`
- `LINGXING_APP_SECRET`
- `LINGXING_TOKEN_CACHE_FILE`
- `LINGXING_MCP_TOKENS_FILE`

建议把这些值写进服务端专用环境文件，不要散落在命令历史里。

---

## 第 4 步：启动 HTTP gateway

最小启动方式：

```bash
python3 mcp-servers/lingxing-openapi/http_server.py --host 127.0.0.1 --port 8099 --tokens-file /etc/lingxing-mcp/tokens.json
```

推荐生产用法是结合：

- `deploy/install_gateway_on_ubuntu.sh`
- `deploy/deploy_gateway_via_ssh.sh`
- `lingxing-mcp.service.template`

---

## 第 5 步：初始化成员令牌

初始化令牌文件：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py --tokens-file /etc/lingxing-mcp/tokens.json init --id admin --description "Gateway admin bootstrap token"
```

新增成员令牌：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py --tokens-file /etc/lingxing-mcp/tokens.json add --id alice-mac --description "Alice MacBook"
```
Role notes:

- `minimal` is the default role and uses the built-in least-privilege role allowlist.
- Existing tokens without `role` are treated as `minimal`.
- Use `--role operations` or `--role finance` when adding role-specific users.
- Use `set-role` to change a role without rotating the token. Every role always includes `lingxing_health_check`, `lingxing_smoke_check`, and `lingxing_rate_limit_policy`.


---

## 第 6 步：做最小验证

建议按这个顺序：

1. 服务器本机 `healthz`
2. `lingxing_health_check`
3. `lingxing_rate_limit_policy`
4. `lingxing_smoke_check`

只要前两步没通，就不要急着排更高层的业务问题。

---

## 管理员最容易漏掉的点

### 1. 白名单 IP 加错

请确认领星里加的是 **固定出口服务器真正出去的公网 IP**，不是你本机 IP。

### 2. API 账号有了，但权限不够

如果始终卡在核心接口，可以先临时放宽只读权限验证，再回收。

### 3. 服务器有公网 IP，但不是长期稳定出口

短期验证可以先用当前公网 IP。  
长期团队共享，仍然更推荐 `EIP`。

---

## 安全提醒

> [!WARNING]
> 管理员尤其要避免泄露：
>
> - 真实 `APP ID`
> - 真实 `AppSecret`
> - 真实 Bearer
> - 真实 `tokens.json`
> - 真实服务器公网 IP
>
> 如果怀疑泄露，优先轮换 API 账号和成员令牌，再继续接入。
