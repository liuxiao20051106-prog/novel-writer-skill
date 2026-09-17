# Context Budget & Memory Packing

Load this for long works and serials, cross-session writing, batch generation, or when diagnosing "the AI forgot earlier canon" or "it contradicts itself". The hard rules (never rely on chat memory; project files are the source of truth; feed only what this chapter needs) live in SKILL.md.

> Related: [Project Continuity](project-continuity.md), [Continuity Ledger](../templates/continuity-ledger.md), [Chapter Brief](../templates/chapter-brief.md), [Automation Workflow](automation-workflow.md).

## Core fact: the AI does not remember

Every generation is a fresh one-off read. The model sees only what you feed this time. "The AI forgot chapter 3" really means **you didn't feed it this time**. So the engineering problem of long-form writing is: **what to feed, and how much.**

## Packing list per generation (priority order)

Always include (missing any invites trouble):

1. **Chapter brief**: goal, resistance, turn, information gained/lost, end-state, constraints.
2. **Last 800-1,500 words of the previous chapter**: the source of continuity, more reliable than a summary.
3. **Previous chapter result summary** (3-5 sentences): what changed, what state characters are in now.
4. **Relevant character cards**: only characters appearing in this chapter (name, goal, speech pattern, current state, relationships).
5. **Active foreshadowing and subplots**: the ones this chapter touches, with "planted in chapter N / planned payoff in chapter M".
6. **Style anchor**: a 200-word sample from the opening chapters + banned-word list + target sentence length.

As needed: world rules relevant to this chapter, timeline fragments, glossary, the boundary between what has and hasn't been revealed.

**Do not** pack every time: the whole outline, every character, every foreshadowing thread, full text of past chapters. Full is not effective — it dilutes.

## Layered summaries (the key to controlling volume)

| Layer | Content | Length | When |
|-------|---------|--------|------|
| **Book summary** | main thread, current volume, protagonist state, core promises | ≤300 words | every generation |
| **Volume summary** | volume goal, key turns, current situation | ≤200 words | every generation within the volume |
| **Chapter summary** | what happened, what changed, what remains | ≤80 words/chapter | take the last 3-5 chapters plus relevant older ones |

Rolling updates: update the chapter summary immediately after writing; recompute the volume summary every 10 chapters; recompute the book summary per volume. **A human must review the summaries** — AI-generated ones accumulate drift.

## Budget allocation (rule-of-thumb ranges; adjust for model context)

| Content | Share |
|---------|-------|
| System instructions (SKILL.md + style anchor) | 15-25% |
| Fact layer (characters / setting / foreshadowing / timeline) | 20-30% |
| Prior text (previous chapter ending + recent summaries) | 20-30% |
| This chapter's brief and constraints | 10-15% |
| Reserved for generation and dialogue | ≥20% |

Leave headroom: 2,000-4,000 Chinese characters of output costs roughly 3-6k tokens. When context nears the limit, compress the fact layer (drop irrelevant characters) before cutting prior text.

## Two-step generation (prevents large-scale drift)

1. **Chapter plan first**: 3-5 key events, characters present and their goals, emotional start → end, foreshadowing to plant or harvest, end-of-chapter state. **Human approves before prose is written.**
2. **Write prose to the plan**: feed the approved plan back in as the contract.

This avoids burning three thousand words before discovering the direction is wrong, and it's the only reliable guardrail for batch generation.

## Three carriers of memory (don't mix them)

| Carrier | Holds | Doesn't hold |
|---------|-------|--------------|
| **Project files (single source of truth)** | setting, character state, timeline, foreshadowing ledger, established facts | ideas, passing thoughts |
| **Chapter prose** | finished text | plans and discussion |
| **Session** | in-process trade-off discussion | any fact that must survive across sessions |

Rule: any **new fact** produced in a session (new character, new rule, a death, a new relationship) must be written back to the project file after writing — otherwise it does not exist next session.

## Three hard anti-drift rules

1. **Carry the style anchor**: feed the same 200-word sample every time, especially when switching models (or the voice breaks).
2. **Prefer one model per book**: when switching, use 200 words from each of the first three chapters as style reference.
3. **Write back immediately**: new facts, character state changes, timeline shifts, foreshadowing changes — into the ledger before starting the next chapter.

## The once-per-volume setting audit

Even with a ledger, long works accumulate edge contradictions. Every 100k words or at each volume end:

1. Export the core entity list (characters, places, props, timeline, secrets revealed).
2. Have the AI check item by item: is the timeline self-consistent, do ages and distances add up, has anything been revealed that shouldn't have?
3. On contradiction: prefer fixing it naturally in later plot (editing published chapters is expensive) and correct the ledger.
4. Check active subplots ≤3; long-stalled ones either advance or merge.

## Session handoff template

At the start of a new session, give the AI three things before making requests:

```
[TASK] Chapter X: … (target words / must advance / must not change)
[STATE] book summary + last 800 words of previous chapter + character cards for those present
[STYLE ANCHOR] 200-word sample + banned words + sentence-length range
```

At the end, require a write-back: new facts in this chapter, character state changes, timeline changes, foreshadowing changes, deviations from the brief, items awaiting the user.
