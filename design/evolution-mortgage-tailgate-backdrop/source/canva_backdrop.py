#!/usr/bin/env python3
"""Editable Canva step-and-repeat: same diamond lattice as make_backdrop.py, but emitted as one Canva
element per mark (plus a glow background image), so every logo can be moved or swapped in the editor.
usage: python3 canva_backdrop.py <W in> <H in> <ppi> [pitch in]  -> writes build/canva_<W>x<H>/{background.html, elements.json}"""
import sys, os, json, math, re
from make_flag import LOGO_W, LOGO_H, INK_BLACK

W, H, PPI = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
PITCH = float(sys.argv[4]) if len(sys.argv) > 4 else 24.0
BLEED = 2.0   # the print files centre the lattice on trim + 2 in bleed; keep that so Canva matches the PDFs
EMB_VB = (1902.0, 2214.0)   # army-west-point-gold.svg viewBox size (portrait)

k = PITCH / 36.0
evo_w, emblem_box, pitch_x, pitch_y = 25.0 * k, 12.5 * k, PITCH, PITCH / 2
evo_h = evo_w * LOGO_H / LOGO_W
emb_h = emblem_box
emb_w = emblem_box * EMB_VB[0] / EMB_VB[1]

cols = int(math.ceil((W + 2*BLEED) / pitch_x)) + 3
rows = int(math.ceil((H + 2*BLEED) / pitch_y)) + 3
y0 = H/2 - ((rows - 1) / 2) * pitch_y
x0 = W/2 - ((cols - 1) / 2) * pitch_x
els = []
for r in range(rows):
    y = y0 + r * pitch_y
    shift = pitch_x/2 if r % 2 else 0
    for c in range(cols):
        x = x0 + c * pitch_x + shift
        if x < -BLEED - pitch_x or x > W + BLEED + pitch_x or y < -BLEED - pitch_y or y > H + BLEED + pitch_y: continue
        kind = 'evo' if r % 2 == 0 else 'emb'
        w, h = (evo_w, evo_h) if kind == 'evo' else (emb_w, emb_h)
        # drop marks that are entirely outside the trim (Canva has no bleed)
        if x + w/2 <= 0 or x - w/2 >= W or y + h/2 <= 0 or y - h/2 >= H: continue
        els.append(dict(kind=kind, row=r, col=c, cx=x, cy=y, w_in=w, h_in=h,
                        left=round((x - w/2) * PPI, 2), top=round((y - h/2) * PPI, 2),
                        width=round(w * PPI, 2), height=round(h * PPI, 2)))

out = f'build/canva_{int(W)}x{int(H)}'
os.makedirs(out, exist_ok=True)
json.dump(dict(W=W, H=H, ppi=PPI, page_w=round(W*PPI), page_h=round(H*PPI), pitch=PITCH,
               evo_w_in=evo_w, evo_h_in=evo_h, emb_w_in=emb_w, emb_h_in=emb_h, elements=els),
          open(f'{out}/elements.json', 'w'), indent=1)
pw, ph = round(W*PPI), round(H*PPI)
open(f'{out}/background.html', 'w').write(
    f'<!doctype html><html><body style="margin:0;background:{INK_BLACK}">'
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{pw}" height="{ph}" viewBox="0 0 {pw} {ph}" style="display:block">'
    f'<defs><radialGradient id="glow" cx="0.5" cy="0.45" r="0.75"><stop offset="0" stop-color="#262626"/><stop offset="1" stop-color="{INK_BLACK}"/></radialGradient></defs>'
    f'<rect width="{pw}" height="{ph}" fill="url(#glow)"/></svg></body></html>')
# local preview of the exact Canva layout (same element boxes) for a before/after check against the Canva thumbnail
evo_png = os.path.abspath('../../../../../home/user/CinemaxMK/design/evolution-mortgage-tailgate-flag/canva-layers/black-logo.png')
evo_png = '/home/user/CinemaxMK/design/evolution-mortgage-tailgate-flag/canva-layers/black-logo.png'
emb_svg = os.path.abspath('brand/army-west-point-gold.svg')
imgs = ''.join(f'<img src="file://{evo_png if e["kind"]=="evo" else emb_svg}" style="position:absolute;left:{e["left"]/PPI*10}px;top:{e["top"]/PPI*10}px;width:{e["width"]/PPI*10}px;height:{e["height"]/PPI*10}px">' for e in els)
open(f'{out}/preview.html', 'w').write(
    f'<!doctype html><html><body style="margin:0"><div style="position:relative;width:{W*10}px;height:{H*10}px;overflow:hidden;'
    f'background:radial-gradient(75% 75% at 50% 45%, #262626, {INK_BLACK})">{imgs}</div></body></html>')
n_evo = sum(e['kind']=='evo' for e in els); n_emb = len(els) - n_evo
print(f'page {pw}x{ph} px  ({W:g}x{H:g} in @ {PPI:g} ppi)  pitch {PITCH:g} in  ->  {n_evo} logos + {n_emb} shields = {len(els)} elements')
print(f'logo {evo_w:.3f} x {evo_h:.3f} in ({evo_w*PPI:.1f} x {evo_h*PPI:.1f} px); shield {emb_w:.3f} x {emb_h:.3f} in ({emb_w*PPI:.1f} x {emb_h*PPI:.1f} px)')
rows_used = sorted(set(e['cy'] for e in els)); print('row centres (in from top):', rows_used)
for kind in ('evo','emb'): print(kind, 'column centres:', sorted(set(e['cx'] for e in els if e['kind']==kind)))
