# Removing the AI Voice

Load this when prose "reads like a machine wrote it", when it must pass an AIGC detector or a first-pass editor, or when running an AI-voice self-check. The hard rules (no boilerplate, no uplift endings, no three-beat parallelism, no summarizing close) live in SKILL.md; this file is the full list plus fixes.

> Tooling: run `python scripts/draft_diagnostics.py chapter.md` first for objective numbers (AI-tell density, sentence/paragraph variation, repeated phrasing), then fix location by location.
> Related: [Prose & Style](craft-prose-style.md), [Emotion & Subtext](craft-emotion-and-subtext.md), [AI Collaboration](ai-collaboration.md).

**Principle: cut the machine's posture, not the author's content.** When in doubt whether a line is AI voice or author voice, flag it for the author — do not delete unilaterally.

## Where the machine voice comes from

Models default to the safest, most common phrasing. Safe phrasing is boilerplate, producing three symptoms:

1. **Uniform** — every paragraph the same length, every sentence the same beat, no emotional contour (verify with the script's coefficient of variation).
2. **Exhaustive** — both sides stated, three parallel points, a summary at the end (real thinking is biased).
3. **Uplifting** — a small thing inflated into a grand statement; the last line always ascends (real writing usually stops on an action or a detail).

## Ten signals and their fixes

| # | Signal | Typical shape | Fix |
|---|--------|---------------|-----|
| 1 | Boilerplate opener | "It is worth noting", "As we all know", "It is not hard to see" | Delete the sentence; start with the event |
| 2 | Swelling uplift | "This was not just a bowl of noodles, it was an attitude" | Cut the uplift; let the fact stand, or convert it into a concrete action |
| 3 | Three-beat parallelism | "faster, better, stronger"; "not only… but… indeed…" | Keep only the strongest beat; delete the rest |
| 4 | Empty analysis | "This reflects… demonstrates… embodies…" | Give a real cause, or delete |
| 5 | Vague attribution | "experts say", "it is widely believed" | Name a source or a character's judgment; no source means delete |
| 6 | Dash/parenthesis abuse | two "— clarifying asides" in one sentence | Cap at 2 per 1,000 words; split into short sentences |
| 7 | Filler hedges | seemingly, as if, in a sense, to some extent, undoubtedly, filled with, suffused with, interwoven with | Replace with plain action or delete |
| 8 | Even paragraphs | 3-4 sentences each, identical length | Deliberately break it: insert a one-sentence paragraph, merge two, split one |
| 9 | Emotional overload / summary close | "Let us look forward to…", "In that moment he finally understood life" | End on fact, action, or one concrete detail — never a conclusion |
| 10 | Perfect symmetry | both sides always balanced; every turn is "however" | Real thought is biased and uncertain; keep that |

## Plus four fiction-specific tells

- **Adverbs naming emotion**: "he shouted angrily", "she lowered her head sadly" → drop the adverb, keep action and line.
- **Saying it four times**: "he clenched his fist, his palm whitened, veins rose, knuckles cracked" — keep the single harshest one.
- **All five senses everywhere** → decide which two senses this scene actually needs; cut the rest.
- **Explanatory narration** summarizing a character's motive for the reader → delete; let readers judge.
- **Recycled similes** ("like a startled rabbit", "the air seemed to freeze") → use imagery from that character's trade or background.
- **Over-complete dialogue**: every line a full, polite compound sentence → add interruptions, ellipsis, non-answers.

## High-frequency word swaps

| Don't write | Write instead |
|-------------|---------------|
| It is worth noting / noteworthy | (delete) |
| As we all know / it is easy to see | (delete) |
| filled with / suffused with / interwoven with | a concrete thing: a tabletop thick with grease |
| as if / seemingly / in a sense | a definite action or sensation |
| not only… but indeed… | keep only the second half |
| complex emotions / mixed feelings | body and action: he set down the cup, picked it up again, did not drink |
| a trace of / a wisp of / a hint of (overused measure words) | a concrete quantity: dust half a finger thick |
| at this moment / in this instant (frequent) | delete, or use a time anchor: the watch drum had just struck |
| a flicker crossed his eyes | write the consequence: he turned his face away and stayed silent a long while |
| secretly in his heart / faintly in his chest | delete (interiority can be written directly) |

## Four-pass rewrite

1. **Measure**: run `draft_diagnostics.py`; record AI-tell density, sentence CV, paragraph CV, repeated phrasing.
2. **Sweep**: search the word list above; for each hit decide delete / replace / keep-as-author-intent.
3. **Break the rhythm**: merge or split paragraphs; insert 1-3 one-sentence paragraphs; split a long sentence or join two short ones.
4. **Re-measure**: AI-tell density should drop and CV rise; hand the change list to the author for final approval.

## Boundaries: don't wreck the prose to look human

- Don't delete a genuinely apt phrase just because models like it.
- Don't add typos, emotional exclamation, or filler slang to seem human.
- Don't rewrite whole passages on statistical suspicion — **statistics locate; they don't convict.**
- The author's own style (even a tidy one) outranks the generic checklist.

## Negative-prompt template

State what must not appear before writing, not after:

> This chapter must not contain: it is worth noting, as we all know, as if, seemingly, to some extent, filled with, complex emotions, mixed feelings, a flicker crossed his eyes, summarizing final lines.
> No three-beat parallelism or "not only… but indeed…"; no equal-length paragraphs; no summary or uplift at chapter end.
> No paragraph may open with the same character as the previous one; no simile twice.
> Emotion must be rendered through action, body response, or dialogue — never named.
