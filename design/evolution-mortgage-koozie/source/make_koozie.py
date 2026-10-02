#!/usr/bin/env python3
"""Varsity koozie (can cooler) artwork: black neoprene body, Army gold #D3BC8D (Pantone 467 C) print.
Front: Evolution Mortgage lockup over a double stripe. Back: USMA / 2016 in Alfa Slab One at 86 % width over the same
double stripe. Each side is one square print area (default 3.5 x 3.5 in, the myKoozie full-colour neoprene can cooler),
gold only on a transparent background so the black neoprene shows through.
Vertical positions are the approved varsity mockup's proportions (measured as % of the koozie body height) mapped onto a
3.88 in tall can-cooler face with the print area centred on it.
usage: python3 make_koozie.py [print area in=3.5] [face height in=3.88]"""
import sys, os
from make_flag import LOGO_D, ARMY_GOLD, Typesetter, INT_SB, _contours

GOLD = ARMY_GOLD
ALFA = Typesetter('fonts/AlfaSlabOne-Regular.ttf')
COND = 0.86                      # horizontal scale of the USMA / 2016 lettering (the mockup's condensed slab)
BACK_SCALE = 1.12                # the mockup koozie is drawn narrower than a real one; this keeps USMA / 2016 as wide
                                 # relative to the visible face as in the mockup (logo 83 %, USMA about 75 % of the face)
INK = (min(c['bbox'][0] for c in _contours), min(c['bbox'][1] for c in _contours),
       max(c['bbox'][2] for c in _contours), max(c['bbox'][3] for c in _contours))

def layout(A=3.5, FACE=3.88):
    off = (FACE - A) / 2
    y = lambda pct: pct / 100 * FACE - off          # mockup % of body height -> print-area inches
    cap = (y(45.1) - y(31.5)) * BACK_SCALE          # USMA cap height
    lead = (y(62.7) - y(45.1)) * BACK_SCALE         # USMA baseline to 2016 baseline
    mid = y((31.5 + 62.7) / 2)                      # stack centred where the mockup centres it
    top = mid - (cap + lead) / 2
    return dict(A=A, FACE=FACE, off=off, logo_w=2.75, logo_cy=y(45.45),
                size=cap / (ALFA.cap / ALFA.upem), usma_base=top + cap, yr_base=top + cap + lead,
                stripes=[(y(76.7), 0.10), (y(82.5), 0.10)])

def stripes(L):
    return ''.join(f'<rect x="0" y="{t:.4f}" width="{L["A"]}" height="{h}"/>' for t, h in L['stripes'])

def condensed(text, size, cx, base):
    d, w = ALFA.path(text, size, cx, base, tracking=0.0, align='center')
    return f'<path d="{d}" transform="translate({cx:.4f},0) scale({COND},1) translate({-cx:.4f},0)"/>', w * COND

def front(L, nmls=False):
    s = L['logo_w'] / (INK[2] - INK[0]); ih = (INK[3] - INK[1]) * s
    x0, y0 = L['A'] / 2 - L['logo_w'] / 2 - INK[0] * s, L['logo_cy'] - ih / 2 - INK[1] * s
    g = [f'<path d="{LOGO_D}" fill-rule="evenodd" transform="translate({x0:.4f},{y0:.4f}) scale({s:.6f})"/>', stripes(L)]
    if nmls:                                         # compliance line: Equal Housing house icon + company NMLS, under the lockup
        size = 0.12; d, w = INT_SB.path('NMLS #2432729', size, 0, 0, tracking=0.04)
        hh = 0.15; u = hh / 0.535; gap = 0.07; iw = 0.62 * u      # house icon only; the mark's tiny words would fill in on neoprene
        total = iw + gap + w; xs = L['A'] / 2 - total / 2; base = L['logo_cy'] + ih / 2 + 0.33
        hx, hy = xs - 0.19 * u, base - hh - 0.05 * u + 0.012
        house = (f'M{0.19*u:.4f},{0.31*u:.4f} L{0.5*u:.4f},{0.05*u:.4f} L{0.81*u:.4f},{0.31*u:.4f} '
                 f'L{0.81*u:.4f},{0.585*u:.4f} L{0.19*u:.4f},{0.585*u:.4f} Z')
        g.append(f'<g transform="translate({hx:.4f},{hy:.4f})"><path d="{house}" fill="none" stroke="{GOLD}" stroke-width="{0.075*u:.4f}" '
                 f'stroke-miterlimit="6"/><rect x="{0.355*u:.4f}" y="{0.335*u:.4f}" width="{0.29*u:.4f}" height="{0.07*u:.4f}"/>'
                 f'<rect x="{0.355*u:.4f}" y="{0.45*u:.4f}" width="{0.29*u:.4f}" height="{0.07*u:.4f}"/></g>')
        g.append(f'<path d="{d}" transform="translate({xs + iw + gap:.4f},{base:.4f})"/>')
    return g, dict(logo_ink_w=L['logo_w'], logo_ink_h=ih)

def back(L):
    a, wa = condensed('USMA', L['size'], L['A'] / 2, L['usma_base'])
    b, wb = condensed('2016', L['size'], L['A'] / 2, L['yr_base'])
    return [a, b, stripes(L)], dict(usma_w=wa, year_w=wb, cap_h=L['size'] * ALFA.cap / ALFA.upem)

def svg(L, parts, px=None, title=''):
    A = L['A']; size = f'width="{px}" height="{px}"' if px else f'width="{A}in" height="{A}in"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" {size} viewBox="0 0 {A} {A}"><title>{title}</title>'
            f'<g fill="{GOLD}">{"".join(parts)}</g></svg>')

def page(body, A):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:{A}in {A}in;margin:0}}'
            f'html,body{{margin:0;padding:0;background:transparent}}svg{{display:block}}</style></head><body>{body}</body></html>')

if __name__ == '__main__':
    A = float(sys.argv[1]) if len(sys.argv) > 1 else 3.5
    FACE = float(sys.argv[2]) if len(sys.argv) > 2 else 3.88
    L = layout(A, FACE); os.makedirs('build/koozie', exist_ok=True)
    jobs = {'front': front(L), 'back': back(L), 'front-nmls': front(L, nmls=True)}
    for name, (parts, info) in jobs.items():
        t = f'Evolution Mortgage varsity koozie, {name}, {A:g} x {A:g} in print area'
        open(f'build/koozie/{name}.svg', 'w').write(svg(L, parts, title=t))
        open(f'build/koozie/{name}_pdf.html', 'w').write(page(svg(L, parts, title=t), A))
        open(f'build/koozie/{name}_png.html', 'w').write(page(svg(L, parts, px=round(A * 600), title=t), A))
        print(name, {k: round(v, 3) for k, v in info.items()})
    print('stripes (top, height) in print-area inches:', [(round(t, 3), h) for t, h in L['stripes']], ' logo centre y', round(L['logo_cy'], 3),
          ' USMA/2016 baselines', round(L['usma_base'], 3), round(L['yr_base'], 3), ' font size', round(L['size'], 4))
