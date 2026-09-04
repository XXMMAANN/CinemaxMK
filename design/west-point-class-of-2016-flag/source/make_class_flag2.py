#!/usr/bin/env python3
"""West Point class flag v2: traced official WEST POINT letters on an arc, full-color USMA crest, stencil CLASS OF <year>."""
import sys, os, json, math, base64
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from make_flag import Typesetter, html_wrap, ARMY_GOLD, INK_BLACK, INT_SB
import uharfbuzz as hb

WP = json.load(open('build/westpoint_letters_clean.json'))
CREST_URI = 'data:image/png;base64,' + base64.b64encode(open('brand/usma-crest.png','rb').read()).decode()
from PIL import Image
CW, CH = Image.open('brand/usma-crest.png').size
OFFICIAL_WIDTH_PER_CAP = WP['width'] / WP['cap']

def official_arc(width_in, cx, base_mid_y, R, fill=ARMY_GOLD):
    s = width_in / WP['width']; cyc = base_mid_y + R; out = []
    for l in WP['letters']:
        xc = (l['bbox'][0] + l['bbox'][2]) / 2
        th = ((xc - WP['x0']) * s - width_in / 2) / R
        px, py = cx + R * math.sin(th), cyc - R * math.cos(th)
        d = ' '.join(l['parts'])
        out.append(f'<path d="{d}" fill="{fill}" fill-rule="evenodd" transform="translate({px:.4f},{py:.4f}) rotate({math.degrees(th):.4f}) scale({s:.6f}) translate({-xc:.3f},{-WP["baseline"]:.3f})"/>')
    return ''.join(out), WP['cap'] * s

def stencil_line(ts, text, size, cx, base_y, stretch, tracking=0.0, fill=ARMY_GOLD):
    """Straight line in the lookalike stencil, stretched horizontally to the official proportions."""
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(ts.font, buf, {"kern": True, "liga": True})
    s = size / ts.upem; x = 0.0; parts = []
    glyphs = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        glyphs.append((ts.order[info.codepoint], x + pos.x_offset * s, -pos.y_offset * s)); x += pos.x_advance * s + tracking * size
    w = (x - tracking * size) * stretch
    for name, gx, gy in glyphs:
        pen = SVGPathPen(ts.gs, ntos=lambda v: f"{v:.4f}".rstrip('0').rstrip('.'))
        ts.gs[name].draw(TransformPen(pen, (s * stretch, 0, 0, -s, cx - w / 2 + gx * stretch, base_y + gy)))
        d = pen.getCommands()
        if d: parts.append(d)
    return f'<path d="{" ".join(parts)}" fill="{fill}"/>', w

def build(year='2016', W=60.0, H=36.0, bleed=0.0, guides=False, top_w=40.0, bottom_w=36.0, crest_h=13.5, R=50.0,
          frame_inset=2.0, frame_w=0.8, gap=1.2, font='fonts/BigShouldersStencil-Black.ttf'):
    ts = Typesetter(font)
    TW, TH = W + 2 * bleed, H + 2 * bleed; cx = W / 2
    o = [f'<rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}" fill="url(#field)"/>']
    i, fw = frame_inset, frame_w
    o.append(f'<path d="M{i},{i}H{W-i}V{H-i}H{i}Z M{i+fw},{i+fw}V{H-i-fw}H{W-i-fw}V{i+fw}Z" fill="{ARMY_GOLD}" fill-rule="evenodd"/>')
    # sizes
    cap = WP['cap'] * (top_w / WP['width'])
    stretch = OFFICIAL_WIDTH_PER_CAP / (ts.width('WEST POINT', 1.0) / (ts.cap / ts.upem))
    text = f'CLASS OF {year}'
    bot_size = bottom_w / (ts.width(text, 1.0) * stretch)
    bcap = ts.cap / ts.upem * bot_size
    inner_top, inner_bot = i + fw, H - i - fw
    stack = cap + gap + crest_h + gap + bcap
    top_gap = (inner_bot - inner_top - stack) / 2
    base_mid = inner_top + top_gap + cap
    arc, _ = official_arc(top_w, cx, base_mid, R); o.append(arc)
    crest_w = crest_h * CW / CH; cy0 = base_mid + gap
    o.append(f'<image href="{CREST_URI}" x="{cx-crest_w/2:.4f}" y="{cy0:.4f}" width="{crest_w:.4f}" height="{crest_h}" preserveAspectRatio="xMidYMid meet"/>')
    bbase = cy0 + crest_h + gap + bcap
    line, _ = stencil_line(ts, text, bot_size, cx, bbase, stretch); o.append(line)
    if guides:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#FF3B7A" stroke-width="0.06" stroke-dasharray="0.5 0.3"/>')
        lab, _ = INT_SB.path(f'TRIM {W:g} x {H:g} in · BLEED {bleed:g} in · cap {cap:.1f} in · crest {crest_h:g} in', 0.6, W - 0.5, H - 0.5, align='right'); o.append(f'<path d="{lab}" fill="#FF3B7A"/>')
    defs = (f'<defs><radialGradient id="field" cx="0.5" cy="0.45" r="0.72"><stop offset="0" stop-color="#1F1F1F"/><stop offset="1" stop-color="{INK_BLACK}"/></radialGradient>'
            f'<clipPath id="page"><rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}"/></clipPath></defs>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{TW}in" height="{TH}in" viewBox="0 0 {TW} {TH}">'
           f'<title>West Point Class of {year} flag {W:g}x{H:g} in</title>{defs}<g transform="translate({bleed},{bleed})" clip-path="url(#page)">{"".join(o)}</g></svg>')
    return svg, dict(cap=cap, stretch=stretch, bot_size=bot_size, bcap=bcap, top_gap=top_gap)

if __name__ == '__main__':
    year = sys.argv[1] if len(sys.argv) > 1 else '2016'
    base = f'classflag2_{year}'
    for name, bleed, guides in [(base, 0, False), (base + '_bleed', 1.0, False), (base + '_proof', 1.0, True)]:
        svg, info = build(year, bleed=bleed, guides=guides)
        open(f'build/{name}.svg', 'w').write(svg); open(f'build/{name}.html', 'w').write(html_wrap(svg, 60 + 2 * bleed, 36 + 2 * bleed))
    print('wrote', base, {k: round(v, 3) for k, v in info.items()})
