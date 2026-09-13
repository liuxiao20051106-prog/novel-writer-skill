# Claude Code 配置指南

## 安装方式

### 方式一：用户级安装（所有项目可用）

```bash
mkdir -p ~/.claude/skills/novel-writer
cp SKILL.md aily-cli-skill.json ~/.claude/skills/novel-writer/
cp -r references templates ~/.claude/skills/novel-writer/
```

### 方式二：项目级安装（仅当前项目）

```bash
mkdir -p .claude/skills/novel-writer
cp SKILL.md aily-cli-skill.json .claude/skills/novel-writer/
cp -r references templates .claude/skills/novel-writer/
```

### 方式三：Clone 安装

```bash
git clone https://github.com/liuxiao20051106-prog/novel-writer-skill.git ~/.claude/skills/novel-writer
```

## 触发方式

安装后在 Claude Code 中说以下任意一句即可：

- 「帮我写小说」
- 「构思一个新故事」
- 「写下一章」
- 「帮我设计一个角色」
- 「润色这一段」

Skill 会在匹配到这些关键词时自动加载。

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 核心 skill 指令，包含 YAML frontmatter |
| `aily-cli-skill.json` | Claude Code skill 元数据（schemaVersion + surfaces） |
| `references/` | 专项指南，SKILL.md 中的链接按需加载，缺失会导致链接失效 |
| `templates/` | 项目模板，创建项目文件时使用 |
