import json
from make_flag import LOGO_D, NAVY, GLOW, WHITE, _contours
INK = (min(c['bbox'][0] for c in _contours), min(c['bbox'][1] for c in _contours), max(c['bbox'][2] for c in _contours), max(c['bbox'][3] for c in _contours))
PPI = 64; W, H = 72, 54; pw, ph = W*PPI, H*PPI
iw, ih = INK[2]-INK[0], INK[3]-INK[1]
# logo layer: ink bounds only, 4400 px wide, transparent
LW = 4400; LH = round(LW * ih / iw); s = LW / iw
open('build/tablecloth/logo_layer.html', 'w').write(f'<!doctype html><html><body style="margin:0;background:transparent"><svg xmlns="http://www.w3.org/2000/svg" width="{LW}" height="{LH}" viewBox="0 0 {LW} {LH}" style="display:block"><path d="{LOGO_D}" fill="{WHITE}" fill-rule="evenodd" transform="scale({s:.6f}) translate({-INK[0]},{-INK[1]})"/></svg></body></html>')
open('build/tablecloth/bg_layer.html', 'w').write(f'<!doctype html><html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="{pw}" height="{ph}" style="display:block"><defs><radialGradient id="g" cx="0.5" cy="0.5" r="0.7"><stop offset="0" stop-color="{GLOW}"/><stop offset="1" stop-color="{NAVY}"/></radialGradient></defs><rect width="{pw}" height="{ph}" fill="url(#g)"/></svg></body></html>')
def box(cx, cy, w):
    h = w * ih / iw
    return dict(left=round((cx - w/2)*PPI, 2), top=round((cy - h/2)*PPI, 2), width=round(w*PPI, 2), height=round(h*PPI, 2))
json.dump(dict(page_w=pw, page_h=ph, ppi=PPI, logo_px=[LW, LH], front=box(36, 54 - 6, 22), center=box(36, 27, 34)), open('build/tablecloth/canva.json', 'w'), indent=1)
print(pw, ph, LW, LH, box(36, 48, 22), box(36, 27, 34))
