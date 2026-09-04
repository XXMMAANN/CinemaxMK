#!/usr/bin/env python3
"""Step-and-repeat backdrop generator: Evolution Mortgage logo + partner emblem. Inches."""
import sys, os, base64, math
from make_flag import (LOGO_D, LOGO_W, LOGO_H, COLOR_LOGO_URI, INT_SB, NAVY, GLOW, BLUE_DEEP, BLUE_CYAN, WHITE, ARMY_GOLD, INK_BLACK, html_wrap)
import re

def emblem_markup(path, box, ink, dark):
    """Return SVG markup for the partner emblem fitted into a box of `box` inches (centred at 0,0)."""
    if path and os.path.exists(path):
        ext = os.path.splitext(path)[1].lower()
        if ext == '.svg':
            src = open(path).read()
            vb = re.search(r'viewBox="([^"]+)"', src).group(1)
            inner = re.sub(r'^.*?<svg[^>]*>', '', src, count=1, flags=re.S).rsplit('</svg>', 1)[0]
            return (f'<svg x="{-box/2}" y="{-box/2}" width="{box}" height="{box}" viewBox="{vb}" preserveAspectRatio="xMidYMid meet">'
                    f'{inner}</svg>')
        mime = 'image/png' if ext == '.png' else 'image/jpeg'
        uri = f'data:{mime};base64,' + base64.b64encode(open(path, 'rb').read()).decode()
        return f'<image href="{uri}" x="{-box/2}" y="{-box/2}" width="{box}" height="{box}" preserveAspectRatio="xMidYMid meet"/>'
    # placeholder: neutral dashed square with a label, same footprint as the real emblem
    stroke = '#9AA8BF' if not dark else 'rgba(255,255,255,0.55)'
    t1, _ = INT_SB.path('WEST POINT', 0.95, 0, -0.35, tracking=0.06, align='center')
    t2, _ = INT_SB.path('EMBLEM HERE', 0.95, 0, 1.15, tracking=0.06, align='center')
    return (f'<rect x="{-box/2}" y="{-box/2}" width="{box}" height="{box}" rx="1.2" fill="none" stroke="{stroke}" stroke-width="0.14" stroke-dasharray="0.7 0.45"/>'
            f'<g fill="{stroke}"><path d="{t1}"/><path d="{t2}"/></g>')

def evo_markup(width, dark, fill=WHITE):
    s = width / LOGO_W; h = LOGO_H * s
    if dark:
        return f'<path d="{LOGO_D}" fill="{fill}" fill-rule="evenodd" transform="translate({-width/2:.4f},{-h/2:.4f}) scale({s:.6f})"/>'
    return (f'<g transform="translate({-width/2:.4f},{-h/2:.4f}) scale({s:.6f})">'
            f'<clipPath id="evoclip"><path d="{LOGO_D}" clip-rule="evenodd"/></clipPath>'
            f'<image href="{COLOR_LOGO_URI}" width="{LOGO_W}" height="{LOGO_H}" clip-path="url(#evoclip)" preserveAspectRatio="none"/></g>')

def build(W=96.0, H=96.0, bleed=2.0, colorway='white', emblem=None, guides=False,
          evo_w=26.0, emblem_box=13.0, pitch_x=34.0, pitch_y=15.5):
    dark = colorway in ('navy', 'black')
    black = colorway == 'black'
    TW, TH = W + 2*bleed, H + 2*bleed
    o = []
    o.append(f'<rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}" fill="{"url(#glow)" if dark else WHITE}"/>')
    # symbols (defined once, reused)
    evo_fill = ARMY_GOLD if black else WHITE
    defs = [f'<g id="evo">{evo_markup(evo_w, dark, evo_fill)}</g>', f'<g id="emb">{emblem_markup(emblem, emblem_box, WHITE if dark else NAVY, dark)}</g>']
    # staggered lattice, centred on the wall
    cols = int(math.ceil((W + 2*bleed) / pitch_x)) + 3
    rows = int(math.ceil((H + 2*bleed) / pitch_y)) + 3
    # centre the lattice so cut-offs are symmetric
    y0 = H/2 - ((rows - 1) / 2) * pitch_y
    x0 = W/2 - ((cols - 1) / 2) * pitch_x
    for r in range(rows):
        y = y0 + r * pitch_y
        shift = pitch_x/2 if r % 2 else 0
        for c in range(cols):
            x = x0 + c * pitch_x + shift
            if x < -bleed - pitch_x or x > W + bleed + pitch_x or y < -bleed - pitch_y or y > H + bleed + pitch_y: continue
            use = 'evo' if (c + r) % 2 == 0 else 'emb'
            o.append(f'<use href="#{use}" x="{x:.3f}" y="{y:.3f}"/>')
    if guides:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#FF3B7A" stroke-width="0.12" stroke-dasharray="1 0.6"/>')
        o.append(f'<rect x="0" y="{H-24}" width="{W}" height="24" fill="#FF3B7A" opacity="0.08"/>')
        lab, _ = INT_SB.path(f'TRIM {W:g} x {H:g} in  ·  BLEED {bleed:g} in', 1.2, W-1, H-1.2, align='right'); o.append(f'<path d="{lab}" fill="#FF3B7A"/>')
        lab, _ = INT_SB.path('LOWER 24 in USUALLY HIDDEN BY PEOPLE / TABLES', 1.1, 1.2, H-22.2); o.append(f'<path d="{lab}" fill="#FF3B7A"/>')
        lab, _ = INT_SB.path('EYE LINE ~ 60-66 in FROM FLOOR', 1.1, 1.2, H-64.5); o.append(f'<path d="{lab}" fill="#3BB273"/>')
        o.append(f'<line x1="0" y1="{H-63}" x2="{W}" y2="{H-63}" stroke="#3BB273" stroke-width="0.1" stroke-dasharray="0.8 0.5"/>')
    gc, ge = ('#262626', INK_BLACK) if black else (GLOW, NAVY)
    d = (f'<defs><radialGradient id="glow" cx="0.5" cy="0.45" r="0.75"><stop offset="0" stop-color="{gc}"/><stop offset="1" stop-color="{ge}"/></radialGradient>'
         f'<clipPath id="page"><rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}"/></clipPath>{"".join(defs)}</defs>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{TW}in" height="{TH}in" viewBox="0 0 {TW} {TH}">'
            f'<title>Evolution Mortgage x West Point step-and-repeat backdrop {W:g}x{H:g} in ({colorway})</title>{d}'
            f'<g transform="translate({bleed},{bleed})" clip-path="url(#page)">{"".join(o)}</g></svg>')

if __name__ == '__main__':
    W = float(sys.argv[1]) if len(sys.argv) > 1 else 96
    H = float(sys.argv[2]) if len(sys.argv) > 2 else 96
    colorway = sys.argv[3] if len(sys.argv) > 3 else 'white'
    emblem = sys.argv[4] if len(sys.argv) > 4 and sys.argv[4] != '-' else None
    base = f'backdrop_{int(W)}x{int(H)}_{colorway}'
    for name, bleed, guides in [(base, 0, False), (base + '_bleed', 2.0, False), (base + '_proof', 2.0, True)]:
        svg = build(W, H, bleed, colorway, emblem, guides)
        open(f'build/{name}.svg', 'w').write(svg)
        open(f'build/{name}.html', 'w').write(html_wrap(svg, W + 2*bleed, H + 2*bleed))
        print('wrote', name, len(svg)//1024, 'KB')
