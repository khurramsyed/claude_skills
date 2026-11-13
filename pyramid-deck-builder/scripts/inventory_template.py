#!/usr/bin/env python3
"""Inventory a PowerPoint template (.pptx or .potx) and optionally write a layout sampler.

Usage:
    python inventory_template.py template.potx                 # markdown report to stdout
    python inventory_template.py template.potx --sampler out/layout-sampler.pptx

The report lists slide size, theme fonts and colours, the master's default text sizes,
and every layout with its placeholders and its non-placeholder decoration (logos,
footer text, pictures). Layouts carrying decoration are flagged as BRANDED: those are
usually the ones to build content slides on.

The sampler is a deck with one slide per layout, each placeholder filled with its own
name, so the layouts can be rendered and looked at (python ../pptx/scripts/thumbnail.py
or soffice -> pdftoppm). The template itself is never modified.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_helpers import open_template, remove_all_slides  # noqa: E402
from lxml import etree  # noqa: E402
from pptx.util import Emu  # noqa: E402

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS = {"a": A, "p": P}


def inch(v):
    return f"{Emu(v).inches:.2f}" if v is not None else "?"


def theme_info(master):
    for rel in master.part.rels.values():
        if rel.reltype.endswith("/theme"):
            root = etree.fromstring(rel.target_part.blob)
            maj = root.find(".//a:majorFont/a:latin", NS)
            mnr = root.find(".//a:minorFont/a:latin", NS)
            colours = {}
            cs = root.find(".//a:clrScheme", NS)
            if cs is not None:
                for el in cs:
                    tag = etree.QName(el).localname
                    child = el[0] if len(el) else None
                    if child is not None:
                        colours[tag] = child.get("val") if child.get("val") not in (None, "windowText", "window") else child.get("lastClr")
            return (maj.get("typeface") if maj is not None else "?",
                    mnr.get("typeface") if mnr is not None else "?", colours)
    return "?", "?", {}


def master_sizes(master):
    out = {}
    tx = master._element.find("p:txStyles", NS)
    if tx is None:
        return out
    for style in ("titleStyle", "bodyStyle"):
        el = tx.find(f"p:{style}", NS)
        if el is None:
            continue
        sizes = []
        for lvl in range(1, 4):
            d = el.find(f"a:lvl{lvl}pPr/a:defRPr", NS)
            if d is not None and d.get("sz"):
                sizes.append(int(d.get("sz")) / 100)
        out[style] = sizes
    return out


def ph_size(ph):
    """Explicit font size set on a layout placeholder (first level), if any."""
    d = ph._element.find(".//a:lstStyle/a:lvl1pPr/a:defRPr", NS)
    if d is not None and d.get("sz"):
        return int(d.get("sz")) / 100
    d = ph._element.find(".//a:defRPr", NS)
    if d is not None and d.get("sz"):
        return int(d.get("sz")) / 100
    return None


def decoration(shapes):
    deco = []
    for sh in shapes:
        if sh.is_placeholder:
            continue
        kind = sh.shape_type
        txt = sh.text_frame.text.strip()[:40] if getattr(sh, "has_text_frame", False) and sh.has_text_frame else ""
        deco.append(f"{sh.name} ({kind}{', text: ' + repr(txt) if txt else ''}) at {inch(sh.left)},{inch(sh.top)} size {inch(sh.width)}x{inch(sh.height)}")
    return deco


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("template")
    ap.add_argument("--sampler", help="write a layout sampler .pptx here")
    args = ap.parse_args()

    prs = open_template(args.template)
    print(f"# Template inventory: {os.path.basename(args.template)}\n")
    print(f"Slide size: {inch(prs.slide_width)} x {inch(prs.slide_height)} in")
    print(f"Existing sample slides: {len(prs.slides)}\n")

    for mi, master in enumerate(prs.slide_masters):
        maj, mnr, colours = theme_info(master)
        print(f"## Master {mi}")
        print(f"Theme fonts: headings = {maj}, body = {mnr}")
        print("Theme colours: " + ", ".join(f"{k}={v}" for k, v in colours.items()))
        sz = master_sizes(master)
        if sz:
            print(f"Master default sizes (pt): title {sz.get('titleStyle')}, body levels 1-3 {sz.get('bodyStyle')}")
        md = decoration(master.shapes)
        if md:
            print("Master decoration (appears on every layout that shows master shapes):")
            for d in md:
                print(f"  - {d}")
        print()
        for li, layout in enumerate(master.slide_layouts):
            deco = decoration(layout.shapes)
            branded = bool(deco) or bool(md)
            print(f"### Layout {li}: \"{layout.name}\"{'  [BRANDED]' if deco else ''}")
            for ph in layout.placeholders:
                pf = ph.placeholder_format
                s = ph_size(ph)
                print(f"  - placeholder idx={pf.idx} type={pf.type} name='{ph.name}' at {inch(ph.left)},{inch(ph.top)} size {inch(ph.width)}x{inch(ph.height)}" + (f" font {s}pt" if s else ""))
            for d in deco:
                print(f"  - decoration: {d}")
            print()

    if args.sampler:
        prs2 = open_template(args.template)
        remove_all_slides(prs2)
        for master in prs2.slide_masters:
            for layout in master.slide_layouts:
                s = prs2.slides.add_slide(layout)
                for ph in s.placeholders:
                    if ph.has_text_frame:
                        label = f"[{layout.name}] {ph.name}" if ph.placeholder_format.type in (1, 3) else ph.name
                        ph.text_frame.text = label
        os.makedirs(os.path.dirname(os.path.abspath(args.sampler)), exist_ok=True)
        prs2.save(args.sampler)
        print(f"Layout sampler written: {args.sampler} ({len(prs2.slides)} slides, one per layout)")


if __name__ == "__main__":
    main()
