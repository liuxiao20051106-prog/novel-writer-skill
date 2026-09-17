#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""草稿量化体检：把「读起来怪怪的」变成可定位的数字。

只依赖标准库，中文/英文通用。用途：

- 写完一章后自查：节奏是否均匀（AI 常见问题）、对话占比是否失衡、
  感官描写是否缺失、情感标签是否过多；
- 去 AI 味前后对比：跑两次，看高频词与句长分布是否改善；
- 长篇风格漂移检查：把第 1 章和第 50 章各跑一次，比对指标差异。

用法：

    python scripts/draft_diagnostics.py chapter.md
    python scripts/draft_diagnostics.py chapters/*.md --top 15
    python scripts/draft_diagnostics.py chapter.md --json
    python scripts/draft_diagnostics.py chapter.md --lexicon my_words.txt

词表文件（可选）格式：一行一个词或正则片段，`#` 开头为注释。

注意：脚本只报数，不判好坏。阈值见 `references/quality-review.md`，
是否修改由作者决定。
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------- #
# 词表
# --------------------------------------------------------------------------- #

# 感官词：视觉 / 听觉 / 嗅觉 / 味觉 / 触觉 / 温度 / 身体感受
SENSORY_WORDS = (
    '看见 看到 望见 瞥 盯着 闪 亮 暗 光 影 颜色 血红 苍白 灰 黑 白 轮廓 '
    '听见 听到 听 声音 响 静 吵 嗡 哐 啪 沙沙 低语 尖叫 脚步声 '
    '闻 气味 味 香 臭 酸 腥 霉 焦 甜腻 呛 '
    '尝 味道 苦 涩 咸 辣 淡 '
    '摸 碰 触 粗糙 光滑 黏 湿 干 硬 软 刺痛 痒 硌 冰凉 滚烫 '
    '冷 热 暖 凉 寒 闷 潮 '
    '心跳 呼吸 喘 抖 颤 汗 疼 痛 酸软 眩晕 恶心 胃 喉咙 手心 后背 腿 '
    'saw see look glow dark light shadow color '
    'heard hear sound loud quiet whisper scream footsteps '
    'smell scent stink sweet sour bitter smoky '
    'taste salty spicy '
    'touch rough smooth sticky wet dry hard soft itchy '
    'cold hot warm chill damp '
    'heart breath sweat shake tremble ache pain dizzy throat palm'
).split()

# 情感标签词：直接给情绪命名的词（应改为行为/身体反应展示）
TELLING_WORDS = (
    '愤怒 生气 悲伤 难过 开心 高兴 快乐 恐惧 害怕 紧张 焦虑 尴尬 羞愧 嫉妒 '
    '失望 绝望 兴奋 激动 感动 愧疚 后悔 厌烦 喜欢 讨厌 爱 恨 震惊 惊讶 '
    '感到 觉得 意识到 明白 知道 认为 觉得 '
    'angry sad happy afraid scared nervous anxious embarrassed ashamed jealous '
    'disappointed desperate excited moved guilty regret annoyed like hate shocked surprised '
    'felt feel realized knew thought understood'
).split()

# 中文 AI 高频腔：模型默认输出里显著偏多的套话与句式片段
AI_TELL_PHRASES = (
    '值得注意', '值得一提', '不难发现', '众所周知', '综上所述', '总而言之',
    '总的来说', '除此之外', '首先', '其次', '最后', '在这个', '的背景下',
    '随着', '赋能', '闭环', '颗粒度', '底层逻辑', '落地', '堪称', '无疑',
    '不仅', '而且', '更是', '某种程度上', '一定程度上', '仿佛', '似乎',
    '与此同时', '充满了', '弥漫着', '交织', '宛如', '犹如', '宛如',
    '不仅仅是', '更是', '某种意义上', '深沉', '无尽的', '莫名', '一丝',
    '这一刻', '此刻', '空气仿佛', '时间仿佛', '重要的是', '事实上',
    '总的来说', '可以说', '某种意义上说',
)

# 说明腔/营销腔（叙事里出现即需警惕）
EXPOSITORY_MARKERS = ('众所周知', '历史上', '据说', '据传', '需要注意的是', '简单来说')

CJK_RE = re.compile(r'[\u4e00-\u9fff]')
SENT_SPLIT_RE = re.compile(r'(?<=[。！？!?…；;])\s*|\n+')
QUOTE_RE = re.compile(r'[“「『"“]([^”」』"”]{2,})[”」』"”]')
CJK_RUN_RE = re.compile(r'[\u4e00-\u9fff]{2,}')
WORD_RE = re.compile(r"[A-Za-z']{3,}")
STOPWORDS = set(
    '我们 你们 他们 她们 它们 这个 那个 什么 怎么 因为 所以 但是 然后 就是 '
    '可以 已经 还是 一下 一个 没有 自己 知道 起来 过去 现在 这样 那样 '
    'the and that with from this have been which their there what'
    .split()
)


# --------------------------------------------------------------------------- #
# 分析
# --------------------------------------------------------------------------- #
def read_text(path: Path) -> str:
    for encoding in ('utf-8', 'utf-8-sig', 'gbk'):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    raise SystemExit(f'无法解码文件：{path}')


def count_chars(text: str) -> dict:
    cjk = len(CJK_RE.findall(text))
    latin_words = len(WORD_RE.findall(text))
    return {
        'chars_total': len(text),
        'chars_no_space': len([c for c in text if not c.isspace()]),
        'cjk_chars': cjk,
        'latin_words': latin_words,
        'words_equivalent': cjk + latin_words,  # 中文按字、英文按词折算
    }


def sentences(text: str) -> list:
    return [s.strip() for s in SENT_SPLIT_RE.split(text) if s and s.strip()]


def paragraphs(text: str) -> list:
    return [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]


def _lengths(items: list) -> list:
    return [len(CJK_RE.findall(i)) + len(WORD_RE.findall(i)) for i in items]


def rhythm(sent_lengths: list, para_lengths: list) -> dict:
    """节奏均匀度：AI 文本的典型症状是方差过小。"""
    def stats(values: list, prefix: str) -> dict:
        if not values:
            return {f'{prefix}_avg': 0, f'{prefix}_p90': 0, f'{prefix}_max': 0,
                    f'{prefix}_stdev': 0, f'{prefix}_cv': 0}
        avg = statistics.fmean(values)
        ordered = sorted(values)
        p90 = ordered[max(0, int(len(ordered) * 0.9) - 1)]
        stdev = statistics.pstdev(values)
        return {
            f'{prefix}_avg': round(avg, 1),
            f'{prefix}_p90': p90,
            f'{prefix}_max': max(values),
            f'{prefix}_stdev': round(stdev, 1),
            f'{prefix}_cv': round(stdev / avg, 2) if avg else 0,
        }

    result = stats(sent_lengths, 'sentence')
    result.update(stats(para_lengths, 'paragraph'))
    result['short_sentence_ratio'] = round(
        sum(1 for n in sent_lengths if n <= 10) / len(sent_lengths), 2) if sent_lengths else 0
    return result


def dialogue_ratio(text: str, total_words: int) -> dict:
    quoted = sum(
        len(CJK_RE.findall(seg)) + len(WORD_RE.findall(seg))
        for seg in QUOTE_RE.findall(text)
    )
    lines = [ln for ln in text.splitlines() if ln.strip()]
    dialogue_lines = sum(1 for ln in lines if ln.strip().startswith(('“', '「', '『', '"')))
    return {
        'dialogue_word_ratio': round(quoted / total_words, 3) if total_words else 0,
        'dialogue_line_ratio': round(dialogue_lines / len(lines), 3) if lines else 0,
    }


def density(text: str, words: tuple | list, total_words: int) -> dict:
    hits = Counter()
    for word in words:
        count = text.count(word)
        if count:
            hits[word] = count
    total = sum(hits.values())
    return {
        'per_1k_words': round(total / total_words * 1000, 2) if total_words else 0,
        'total': total,
        'top': hits.most_common(8),
    }


def ai_tells(text: str, total_words: int, extra: tuple = ()) -> dict:
    phrases = tuple(dict.fromkeys(AI_TELL_PHRASES + tuple(extra)))
    return density(text, phrases, total_words)


def cjk_ngrams(text: str, min_len: int = 2, max_len: int = 4):
    """在连续中文串上做滑窗切词（无分词库时的折中：统计重复片段）。"""
    for run in CJK_RUN_RE.findall(text):
        for size in range(min_len, max_len + 1):
            for index in range(len(run) - size + 1):
                yield run[index:index + size]


def repeats(text: str, top: int) -> dict:
    ngrams = Counter(cjk_ngrams(text))
    words = Counter(w.lower() for w in WORD_RE.findall(text))
    # 长 n-gram 优先，过滤被更长片段包含的短片段
    def meaningful(counter: Counter, min_len: int):
        items = [(k, v) for k, v in counter.items()
                 if v >= 3 and k not in STOPWORDS and len(k) >= min_len]
        items.sort(key=lambda kv: (-kv[1], -len(kv[0])))
        picked = []
        for key, value in items:
            if any(key in kept for kept, _ in picked):
                continue
            picked.append((key, value))
            if len(picked) >= top:
                break
        return picked

    heads = [p.strip()[:1] for p in paragraphs(text) if p.strip()]
    head_repeat = Counter(h for h in heads if h)
    return {
        'repeated_cjk': meaningful(ngrams, 2),
        'repeated_words': meaningful(words, 4),
        'paragraph_head_repeat': head_repeat.most_common(5),
    }


def punctuation(text: str, total_words: int) -> dict:
    def per_1k(char: str) -> float:
        count = text.count(char)
        return round(count / total_words * 1000, 2) if total_words else 0

    return {
        'em_dash_per_1k': per_1k('——'),
        'ellipsis_per_1k': per_1k('……'),
        'exclamation_per_1k': per_1k('！'),
        'de_per_1k': per_1k('的'),          # 「的」密度高＝啰嗦/翻译腔
        'bei_per_1k': per_1k('被'),          # 被动句密度
        'punctuation_total': sum(text.count(c) for c in '，。！？；：、,.!?;:'),
    }


def _one_line(text: str) -> str:
    """把换行折叠成空格，便于在报告里展示开头/结尾片段。"""
    return re.sub(r'\s+', ' ', text).strip()


def analyze(text: str, lexicon: tuple = (), top: int = 10) -> dict:
    text = unicodedata.normalize('NFKC', text)
    counts = count_chars(text)
    total_words = counts['words_equivalent'] or 1
    sent_lengths = _lengths(sentences(text))
    para_lengths = _lengths(paragraphs(text))

    result = {
        'counts': counts,
        'structure': {
            'paragraphs': len(para_lengths),
            'sentences': len(sent_lengths),
        },
        'rhythm': rhythm(sent_lengths, para_lengths),
        'dialogue': dialogue_ratio(text, total_words),
        'sensory': density(text, SENSORY_WORDS, total_words),
        'telling': density(text, TELLING_WORDS, total_words),
        'ai_tells': ai_tells(text, total_words, lexicon),
        'expository': density(text, EXPOSITORY_MARKERS, total_words),
        'punctuation': punctuation(text, total_words),
        'repeats': repeats(text, top),
        'head': _one_line(text)[:120],
        'tail': _one_line(text)[-120:],
    }
    return result


# --------------------------------------------------------------------------- #
# 输出
# --------------------------------------------------------------------------- #
def render_markdown(name: str, result: dict) -> str:
    counts = result['counts']
    rhythm_data = result['rhythm']
    lines = [
        f'### {name}',
        '',
        f"- 篇幅：约 {counts['words_equivalent']} 字（中文 {counts['cjk_chars']} 字 / "
        f"英文 {counts['latin_words']} 词），{result['structure']['paragraphs']} 段、"
        f"{result['structure']['sentences']} 句",
        f"- 句长：均 {rhythm_data['sentence_avg']} 字，标准差 {rhythm_data['sentence_stdev']}，"
        f"变异系数 {rhythm_data['sentence_cv']}（<0.5 说明句式偏单一），短句占比 "
        f"{rhythm_data['short_sentence_ratio']}",
        f"- 段落：均 {rhythm_data['paragraph_avg']} 字，变异系数 {rhythm_data['paragraph_cv']}"
        f"（<0.4 说明段落过于均匀，AI 痕迹之一）",
        f"- 对话：字数占比 {result['dialogue']['dialogue_word_ratio']}，"
        f"行占比 {result['dialogue']['dialogue_line_ratio']}",
        f"- 感官密度：{result['sensory']['per_1k_words']} 次/千字"
        f"（重要场景建议 ≥8）",
        f"- 情感标签密度：{result['telling']['per_1k_words']} 次/千字（过高＝在说而非演）",
        f"- AI 高频腔：{result['ai_tells']['per_1k_words']} 次/千字"
        + (f"，命中 {dict(result['ai_tells']['top'])}" if result['ai_tells']['top'] else ''),
        f"- 标点：破折号 {result['punctuation']['em_dash_per_1k']}/千字、"
        f"省略号 {result['punctuation']['ellipsis_per_1k']}/千字、"
        f"「的」{result['punctuation']['de_per_1k']}/千字、"
        f"被动「被」{result['punctuation']['bei_per_1k']}/千字",
    ]

    repeated = result['repeats']['repeated_cjk'] or result['repeats']['repeated_words']
    if repeated:
        shown = '、'.join(f'{word}×{count}' for word, count in repeated[:8])
        lines.append(f'- 重复表达：{shown}')
    head_repeat = result['repeats']['paragraph_head_repeat']
    if head_repeat and head_repeat[0][1] >= 3:
        lines.append(f'- 段首重复：{dict(head_repeat)}')
    lines += ['', f"- 开头：{result['head']}", f"- 结尾：{result['tail']}", '']
    return '\n'.join(lines)


def load_lexicon(path: Path) -> tuple:
    words = []
    for line in read_text(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            words.append(line)
    return tuple(words)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description='小说草稿量化体检（零依赖，中英通用）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('paths', nargs='+', type=Path, help='待检查的 .md/.txt 文件')
    parser.add_argument('--json', action='store_true', help='输出 JSON 而非 Markdown')
    parser.add_argument('--top', type=int, default=10, help='重复表达展示条数，默认 10')
    parser.add_argument('--lexicon', type=Path, help='自定义 AI 高频词表（一行一个）')
    args = parser.parse_args(argv)

    lexicon = load_lexicon(args.lexicon) if args.lexicon else ()
    report = {}
    for path in args.paths:
        if not path.is_file():
            print(f'跳过（不是文件）：{path}', file=sys.stderr)
            continue
        report[str(path)] = analyze(read_text(path), lexicon, args.top)

    if not report:
        print('没有可分析的文件。', file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        for name, result in report.items():
            print(render_markdown(name, result))
    return 0


if __name__ == '__main__':
    sys.exit(main())
