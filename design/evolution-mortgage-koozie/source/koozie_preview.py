#!/usr/bin/env python3
"""Front-view preview of the koozie on a 12 oz can: wraps a flat print-area PNG around a cylinder.
Real dimensions: koozie 2.8 in outside diameter x 3.88 in tall on a 2.6 in x 4.83 in can; print area centred on the face."""
import sys, numpy as np
from PIL import Image, ImageFilter
PPI = 160
D, FACE, A, CAN_H, CAN_D = 2.8, 3.88, 3.5, 4.83, 2.6
GOLD = np.array([211, 188, 141], float); BLACK = np.array([22, 22, 22], float)

def wrap(art_png, out_png, seed=1):
    art = Image.open(art_png).convert('RGBA').resize((round(A * PPI), round(A * PPI)), Image.LANCZOS)
    alpha = np.asarray(art)[..., 3].astype(float) / 255
    r = D / 2 * PPI; W = round(D * PPI) + 2; H = round(FACE * PPI)
    rng = np.random.default_rng(seed)
    xs = np.arange(W) - W / 2 + 0.5
    inside = np.abs(xs) < r
    th = np.zeros(W); th[inside] = np.arcsin(xs[inside] / r)
    u = (r * th + A * PPI / 2).round().astype(int)                     # flat x for each output column
    off = round((FACE - A) / 2 * PPI)
    img = np.zeros((H, W, 3)); a_out = np.zeros((H, W))
    for yo in range(H):
        ya = yo - off
        row_a = np.zeros(W)
        if 0 <= ya < art.height:
            ok = inside & (u >= 0) & (u < art.width)
            row_a[ok] = alpha[ya, u[ok]]
        img[yo] = BLACK[None, :] * (1 - row_a[:, None]) + GOLD[None, :] * row_a[:, None]
        a_out[yo] = inside
    tex = rng.normal(0, 3.0, (H, W))[..., None]                         # neoprene grain
    shade = (0.42 + 0.58 * np.clip(np.cos(th), 0, 1) ** 0.7)[None, :, None]
    spec = (26 * np.exp(-((th + 0.5) / 0.22) ** 2))[None, :, None]
    img = np.clip(img * shade + spec + tex, 0, 255)
    # collar: darker stitched band along the top, rounded bottom
    img[:7] *= 0.55
    yy, xx = np.mgrid[0:H, 0:W]; rad = 26
    for cx in (rad, W - rad):
        m = (yy > H - rad) & (np.abs(xx - cx) < rad) & ((xx - cx) ** 2 + (yy - (H - rad)) ** 2 > rad ** 2) & ((xx < rad) | (xx > W - rad))
        a_out[m] = 0
    a_out[~np.broadcast_to(inside[None, :], a_out.shape)] = 0
    # can top above the koozie
    ch = round((CAN_H - FACE + 0.12) * PPI); cw = round(CAN_D * PPI); can = np.zeros((ch, W, 3)); can_a = np.zeros((ch, W))
    cr = cw / 2; cin = np.abs(xs) < cr; cth = np.zeros(W); cth[cin] = np.arcsin(xs[cin] / cr)
    metal = 150 + 80 * np.cos(cth) ** 2 + 45 * np.exp(-((cth + 0.55) / 0.2) ** 2)
    for yo in range(ch):
        can[yo] = np.clip(metal, 0, 255)[:, None]; can_a[yo] = cin
    neck = round(0.32 * PPI)
    for yo in range(neck):                                                  # tapered neck
        half = cr - (neck - yo) * 0.22
        m = np.abs(xs) < half; can_a[yo] = m
    can[:4] *= 0.8
    out = np.zeros((ch + H - 10, W, 4))
    out[:ch, :, :3] = can; out[:ch, :, 3] = can_a * 255
    seg = out[ch - 10:, :, :]
    m = a_out > 0
    seg[..., :3][m] = img[m]; seg[..., 3][m] = 255
    Image.fromarray(out.astype(np.uint8), 'RGBA').save(out_png)

if __name__ == '__main__':
    for side in sys.argv[1:]:
        wrap(f'build/koozie/{side}-600dpi.png', f'build/koozie/preview-{side}.png')
        print('preview', side)
