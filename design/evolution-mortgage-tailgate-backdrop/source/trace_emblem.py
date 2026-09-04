import numpy as np, json, potrace
from PIL import Image
src = '/root/.claude/uploads/82e5b570-3f7c-5628-bfa5-d70dcf2a1df6/22d141ca-image.webp'
im = Image.open(src).convert('RGBA'); W, H = im.size
a = np.array(im).astype(np.float32); rgb = a[..., :3]; alpha = a[..., 3]
print('source', W, H, 'alpha min', alpha.min())
# treat transparent as white
rgb = np.where((alpha < 8)[..., None], 255.0, rgb)
lum = rgb @ np.array([0.299, 0.587, 0.114])
sat = rgb.max(-1) - rgb.min(-1)
gold_px = rgb[(sat > 40) & (lum > 120) & (lum < 220)]
black_px = rgb[(lum < 60)]
gold = np.median(gold_px, 0); black = np.median(black_px, 0)
print('sampled gold #%02x%02x%02x  black #%02x%02x%02x  (gold px %d)' % (*gold.astype(int), *black.astype(int), len(gold_px)))
white = np.array([255, 255, 255.0])
d = lambda c: np.linalg.norm(rgb - c, axis=-1)
dg, dk, dw = d(gold), d(black), d(white)
gold_mask = (dg < dk) & (dg < dw)
ink_mask = (dw > dg) | (dw > dk)          # anything not closest to white = silhouette
print('gold px', gold_mask.sum(), 'ink px', ink_mask.sum())

def trace(mask, turd=6):
    bm = potrace.Bitmap(~mask)  # potracer convention observed earlier: invert
    path = bm.trace(turdsize=turd, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0, opticurve=1, opttolerance=0.2)
    parts = []
    for curve in path:
        s = curve.start_point; parts.append(f'M{s.x:.1f},{s.y:.1f}')
        for seg in curve.segments:
            e = seg.end_point
            if seg.is_corner:
                c = seg.c; parts.append(f'L{c.x:.1f},{c.y:.1f}L{e.x:.1f},{e.y:.1f}')
            else:
                c1, c2 = seg.c1, seg.c2; parts.append(f'C{c1.x:.1f},{c1.y:.1f} {c2.x:.1f},{c2.y:.1f} {e.x:.1f},{e.y:.1f}')
        parts.append('Z')
    return ''.join(parts)

gold_d = trace(gold_mask); ink_d = trace(ink_mask)
gh = '#%02x%02x%02x' % tuple(gold.astype(int)); kh = '#%02x%02x%02x' % tuple(black.astype(int))
# bounding box of the silhouette for tight fitting
ys, xs = np.where(ink_mask); bbox = [int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1]
print('bbox', bbox, 'aspect w/h = %.3f' % ((bbox[2]-bbox[0]) / (bbox[3]-bbox[1])))
vb = f'{bbox[0]} {bbox[1]} {bbox[2]-bbox[0]} {bbox[3]-bbox[1]}'
open('brand/army-west-point-2color.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><path d="{ink_d}" fill="{kh}" fill-rule="evenodd"/><path d="{gold_d}" fill="{gh}" fill-rule="evenodd"/></svg>')
open('brand/army-west-point-gold.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><path d="{gold_d}" fill="{gh}" fill-rule="evenodd"/></svg>')
json.dump({'gold': gh, 'black': kh, 'viewBox': vb, 'gold_d': gold_d, 'ink_d': ink_d}, open('build/emblem_paths.json', 'w'))
# quick check renders: 2-color on white, gold-only on black
open('build/emblem_check.html', 'w').write(f'''<html><body style="margin:0;background:#888"><div style="display:flex">
<div style="background:#fff;padding:20px"><svg width="440" height="500" viewBox="{vb}"><path d="{ink_d}" fill="{kh}" fill-rule="evenodd"/><path d="{gold_d}" fill="{gh}" fill-rule="evenodd"/></svg></div>
<div style="background:#0a0a0a;padding:20px"><svg width="440" height="500" viewBox="{vb}"><path d="{gold_d}" fill="{gh}" fill-rule="evenodd"/></svg></div></div></body></html>''')
print('gold path', len(gold_d)//1024, 'KB; ink path', len(ink_d)//1024, 'KB')
