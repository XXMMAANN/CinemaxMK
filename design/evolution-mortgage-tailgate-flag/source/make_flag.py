#!/usr/bin/env python3
"""Evolution Mortgage tailgate flag generator. All geometry in inches."""
import json, sys, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

NAVY, GLOW = '#0B1F3F', '#163D72'
BLUE_DEEP, BLUE_MID, BLUE_CYAN = '#1456AA', '#1088C8', '#21A0DE'
WHITE = '#FFFFFF'
ARMY_GOLD, INK_BLACK, CHARCOAL = '#D4BF91', '#0A0A0A', '#3B3B3B'   # Army West Point gold; black colorway field

class Typesetter:
    def __init__(self, path):
        self.tt = TTFont(path); self.gs = self.tt.getGlyphSet(); self.order = self.tt.getGlyphOrder()
        self.upem = self.tt['head'].unitsPerEm
        face = hb.Face(hb.Blob.from_file_path(path)); self.font = hb.Font(face); self.font.scale = (self.upem, self.upem)
        os2 = self.tt['OS/2']; self.cap = getattr(os2, 'sCapHeight', 0) or 0.7*self.upem; self.xh = getattr(os2, 'sxHeight', 0) or 0.5*self.upem
    def shape(self, text, size, tracking=0.0):
        buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
        hb.shape(self.font, buf, {"kern": True, "liga": True})
        s = size/self.upem; x = 0.0; out = []
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            out.append((self.order[info.codepoint], info.cluster, x + pos.x_offset*s, -pos.y_offset*s))
            x += pos.x_advance*s + tracking*size
        return out, (x - tracking*size if out else 0.0)
    def width(self, text, size, tracking=0.0):
        return self.shape(text, size, tracking)[1]
    def glyphs(self, text, size, x, y, tracking=0.0, align='left'):
        """-> list of (cluster, d); baseline at y."""
        gl, w = self.shape(text, size, tracking)
        if align == 'center': x -= w/2
        elif align == 'right': x -= w
        s = size/self.upem; out = []
        for name, cluster, gx, gy in gl:
            pen = SVGPathPen(self.gs, ntos=lambda v: f"{v:.4f}".rstrip('0').rstrip('.'))
            self.gs[name].draw(TransformPen(pen, (s, 0, 0, -s, x+gx, y+gy)))
            d = pen.getCommands()
            if d: out.append((cluster, d))
        return out, w
    def path(self, text, size, x, y, tracking=0.0, align='left'):
        gl, w = self.glyphs(text, size, x, y, tracking, align)
        return ' '.join(d for _, d in gl), w

POP_SB = Typesetter('fonts/Poppins-SemiBold.ttf')
POP_M  = Typesetter('fonts/Poppins-Medium.ttf')
INT_M  = Typesetter('fonts/Inter-Medium.ttf')
INT_SB = Typesetter('fonts/Inter-SemiBold.ttf')
INT_B  = Typesetter('fonts/Inter-Bold.ttf')

# ---- logo (traced from approved White Evolution Logo.png, 2110x640 px space) ----
_logo = json.load(open('build/logo_paths.json'))
_contours = _logo['helix'] + _logo['mortgage'] + _logo['evolution_rest']
LOGO_W, LOGO_H = _logo['size']
def _is_helix(c):
    b = c['bbox']; return b[0] >= 540 and b[2] <= 800 and b[3] <= 440
HELIX = [c for c in _contours if _is_helix(c)]
LOGO_D = ' '.join(c['d'] for c in _contours)
HELIX_D = ' '.join(c['d'] for c in HELIX)
HB = (min(c['bbox'][0] for c in HELIX), min(c['bbox'][1] for c in HELIX), max(c['bbox'][2] for c in HELIX), max(c['bbox'][3] for c in HELIX))
HELIX_CX, HELIX_CY, HELIX_W, HELIX_H = (HB[0]+HB[2])/2, (HB[1]+HB[3])/2, HB[2]-HB[0], HB[3]-HB[1]

import base64
COLOR_LOGO_URI = 'data:image/png;base64,' + base64.b64encode(open('brand/logo_color_opaque.png','rb').read()).decode()

def logo(x, y, width, fill=WHITE, opacity=1.0, color=False):
    s = width/LOGO_W
    if color:
        return (f'<g transform="translate({x:.4f},{y:.4f}) scale({s:.6f})">'
                f'<clipPath id="logoclip"><path d="{LOGO_D}" clip-rule="evenodd"/></clipPath>'
                f'<image href="{COLOR_LOGO_URI}" x="0" y="0" width="{LOGO_W}" height="{LOGO_H}" clip-path="url(#logoclip)" preserveAspectRatio="none"/>'
                f'</g>'), LOGO_H*s
    return (f'<path d="{LOGO_D}" fill="{fill}" fill-rule="evenodd" opacity="{opacity}" '
            f'transform="translate({x:.4f},{y:.4f}) scale({s:.6f})"/>'), LOGO_H*s

def helix(cx, cy, height, fill=WHITE, opacity=1.0, rotate=0):
    s = height/HELIX_H
    tx, ty = cx - HELIX_CX*s, cy - HELIX_CY*s
    rot = f' rotate({rotate},{cx:.3f},{cy:.3f})' if rotate else ''
    return (f'<path d="{HELIX_D}" fill="{fill}" fill-rule="evenodd" opacity="{opacity}" '
            f'transform="{rot} translate({tx:.4f},{ty:.4f}) scale({s:.6f})"/>')

def eho_mark(x, y, h, fill=WHITE):
    """Equal Housing Opportunity mark, (x,y) top-left, h = total height (mark is square)."""
    u = h; sw = 0.062*u
    house = f'M{0.19*u:.4f},{0.31*u:.4f} L{0.5*u:.4f},{0.05*u:.4f} L{0.81*u:.4f},{0.31*u:.4f} L{0.81*u:.4f},{0.585*u:.4f} L{0.19*u:.4f},{0.585*u:.4f} Z'
    bars = (f'<rect x="{0.355*u:.4f}" y="{0.335*u:.4f}" width="{0.29*u:.4f}" height="{0.062*u:.4f}"/>'
            f'<rect x="{0.355*u:.4f}" y="{0.445*u:.4f}" width="{0.29*u:.4f}" height="{0.062*u:.4f}"/>')
    t1, _ = INT_B.path('EQUAL HOUSING', 0.135*u, 0.5*u, 0.775*u, tracking=0.02, align='center')
    t2, _ = INT_B.path('OPPORTUNITY', 0.135*u, 0.5*u, 0.945*u, tracking=0.02, align='center')
    return (f'<g transform="translate({x:.4f},{y:.4f})" fill="{fill}">'
            f'<path d="{house}" fill="none" stroke="{fill}" stroke-width="{sw:.4f}" stroke-linejoin="miter" stroke-miterlimit="6"/>'
            f'{bars}<path d="{t1}"/><path d="{t2}"/></g>')

def build(variant='A', bleed=0.0, guides=False, W=60.0, H=36.0, colorway='navy', layout='logo'):
    TW, TH = W + 2*bleed, H + 2*bleed
    dark = colorway in ('navy', 'black')
    if colorway == 'black':
        BG_EDGE, BG_CENTER = INK_BLACK, CHARCOAL
        INK = ARMY_GOLD                      # lettering in Army West Point gold
        WM_FILL, WM_OP = ARMY_GOLD, 0.22     # gold helix, kept transparent so it stays in the background
    else:
        BG_EDGE, BG_CENTER = NAVY, GLOW
        INK = WHITE if dark else NAVY        # text / marks
        WM_FILL, WM_OP = (WHITE, 0.07) if dark else (BLUE_DEEP, 0.06)
    FOOT_OP = 0.9 if dark else 0.85
    o = []  # content in flag coordinates; wrapped in translate(bleed, bleed)
    cx = W/2 + 0.5          # optical center, nudged toward the fly (away from the pole sleeve)
    # background
    o.append(f'<rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}" fill="{"url(#glow)" if dark else WHITE}"/>')
    # super-scale helix watermark, cropped by the fly edge
    if variant in ('A', 'C'):
        o.append(helix(cx=52.5, cy=H/2, height=54, fill=WM_FILL, opacity=WM_OP))
    if variant == 'B':
        o.append(helix(cx=cx, cy=13.2, height=40, fill=WM_FILL, opacity=WM_OP))
    # logo
    if layout == 'logo':
        logo_w = 47.0
        lh = LOGO_H * logo_w / LOGO_W
        lg, lh = logo(cx - logo_w/2, H/2 - lh/2, logo_w, fill=INK, color=not dark)
        o.append(lg)
    else:
        logo_w = 44.0
        lg, lh = logo(cx - logo_w/2, 5.2, logo_w, fill=INK, color=not dark)
        o.append(lg)
    if layout != 'logo':
        # tagline: one accent word (brand rule), sentence case
        size = 2.75; base = 23.55
        text = 'Home loans made simple.'
        gl, w = POP_SB.glyphs(text, size, cx, base, align='center')
        accent_from = text.index('simple')
        white_d = ' '.join(d for c, d in gl if c < accent_from)
        blue_d  = ' '.join(d for c, d in gl if c >= accent_from)
        o.append(f'<path d="{white_d}" fill="{INK}"/>')
        o.append(f'<path d="{blue_d}" fill="url(#accent)"/>')
        # rule
        o.append(f'<rect x="{cx-7:.3f}" y="26.75" width="14" height="0.16" rx="0.08" fill="url(#brand)"/>')
        # footer: company · NMLS · site + EHO mark
        fsize = 0.95; fbase = 31.1
        sep = '     '
        ftext = f'Evolution Mortgage, LLC{sep}NMLS #2432729{sep}evolutionmortgage.com'
        fw = INT_M.width(ftext, fsize, tracking=0.01)
        eh = 2.0; gap = 1.1
        total = fw + gap + eh
        fx = cx - total/2
        fd, _ = INT_M.path(ftext, fsize, fx, fbase, tracking=0.01)
        o.append(f'<path d="{fd}" fill="{INK}" opacity="{FOOT_OP}"/>')
        # small dots as separators (drawn, so spacing is exact)
        xh = INT_M.xh/INT_M.upem*fsize
        for part in ['Evolution Mortgage, LLC', 'Evolution Mortgage, LLC' + sep + 'NMLS #2432729']:
            wpart = INT_M.width(part, fsize, tracking=0.01); wsep = INT_M.width(sep, fsize, tracking=0.01)
            dot_x = fx + wpart + wsep/2
            o.append(f'<circle cx="{dot_x:.3f}" cy="{fbase - xh/2:.3f}" r="0.075" fill="{BLUE_CYAN}"/>')
        o.append(eho_mark(fx + fw + gap, fbase - xh/2 - eh/2, eh, fill=INK))
    if guides:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#FF3B7A" stroke-width="0.06" stroke-dasharray="0.5 0.3"/>')
        o.append(f'<rect x="4" y="3" width="{W-7}" height="{H-6}" fill="none" stroke="#3BFF9C" stroke-width="0.06" stroke-dasharray="0.5 0.3"/>')
        lab, _ = INT_SB.path('TRIM 60 x 36 in', 0.6, W-0.5, H-0.5, align='right')
        o.append(f'<path d="{lab}" fill="#FF3B7A"/>')
        lab, _ = INT_SB.path('SAFE AREA (3 in, 4 in at hoist)', 0.6, W-3.5, H-3.5, align='right')
        o.append(f'<path d="{lab}" fill="#3BFF9C"/>')
        lab, _ = INT_SB.path('HOIST / POLE SIDE', 0.6, 4.6, 33.4)
        o.append(f'<path d="{lab}" fill="#3BFF9C"/>')
        if bleed:
            lab, _ = INT_SB.path(f'BLEED {bleed:g} in', 0.6, -bleed+0.4, -bleed+1.0)
            o.append(f'<path d="{lab}" fill="#FF3B7A"/>')
    defs = f'''<defs>
  <radialGradient id="glow" cx="0.5" cy="0.40" r="0.68"><stop offset="0" stop-color="{BG_CENTER}"/><stop offset="1" stop-color="{BG_EDGE}"/></radialGradient>
  <linearGradient id="brand" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE_DEEP}"/><stop offset="1" stop-color="{BLUE_CYAN}"/></linearGradient>
  <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BLUE_CYAN if dark else BLUE_DEEP}"/><stop offset="1" stop-color="{'#4FC3F0' if dark else BLUE_CYAN}"/></linearGradient>
  <clipPath id="page"><rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}"/></clipPath>
</defs>'''
    body = '\n'.join(o)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW}in" height="{TH}in" viewBox="0 0 {TW} {TH}">\n'
           f'<title>Evolution Mortgage tailgate flag 3x5 ft ({colorway})</title>\n{defs}\n'
           f'<g transform="translate({bleed},{bleed})" clip-path="url(#page)">\n{body}\n</g>\n</svg>\n')
    return svg

def html_wrap(svg, TW, TH):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:{TW}in {TH}in;margin:0}}'
            f'html,body{{margin:0;padding:0;background:#111}}svg{{display:block}}</style></head><body>{svg}</body></html>')

if __name__ == '__main__':
    variant = sys.argv[1] if len(sys.argv) > 1 else 'A'
    colorway = sys.argv[2] if len(sys.argv) > 2 else 'navy'
    layout = sys.argv[3] if len(sys.argv) > 3 else 'logo'
    os.makedirs('build', exist_ok=True)
    base = f'flag_{variant}_{colorway}' + ('' if layout == 'logo' else f'_{layout}')
    for name, bleed, guides in [(base, 0, False), (f'{base}_bleed', 1.0, False), (f'{base}_proof', 1.0, True)]:
        svg = build(variant, bleed, guides, colorway=colorway, layout=layout)
        open(f'build/{name}.svg', 'w').write(svg)
        open(f'build/{name}.html', 'w').write(html_wrap(svg, 60+2*bleed, 36+2*bleed))
        print('wrote', name, len(svg), 'bytes')
