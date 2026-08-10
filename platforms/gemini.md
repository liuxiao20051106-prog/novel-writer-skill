# Google Gemini 配置指南

适用于 Gemini (gemini.google.com / Gemini API / Gemini in AI Studio)。

## 方式一：Gemini Gems（自定义专家）

1. 打开 [gemini.google.com](https://gemini.google.com)，点击「Gems」→「创建 Gem」
2. 在「指令」栏粘贴 `SKILL.md` 的正文内容（去掉 YAML frontmatter）
3. 设置名称（如"小说写作助手"）和描述
4. 保存后每次选择该 Gem 开启对话即可

## 方式二：AI Studio 系统提示词

1. 打开 [aistudio.google.com](https://aistudio.google.com)
2. 创建新的提示词 → 在「System Instructions」栏粘贴 `SKILL.md` 完整内容
3. 可以直接测试和调整温度、top-p 等参数
4. 适合需要调参的高级用户

## 方式三：API 调用

使用 Gemini API 时，将 `SKILL.md` 内容作为 `system_instruction` 传入：

```python
import google.generativeai as genai

with open("SKILL.md", "r", encoding="utf-8") as f:
    system_instruction = f.read()

model = genai.GenerativeModel(
    model_name="gemini-2.5-pro",
    system_instruction=system_instruction
)
```

## 方式四：直接对话

在 Gemini 对话中，将 `SKILL.md` 内容作为第一条消息发送：

```
请以以下身份和规则协助我写作：

（粘贴 SKILL.md 内容）
```

## 推荐

- **免费用户**：方式一（Gems）
- **开发者**：方式三（API）
- **快速测试**：方式四（直接粘贴）
