#!/usr/bin/env python3
"""Fabric pop-up straight display, 10 x 8 ft, on the printer's template (147.51 x 89.51 in file: 2 in bleed left/right,
12.96 in end caps, 117.60 x 89.50 in visible front). Diamond step-and-repeat on the front face only, every mark whole
and inside the front safe area; the end caps and bleed carry only the black field ("nothing on the sides"). Inches.
usage: python3 make_popup.py [pitch in=23] [canva px per in=42]"""
import sys, os, json
from make_flag import LOGO_W, LOGO_H, ARMY_GOLD, INK_BLACK, WHITE, INT_SB, html_wrap
from make_backdrop import evo_markup, emblem_markup

TOTAL_W, TOTAL_H = 147.51, 89.51
BLEED, CAP, FRONT_W, FRONT_H = 2.0, 12.96, 117.60, 89.50
SAFE_W, SAFE_H = 103.64, 75.52
CAP_SAFE_W, CAP_SAFE_H = 6.98, 75.54
FX, FY = (TOTAL_W - FRONT_W) / 2, (TOTAL_H - FRONT_H) / 2     # front's top-left corner in file coordinates
EMBLEM = 'brand/army-west-point-gold.svg'
EMB_VB = (1902.0, 2214.0)

def lattice(pitch):
    """Diamond lattice centred on the front: lockup rows on the half-step, shield rows on the step, rows pitch/2 apart.
    Keeps only marks that sit entirely inside the front safe area. Returns marks in front coordinates (inches)."""
    k = pitch / 36.0
    evo_w, emb_box = 25.0 * k, 12.5 * k
    evo_h = evo_w * LOGO_H / LOGO_W
    emb_w = emb_box * EMB_VB[0] / EMB_VB[1]
    px, py = pitch, pitch / 2
    cx, cy = FRONT_W / 2, FRONT_H / 2
    sx0, sy0 = (FRONT_W - SAFE_W) / 2, (FRONT_H - SAFE_H) / 2
    sx1, sy1 = sx0 + SAFE_W, sy0 + SAFE_H
    marks = []
    for j in range(-8, 9):                      # row offset from the centre row
        y = cy + j * py
        if j % 2:                               # odd rows: lockups on the half-step
            cands = [('evo', cx + (i + 0.5) * px, evo_w, evo_h) for i in range(-6, 6)]
        else:                                   # even rows (incl. centre): shields on the step
            cands = [('emb', cx + i * px, emb_w, emb_box) for i in range(-6, 7)]
        for kind, x, w, h in cands:
            if x - w/2 >= sx0 and x + w/2 <= sx1 and y - h/2 >= sy0 and y + h/2 <= sy1:
                marks.append(dict(kind=kind, cx=x, cy=y, w=w, h=h))
    return marks, evo_w, emb_box

def build(pitch=23.0, guides=False, marks_on=True):
    marks, evo_w, emb_box = lattice(pitch)
    o = [f'<rect x="0" y="0" width="{TOTAL_W}" height="{TOTAL_H}" fill="url(#glow)"/>']
    defs = [f'<g id="evo">{evo_markup(evo_w, True, ARMY_GOLD)}</g>',
            f'<g id="emb">{emblem_markup(EMBLEM, emb_box, WHITE, True)}</g>']
    if marks_on:
        for m in marks:
            o.append(f'<use href="#{m["kind"]}" x="{FX + m["cx"]:.3f}" y="{FY + m["cy"]:.3f}"/>')
    if guides:
        R, G, B = '#FF3B7A', '#3BB273', '#9AA8BF'
        for x in (0, TOTAL_W - BLEED):
            o.append(f'<rect x="{x}" y="0" width="{BLEED}" height="{TOTAL_H}" fill="{R}" opacity="0.35"/>')
        for x, lab in ((BLEED, 'LEFT SIDE'), (TOTAL_W - BLEED - CAP, 'RIGHT SIDE')):
            o.append(f'<rect x="{x}" y="0" width="{CAP}" height="{TOTAL_H}" fill="{B}" opacity="0.28"/>')
            o.append(f'<rect x="{x + (CAP-CAP_SAFE_W)/2}" y="{(TOTAL_H-CAP_SAFE_H)/2}" width="{CAP_SAFE_W}" height="{CAP_SAFE_H}" fill="none" stroke="{B}" stroke-width="0.12" stroke-dasharray="0.8 0.5"/>')
            for i, word in enumerate([lab, 'END CAP', 'BLANK']):
                p, _ = INT_SB.path(word, 1.6, x + CAP/2, 30 + i*2.6, align='center'); o.append(f'<path d="{p}" fill="{WHITE}"/>')
        o.append(f'<rect x="{FX}" y="{FY}" width="{FRONT_W}" height="{FRONT_H}" fill="none" stroke="{R}" stroke-width="0.14" stroke-dasharray="1 0.6"/>')
        o.append(f'<rect x="{FX + (FRONT_W-SAFE_W)/2}" y="{FY + (FRONT_H-SAFE_H)/2}" width="{SAFE_W}" height="{SAFE_H}" fill="none" stroke="{G}" stroke-width="0.14" stroke-dasharray="1 0.6"/>')
        for i, (txt, col) in enumerate([(f'FILE {TOTAL_W} x {TOTAL_H} in  =  2 in BLEED + 12.96 in END CAP + 117.60 x 89.50 in FRONT + END CAP + BLEED', R),
                                        (f'GREEN: FRONT SAFE AREA {SAFE_W} x {SAFE_H} in  -  every logo and shield sits inside it', G),
                                        ('END CAPS AND BLEED: BLACK FIELD ONLY, NO ARTWORK', B)]):
            p, _ = INT_SB.path(txt, 1.1, FX + 1.2, FY + 2.0 + i*1.7); o.append(f'<path d="{p}" fill="{col}"/>')
    d = (f'<defs><radialGradient id="glow" cx="0.5" cy="0.45" r="0.75"><stop offset="0" stop-color="#262626"/><stop offset="1" stop-color="{INK_BLACK}"/></radialGradient>'
         f'{"".join(defs)}</defs>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{TOTAL_W}in" height="{TOTAL_H}in" viewBox="0 0 {TOTAL_W} {TOTAL_H}">'
           f'<title>Evolution Mortgage x West Point fabric pop-up 10x8 ft, front-only step-and-repeat</title>{d}{"".join(o)}</svg>')
    return svg, marks, evo_w, emb_box

if __name__ == '__main__':
    pitch = float(sys.argv[1]) if len(sys.argv) > 1 else 23.0
    ppi = float(sys.argv[2]) if len(sys.argv) > 2 else 42.0
    os.makedirs('build/popup', exist_ok=True)
    for name, guides, marks_on in (('popup_10x8_black', False, True), ('popup_10x8_black_proof', True, True), ('popup_10x8_black_background', False, False)):
        svg, marks, evo_w, emb_box = build(pitch, guides, marks_on)
        open(f'build/popup/{name}.svg', 'w').write(svg)
        open(f'build/popup/{name}.html', 'w').write(html_wrap(svg, TOTAL_W, TOTAL_H))
        prev = svg.replace(f'width="{TOTAL_W}in" height="{TOTAL_H}in"', f'width="{round(TOTAL_W*10)}" height="{round(TOTAL_H*10)}"', 1)
        open(f'build/popup/{name}_preview.html', 'w').write(html_wrap(prev, TOTAL_W, TOTAL_H))
    # Canva element sheet (same schema as canva_backdrop.py), file coordinates, ppi px per inch
    pw, ph = round(TOTAL_W * ppi), round(TOTAL_H * ppi)
    els = [dict(kind=m['kind'], cx=FX + m['cx'], cy=FY + m['cy'], w_in=m['w'], h_in=m['h'],
                left=round((FX + m['cx'] - m['w']/2) * ppi, 2), top=round((FY + m['cy'] - m['h']/2) * ppi, 2),
                width=round(m['w'] * ppi, 2), height=round(m['h'] * ppi, 2)) for m in marks]
    json.dump(dict(W=TOTAL_W, H=TOTAL_H, ppi=ppi, page_w=pw, page_h=ph, pitch=pitch,
                   title='Evolution Mortgage x West Point – Fabric Pop Up 10x8 ft, front only (editable)', label='10x8 ft pop-up, blank sides',
                   background='popup-10x8ft-black-background.png', elements=els), open('build/popup/elements.json', 'w'), indent=1)
    n_evo = sum(m['kind'] == 'evo' for m in marks)
    print(f'pitch {pitch} in: {n_evo} lockups ({evo_w:.2f} in wide) + {len(marks)-n_evo} shields ({emb_box:.2f} in tall) = {len(marks)} marks; canva page {pw}x{ph} px @ {ppi:g} ppi')
    xs = sorted(set(round(m['cx'], 2) for m in marks if m['kind']=='evo')); ys = sorted(set(round(m['cy'], 2) for m in marks))
    print('lockup columns (front in):', xs); print('shield columns:', sorted(set(round(m['cx'],2) for m in marks if m['kind']=='emb'))); print('rows:', ys)
    ext_x0 = min(m['cx']-m['w']/2 for m in marks); ext_x1 = max(m['cx']+m['w']/2 for m in marks); ext_y0 = min(m['cy']-m['h']/2 for m in marks); ext_y1 = max(m['cy']+m['h']/2 for m in marks)
    print(f'art extent on front: x {ext_x0:.2f}..{ext_x1:.2f} (safe {(FRONT_W-SAFE_W)/2:.2f}..{(FRONT_W+SAFE_W)/2:.2f}), y {ext_y0:.2f}..{ext_y1:.2f} (safe {(FRONT_H-SAFE_H)/2:.2f}..{(FRONT_H+SAFE_H)/2:.2f})')
