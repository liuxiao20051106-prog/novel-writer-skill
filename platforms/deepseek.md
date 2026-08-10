# DeepSeek 配置指南

适用于 DeepSeek Chat (chat.deepseek.com / API)。

## 方式一：Web 端对话

1. 打开 [chat.deepseek.com](https://chat.deepseek.com)
2. 在对话设置中开启「深度思考」可获得更好的长篇写作效果（推荐用于大纲规划和修改润色）
3. 将 `SKILL.md` 完整内容作为第一条消息发送即可

## 方式二：API 调用（推荐）

将 `SKILL.md` 作为 system prompt 传入：

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-deepseek-api-key",
    base_url="https://api.deepseek.com"
)

with open("SKILL.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "帮我写一个玄幻小说的开头，主角是一个……"}
    ]
)
```

## 方式三：第三方客户端

在支持 DeepSeek 的第三方客户端（如 ChatBox、Cherry Studio、LobeChat 等）中：
1. 创建新的「助手」或「角色」
2. 将 `SKILL.md` 正文粘贴到「系统提示词」栏
3. 选择 DeepSeek 模型即可

## 推荐

- DeepSeek 性价比极高，适合大量文本生成
- 使用「深度思考」模式进行大纲规划和情节设计
- 使用普通模式进行章节写作（速度更快）
- API 方式最灵活，可自定义参数
