---
name: writing-craft
description: Write or rewrite any document, message, or generated output so every line works toward the document's goal. Invoke before writing to produce quality prose the first time, or after to fix text that reads as filler or drifts from its purpose. Distinct from no-nonsense: that skill fixes convoluted expression; this one fixes what deserves to be said at all.
---

# writing-craft

## Purpose

Most bad writing is not unclear. It is pointless. Sentences are polished, formatted, and grammatically correct, yet the reader finishes with nothing. This skill fixes that: it makes every line work toward the goal of the document, then makes what survives clear.

Two separate problems, two separate passes. **Selection** decides what deserves to be said. **Clarity** decides how the survivors are said. They are independent. A line can be useful and still read badly. A line can be clear and still be pointless. Fix selection first, then clarity.

## The one rule that matters

**Everything earns its keep.** Every line either moves the reader toward the document's goal or it gets cut. And every line that survives gets rewritten until it is plain.

## Step 1 — State the goal

Before touching a word, answer: what should the reader walk away with? One sentence. If you cannot state it, nothing below it can be fixed.

For a README: "there are skills here, here's how to grab them." For a changelog: "what changed and why it matters." For a status update: "what is done, what is blocked."

The goal is the yardstick. Every later decision is "does this line serve the goal?"

## Step 2 — Select: keep or cut

Go through the text line by line. For each, ask one question: does this line help the reader do something toward the goal? If yes, keep it. If no, cut it.

Do not decide "keep" and stop. Keeping a line only means it survives to the rewrite pass. It does not mean it is finished.

Common reasons to cut:

- **Self-reference.** "Published one at a time", "watch the repo", "iterated privately first". Notes to the author, not the reader.
- **Format-explaining.** "Each is a directory with a SKILL.md file." The reader already knows what the thing is, or they would not be here.
- **Signatures.** "By Elliott Lawson." It is in the repo. The byline is not information.
- **Worse alternatives.** "Or clone the repo" when one official path exists. Offer the official way; do not invent a second one.
- **Mechanics nobody asked about.** "Any agent that supports the spec can load them." Explains the format, not the value.

The biggest wins are deletions, not rewordings. Never polish a sentence that should not exist. If you are unsure, cut it and see if the document still works. It usually does.

## Step 3 — Clarify: rewrite every survivor

Now take every line that survived Step 2 and rewrite it. Do not skip lines because they were "useful" or "fine." Useful is not the same as plain. Apply these rules to every surviving line:

- **One idea per sentence.** Under 20 words.
- **Active voice.** Name things plainly.
- **No em dashes.** No stacked qualifiers. No invented shorthand.
- **No trailing comments in code blocks.** A `# comment` on a command is a sentence hiding in a code block. Move it into prose, or cut it.
- **Shortest clear version.** If a description has a redundant clause, cut the clause. "Instructs your agent to use plain English instead of cryptic, convoluted output" beats the same idea with "i.e." and "over-engineered" tacked on.
- **Do not use the very thing you are removing.** If the goal is plain English, the rewrite must be plain English.

## Step 4 — Verify against the goal

Read the result as a newcomer would. Ask: does every remaining line serve the goal? Would the reader walk away with the one thing you wanted?

Then ask the harder question: is every surviving line as plain as it can be? If a line is correct but still wordy, it is not done. Rewrite it again.

## Boundaries

- **Do not judge facts.** If the original is wrong, the rewrite is still wrong. This skill fixes what is said and how, not whether it is true.
- **Do not add what is not there.** If the original was vague, the rewrite is equally vague, just plain. Do not invent content the original lacked.
- **Do not preserve structure.** Tables, headings, and bullets exist to serve the goal. If they do not, they go.
- **Do not over-index on examples.** The cut reasons above are common, not exhaustive. Judge every line against the goal, not against the list.

## Relationship to no-nonsense

- **no-nonsense** fixes expression: convoluted becomes plain, same content.
- **writing-craft** fixes selection: pointless becomes absent, then what survives is made plain.

Use no-nonsense when the content is right but the words are wrong. Use writing-craft when you are not sure the content should exist at all. When in doubt, run writing-craft first: cutting filler often removes the need to rewrite anything.