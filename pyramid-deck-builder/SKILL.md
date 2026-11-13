---
name: 'pyramid-deck-builder'
description: 'Build a PowerPoint deck on a user-supplied .pptx/.potx template using the Minto Pyramid Principle, addressing customer/RFP concerns, with rich speaker notes.'
---

# Pyramid Deck Builder

Use this skill when the user wants a presentation built on their own PowerPoint template (.pptx or .potx), structured with the Minto Pyramid Principle, and delivered with speaker notes that give the presenter full context. It is designed for consulting work, including responses to customer RFPs where the customer has specific concerns that must be visibly addressed.

The output is always a .pptx file built on the user's template. Load the `pptx` skill's SKILL.md with the Skill tool before building or editing the file, and follow it for template handling, layouts and speaker notes.

## Inputs

The user may provide any of these, and the skill must adapt:

- Rough notes, a brief or a brain dump that needs structuring
- Existing documents (Word, PDF, reports, proposals, RFPs, RFP Q&A logs) to distil
- Just a topic, in which case research it (web search, connected sources) before drafting
- The template file (.pptx/.potx). If no template is attached, ask for it before building.

If any documentation or customer brief is provided, read it fully and extract the customer's stated concerns, requirements, evaluation criteria and pain points before asking the intake questions, so you can propose a list rather than asking from scratch.

## Step 1 — Intake questions (ask one at a time)

Ask these one by one, waiting for each answer. Skip any the user has already answered.

1. Who is the audience (e.g. client executives, technical stakeholders, procurement/evaluation panel, mixed)? Use the answer to set tone, depth and jargon level.
2. What decision, action or belief should the audience leave with? (This becomes the governing thought.)
3. **What specific customer concerns do we want to highlight?** If an RFP was provided, present the concerns you extracted (citing the RFP section where each came from) and ask the user to confirm, remove, add or prioritise them. For each confirmed concern, ask for anything the user knows beyond the documents: the root cause, the customer's past experience with it, our differentiator, proof points (case studies, metrics, certifications).
4. How long is the talk? Size the main deck at roughly 2 minutes per slide (e.g. 20 minutes → ~10 main slides). Supporting detail goes to an appendix.
5. What are the important points you specifically want to discuss or make sure are covered? Any sensitivities, politics in the room, competitors, or topics to avoid?
6. Anything else that must be included (specific data, case studies, logos, a mandated agenda or RFP response structure)?

## Step 2 — Analyse the template

If a powerpoint template is provided open the template and inventory its slide masters and layouts (title, section header, title+content, two-column/comparison, chart, table, quote, closing, etc.), placeholders, fonts and colour theme. Keep this inventory to map each slide to a layout later.

## Step 3 — Frame each customer concern

For every confirmed concern, write a concern block:

- **Concern**: in the customer's own terms (reference the RFP section if applicable).
- **Problem statement**: a crisp statement of the underlying problem and its business impact if left unsolved (cost, risk, time, compliance, customer experience). Make it specific and, where possible, quantified.
- **Solution**: how we address it — approach, architecture or service, and why it works.
- **Proof**: evidence that we can deliver (case study, metric, reference, certification, accelerator).
- **Outcome**: the measurable result for the customer.

These blocks feed the pyramid: each priority concern should map to a key line or a supporting point, never be left floating.

## Step 4 — Build the pyramid (full Minto structure)

- **SCQA opening**: Situation, Complication, Question, Answer. The Complication should reflect the customer's top concerns; the Answer is the governing thought.
- **Governing thought first**: the main recommendation/answer appears at the start (title or executive summary slide), not at the end.
- **Key lines**: 3–5 supporting arguments directly under the governing thought. Check they are MECE (mutually exclusive, collectively exhaustive) and that each answers the "why?" or "how?" raised by the level above. Organise key lines around the customer's concerns where that fits naturally.
- **Logical ordering** within each group: deductive (argument chain) or inductive (grouped like ideas), ordered by time, structure or importance (for RFPs, usually by the customer's priority or evaluation weighting) — state which.
- **Concern slides**: give each priority concern its own slide (or slide pair) showing Problem statement → Solution → Proof/Outcome. Lesser concerns can be grouped on a single "addressing your concerns" slide or in the appendix.
- **Concern traceability slide**: include a summary slide (or appendix table) mapping each customer concern / RFP reference → our solution → slide number.
- **Action titles**: every slide title is a full-sentence takeaway ("Consolidating to two regions cuts run cost by 30%"), never a topic label ("Cost"). Reading only the titles in order must tell the whole story.
- Map pyramid → slides: title / exec summary (governing thought + key lines), one section per key line including concern slides, concern traceability, recommendation and next steps, appendix.

## Checkpoint 1 — Storyline approval

Before building anything, present to the user:

- The SCQA and governing thought
- The concern blocks (concern, problem statement, solution, proof, outcome)
- The pyramid (governing thought → key lines → supporting points) as an indented outline, showing where each concern sits
- The ordered list of slide action titles, each with the template layout it will use and main/appendix placement
- How each of the user's "important points" from Step 1 is covered
- **Layout gaps**: any slide whose content doesn't fit an available template layout (e.g. no chart or comparison layout). List them and ask how the user wants each handled — do not invent layouts silently.

Run a MECE, concern-coverage and "titles-only read-through" check and mention any weaknesses (e.g. a concern with weak proof). Wait for approval or changes.

## Step 5 — Draft speaker notes

For every slide, write notes with three labelled sections:

**Context & why it matters** — where this slide sits in the pyramid (which key line it supports), which customer concern(s) and RFP references it addresses, the background the speaker needs, and the "so what" for this audience.

**Talk track** — what to actually say, in natural spoken language, sized to ~2 minutes; on concern slides, acknowledge the concern in the customer's words before presenting the problem statement and solution; include the transition into the next slide.

**Likely questions & answers** — 2–4 questions this audience is likely to ask about the slide, each with a concise suggested answer. On concern slides, include the toughest probing or objection-style questions an evaluator might ask. Flag any where the answer depends on information the user must confirm.

Keep notes in plain text so they render cleanly in PowerPoint's notes pane.

## Checkpoint 2 — Notes approval

Share the notes draft (slide title + the three sections per slide) and ask the user to confirm or adjust tone, depth and Q&A before building the file. Also ask if there are further points or concerns they want to discuss that the notes should prepare them for.

## Step 6 — Build the deck

Following the `pptx` skill:

- Build on the user's template, using its masters and layouts as mapped and approved; keep its fonts, colours and placeholders.
- Handle layout-gap slides exactly as the user decided at Checkpoint 1.
- Put the action title in each slide's title placeholder; keep body text lean (the detail lives in the notes).
- Present concern slides consistently (same Problem → Solution → Proof/Outcome structure each time).
- Add the approved speaker notes to every slide, including appendix slides.
- Add an appendix section for supporting detail and the concern traceability table if not in the main deck.

## Step 7 — Check before delivering

- Render slides to images and visually inspect for overflow, overlap and off-brand formatting.
- Read titles only, in order: the story must stand on its own.
- Confirm every confirmed customer concern has a problem statement and solution in the deck and appears in the traceability mapping.
- Confirm every slide has notes with all three sections.
- Confirm slide count matches the talk length (~2 min/slide) and that each "important point" is covered.

Deliver the .pptx with a one-line summary, and note any open items (e.g. concerns with weak proof, Q&A answers needing user confirmation).
Í
