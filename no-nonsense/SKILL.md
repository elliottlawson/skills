---
name: no-nonsense
description: Translate cryptic, convoluted, or over-engineered AI output into plain English. Trigger by saying "that's just nonsense", "that smells like agent speak", "cmon bro", "speak plainly", "stop with the agentspeech", or any phrase calling out convoluted AI language. Use when the user pastes AI-generated text that is hard to parse, overly abstract, packed with shorthand, or wrapped in excessive structure. Preserves all meaning; only the expression changes.
---

# no-nonsense

## Purpose

Frontier models sometimes produce output that is technically grammatical but human-unfriendly: reasoning tokens leak into the text, word-count pressure packs multiple ideas into one clause, or simple points get buried in tables, nested bullets, and abstract jargon. This skill decodes that output. Feed it cryptic text; get back the same information in plain English.

## Trigger words

This skill fires on any of these (or similar) phrases:

- "that's just nonsense"
- "that smells like agent speak"
- "cmon bro"
- "speak plainly"
- "stop with the agentspeech"
- "going forward, speak clearly and avoid agentspeech"

When the user says one of these, treat it as a request to decode the offending text into plain English. If the user says it about their own message ("going forward in this conversation, I want you to speak clearly and avoid agentspeech"), it is a standing instruction: keep all future replies plain and direct, and flag any of your own output that drifts into agentspeech.

## The one rule that matters

**Say what the original said, the way a person would say it.** Not shorter. Not simpler at the cost of accuracy. Just clear.

## Cryptic patterns — what to look for

These are the six patterns this skill recognizes and unpacks. Every translation should name which patterns were found.

### 1. Compression artifacts

The model was squeezed by a word or line cap and started packing. Tells: sentences over 25 words, multiple ideas joined by colons or em-dashes, shorthand the reader has to decode.

> "The certificate question now has a written answer: keep one cert per service. Approving it — or asking for the wildcard instead — is the one decision waiting on you."

**Unpacked:** "You asked whether to keep one certificate per service or switch to a wildcard. I recommend keeping it as is. I need your yes or no."

### 2. Empty abstraction

The model uses abstract nouns and passive voice to sound analytical while saying very little. Tells: "optimization", "streamlining", "leveraging", "it should be noted that", "essentially".

> "In order to optimize the deployment pipeline, it would be worth considering the streamlining of artifact generation processes."

**Unpacked:** "Consider simplifying how build artifacts are created."

### 3. Structure bloat

Simple information is wrapped in tables, nested bullets, or hierarchical headings that add more reading work than they save. Tells: a table with 2 rows, bullets inside bullets, headings for single-sentence sections.

> "## Recommendation\n\n| Approach | Pros | Cons |\n|---|---|---|\n| A | fast | risky |\n| B | safe | slow |"

**Unpacked:** "Two options: A is fast but risky. B is safe but slow."

### 4. Reasoning leakage

The model's internal chain-of-thought or reasoning tags bleed into the visible output. Tells: `<thinking>`, `<|思考|>`, "Step 1: First, I need to...", "Let me work through this..."

> "<thinking>The user wants to know why the build failed. Let me check the logs.</thinking> The build failed because the test runner timed out."

**Unpacked:** "The build failed because the test runner timed out."

### 5. Jargon density

Technical terms are used where everyday words would do, or terms are invented on the spot. Tells: "surface" as a verb, "hydrate" for load, "drain" for process, "materialize" for create.

> "We should surface the error to the user and hydrate the cache before the UI materializes."

**Unpacked:** "Show the error to the user and load the cache before rendering the UI."

### 6. Fragment stacks

The model emits telegraphic fragments instead of sentences. Tells: lines with no verb, labels doing the work of prose ("Root cause: token budget"), lists where the items don't form a coherent paragraph.

> "- Root cause: token budget mismatch\n- Impact: empty titles\n- Fix: bump max_tokens"

**Unpacked:** "The model ran out of tokens, so titles came back empty. Increase max_tokens to fix it."

## How to produce a translation

1. **Read the whole input.** Don't start rewriting sentence by sentence — you need to understand the full intent first.
2. **Identify patterns.** Which of the six (or more) are present? Name them.
3. **Extract the payload.** What is the model actually trying to communicate? Strip the wrapper.
4. **Rewrite in whole sentences.** Use active voice. Name things plainly. One idea per sentence.
5. **Verify fidelity.** Can someone reading only your translation answer "what happened?", "what should I do?", and "why does it matter?" as well as someone who read the original? If not, you lost something — put it back.

## Output format

```
## Patterns found
[List the cryptic patterns detected, with a one-line example from the original for each]

## Translation
[The plain-English rewrite. Whole sentences. No filler. Same information, same order of importance.]

## Fidelity check
[One sentence: what was preserved and whether anything was dropped or added]
```

## Boundaries

- **Do not judge correctness.** If the original is wrong, the translation is still wrong. This skill only fixes expression, not facts.
- **Do not add what isn't there.** If the original was vague, the translation should be equally vague — just in plain English.
- **Do not preserve cryptic formatting.** Tables become sentences. Nested bullets become paragraphs. The shape of the information changes; the content does not.