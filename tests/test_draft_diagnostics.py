# -*- coding: utf-8 -*-
"""draft_diagnostics.py 的单元测试（零依赖，可直接 python -m unittest 运行）。"""

import json
import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

import draft_diagnostics as dd  # noqa: E402

SAMPLE = """第一章 夜里的敲门声

林默听见敲门声的时候，正把最后一口面汤喝完。
门外的风很冷，他把袖口往下拽了拽。

“谁？”他问。

“是我。”门外的人说，“开一下。”

他没有开。他盯着门缝底下那道影子，影子里有三个人。

值得注意的一幕出现了：他忽然意识到，这不仅仅是有人来找他，更是某种命运的安排。
"""


class TextMetricsTests(unittest.TestCase):
    def test_count_chars_handles_mixed_languages(self):
        counts = dd.count_chars('你好 hello world')
        self.assertEqual(counts['cjk_chars'], 2)
        self.assertEqual(counts['latin_words'], 2)
        self.assertEqual(counts['words_equivalent'], 4)

    def test_sentences_split_by_punctuation(self):
        result = dd.sentences('他停下了。他回头看了一眼！没人。')
        self.assertEqual(len(result), 3)

    def test_dialogue_ratio_detects_quotes(self):
        result = dd.dialogue_ratio('“谁？”他问。门外没人回答。', 12)
        self.assertGreater(result['dialogue_word_ratio'], 0)

    def test_uniform_rhythm_has_low_variation(self):
        uniform = ['一二三四五六'] * 10
        varied = ['一二'] * 5 + ['一二三四五六七八九十'] * 5
        self.assertLess(dd.rhythm([6] * 10, [6] * 10)['sentence_cv'], 0.1)
        self.assertGreater(dd.rhythm([2] * 5 + [10] * 5, [6] * 10)['sentence_cv'], 0.1)
        self.assertTrue(uniform and varied)

    def test_ai_tells_detects_known_phrase(self):
        hits = dd.ai_tells('值得注意的是，事情发生了变化。', 15)
        self.assertIn('值得注意', dict(hits['top']))

    def test_repeats_finds_repeated_phrase(self):
        text = '他握紧了刀锋。他又松开了刀锋。最后他把刀锋放下。'
        repeated = dict(dd.repeats(text, 10)['repeated_cjk'])
        self.assertTrue(any('刀锋' in key for key in repeated), repeated)

    def test_punctuation_counts_de(self):
        result = dd.punctuation('他的刀和他的剑。', 8)
        self.assertGreater(result['de_per_1k'], 0)

    def test_analyze_returns_all_sections(self):
        result = dd.analyze(SAMPLE)
        for key in ('counts', 'structure', 'rhythm', 'dialogue', 'sensory',
                    'telling', 'ai_tells', 'expository', 'punctuation', 'repeats'):
            self.assertIn(key, result)
        self.assertGreater(result['counts']['cjk_chars'], 50)

    def test_render_markdown_includes_key_metrics(self):
        text = dd.render_markdown('示例', dd.analyze(SAMPLE))
        for keyword in ('篇幅', '句长', '对话', '感官密度', 'AI 高频腔'):
            self.assertIn(keyword, text)


class CommandLineTests(unittest.TestCase):
    def test_json_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'chapter.md'
            path.write_text(SAMPLE, encoding='utf-8')
            buffer = StringIO()
            old = sys.stdout
            sys.stdout = buffer
            try:
                code = dd.main([str(path), '--json'])
            finally:
                sys.stdout = old
            self.assertEqual(code, 0)
            data = json.loads(buffer.getvalue())
            self.assertIn(str(path), data)

    def test_missing_file_reports_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            code = dd.main([str(Path(tmp) / 'nope.md')])
            self.assertEqual(code, 1)

    def test_custom_lexicon_is_used(self):
        with tempfile.TemporaryDirectory() as tmp:
            lexicon = Path(tmp) / 'words.txt'
            lexicon.write_text('# 自定义\n铁锅\n', encoding='utf-8')
            words = dd.load_lexicon(lexicon)
            self.assertEqual(words, ('铁锅',))


if __name__ == '__main__':
    unittest.main()
