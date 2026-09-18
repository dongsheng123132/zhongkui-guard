# 钟馗卫士 / Zhongkui Guard

钟馗卫士是一个本地优先的 Agent Skill：检查指定 Skill、模型回复和工具调用记录中的可疑指令；脱敏 UTF-8 文本、Markdown 和 JSON；并以合成题目评估用户配置的模型 API。

v0.1 提供按需检查，不提供全局实时拦截、模型身份认证或“中转站不保存聊天”的保证。离线扫描不会运行被检查的代码。端点体检只会向配置的端点发送合成题目。

发布物：[GitHub Release v0.1.0](https://github.com/dongsheng123132/zhongkui-guard/releases/tag/v0.1.0)。ClawHub 上传状态以 `RELEASE_STATUS.md` 的真实记录为准。

## 快速开始

需要 Python 3.11+，没有第三方依赖：

```powershell
python scripts/zkguard.py doctor --format json
python scripts/zkguard.py scan --path .\sample --kind skill --format json
python scripts/zkguard.py redact --input .\customer-note.txt --output .\customer-note.redacted.txt --format json
python scripts/zkguard.py audit --target relay-a --profile quick --plan --config .\config.local.json --format json
```

不要把 API 密钥放进配置文件或命令行。配置只保存环境变量名称，示例见 `assets/config.example.json`。

## 安装

从 Release 解压 `zhongkui-guard` 到宿主支持的 skills 目录，或将 `skills/zhongkui-guard` 放入项目 `.agents/skills/`。Skill 会以自身目录定位 `scripts/zkguard.py`，不依赖当前目录。

卸载时删除该技能目录即可；报告和脱敏副本在你指定的目录中，需由你决定是否删除。

## 边界

- “未发现”只表示选定范围没有命中已知规则，不代表绝对安全。
- 脱敏必须在原文发给远程模型前完成；已粘贴到聊天中的数据无法撤回。
- 没有宿主 hook 时，本工具不能阻止其他工具调用。
- 缺少可信参考端点时，体检只报告能力结果，不声明模型相同或真实。

详见 `PRIVACY.md`、`SECURITY.md` 和 Skill 内的 references。
