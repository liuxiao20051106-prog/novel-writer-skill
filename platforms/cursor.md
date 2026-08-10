# Cursor 配置指南

## 方式一：项目级规则文件

在项目根目录创建 `.cursor/rules/novel-writer.mdc`：

```bash
mkdir -p .cursor/rules
cp SKILL.md .cursor/rules/novel-writer.mdc
```

> **注意**：Cursor 的 `.mdc` 文件需要去掉 YAML frontmatter（`---` 之间的内容），或将 frontmatter 改为 Cursor 格式。

推荐的文件头部格式：

```markdown
---
description: 写小说全流程助手
globs: "**/*.md"
alwaysApply: false
---

# 写小说助手

（接下来粘贴 SKILL.md 正文内容）
```

## 方式二：全局规则

Cursor → Settings → General → Rules for AI，粘贴 `SKILL.md` 的核心内容。

## 方式三：Notepad 模式

在 Cursor 中打开一个 `.md` 文件（如 `novel-project.md`），在 Composer 中输入写作指令，同时 @ 引用 `SKILL.md` 作为上下文。

## 推荐

使用方式一（项目级规则），写作时可以随时 Cmd/Ctrl+L 调出 AI 对话，AI 自动遵循 skill 规则。
