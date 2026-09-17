# Pacing

Load this when diagnosing "the chapter drags", "it rushes and readers can't keep up", "the climax doesn't pay off", or when planning the rise and fall across several chapters. The baseline (alternate tempo; climactic impact = suppression time × release intensity) lives in SKILL.md; this is the full expansion.

> Related: scene length and genre ratios in [Scene Design](craft-scene-design.md); payoff density and retention in [Web Serial Rhythm](craft-webnovel-rhythm.md); paragraph uniformity is measurable with `scripts/draft_diagnostics.py`.

## I. What pacing is

Not "write fast or slow" but **the frequency of information released and emotion stimulated**. Sustained high intensity numbs the reader; sustained low intensity loses them. Pacing has to breathe.

## II. Tools for fast and slow

| Direction | Tools |
|-----------|-------|
| **Accelerate** | cut filler, short sentences, continuous action, shorter scenes, less interior monologue, one-sentence paragraphs |
| **Decelerate** | interiority, environmental rendering, multi-viewpoint pull, longer scenes, more body-sensation detail, long and compound sentences |

**Paragraph length is the throttle**: short paragraphs (1-3 lines) read fast, long paragraphs read slow. AI output tends toward uniform paragraph length (coefficient of variation < 0.4) and needs manual breaking up.

## III. Suppression before the climax

Impact ≈ suppression time × release intensity. Before a climax, apply pressure: the protagonist is thwarted, the situation worsens, the reader worries for them. The longer the pressure, the bigger the release — but small payoffs must be sprinkled in between or readers fatigue and drop the book (see the web-serial guide).

**Suppression tools**: countdown, depleted resources, allies leaving, the cost of a mistake, the antagonist winning a round, the protagonist wounded.

## IV. Pacing breaks and transitions

- Don't cut straight to daily life after a big conflict (the reader is still digesting); give a transition beat or two that carries the emotional afterglow.
- Conversely, after a long calm stretch, insert a "wake-up" event — otherwise the flat ground runs too long.
- Every chapter needs internal contour: setup (carry-over) → rise (escalation) → turn (reversal / false ending) → landing (payoff or hook).

## V. Chapter templates (paste into the chapter brief)

1. **Setup → rise → turn → payoff (general)**: setup 300-500 words → rise 800 → turn 300 → payoff 400 + hook
2. **Roller coaster (battle / crisis)**: tension → brief breath → more tension → false ending → maximum tension → hook
3. **Information ladder (mystery / puzzle)**: clue A → conclusion 1 → something's off → clue B overturns conclusion 1 → new reasoning → a bigger secret

## VI. Cool-down chapters

After consecutive climaxes, insert a **low-intensity but informative** chapter (regrouping, relationship scenes, world expansion) so the reader's sensitivity recovers. A cool-down chapter is not a filler chapter: it must advance relationships, foreshadowing, or character state.

## VII. Pacing diagnosis

| Symptom | Check | Fix |
|---------|-------|-----|
| Dragging | does the chapter have passages where nothing changes? | compress or delete; turn exposition into conflict |
| Relentless rush | is there a sequel (reaction–dilemma–decision)? | add a reaction beat; let the reader breathe |
| Climax doesn't pay | how many chapters of pressure? what did it cost? | add suppression, cost, and higher stakes |
| Exhausting to read | consecutive chapters peaking on the same emotion | change the emotion type; insert a cool-down |
| Feels flat | paragraph CV, sentence-length CV | break up paragraphs; alternate sentence length |
| Retention dropping | the last 3-5 chapter-end hooks | see [Web Serial Rhythm](craft-webnovel-rhythm.md) |

## VIII. Numbers to watch

After `python scripts/draft_diagnostics.py chapter.md`:

- **Sentence-length CV < 0.5** → sentence patterns too uniform
- **Paragraph CV < 0.4** → paragraphs too even (an AI tell)
- **Sensory density < 8 per 1,000 words** → thin scenes (for important scenes)

Numbers localize. Whether and how to change things remains the author's call.
