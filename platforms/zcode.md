# ZCode 配置指南

ZCode 原生支持 skill 发现机制，无需任何转换，把仓库作为 skill 目录放入即可。`references/` 与 `templates/` 会随主文件一起被按需加载，建议完整复制。

## 安装方式

ZCode 按以下顺序发现 skill（前者优先）：

1. `<项目>/.zcode/skills/<name>/SKILL.md`
2. `<项目>/.agents/skills/<name>/SKILL.md`
3. `~/.zcode/skills/<name>/SKILL.md`
4. `~/.agents/skills/<name>/SKILL.md`

### 方式一：用户级安装（所有项目可用，推荐放到 `.agents`）

```bash
mkdir -p ~/.agents/skills/novel-writer
cp SKILL.md references/ templates/ -r ~/.agents/skills/novel-writer/
```

Windows（PowerShell）：

```powershell
New-Item -ItemType Directory -Force ~\.agents\skills\novel-writer
Copy-Item SKILL.md, references, templates ~\.agents\skills\novel-writer -Recurse
```

### 方式二：项目级安装（仅当前写作项目）

```bash
mkdir -p .agents/skills/novel-writer
cp SKILL.md references/ templates/ -r .agents/skills/novel-writer/
```

### 方式三：Clone 安装

```bash
git clone https://github.com/liuxiao20051106-prog/novel-writer-skill.git ~/.agents/skills/novel-writer
```

## 触发方式

安装后自动触发（按 description 匹配）或显式调用：

- 「帮我写小说」「构思一个新故事」「写下一章」「续写」「帮我审稿」
- 显式调用：输入 `/novel-writer <你的需求>`

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 核心 skill 指令，包含 YAML frontmatter（`name` + `description`） |
| `references/` | 专项指南，触发后按需读取，不占用初始上下文 |
| `templates/` | 项目模板，创建项目文件时使用 |

`aily-cli-skill.json` 是 Claude Code 的元数据文件，ZCode 不需要，可不复制。
