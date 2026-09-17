# 📖 Novel Writer Skill — AI Novel-Writing Assistant for Every Platform

A complete novel-writing methodology that works on **Claude Code, ZCode, ChatGPT, Cursor, GitHub Copilot, Gemini, DeepSeek, Kimi, Doubao, Qwen, Ollama** and other mainstream AI platforms.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)
[![Platforms](https://img.shields.io/badge/Platforms-8+-blue)](../platforms/)
[![中文](https://img.shields.io/badge/语言-中文-red)](../README.md)
[![English](https://img.shields.io/badge/Lang-English-blue)](SKILL.md)

---

## What is this?

A "novel-writing system prompt" for AI. Load [SKILL.md](SKILL.md) into any AI platform and it becomes a professional novel-writing assistant — not a cheerleader that says "nice draft," but a partner that can actually:

- Build a story from scratch (genre, premise, theme, world, characters, outline)
- Write chapter by chapter with smooth bridging and emotional continuity
- Self-check after writing (plot holes? dumbed-down characters? immersion?)
- Revise layer by layer (structure → language → detail)
- Deliver on genre promises and plan sustainable serialization
- Run controllable AI workflows with rollback, human gates, and test-based acceptance

## Why do you need it?

Say "help me write a novel" to an AI and you'll get a decent passage — and nothing more. The AI won't proactively:

- ❌ Confirm genre and target readers → the output has no audience
- ❌ Design deep characters → flat characters, vague motivation
- ❌ Plan chapter structure and climax placement → the plot drifts apart
- ❌ Keep chapters connected → crying last chapter, laughing this one
- ❌ Check immersion → readers can't get in
- ❌ Track foreshadowing and character states → forgotten by chapter ten

This skill encodes a professional author's full workflow into the AI's system instructions, **so the AI becomes a competent writing partner before a single word is written**.

## Highlights

| Feature | What it means |
|------|------|
| 🎯 **Methodology-driven** | Concrete techniques, not vague directives: the four-part chapter structure, five-layer character design, four chapter-bridging patterns — each with a clear "how" and "why" |
| 🔗 **Chapter continuity** | Built-in pre-writing checks: every chapter reviews the previous ending across timeline, scene, POV, and mood |
| 👁️ **Immersion first** | Five-layer immersion system: POV lock + sensory immersion + emotional resonance + situation design + breakers to avoid |
| 🌍 **Platform-agnostic** | One methodology for 10+ platforms, each with its own setup guide |
| 🧭 **Genre & serialization** | Covers fantasy, sci-fi, romance, mystery and more; reader positioning, contract and rights checklists |
| 🧹 **De-AI the voice** | Ten machine-voice signals with fixes, a high-frequency word swap list, and a negative-prompt template to sweep before submitting |
| 🧪 **Quantified draft diagnostics** | `scripts/draft_diagnostics.py` reports sentence/paragraph coefficient of variation, dialogue share, sensory density, AI-tell density, and repeated phrasing — data to localize suspect passages |
| 🤖 **Controllable AI workflow** | Explicit states, human approval, idempotent retries, and run logs for cross-session and batch work |
| ✅ **Quality gates** | Hard gates, evidence-based scoring, and behavioral tests for continuity, originality, facts, and publishing risk |
| 📋 **Project templates** | 11 bilingual templates for characters, foreshadowing, style anchors, sources, market assumptions, automation runs, and release acceptance |
| 🔒 **Structure self-check** | `scripts/validate_skill.py` verifies frontmatter, link validity, zh/en mirror parity, and script syntax — run it after any edit |

## Who is it for?

- 🖊️ **Web-novel and fiction writers** who want AI to understand the writing process, not just produce pretty prose
- 🎓 **Beginners** learning story craft through an AI-guided methodology
- 🔄 **Multi-platform users** — outline in Claude Code, draft in DeepSeek, polish in ChatGPT, same standards everywhere
- 📚 **Serial authors** — project templates keep characters, foreshadowing, and emotional pacing tracked

---

## 🚀 Quick start

Pick your platform:

| Platform | Setup guide | Install |
|------|---------|---------|
| **Claude Code** | [platforms/claude-code.md](../platforms/claude-code.md) | Copy to `~/.claude/skills/` |
| **ChatGPT** | [platforms/chatgpt.md](../platforms/chatgpt.md) | Create a Custom GPT |
| **Cursor** | [platforms/cursor.md](../platforms/cursor.md) | Add `.cursorrules` |
| **GitHub Copilot** | [platforms/copilot.md](../platforms/copilot.md) | Add `copilot-instructions.md` |
| **Gemini** | [platforms/gemini.md](../platforms/gemini.md) | Create a Gem / API |
| **DeepSeek** | [platforms/deepseek.md](../platforms/deepseek.md) | System Prompt / Web |
| **ZCode** | [platforms/zcode.md](../platforms/zcode.md) | `~/.agents/skills/` or project `.zcode/skills/` |
| **Other platforms** | [platforms/generic.md](../platforms/generic.md) | Paste as system prompt |

The entry file is [SKILL.md](SKILL.md) (English) or [../SKILL.md](../SKILL.md) (Chinese); specialist guides and templates load on demand.

---

## ✨ Fifteen craft deep dives + long-form engineering

Each technique keeps its non-negotiable baseline in SKILL.md; the full methodology loads on demand:

| Technique | Core content | Deep guide |
|------|---------|---------|
| **Story structure** | Causal chains · beat–scene–sequence–act–story · fifteen beats · chapter/volume mapping | [Open](references/craft-story-structure.md) |
| **Opening hooks** | The golden 300 words · first-three-chapter task split · four hook types · opening killers | [Open](references/craft-opening-hooks.md) |
| **Character building** | Five-layer design · want vs. need · three arc types · speech fingerprints | [Open](references/craft-character.md) |
| **Emotion & subtext** | Three emotional layers · the three-column method · four micro-tension tools · subtext pairs | [Open](references/craft-emotion-and-subtext.md) |
| **POV & distance** | Four fixed decisions · four distance gears · viewpoint violation · multi-thread switching | [Open](references/craft-pov-and-distance.md) |
| **Scene design** | Scene & sequel · four-part structure · genre pace ratios | [Open](references/craft-scene-design.md) |
| **Dialogue** | Six goals · resistance as the core · break the ping-pong rally · three AI diseases | [Open](references/craft-dialogue.md) |
| **Pacing** | Alternate tempo · accelerate/decelerate · suppression-release · cool-down chapters | [Open](references/craft-pacing.md) |
| **Suspense & foreshadowing** | Three information asymmetries · three suspense layers · four planting patterns and the three-stage payoff · fair play | [Open](references/craft-suspense-foreshadowing.md) |
| **Prose & style** | Five style registers · filter-word removal · verbs first · density control · white space | [Open](references/craft-prose-style.md) |
| **Immersion** | Five-layer system (POV lock + sensory + resonance + situation + breakers) | [Open](references/craft-immersion.md) |
| **Chapter bridging** | Four bridging patterns · time jumps · multi-thread continuity | [Open](references/craft-chapter-bridging.md) |
| **Web serial rhythm** | Three payoff tiers · anticipation management · four cliffhanger types · poison points | [Open](references/craft-webnovel-rhythm.md) |
| **Revision process** | Four-round revision · reverse outline · cooling and read-through · when to stop | [Open](references/craft-revision.md) |
| **Removing the AI voice** | Three roots of the machine voice · ten signals · four fiction tells · swap list | [Open](references/craft-ai-tells.md) |
| **Long-form continuity** | Context budget · layered summaries · two-step generation · per-volume audit · handoff | [Open](references/context-budget.md) |

---

## 🧪 Bundled scripts

Two zero-dependency Python scripts (standard library only), plain text or JSON output:

```bash
# Draft diagnostics: word count, sentence/paragraph CV, dialogue share, sensory density,
# AI-tell words, repeated phrases, dash density
python scripts/draft_diagnostics.py chapter.md
python scripts/draft_diagnostics.py chapter.md --top 15 --json

# Skill self-check: frontmatter, link validity, zh/en mirror parity, script syntax
python scripts/validate_skill.py
python scripts/validate_skill.py --warnings-as-errors

# Unit tests for the scripts (23 cases)
python -m unittest discover -s tests
```

Diagnostics are **leads, not verdicts** — read the passage before changing it. GitHub Actions runs the tests and the self-check on every push and PR.

---

## 📁 Project structure

```
novel-writer-skill/
├── README.md                      # Chinese project overview
├── CHANGELOG.md                   # Changelog
├── SKILL.md                       # Core skill file (Chinese)
├── aily-cli-skill.json            # Claude Code metadata
├── LICENSE                        # MIT license
│
├── scripts/                       # Zero-dependency Python scripts
│   ├── draft_diagnostics.py       # Draft diagnostics
│   └── validate_skill.py          # Structure & zh/en mirror check
├── tests/                         # Script unit tests (23 cases)
├── .github/workflows/validate.yml # CI: tests + self-check on push/PR
│
├── platforms/                     # Per-platform setup guides
│
├── en/                            # Full English version
│   ├── README.md                  # English project overview (this file)
│   ├── SKILL.md                   # English core skill
│   ├── references/                # 27 English specialist guides (incl. 15 craft deep dives)
│   └── templates/                 # 11 English project templates
│
├── references/                    # On-demand specialist guides (Chinese, 27 files)
│   ├── craft-*.md                 # 15 craft deep dives
│   ├── context-budget.md          # Context budget & long-form memory packing
│   └── *.md                       # 11 workflow/compliance guides
│
└── templates/                     # Copy-ready project templates (Chinese, 11 files)
```

---

## 🔧 Three ways to install

### Option 1: As an AI system prompt (most universal)

1. Open `SKILL.md` and remove the opening `---` block (YAML frontmatter)
2. Paste the entire body into your platform's "system prompt," "custom instructions," or persona field
3. Start chatting

### Option 2: Paste per conversation

Send the full `SKILL.md` content as the first message.

### Option 3: Git clone

```bash
git clone https://github.com/liuxiao20051106-prog/novel-writer-skill.git
```

---

## 🧠 Design philosophy

1. **Immersion first** — every technique serves "the reader forgets they're reading"
2. **Emotion-driven** — plot + emotional journey = good fiction; both required
3. **Characters and plot as cause and effect** — they grow together or drag each other down
4. **Chapters must flow** — readers never re-adapt at a chapter opening
5. **"Write like a loving parent; revise like an unmerciful god"** — Elizabeth McCracken

---

## 📊 Token usage

The core methodology and all 15 techniques' non-negotiable baselines stay in `SKILL.md` (193 body lines); the full craft expansions (`references/craft-*.md`) plus genre, long-form, commercialization, automation, fact-checking, compliance, and QA guides live in `references/` and load on demand, so context stays lean. `en/` mirrors the same scope in English.

For long works, pack context by the [budget](references/context-budget.md): system instructions 15-25%, fact layer 20-30%, prior text 20-30%, this chapter's brief 10-15%, and keep ≥20% free for generation.

---

## 🤝 Contributing

Issues and PRs welcome!

- New platform guides → `platforms/`
- Translations → new `xx/` directory
- Methodology improvements → edit `SKILL.md`

---

## 📄 License

MIT — see [LICENSE](../LICENSE).
