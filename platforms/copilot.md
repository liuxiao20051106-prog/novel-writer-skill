# GitHub Copilot 配置指南

适用于 GitHub Copilot Chat (VS Code / JetBrains / GitHub.com)。

## 方式一：Copilot 指令文件（推荐）

在项目根目录创建 `.github/copilot-instructions.md`：

```bash
mkdir -p .github
cp SKILL.md .github/copilot-instructions.md
```

Copilot Chat 会自动读取该文件作为行为指引。去掉 YAML frontmatter 效果更佳。

## 方式二：VS Code 自定义指令

1. 安装 GitHub Copilot Chat 扩展
2. VS Code → Settings → `github.copilot.chat.codeGeneration.instructions`
3. 粘贴 `SKILL.md` 中的核心写作要求

## 方式三：对话中引用

在 Copilot Chat 对话中使用 `#file:SKILL.md` 或直接粘贴关键段落作为上下文。

## 方式四：Workspace 级别

在 VS Code 的 `.vscode/settings.json` 中添加：

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": "SKILL.md" }
  ]
}
```

## 推荐

方式一（`.github/copilot-instructions.md`），可以随项目代码一起版本管理。
