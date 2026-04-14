# Lingxing MCP Windows Teammate Kit

先看这个文件，再按顺序操作。

## 这个压缩包里有什么

- `01_open_tunnel.cmd`
  用来建立本地 SSH 隧道，把你电脑的 `18099` 转到公司领星网关。
- `02_test_health.ps1`
  用来验证本地 `18099` 是否已经打通。
- `03_project_mcp.json`
  给 `Codex / Claude Code / Cursor / Kiro` 用的项目级 MCP 配置示例。
- `04_claude_desktop_config.json`
  给 `Claude App` 用的 MCP 配置示例。
- `05_gateway_info.txt`
  网关连接信息。如果管理员已经填好，你直接用即可。

## 你还需要管理员单独发你的两样东西

1. 你的成员令牌  
   形式一般是：

```text
Bearer xxxxx
```

2. 如果 `05_gateway_info.txt` 里还是占位符，还需要管理员发你真实网关地址

## 先装什么

请先确认你的 Windows 电脑已经有：

- `OpenSSH Client`
- `Node.js LTS`

检查方法：

```powershell
ssh -V
npx.cmd -v
```

如果任意一个命令报错，先安装对应软件，再继续。

## 推荐接入顺序

### 方案 A：Claude App

1. 双击或在终端运行 `01_open_tunnel.cmd`
2. 另开一个 PowerShell，运行 `02_test_health.ps1`
3. 打开 `04_claude_desktop_config.json`
4. 把其中 `replace-with-your-member-token` 替换成管理员单独发给你的令牌
5. 把内容合并到你的 Claude Desktop MCP 配置里
6. 重启 Claude App

### 方案 B：Codex / Claude Code / Cursor / Kiro

1. 双击或在终端运行 `01_open_tunnel.cmd`
2. 另开一个 PowerShell，运行 `02_test_health.ps1`
3. 打开 `03_project_mcp.json`
4. 把其中 `replace-with-your-member-token` 替换成管理员单独发给你的令牌
5. 把内容复制到对应工作区配置文件

建议放置位置：

- `Codex / Claude Code`：工作区根目录 `.mcp.json`
- `Cursor`：工作区 `.cursor/mcp.json`
- `Kiro`：工作区 `.kiro/settings/mcp.json`

## 第一次验证成功应该看到什么

`02_test_health.ps1` 成功时，会返回类似：

```json
{"ok":true,"server":"lingxing-openapi"}
```

之后在你的 IDE 里应该能看到 `lingxing_mcp`，或看到一组 `lingxing_*` 工具。

## 常见问题

### 1. `ssh` 命令报错

- 先确认 Windows 已安装 `OpenSSH Client`
- 再确认 `05_gateway_info.txt` 里的用户和地址是否正确

### 2. `healthz` 不通

- 确认 `01_open_tunnel.cmd` 那个窗口仍然开着
- 确认本地端口是 `18099`

### 3. IDE 里连不上

- 先确认你已经把成员令牌正确填入 JSON 配置
- 成员令牌前面要保留 `Bearer `
- 改完配置后，重启对应 IDE

### 4. 返回 `missing_or_invalid_bearer`

- 说明你的成员令牌不对、过期、被吊销，或者复制时丢了 `Bearer `
- 联系管理员重发或轮换令牌

## 安全说明

- 不要把你的成员令牌发给其他同事
- 不要把这个配置提交到 Git
- 不要向任何人索要 `App ID / App Secret`
