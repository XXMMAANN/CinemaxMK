#!/usr/bin/env python3
"""Fabric pop-up straight display, 10 x 8 ft: diamond step-and-repeat on the front face only, every mark whole and
inside the front safe area; end caps and bleed carry only the black field ("nothing on the sides"). Inches.

Two layouts ("specs"):
  template  the printer's downloadable template: 147.51 x 89.51 in = 2 in bleed + 12.96 in end cap + 117.60 x 89.50 in
            front + end cap + bleed; front safe area 103.64 x 75.52 in.
  canvas    the printer's online design tool: 144 x 90 in canvas, fold lines 13 in from each edge (118 in front),
            front safe area 104 x 76 in, no separate bleed.
usage: python3 make_popup.py [pitch in=23] [canva px per in=42] [spec=template|canvas]
       python3 make_popup.py front [W=120] [H=96] [inset=8] [pitch=24]   (plain front-only image at the nominal size)"""
import sys, os, json
from make_flag import LOGO_W, LOGO_H, ARMY_GOLD, INK_BLACK, WHITE, INT_SB, html_wrap
from make_backdrop import evo_markup, emblem_markup

SPECS = {
    'template': dict(total_w=147.51, total_h=89.51, bleed=2.0, cap=12.96, front_w=117.60, front_h=89.50, safe_w=103.64, safe_h=75.52, cap_safe_w=6.98, cap_safe_h=75.54),
    'canvas':   dict(total_w=144.0, total_h=90.0, bleed=0.0, cap=13.0, front_w=118.0, front_h=90.0, safe_w=104.0, safe_h=76.0, cap_safe_w=7.0, cap_safe_h=76.0),
}
EMBLEM = 'brand/army-west-point-gold.svg'
EMB_VB = (1902.0, 2214.0)

def sizes(pitch):
    k = pitch / 36.0
    evo_w, emb_box = 25.0 * k, 12.5 * k
    return evo_w, evo_w * LOGO_H / LOGO_W, emb_box * EMB_VB[0] / EMB_VB[1], emb_box

def lattice(pitch, box_w, box_h, safe):
    """Diamond lattice centred on a box_w x box_h face: lockup rows on the half-step, shield rows on the step, rows
    pitch/2 apart. Keeps only marks entirely inside `safe` = (x0, y0, x1, y1) in face coordinates."""
    evo_w, evo_h, emb_w, emb_h = sizes(pitch)
    px, py = pitch, pitch / 2
    cx, cy = box_w / 2, box_h / 2
    x0, y0, x1, y1 = safe
    marks = []
    for j in range(-8, 9):
        y = cy + j * py
        cands = ([('evo', cx + (i + 0.5) * px, evo_w, evo_h) for i in range(-6, 6)] if j % 2
                 else [('emb', cx + i * px, emb_w, emb_h) for i in range(-6, 7)])
        for kind, x, w, h in cands:
            if x - w/2 >= x0 and x + w/2 <= x1 and y - h/2 >= y0 and y + h/2 <= y1:
                marks.append(dict(kind=kind, cx=x, cy=y, w=w, h=h))
    return marks

def svg_doc(W, H, marks, evo_w, emb_box, extra='', title=''):
    defs = [f'<g id="evo">{evo_markup(evo_w, True, ARMY_GOLD)}</g>', f'<g id="emb">{emblem_markup(EMBLEM, emb_box, WHITE, True)}</g>']
    o = [f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#glow)"/>'] + [f'<use href="#{m["kind"]}" x="{m["cx"]:.3f}" y="{m["cy"]:.3f}"/>' for m in marks] + [extra]
    d = (f'<defs><radialGradient id="glow" cx="0.5" cy="0.45" r="0.75"><stop offset="0" stop-color="#262626"/><stop offset="1" stop-color="{INK_BLACK}"/></radialGradient>{"".join(defs)}</defs>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}in" height="{H}in" viewBox="0 0 {W} {H}">'
            f'<title>{title}</title>{d}{"".join(o)}</svg>')

def build(pitch=23.0, guides=False, marks_on=True, spec='template'):
    s = SPECS[spec]
    TW, TH, BLEED, CAP, FW, FH = s['total_w'], s['total_h'], s['bleed'], s['cap'], s['front_w'], s['front_h']
    FX, FY = (TW - FW) / 2, (TH - FH) / 2                      # front's top-left corner in file coordinates
    sx0, sy0 = (FW - s['safe_w']) / 2, (FH - s['safe_h']) / 2
    marks = lattice(pitch, FW, FH, (sx0, sy0, sx0 + s['safe_w'], sy0 + s['safe_h']))
    placed = [dict(m, cx=FX + m['cx'], cy=FY + m['cy']) for m in marks] if marks_on else []
    evo_w, _, _, emb_box = sizes(pitch)
    g = []
    if guides:
        R, G, B = '#FF3B7A', '#3BB273', '#9AA8BF'
        if BLEED:
            for x in (0, TW - BLEED):
                g.append(f'<rect x="{x}" y="0" width="{BLEED}" height="{TH}" fill="{R}" opacity="0.35"/>')
        for x, lab in ((BLEED, 'LEFT SIDE'), (TW - BLEED - CAP, 'RIGHT SIDE')):
            g.append(f'<rect x="{x}" y="0" width="{CAP}" height="{TH}" fill="{B}" opacity="0.28"/>')
            g.append(f'<rect x="{x + (CAP-s["cap_safe_w"])/2}" y="{(TH-s["cap_safe_h"])/2}" width="{s["cap_safe_w"]}" height="{s["cap_safe_h"]}" fill="none" stroke="{B}" stroke-width="0.12" stroke-dasharray="0.8 0.5"/>')
            for i, word in enumerate([lab, 'END CAP', 'BLANK']):
                p, _ = INT_SB.path(word, 1.6, x + CAP/2, 30 + i*2.6, align='center'); g.append(f'<path d="{p}" fill="{WHITE}"/>')
        g.append(f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" fill="none" stroke="{R}" stroke-width="0.14" stroke-dasharray="1 0.6"/>')
        g.append(f'<rect x="{FX + sx0}" y="{FY + sy0}" width="{s["safe_w"]}" height="{s["safe_h"]}" fill="none" stroke="{G}" stroke-width="0.14" stroke-dasharray="1 0.6"/>')
        lines = [(f'FILE {TW:g} x {TH:g} in  =  ' + (f'{BLEED:g} in BLEED + ' if BLEED else '') + f'{CAP:g} in END CAP + {FW:g} x {FH:g} in FRONT + END CAP' + (' + BLEED' if BLEED else ''), R),
                 (f'GREEN: FRONT SAFE AREA {s["safe_w"]:g} x {s["safe_h"]:g} in  -  every logo and shield sits inside it', G),
                 ('END CAPS' + (' AND BLEED' if BLEED else '') + ': BLACK FIELD ONLY, NO ARTWORK', B)]
        for i, (txt, col) in enumerate(lines):
            p, _ = INT_SB.path(txt, 1.1, FX + 1.2, FY + 2.0 + i*1.7); g.append(f'<path d="{p}" fill="{col}"/>')
    svg = svg_doc(TW, TH, placed, evo_w, emb_box, ''.join(g), f'Evolution Mortgage x West Point fabric pop-up 10x8 ft ({spec}), front-only step-and-repeat')
    return svg, placed, marks, evo_w, emb_box, s

def build_front(W=120.0, H=96.0, inset=8.0, pitch=24.0):
    """Plain front-only image at the nominal display size (default 10 x 8 ft, exact 5:4), marks inside the box inset
    by `inset` inches. For a tool whose canvas is the bare front rather than the template."""
    marks = lattice(pitch, W, H, (inset, inset, W - inset, H - inset))
    evo_w, _, _, emb_box = sizes(pitch)
    return svg_doc(W, H, marks, evo_w, emb_box, '', f'Evolution Mortgage x West Point pop-up front, {W:g} x {H:g} in'), marks

def report(marks, evo_w, emb_box, W, H, safe):
    n = sum(m['kind'] == 'evo' for m in marks)
    ext = (min(m['cx']-m['w']/2 for m in marks), max(m['cx']+m['w']/2 for m in marks), min(m['cy']-m['h']/2 for m in marks), max(m['cy']+m['h']/2 for m in marks))
    print(f'{n} lockups ({evo_w:.2f} in wide) + {len(marks)-n} shields ({emb_box:.2f} in tall) on a {W:g} x {H:g} in face; art extent x {ext[0]:.1f}..{ext[1]:.1f}, y {ext[2]:.1f}..{ext[3]:.1f}; safe box {safe}')

if __name__ == '__main__':
    os.makedirs('build/popup', exist_ok=True)
    if len(sys.argv) > 1 and sys.argv[1] == 'front':
        W, H, inset, pitch = (float(a) for a in (sys.argv[2:6] + ['120', '96', '8', '24'][len(sys.argv) - 2:]))
        svg, marks = build_front(W, H, inset, pitch)
        open(f'build/popup/front_{W:g}x{H:g}.svg', 'w').write(svg)
        report(marks, *sizes(pitch)[::3], W, H, (inset, inset, W - inset, H - inset)); sys.exit(0)
    pitch = float(sys.argv[1]) if len(sys.argv) > 1 else 23.0
    ppi = float(sys.argv[2]) if len(sys.argv) > 2 else 42.0
    spec = sys.argv[3] if len(sys.argv) > 3 else 'template'
    s = SPECS[spec]; TW, TH = s['total_w'], s['total_h']
    for name, guides, marks_on in ((f'popup_{spec}', False, True), (f'popup_{spec}_proof', True, True), (f'popup_{spec}_background', False, False)):
        svg, placed, marks, evo_w, emb_box, _ = build(pitch, guides, marks_on, spec)
        open(f'build/popup/{name}.svg', 'w').write(svg)
        open(f'build/popup/{name}.html', 'w').write(html_wrap(svg, TW, TH))
        prev = svg.replace(f'width="{TW}in" height="{TH}in"', f'width="{round(TW*10)}" height="{round(TH*10)}"', 1)
        open(f'build/popup/{name}_preview.html', 'w').write(html_wrap(prev, TW, TH))
    svg, placed, marks, evo_w, emb_box, _ = build(pitch, False, True, spec)
    pw, ph = round(TW * ppi), round(TH * ppi)
    els = [dict(kind=m['kind'], cx=m['cx'], cy=m['cy'], w_in=m['w'], h_in=m['h'], left=round((m['cx'] - m['w']/2) * ppi, 2), top=round((m['cy'] - m['h']/2) * ppi, 2),
                width=round(m['w'] * ppi, 2), height=round(m['h'] * ppi, 2)) for m in placed]
    json.dump(dict(W=TW, H=TH, ppi=ppi, page_w=pw, page_h=ph, pitch=pitch, spec=spec,
                   title=f'Evolution Mortgage x West Point – Fabric Pop Up 10x8 ft, front only ({spec}, editable)', label='10x8 ft pop-up, blank sides',
                   elements=els), open(f'build/popup/elements_{spec}.json', 'w'), indent=1)
    print(f'spec {spec}: file {TW:g} x {TH:g} in, pitch {pitch:g}; canva page {pw}x{ph} px @ {ppi:g} ppi')
    report(marks, evo_w, emb_box, s['front_w'], s['front_h'], ((s['front_w']-s['safe_w'])/2, (s['front_h']-s['safe_h'])/2, (s['front_w']+s['safe_w'])/2, (s['front_h']+s['safe_h'])/2))
