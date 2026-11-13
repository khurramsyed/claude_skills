# Minto Pyramid & SCQA cheat sheet

Read this while building the storyline (Step 4). It is the reasoning behind the shape, so
you can apply it to material that doesn't fit the examples.

## Contents

1. The pyramid in one picture
2. SCQA opening
3. Governing thought
4. Key lines, MECE and ordering logic
5. Action titles
6. Concern and assumption blocks
7. Traceability table
8. Common failure modes

## 1. The pyramid in one picture

```
                 Governing thought (the answer, slide 1-2)
          ┌─────────────────┼─────────────────┐
      Key line 1        Key line 2        Key line 3      ← each answers "why?" or "how?"
     ┌────┴────┐       ┌────┴────┐       ┌────┴────┐        of the governing thought
   slide     slide   slide     slide   slide     slide   ← each slide supports its key line
```

Read top-down, every level answers the question the level above raises in the listener's
head. Read bottom-up, each group of slides summarises into the line above it. If a slide
cannot say which key line it supports, it belongs in the appendix or nowhere.

## 2. SCQA opening

| Part         | What it is                                                                             | Test                                           |
| ------------ | -------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Situation    | Facts the audience already accepts. No news.                                           | Would they nod?                                |
| Complication | What changed or what is at risk. For RFPs: the customer's top concerns, in their words | Does it create tension that demands an answer? |
| Question     | The question the complication raises (often implicit)                                  | Is there exactly one obvious question?         |
| Answer       | The governing thought                                                                  | Does it answer that question directly?         |

Example (RFP orals for a housing association's contact-centre replacement): S: "Tenants
contact you 600,000 times a year, mostly by phone." C: "Call abandonment hit 28% last winter
and the last channel change was rolled back after six weeks because staff weren't ready."
Q: "How do we change platforms without repeating that?" A: "Move staff before tenants: a
pilot-led cutover where every team is proven on the new platform before its callers move."

## 3. Governing thought

One sentence, a claim not a topic, that the audience could act on or disagree with. It comes
from the intake answer to "what should they leave with?". Put it on slide 1 (subtitle or
title) or slide 2 (the executive summary title). Weak: "Our implementation approach". Strong:
"A pilot-led cutover removes the readiness risk that forced last year's rollback".

## 4. Key lines, MECE and ordering logic

3-5 key lines. Each is itself a sentence. Together they must be:

- **Mutually exclusive**: no two key lines claim the same ground (if a slide could sit under
  two, the split is wrong).
- **Collectively exhaustive**: together they are sufficient to believe the governing
  thought; a sceptical evaluator should not be able to say "but what about X?" where X is a
  top concern.

State the ordering logic explicitly in the storyline, because it is what makes the deck
feel inevitable:

- **Time** (phase 1 → 2 → 3): plans, transitions, roadmaps.
- **Structure** (component by component): architectures, org designs.
- **Importance** (biggest first): recommendations, cost levers.
- **RFP weighting**: evaluation criteria by weight, so the panel sees its biggest-scoring
  questions answered first.

## 5. Action titles

Every title is a full sentence carrying the slide's single message, so that reading the
titles alone tells the whole story. Aim for under ~90 characters so it fits on one line in
the template's title placeholder (check the actual width and size; a 28pt title on a 12"
placeholder fits roughly 70-80 characters).

| Topic label (don't)     | Action title (do)                                                          |
| ----------------------- | -------------------------------------------------------------------------- |
| Implementation approach | Each team goes live in a pilot before any of its callers move              |
| Cost breakdown          | Overtime to cover abandonment drives a third of contact-centre cost        |
| Risks                   | Cutting over before training completes would repeat last winter's rollback |
| Team                    | A team that has run four social-housing cutovers leads delivery            |

Titles-only test: list the titles in order and read them aloud. If the story jumps, a slide
is missing; if two titles say the same thing, merge them; if one does not follow from its
key line, move it.

## 6. Concern and assumption blocks

**Concern block** (one per confirmed customer concern):

| Field             | Content                                                                                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Concern           | In the customer's own words, with the RFP reference (e.g. "staff weren't ready" – §2.4, REQ-07)                                                                                                        |
| Problem statement | The specific business impact: cost, risk, time, compliance or customer experience. Quantify only where the source supports it ("28% abandonment", "rolled back after six weeks"); never invent numbers |
| Solution          | What we will do, concretely                                                                                                                                                                            |
| Proof             | Case study, metric, certification, method; mark [CONFIRM] if the user must supply it                                                                                                                   |
| Outcome           | What the customer gets, in their terms                                                                                                                                                                 |

Priority concerns get their own slide laid out Problem → Solution → Proof/Outcome. Lesser
ones are grouped on one slide or moved to the appendix.

**Assumption block**: one sentence ("We assume the association will release 20 agents
per week for training from month 2") plus the slides that depend on it. Assumptions go on a dedicated
slide near the end of the main deck, so the panel sees them stated plainly rather than
buried.

## 7. Traceability table

A table on its own slide (main deck if the audience is an evaluation panel, otherwise
appendix): `Ref | Concern / requirement / assumption | How we address it | Slide`. Every
confirmed concern and assumption appears exactly once. Evaluators use it to score; the
presenter uses it to answer "where do you cover X?".

## 8. Common failure modes

- Governing thought arrives on slide 9 after the methodology. Move it to slide 1-2.
- Key lines that are topics ("People, Process, Technology") rather than claims.
- A "Why us" slide that does not connect to any concern. Tie each differentiator to a concern.
- Concerns paraphrased into vendor language; the panel wants to hear its own words first.
- Numbers on slides that the source never gave. Use the source's numbers or none.
- Every slide on the same layout with a bullet wall. One message, one visual.
