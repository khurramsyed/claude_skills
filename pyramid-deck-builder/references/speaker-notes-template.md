# Speaker notes template

Use this for Step 5. Notes are plain text (no markdown symbols, since PowerPoint shows them
raw), with exactly these three labelled sections on every slide, appendix included. The
labels are what the presenter scans for while talking, so keep them identical everywhere.

```
Context & why it matters:
<2-5 sentences: where this slide sits in the pyramid (which key line it supports), which
concerns / RFP refs it addresses, background the presenter needs, and the "so what" for
this audience.>

Talk track:
<~200-280 words of natural spoken English, roughly 2 minutes. On a concern slide, open by
naming the concern in the customer's own words before offering anything. Short sentences.
No bullet fragments. End with a one-line transition into the next slide's title.>

Likely questions & answers:
Q: <question in the evaluator's voice>
A: <concise answer, 1-3 sentences>
Q: ...
A: ...
```

## Guidance

**Context** is for the presenter, not the audience: it says why this slide exists. Mention the
RFP refs and the concern by name so the presenter can map a panel question to this slide.

**Talk track** is spoken, so write how people talk: "You told us staff weren't ready last time.
That's exactly where we'd start." not "Readiness concerns are addressed via a phased training model."
Aim for the slide's ~2 minutes; cover slides, dividers and the appendix can be shorter
(30-60 seconds for a divider; appendix notes are backup, so make them a short briefing
the presenter can use if a question takes them there).

**Likely questions** has 2-4 Q&As. On concern slides include the toughest objection an
evaluator would raise (cost, risk, "what if the outgoing supplier won't cooperate?", "how is this
different from what we have now?"). Answers are short and honest; where the answer
depends on facts the user hasn't confirmed, write the best answer and mark it [CONFIRM].

**Sensitivities** from intake apply to notes as much as slides: if the user said not to name
the incumbent, the notes say "the outgoing supplier"; if tool names are banned from notes,
describe the capability ("automated discovery tooling").

## Example (concern slide)

```
Context & why it matters:
Supports key line 1 (prove staff readiness before moving callers). Addresses REQ-07 and the
§2.4 concern that the last channel change was rolled back. The panel's Head of Customer
Services lived through that rollback, so this slide earns credibility on the 35% "delivery
risk" criterion.

Talk track:
You told us that last winter one in four callers hung up before reaching anyone, and that the
last time the channels changed it was rolled back after six weeks because staff weren't
ready. We think readiness is the single biggest risk here, so that's where we start. Every
team goes live in a pilot first, handling a small share of real calls on the new platform
while the old one carries the rest... [continues ~2 min] ...Which brings us to how we decide
when a team is ready to take all of its calls.

Likely questions & answers:
Q: A pilot per team sounds slow. How long does the whole cutover take?
A: Pilots overlap, so the full cutover runs in four waves over about five months. [CONFIRM: wave plan]
Q: What if a pilot fails?
A: That team stays on the old platform, which keeps running until the last wave exits, so a
failed pilot costs time, not service.
```
