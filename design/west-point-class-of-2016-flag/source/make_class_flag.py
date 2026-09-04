#!/usr/bin/env python3
"""West Point class flag: arched WEST POINT, Army West Point shield, CLASS OF <year>. Inches."""
import sys, os, json, math
import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from make_flag import Typesetter, html_wrap, ARMY_GOLD, INK_BLACK, INT_SB

EMB = json.load(open('build/emblem_paths.json'))
EMB_VB = [float(v) for v in EMB['viewBox'].split()]
EMB_ASPECT = EMB_VB[2] / EMB_VB[3]

def runs(ts, text, size, tracking=0.0):
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties(); hb.shape(ts.font, buf, {"kern": True, "liga": True})
    s = size / ts.upem; x = 0.0; out = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        adv = pos.x_advance * s
        out.append((ts.order[info.codepoint], x, adv, pos.x_offset * s, -pos.y_offset * s))
        x += adv + tracking * size
    return out, x - tracking * size

def glyph_d(ts, name, size, dx, dy):
    pen = SVGPathPen(ts.gs, ntos=lambda v: f"{v:.4f}".rstrip('0').rstrip('.'))
    ts.gs[name].draw(TransformPen(pen, (size / ts.upem, 0, 0, -size / ts.upem, dx, dy)))
    return pen.getCommands()

def arc_text(ts, text, size, cx, base_mid_y, R, tracking=0.0, fill=ARMY_GOLD):
    """Text whose baseline follows a circle of radius R; the middle of the text sits at (cx, base_mid_y)."""
    gl, w = runs(ts, text, size, tracking); cyc = base_mid_y + R; out = []
    for name, x, adv, xo, yo in gl:
        th = (x + adv / 2 - w / 2) / R
        px, py = cx + R * math.sin(th), cyc - R * math.cos(th)
        d = glyph_d(ts, name, size, -adv / 2 + xo, yo)
        if d: out.append(f'<path d="{d}" fill="{fill}" transform="translate({px:.4f},{py:.4f}) rotate({math.degrees(th):.4f})"/>')
    return ''.join(out), w

def straight_text(ts, text, size, cx, base_y, tracking=0.0, fill=ARMY_GOLD):
    d, w = ts.path(text, size, cx, base_y, tracking=tracking, align='center')
    return f'<path d="{d}" fill="{fill}"/>', w

def fit_size(ts, text, target_w, tracking=0.0):
    return target_w / runs(ts, text, 1.0, tracking)[1]

def build(year='2016', font='fonts/Graduate-Regular.ttf', W=60.0, H=36.0, bleed=0.0, guides=False,
          top_w=48.0, bottom_w=40.0, emblem_h=13.0, R=50.0, frame_inset=2.0, frame_w=0.8, tracking=0.03, gap=1.3):
    ts = Typesetter(font)
    TW, TH = W + 2 * bleed, H + 2 * bleed
    cx = W / 2
    o = [f'<rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}" fill="url(#field)"/>']
    # gold frame as a filled ring (print-safe, no strokes)
    i, fw = frame_inset, frame_w
    o.append(f'<path d="M{i},{i}H{W-i}V{H-i}H{i}Z M{i+fw},{i+fw}V{H-i-fw}H{W-i-fw}V{i+fw}Z" fill="{ARMY_GOLD}" fill-rule="evenodd"/>')
    # sizes first, then centre the whole stack between the frame's inner edges
    top_size = fit_size(ts, 'WEST POINT', top_w, tracking)
    cap = ts.cap / ts.upem * top_size
    bot_size = fit_size(ts, f'CLASS OF {year}', bottom_w, tracking)
    bcap = ts.cap / ts.upem * bot_size
    inner_top, inner_bot = i + fw, H - i - fw
    stack = cap + gap + emblem_h + gap + bcap
    top_gap = (inner_bot - inner_top - stack) / 2
    base_mid = inner_top + top_gap + cap
    arc, _ = arc_text(ts, 'WEST POINT', top_size, cx, base_mid, R, tracking)
    o.append(arc)
    # shield
    ew = emblem_h * EMB_ASPECT
    ey = base_mid + gap
    o.append(f'<svg x="{cx-ew/2:.4f}" y="{ey:.4f}" width="{ew:.4f}" height="{emblem_h}" viewBox="{EMB["viewBox"]}" preserveAspectRatio="xMidYMid meet">'
             f'<path d="{EMB["gold_d"]}" fill="{ARMY_GOLD}" fill-rule="evenodd"/></svg>')
    # CLASS OF year
    bbase = ey + emblem_h + gap + bcap
    st, _ = straight_text(ts, f'CLASS OF {year}', bot_size, cx, bbase, tracking)
    o.append(st)
    bottom_gap = (H - i - fw) - bbase
    if guides:
        o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="#FF3B7A" stroke-width="0.06" stroke-dasharray="0.5 0.3"/>')
        lab, _ = INT_SB.path(f'TRIM {W:g} x {H:g} in · BLEED {bleed:g} in · top gap {top_gap:.1f} · bottom gap {bottom_gap:.1f}', 0.6, W - 0.5, H - 0.5, align='right')
        o.append(f'<path d="{lab}" fill="#FF3B7A"/>')
    defs = (f'<defs><radialGradient id="field" cx="0.5" cy="0.45" r="0.72"><stop offset="0" stop-color="#1F1F1F"/><stop offset="1" stop-color="{INK_BLACK}"/></radialGradient>'
            f'<clipPath id="page"><rect x="{-bleed}" y="{-bleed}" width="{TW}" height="{TH}"/></clipPath></defs>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{TW}in" height="{TH}in" viewBox="0 0 {TW} {TH}">'
           f'<title>West Point Class of {year} flag {W:g}x{H:g} in</title>{defs}'
           f'<g transform="translate({bleed},{bleed})" clip-path="url(#page)">{"".join(o)}</g></svg>')
    return svg, dict(top_size=top_size, cap=cap, base_mid=base_mid, emblem_y=ey, bottom_size=bot_size, bottom_base=bbase, bottom_gap=bottom_gap)

if __name__ == '__main__':
    year = sys.argv[1] if len(sys.argv) > 1 else '2016'
    font = sys.argv[2] if len(sys.argv) > 2 else 'fonts/AlfaSlabOne-Regular.ttf'
    tag = os.path.splitext(os.path.basename(font))[0].split('-')[0].lower()
    base = f'classflag_{year}_{tag}'
    for name, bleed, guides in [(base, 0, False), (base + '_bleed', 1.0, False), (base + '_proof', 1.0, True)]:
        svg, info = build(year, font, bleed=bleed, guides=guides)
        open(f'build/{name}.svg', 'w').write(svg); open(f'build/{name}.html', 'w').write(html_wrap(svg, 60 + 2 * bleed, 36 + 2 * bleed))
    print('wrote', base, {k: round(v, 2) for k, v in info.items()})
