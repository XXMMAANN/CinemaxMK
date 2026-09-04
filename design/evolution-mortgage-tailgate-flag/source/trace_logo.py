import numpy as np, potrace, json
from PIL import Image

def trace(png, scale=2, thresh=128):
    im = Image.open(png).convert('RGBA')
    a = im.split()[3]
    a = a.resize((a.width*scale, a.height*scale), Image.LANCZOS)
    arr = ~(np.array(a) > thresh)
    bm = potrace.Bitmap(arr)
    path = bm.trace(turdsize=4, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=1.0, opticurve=True, opttolerance=0.2)
    curves = []
    for curve in path:
        pts = []
        sx, sy = curve.start_point.x, curve.start_point.y
        d = [f"M{sx/scale:.2f},{sy/scale:.2f}"]
        xs=[sx]; ys=[sy]
        for seg in curve.segments:
            ex, ey = seg.end_point.x, seg.end_point.y
            if seg.is_corner:
                cx, cy = seg.c.x, seg.c.y
                d.append(f"L{cx/scale:.2f},{cy/scale:.2f}L{ex/scale:.2f},{ey/scale:.2f}")
                xs += [cx, ex]; ys += [cy, ey]
            else:
                c1x, c1y = seg.c1.x, seg.c1.y; c2x, c2y = seg.c2.x, seg.c2.y
                d.append(f"C{c1x/scale:.2f},{c1y/scale:.2f} {c2x/scale:.2f},{c2y/scale:.2f} {ex/scale:.2f},{ey/scale:.2f}")
                xs += [ex]; ys += [ey]
        d.append("Z")
        curves.append({"d": "".join(d), "bbox": [min(xs)/scale, min(ys)/scale, max(xs)/scale, max(ys)/scale]})
    return curves, (im.width, im.height)

curves, size = trace('brand/White_Evolution_Logo.png')
print('logo contours:', len(curves), 'size', size)
# classify contours: helix "o" occupies x in ~[505,770], y in [0,415] in the 2110x640 source
helix = [c for c in curves if c['bbox'][0] >= 500 and c['bbox'][2] <= 780 and c['bbox'][3] <= 420]
mortgage = [c for c in curves if c['bbox'][1] >= 360 and c['bbox'][0] > 800]
evolution_rest = [c for c in curves if c not in helix and c not in mortgage]
print('helix contours', len(helix), 'mortgage', len(mortgage), 'evolution(no helix)', len(evolution_rest))
for name, group in [('helix', helix), ('mortgage', mortgage), ('evolution_rest', evolution_rest)]:
    bb = [min(c['bbox'][0] for c in group), min(c['bbox'][1] for c in group), max(c['bbox'][2] for c in group), max(c['bbox'][3] for c in group)]
    print(f"  {name}: bbox {[round(v,1) for v in bb]}")
json.dump({"size": size, "helix": helix, "mortgage": mortgage, "evolution_rest": evolution_rest}, open('build/logo_paths.json','w'))
# quick test svg: white logo on navy
allpath = "".join(c['d'] for c in curves)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size[0]} {size[1]}" width="{size[0]}" height="{size[1]}"><rect width="100%" height="100%" fill="#0b1f3f"/><path d="{allpath}" fill="#fff" fill-rule="evenodd"/></svg>'''
open('build/logo_trace_test.svg','w').write(svg)
print('path chars:', len(allpath))
