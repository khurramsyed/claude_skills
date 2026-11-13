---
name: 'simplify-deck'
description: 'Convert an existing PowerPoint deck (or create a new one) into a simplified Pyramid Principle deck: one message per slide, visuals over text, full speaker notes.'
---

# Simplify Deck

Use this skill when the user wants an existing PowerPoint deck converted into a simpler, Pyramid Principle (Minto) deck, or wants a new deck created in that style. The output is always a .pptx file. Load the `pptx` skill's SKILL.md with the Skill tool before reading, building or editing any .pptx, and follow it for extraction, templates, layouts, rendering and speaker notes.

## Modes

- **Convert mode** (a source deck is attached): diagnose the deck, restructure it into a pyramid, simplify the slides.
- **Create mode** (no source deck, only notes, documents, an RFP or a topic): skip the diagnosis, gather the material (research the topic if needed), then follow the same intake, pyramid, simplification, notes and build steps below. If the `pyramid-deck-builder` skill is available, its intake and concern framing can be reused.

Treat the user's original file as read-only; work on a copy and deliver a new file (e.g. `<original-name>-simplified.pptx`).

## Step 1 — Read the source deck (convert mode)

Extract every slide's title, body text, tables, charts, images and existing speaker notes, plus the masters/layouts, fonts and colour theme. Render the slides to images so you can see how they actually look.

## Step 2 — Infer the context, then confirm

From the deck (and any RFP or brief provided), infer and present to the user for confirmation:

- Audience (e.g. client executives, technical stakeholders, evaluation panel)
- Governing thought: the main answer or recommendation the deck is trying to land
- Customer / RFP concerns the deck addresses, citing the slide or RFP section each came from
- Talk length implied by the deck

For anything you cannot infer with confidence, ask the user, one question at a time:

1. Who is the audience?
2. What decision, action or belief should they leave with?
3. What specific customer concerns should we highlight? For each, what do you know beyond the documents: root cause, the customer's past experience, our differentiator, proof points?
4. How long is the talk? (Size the main deck at ~2 minutes per slide.)
5. Any important points to discuss, sensitivities, competitors or topics to avoid?

## Step 3 — Ask two set-up questions (one at a time)

1. **How much should I change the deck?** Offer: full restructure (reorder, merge, split, cut slides); restructure but keep all content (cut material goes to an appendix); light touch (keep order, rewrite titles as action titles and tighten text).
2. **What should it look like?** Offer: keep the original deck's design (its own masters and layouts), or rebuild on a template the user supplies (.pptx/.potx). If they choose a template and haven't attached it, ask for it.

## Step 4 — Diagnose the original (convert mode)

Produce a short diagnosis covering:

- **Answer placement**: is the governing thought stated up front, buried, or missing?
- **Titles**: which slides have topic labels instead of action titles
- **Overloaded slides**: slides making more than one point
- **Text walls**: slides that are dense bullets that could be a visual
- **Logic gaps**: missing "why?"/"how?" support, overlapping or missing arguments (not MECE), redundant slides
- **Concern coverage**: which customer/RFP concerns are addressed weakly or not at all
- An overall verdict in a sentence or two

## Step 5 — Build the new pyramid

- **SCQA opening**: Situation, Complication (reflecting the customer's top concerns), Question, Answer. The Answer is the governing thought and appears at the start.
- **Key lines**: 3–5 MECE supporting arguments, each answering the "why?" or "how?" raised by the level above, ordered deductively or inductively (by time, structure or importance; for RFPs, by customer priority or evaluation weighting).
- **Concern blocks**: for each confirmed concern, write Concern (customer's words, RFP ref) → Problem statement (specific, quantified business impact) → Solution → Proof → Outcome. Priority concerns get their own slide; lesser ones can be grouped. Include a concern traceability table (concern / RFP ref → solution → slide).
- **Action titles**: every slide title is a full-sentence takeaway; reading titles alone must tell the story.
- Map original slides to new slides: kept, retitled, split, merged, moved to appendix or cut (respecting the change level chosen in Step 3).

## Step 6 — Simplify each slide

- **One message per slide**: the action title states it; split any slide carrying more than one point.
- **Visuals over text**: replace bullet walls with the simplest visual that carries the message — a chart for numbers and trends, a process/flow diagram for sequences, a comparison or two-column layout for options, a simple table for structured facts, a single big number for a key metric. Keep only the words needed to support the title.
- Preserve accuracy: never change figures or claims while simplifying; keep source references.

## Checkpoint — Diagnosis and storyline approval

Present to the user before building:

- The diagnosis from Step 4
- The SCQA, governing thought and pyramid outline, showing where each concern sits
- The concern blocks
- The new slide list: action title, visual treatment, layout to use, main/appendix, and which original slide(s) it came from
- A list of anything cut or moved to the appendix
- **Layout gaps**: any slide whose content or visual doesn't fit an available layout in the chosen design. List them and ask how to handle each — never invent layouts silently.

Run MECE, concern-coverage and titles-only read-through checks and mention weaknesses. Wait for approval or changes.

## Step 7 — Draft speaker notes

For every slide, write plain-text notes with three labelled sections:

**Context & why it matters** — where the slide sits in the pyramid, which concern(s)/RFP references it addresses, background the speaker needs, and the "so what" for this audience. Fold in any useful detail removed from the slide body or carried in the original notes.

**Talk track** — what to say in natural spoken language, ~2 minutes; on concern slides, acknowledge the concern in the customer's words first; end with the transition to the next slide.

**Likely questions & answers** — 2–4 likely questions with concise suggested answers; on concern slides include the toughest evaluator objections. Flag answers that need the user to confirm facts.

Share the notes draft and ask the user to confirm or adjust before building, and whether there are further points or concerns the notes should prepare them for.

## Step 8 — Build the deck

Following the `pptx` skill:

- Use the design chosen in Step 3 (original masters/layouts or the supplied template), keeping its fonts, colours and placeholders.
- Handle layout-gap slides as the user decided.
- Build visuals as native, editable PowerPoint elements (charts, shapes, tables) where possible, not flattened images.
- Add the approved notes to every slide, including appendix slides.
- Add the appendix and concern traceability table.

## Step 9 — Check before delivering

- Render every slide and inspect for overflow, overlap, unreadable visuals and off-brand formatting.
- Titles-only read-through tells the whole story; every slide carries one message.
- No figures or claims changed from the source; nothing dropped that the chosen change level said to keep.
- Every confirmed concern has a problem statement and solution and appears in the traceability table.
- Every slide has notes with all three sections; slide count fits the talk length (~2 min/slide).

Deliver the new .pptx with a one-line before/after summary (e.g. "28 slides → 12 main + 9 appendix; answer now on slide 2") and list open items.
