#!/usr/bin/env python3
"""Navy tablecloth, 72 x 54 in flat, Evolution Mortgage white lockup. Inches.
On a standard 6 ft table (72 x 30 in top) the 54 in width leaves a 12 in drop front and back, so layout 'front'
puts the lockup on the front drop where people see it; layout 'center' centres it on the cloth.
usage: python3 make_tablecloth.py"""
import os
from make_flag import LOGO_D, NAVY, GLOW, WHITE, INT_SB, html_wrap, _contours
INK = (min(c['bbox'][0] for c in _contours), min(c['bbox'][1] for c in _contours),
       max(c['bbox'][2] for c in _contours), max(c['bbox'][3] for c in _contours))
W, H, TABLE_D = 72.0, 54.0, 30.0
DROP = (H - TABLE_D) / 2

def lockup(cx, cy, w):
    s = w / (INK[2] - INK[0]); ih = (INK[3] - INK[1]) * s
    x0, y0 = cx - w / 2 - INK[0] * s, cy - ih / 2 - INK[1] * s
    return f'<path d="{LOGO_D}" fill="{WHITE}" fill-rule="evenodd" transform="translate({x0:.4f},{y0:.4f}) scale({s:.6f})"/>', ih

REP_W, REP_PX, REP_PY = 11.0, 18.0, 9.0      # repeat: lockup width, step along a row, row spacing (diamond offset)

def repeat_marks(bleed=0.0):
    """Diamond step-and-repeat: six whole rows (4.5 in from top and bottom), every other row shifted half a step, running off the sides."""
    out = []
    for j in range(-4, 5):
        cy = H/2 + (j + 0.5)*REP_PY
        for i in range(-4, 5):
            cx = W/2 + (i + (0.5 if j % 2 else 0)) * REP_PX
            if -bleed - REP_W/2 < cx < W + bleed + REP_W/2 and -bleed - 4 < cy < H + bleed + 4:
                out.append(dict(cx=cx, cy=cy))
    return out

def build(layout='front', bleed=0.0, guides=False):
    TW, TH = W + 2*bleed, H + 2*bleed
    if layout == 'front':
        logo, ih = lockup(W/2, H - DROP/2, 22.0)
    elif layout == 'repeat':
        parts = [lockup(m['cx'], m['cy'], REP_W)[0] for m in repeat_marks(bleed)]
        logo, ih = ''.join(parts), lockup(0, 0, REP_W)[1]
    else:
        logo, ih = lockup(W/2, H/2, 34.0)
    g = []
    if guides:
        R, G = '#FF3B7A', '#3BB273'
        g.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="{R}" stroke-width="0.12" stroke-dasharray="1 0.6"/>')
        g.append(f'<rect x="0" y="{DROP}" width="{W}" height="{TABLE_D}" fill="none" stroke="{G}" stroke-width="0.12" stroke-dasharray="1 0.6"/>')
        for txt, y, col in ((f'TRIM {W:g} x {H:g} in' + (f'  ·  BLEED {bleed:g} in' if bleed else ''), 1.6, R),
                            ('GREEN: 6 ft TABLE TOP 72 x 30 in  ·  12 in DROP FRONT AND BACK', DROP + 1.8, G),
                            ('FRONT DROP', H - DROP + 1.6, G)):
            p, _ = INT_SB.path(txt, 0.9, 1.0, y); g.append(f'<path d="{p}" fill="{col}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW}in" height="{TH}in" viewBox="0 0 {TW} {TH}">'
            f'<title>Evolution Mortgage navy tablecloth {W:g} x {H:g} in ({layout})</title>'
            f'<defs><radialGradient id="glow" cx="0.5" cy="0.5" r="0.7"><stop offset="0" stop-color="{GLOW}"/><stop offset="1" stop-color="{NAVY}"/></radialGradient></defs>'
            f'<rect x="0" y="0" width="{TW}" height="{TH}" fill="url(#glow)"/>'
            f'<g transform="translate({bleed},{bleed})">{logo}{"".join(g)}</g></svg>'), ih

if __name__ == '__main__':
    os.makedirs('build/tablecloth', exist_ok=True)
    for layout in ('front', 'center', 'repeat'):
        for name, bleed, guides in (('trim', 0, False), ('bleed-1in', 1.0, False), ('proof', 0, True)):
            svg, ih = build(layout, bleed, guides)
            base = f'build/tablecloth/{layout}-{name}'
            open(base + '.svg', 'w').write(svg)
            open(base + '.html', 'w').write(html_wrap(svg, W + 2*bleed, H + 2*bleed))
            prev = svg.replace(f'width="{W+2*bleed}in" height="{H+2*bleed}in"', f'width="{round((W+2*bleed)*20)}" height="{round((H+2*bleed)*20)}"', 1)
            open(base + '_prev.html', 'w').write(html_wrap(prev, W + 2*bleed, H + 2*bleed))
        print(layout, 'logo ink height', round(ih, 2), 'in')
