#!/usr/bin/env python3
"""Emit the HTML that Canva's importer turns into an editable step-and-repeat: one page div plus one <img> per mark.
usage: python3 make_canva_html.py <elements.json> <out.html> <raw base url> <bg png path> <evo png path> <emblem png path>"""
import json, sys
src, out, raw, bg, evo, emb = sys.argv[1:7]
d = json.load(open(src))
pw, ph = d['page_w'], d['page_h']
imgs = []
for e in d['elements']:
    url = f'{raw}/{evo if e["kind"] == "evo" else emb}'
    alt = 'Evolution Mortgage logo, gold' if e['kind'] == 'evo' else 'Army West Point shield, gold'
    imgs.append(f'<img src="{url}" alt="{alt}" style="position:absolute;left:{e["left"]}px;top:{e["top"]}px;width:{e["width"]}px;height:{e["height"]}px">')
html = (f'<!doctype html><html><head><meta charset="utf-8"><title>Evolution Mortgage x West Point – Step and Repeat {d["W"]/12:g}x{d["H"]/12:g} ft (editable)</title></head>'
        f'<body style="margin:0"><div data-document-role="page" data-label="{d["W"]/12:g}x{d["H"]/12:g} ft black" style="position:relative;width:{pw}px;height:{ph}px;overflow:hidden;background:#0A0A0A">'
        f'<img src="{raw}/{bg}" alt="Black field with centre glow" style="position:absolute;left:0;top:0;width:{pw}px;height:{ph}px">'
        + ''.join(imgs) + '</div></body></html>')
open(out, 'w').write(html)
print(f'{out}: page {pw}x{ph} px, {len(imgs)} marks')
