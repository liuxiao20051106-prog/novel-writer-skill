# Prose & Style

Load this when setting the voice, polishing language, or diagnosing "the style drifted", "ornate but empty", "emotion-by-label writing", "reads like AI". The baseline (concrete > abstract, verbs > adjectives, body before brain, white space) lives in SKILL.md; this is the full expansion.

> Related: body-before-brain and white space in scenes: [Immersion](craft-immersion.md); the machine-voice word list: [Removing the AI Voice](craft-ai-tells.md); not naming emotion: [Emotion & Subtext](craft-emotion-and-subtext.md).

## I. Set the voice before drafting; lock it in the first three chapters

| Style | Diction | Sentence strategy |
|-------|---------|-------------------|
| Historical / classical | refined, archaic-leaning, compact | mix long and short; avoid modern colloquialism |
| Contemporary romance | direct, fine-grained, everyday | interiority plus environment |
| Mystery | cold, restrained, high white space | mostly short sentences; build tension |
| Payoff-driven | crisp, forceful, emotionally direct | short sentences plus parallelism (sparingly) |
| Healing / cozy | gentle, unhurried | focus on warm concrete detail |

**How to lock it**: once the first three chapters are fixed, pull 200 words from each as a "style anchor" and carry it into every generation — the cheapest defense against drift (see [Context Budget](context-budget.md)).

## II. Four hard rules

- **Concrete > abstract**: write behavior, not emotion labels
- **Verbs > adjectives**: precise verbs give prose force
- **Body before brain**: physiological response first, conscious judgment second
- **White space**: don't spend the feeling; let readers fill it from their own experience

## III. Filter words — the category to cut first

"He **felt**…", "she **saw**…", "he **noticed**…", "he **realized**…" — these put a pane of glass between character and reader. Delete them and write the thing perceived:

- ✗ He felt a chill → ✓ His nape cooled; the hair on his arms stood up
- ✗ She noticed a letter on the desk → ✓ A letter lay on the desk, its seal broken once already
- ✗ He realized he'd been deceived → ✓ The edge of that seal was half a shade shallower than he remembered

**Exception**: keep them when emphasizing misunderstanding or delayed reaction ("only much later did he understand…").

## IV. Verbs first

| Weak | Strong |
|------|--------|
| He walked quickly across the room | He brushed past / he charged across |
| She said, very angry | She set the cup down hard |
| The rain was heavy | Rain hammered the tiles and threw up a white mist |

Principle: in a sentence, verbs carry ~70% of the information and adjectives at most 20%; the rest comes from the concreteness of nouns.

## V. Density control

- **Adjectives/adverbs**: no more than 2 modifiers per passage; adverbs especially ("very / extremely / utterly" are almost always deletable).
- **Similes**: 1-3 per 1,000 words; imagery should come from the character's life (a carpenter doesn't think "like an ink painting").
- **Sensory density**: ≥8 per 1,000 words in important scenes — but not all five senses; pick the two or three the scene needs.
- **"的" density** (Chinese): over ~45 per 1,000 words usually means tangled, translation-flavored sentences.

All of these are measurable with `scripts/draft_diagnostics.py`.

## VI. Sentence rhythm

- Action / tense scenes: mostly short sentences (≤15 characters); one-sentence paragraphs are fine.
- Lyric / reflective scenes: mix lengths for breathing room.
- Avoid three consecutive sentences of the same length (a common AI habit) — but don't vary for its own sake.
- In Chinese, prefer active over passive (too many "被" makes the prose feel insubstantial).

## VII. White space and endings

- End paragraphs on an action or an image, never on a summary or an uplift.
- Especially never close a chapter with a summarizing line — that's AI's home turf (see [Removing the AI Voice](craft-ai-tells.md)).
- Let readers reach the emotional conclusion themselves: write the cause, not the effect.

## VIII. An offline polishing routine

1. Run `draft_diagnostics.py`; note filter-word density, AI-tell density, sentence and paragraph CV.
2. Search the whole text for filter words and for "very / extremely / filled with / as if"; handle each.
3. Check each paragraph's last sentence — is it summarizing? Cut it.
4. Replace three verbs with more precise ones.
5. Run the script again and compare.
