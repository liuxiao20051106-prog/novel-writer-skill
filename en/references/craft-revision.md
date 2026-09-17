# The Revision Process

Load this after a draft is finished, when planning a systematic revision, or when diagnosing "revised many times and still wrong" or "it gets flatter every pass". The core stance (draft like a loving parent, revise like a ruthless god) lives in SKILL.md.

> Related: [Quality Review](quality-review.md); technique-specific fixes via the SKILL.md index; cross-session batch revision: [Automation Workflow](automation-workflow.md).

## Why revision is round-based

Fixing everything at once usually yields pretty sentences on a collapsed structure. Revision goes **large to small, one class of problem per pass**.

| Pass | Goal | Main actions | Don't |
|------|------|--------------|-------|
| **0. Cool off** | restore judgment | wait 3-7 days; record only, revise nothing | sneak in a polish |
| **1. Structure** | causation, arc, rhythm | reverse outline, cut/merge chapters, add missing beats | touch sentences |
| **2. Scene & character** | does each scene have conflict and change; do actions fit the character | rewrite dead scenes, fix character voice | fiddle with wording |
| **3. Language** | concreteness, verbs, repetition, AI voice | polish passage by passage, cut boilerplate | change plot |
| **4. Read-through** | flow and rhythm feel | read 3-5 chapters continuously; mark drifts and drags | do major surgery |

## The reverse outline (first cut)

After the draft, write a one-line summary per chapter — from memory, without looking — then check it against the text.

```
Chapter N: [POV] [what the character wants] [what resists] [what changes as a result] [what hook remains]
```

Three things surface immediately:

1. **Chapters you can't summarize** — usually "nothing happened"; merge or rewrite.
2. **Runs of identical summaries** — the rhythm has flattened; insert change or compress.
3. **Summaries with no character choice** — the protagonist is passive and readers stop identifying.

Laid out as a table, the reverse outline *is* the revision map: structure first, sentences later.

## Cooling off and reading through

- Cool for at least 3 days; for long works, cool per volume.
- While reading through, **don't edit** — only log "where I drifted / skipped / got impatient". Those spots beat any rubric.
- Reading aloud (or TTS) is the fastest detector for dialogue and sentence faults; fix whatever trips the tongue.
- For important work, add a human read-through on top of AI checks — AI repeats its own blind spots.

## Using AI to revise, correctly

**Good for AI**: continuity checks (who is where, in what state), listing repeated phrasing and high-frequency words, checklist-driven diagnostics, offering 2-3 rewrite options, batch term/address replacement.

**Bad for AI**: deciding to cut your favorite passage, judging your theme, one-click "polish the whole book" (it sands personal style into generic voice).

**Three anti-drift rules**:

1. Give AI a **style anchor** for this chapter only: a 200-word sample from the opening chapters + a banned-word list + target sentence length.
2. Make AI produce a **problem list and options** first; you approve before anything is rewritten.
3. Changes must be diffable: keep the original, output "before → after → reason", so rollback is easy.

## File rules before revising

- Read the target file and confirm the path before writing; default to a new version or a recoverable copy — never overwrite the original.
- Local polishing must not silently change plot facts; deleting, merging, or large-scale rewriting requires explicit authorization.
- Tag versions (AI draft / author revision / final) with date, scope, and reason.
- On interruption or failure, leave a clear marker — never a half-finished file that looks complete.

## Single-chapter revision checklist

- [ ] Does the chapter have one clear line in the reverse outline?
- [ ] Does the opening carry over the previous chapter's ending (time / place / POV / emotion)?
- [ ] Does it complete at least one advance (plot / character / relationship / foreshadowing)?
- [ ] Any "nothing happens" scene to cut or compress?
- [ ] Is the emotional landing different from the opening?
- [ ] Is the end hook natural, not contrived or coy?
- [ ] Have high-frequency words, repetition, and AI voice been swept (use `scripts/draft_diagnostics.py`)?
- [ ] Is word count within ±15% of target?

## When to stop revising

- Changes start oscillating between two versions (that's preference, not a problem).
- Every edit is just a synonym swap (go fix structure or scene).
- Three consecutive passes touched only language (ship it, or get outside feedback).
