# Building the deck on the user's template

Read this at Step 2 (template analysis) and Step 6 (build). The pptx skill's SKILL.md is
still the authority for validation, rendering and visual QA; this file covers what is
specific to building a *new* deck *on a supplied template* with the bundled helpers.

## Why python-pptx on the template itself

The deliverable must look like the user's firm made it: their masters, layouts, theme
fonts and colours, logo and footer. The most reliable way to keep all of that is to open
the template, delete its sample slides, and add new slides from its own layouts. Building
from scratch with pptxgenjs and imitating the look loses the real masters, so the user
can't restyle or re-layout the deck in PowerPoint. Use pptxgenjs only if the user has no
template and explicitly accepts a from-scratch design.

## Step 2: analyse the template

```bash
SKILL=<this skill's directory>
PPTX=<pptx skill's directory>
python $SKILL/scripts/inventory_template.py template.potx --sampler work/layout-sampler.pptx > work/template-inventory.md
python $PPTX/scripts/thumbnail.py work/layout-sampler.pptx work/layout-thumbs
```

The inventory gives slide size, theme fonts/colours, the master's default title and body
sizes, and each layout's placeholders and decoration. Layouts flagged `[BRANDED]` carry a
logo/footer: default to these for content slides. Look at the thumbnail grid too, because
names lie (a layout called "Content" may be a dark section style).

Record in the storyline: which layout is the default content layout, which is the cover,
which is the section divider, and the template's body size (the floor for body text).

## Mapping slides to layouts, and layout gaps

Map each storyline slide to a layout by what it needs:

| Slide need | Usual layout |
|---|---|
| Cover | Title/cover layout |
| Section break, "Appendix" divider | Section header layout (or a branded title-only slide with a large title, if none) |
| Single visual (flow, table, chart, 2x2, plan on a page) | Branded *title only* layout + native shapes/table/chart composed on top |
| Text + supporting visual | Branded two-content or content layout |
| Before/after, option comparison | Comparison layout, or title-only + two columns of shapes |

A **layout gap** is content no layout serves well: e.g. a plan-on-a-page needs the full
width but every branded layout reserves a sidebar; a cover needs a client logo slot that
doesn't exist; no section divider exists. List gaps at Checkpoint 1 with options (compose on
the title-only layout; use an unbranded layout; simplify the content; split the slide) and
let the user choose. Don't add new layouts to their template silently: it is their brand
asset, and an invented layout won't match their guidelines.

## Step 6: build

```python
import sys; sys.path.insert(0, "<this skill's directory>/scripts")
from deck_helpers import *

prs = open_template("template.potx")       # works for .potx and .pptx; the file is not modified
remove_all_slides(prs)                       # the template's sample slides go
W, H = slide_size_in(prs)
ACC = theme_rgb(prs, "accent1"); DK = theme_rgb(prs, "dk2"); LT = theme_rgb(prs, "lt2")

s = add_slide(prs, "Title Only - Branded")
set_title(s, "A 12-week discovery maps every dependency before anything moves")
# compose native visuals inside the free area under the title and above the footer
add_box(s, 0.7, 1.9, 3.6, 1.4, "Weeks 1-4\nAutomated scan", fill=LT, size=16, bold=True)
add_arrow(s, 4.4, 2.4, 0.5, 0.4, fill=ACC)
...
set_notes(s, context="...", talk_track="...", qa=[("...", "..."), ("...", "...")])
remove_empty_placeholders(s)                 # no "Click to add text" leftovers
save(prs, "out/<Client>-<topic>-deck.pptx")  # always a new file, never the template path
```

Helper notes:
- `set_title` and `set_bullets` fill placeholders without hard-coding fonts, so the
  template's typography wins. Don't set a font face anywhere; set sizes only where a
  composed shape needs one, and never below the template's body size (usually 14-18pt;
  12pt is acceptable only inside dense tables, captions and the traceability table).
- `add_box`, `add_arrow`, `add_table` create native, editable shapes in theme colours
  read with `theme_rgb`. Use them instead of bullet walls: process flows (boxes +
  arrows), problem → solution → outcome rows, 2x2s, timelines, plan-on-a-page grids
  (workstreams as rows, phases as columns, gates as diamonds `MSO_SHAPE.DIAMOND`).
- For charts use python-pptx `slide.shapes.add_chart(...)` with `CategoryChartData`,
  native and editable, never an image.
- Keep composed content inside the safe area: below the title placeholder's bottom edge
  and above the footer/logo (read their positions from the inventory). Overlapping the
  footer is the most common defect on templates.
- Footers and slide numbers come from the layout. Don't draw your own.

## Title fit

Action titles are long by design. Estimate fit before building: at the template's title
size, a placeholder fits roughly `width_in * 72 / (size_pt * 0.55)` characters per line
(e.g. 12" at 28pt in a bold serif ≈ 55 chars; the ~90-character aim in SKILL.md only holds
for ~20pt titles on a wide placeholder). Compute this number once in Step 2, record it in
the storyline as the title budget, and write every title to it. If titles routinely exceed one line,
shorten the titles first; if they still don't fit, ask at Checkpoint 1 whether to reduce
the title size on the slides (a deviation from the template, so it's the user's call).

## Render and check

Follow the pptx skill's Converting to Images and Visual QA sections: convert to PDF with its
`scripts/office/soffice.py`, rasterise with `pdftoppm`, and look at every slide. Run its
`validate.py out.pptx --original template.pptx` (copy a .potx to a .pptx name first for the
`--original` baseline). Then run this skill's checker:

```bash
python $SKILL/scripts/check_deck.py out.pptx --template template.potx --talk-minutes 30 --max-title-chars <title budget> \
    --banned "IncumbentName" --banned-slides-only "ToolA,ToolB" --json work/check.json
```

It prints the titles-only read-through, per-slide notes completeness, banned-term hits,
main/appendix split vs talk length, and whether a traceability table exists. Fix every
problem it lists, re-render the slides you changed, and re-run it until it is clean.
