#!/usr/bin/env python3
"""Build the "CinemaxMK Fuji Retro" Lightroom preset pack.

Outputs:
  presets/lightroom/*.xmp        Lightroom / Camera Raw develop presets
  presets/previews/*.png         approximate before/after previews
  presets/CinemaxMK-Fuji-Retro-Lightroom-Presets.zip

The preview renderer is a rough numeric approximation of what the sliders do.
It exists so the looks can be compared at a glance; Lightroom's own rendering
is the reference, not this script.

Usage:  python3 tools/build_fuji_retro_presets.py
Needs:  numpy, pillow
"""
from __future__ import annotations

import hashlib
import os
import zipfile
from dataclasses import dataclass, field

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_XMP = os.path.join(ROOT, "presets", "lightroom")
OUT_PREVIEW = os.path.join(ROOT, "presets", "previews")
OUT_ZIP = os.path.join(ROOT, "presets", "CinemaxMK-Fuji-Retro-Lightroom-Presets.zip")

GROUP = "CinemaxMK Fuji Retro"
HSL_ORDER = ["Red", "Orange", "Yellow", "Green", "Aqua", "Blue", "Purple", "Magenta"]


# --------------------------------------------------------------------------
# Look definitions
# --------------------------------------------------------------------------
@dataclass
class Look:
    key: str
    name: str
    description: str
    # Basic panel (exposure and white balance are intentionally left alone)
    basic: dict
    # Point curves, 0-255 in/out. rgb = master curve
    curve: dict
    # HSL: lists in HSL_ORDER, each -100..100
    hsl: dict
    # Color grading: (hue 0-359, sat 0-100, lum -100..100)
    grading: dict
    # Calibration: shadow_tint, and (hue, sat) for red/green/blue primaries
    calib: dict
    # Grain: (amount, size, roughness)
    grain: tuple
    # Post-crop vignette amount
    vignette: int
    extra: dict = field(default_factory=dict)


LOOKS = [
    Look(
        key="01-superia-400",
        name="01 Superia 400",
        description=(
            "Warm consumer colour-negative look inspired by Fujicolor Superia 400: "
            "green-cyan shadows, yellow-warm highlights, cyan-leaning skies, punchy "
            "reds, a lifted film base and 400-speed grain."
        ),
        basic=dict(Contrast=10, Highlights=-20, Shadows=10, Whites=-5, Blacks=5,
                   Texture=0, Clarity=-5, Dehaze=0, Vibrance=5, Saturation=-8),
        curve=dict(
            rgb=[(0, 14), (48, 47), (128, 132), (212, 218), (255, 247)],
            red=[(0, 0), (128, 131), (255, 254)],
            green=[(0, 6), (128, 130), (255, 251)],
            blue=[(0, 10), (128, 125), (255, 240)],
        ),
        hsl=dict(
            hue=[5, -3, -8, -15, -10, -12, 0, 5],
            sat=[8, -5, -10, -15, -10, -15, -15, -5],
            lum=[-5, 5, 5, -5, 0, -10, 0, 0],
        ),
        grading=dict(shadow=(150, 8, 0), midtone=(45, 5, 0), highlight=(50, 10, 0),
                     blending=50, balance=0, global_=(0, 0, 0)),
        calib=dict(shadow_tint=-6, red=(5, 10), green=(-10, -5), blue=(-10, 5)),
        grain=(25, 30, 55),
        vignette=-8,
    ),
    Look(
        key="02-classic-chrome",
        name="02 Classic Chrome",
        description=(
            "Muted documentary look inspired by the Classic Chrome film simulation: "
            "desaturated steel-cyan blues, deeper reds, hard shadows with soft "
            "highlights and a magazine-print feel."
        ),
        basic=dict(Contrast=15, Highlights=-25, Shadows=-10, Whites=5, Blacks=0,
                   Texture=0, Clarity=5, Dehaze=0, Vibrance=-15, Saturation=-15),
        curve=dict(
            rgb=[(0, 6), (48, 40), (128, 128), (200, 205), (255, 250)],
            red=[(0, 0), (255, 250)],
            green=[(0, 2), (255, 252)],
            blue=[(0, 6), (128, 130), (255, 250)],
        ),
        hsl=dict(
            hue=[-3, -5, -10, -10, -5, -20, -10, -5],
            sat=[-5, -10, -25, -20, -20, -30, -25, -15],
            lum=[-15, 0, 5, -5, 0, -20, -10, -5],
        ),
        grading=dict(shadow=(210, 8, 0), midtone=(40, 3, 0), highlight=(45, 5, 0),
                     blending=50, balance=-10, global_=(0, 0, 0)),
        calib=dict(shadow_tint=0, red=(-5, -5), green=(5, -15), blue=(-8, 5)),
        grain=(15, 25, 50),
        vignette=-12,
    ),
    Look(
        key="03-pro-400h",
        name="03 Pro 400H",
        description=(
            "Airy pastel look inspired by Fujicolor Pro 400H: lifted mint-green "
            "shadows, soft cyan skies, pale peachy skin, low contrast and gentle grain. "
            "Likes a little extra exposure."
        ),
        basic=dict(Contrast=-15, Highlights=-20, Shadows=25, Whites=10, Blacks=15,
                   Texture=0, Clarity=-10, Dehaze=-5, Vibrance=-10, Saturation=-12),
        curve=dict(
            rgb=[(0, 22), (64, 74), (128, 138), (192, 200), (255, 248)],
            red=[(0, 2), (255, 250)],
            green=[(0, 10), (128, 130), (255, 252)],
            blue=[(0, 8), (128, 126), (255, 244)],
        ),
        hsl=dict(
            hue=[5, 5, 5, 15, 5, -10, 0, -5],
            sat=[-5, -10, -20, -25, -10, -15, -20, -10],
            lum=[5, 10, 10, 10, 5, 5, 0, 0],
        ),
        grading=dict(shadow=(160, 12, 0), midtone=(170, 3, 0), highlight=(40, 6, 0),
                     blending=60, balance=10, global_=(0, 0, 0)),
        calib=dict(shadow_tint=-10, red=(3, -5), green=(5, -10), blue=(-5, 10)),
        grain=(20, 35, 50),
        vignette=0,
    ),
    Look(
        key="04-nostalgic-neg",
        name="04 Nostalgic Neg",
        description=(
            "1970s 'American New Color' look inspired by the Nostalgic Neg film "
            "simulation: amber highlights, warm rich midtones, soft contrast, "
            "quiet greens and blues, and a light fade."
        ),
        basic=dict(Contrast=5, Highlights=-15, Shadows=15, Whites=-10, Blacks=5,
                   Texture=0, Clarity=-5, Dehaze=0, Vibrance=5, Saturation=-5),
        curve=dict(
            rgb=[(0, 12), (60, 60), (128, 134), (200, 208), (255, 246)],
            red=[(0, 0), (128, 134), (255, 255)],
            green=[(0, 2), (128, 128), (255, 250)],
            blue=[(0, 4), (128, 118), (255, 232)],
        ),
        hsl=dict(
            hue=[5, -5, -15, -20, -10, -10, 5, 5],
            sat=[10, 5, -5, -25, -20, -20, -15, 0],
            lum=[-5, 5, 5, -10, -5, -15, -5, 0],
        ),
        grading=dict(shadow=(35, 5, 0), midtone=(40, 8, 0), highlight=(45, 15, 0),
                     blending=50, balance=15, global_=(0, 0, 0)),
        calib=dict(shadow_tint=3, red=(-5, 10), green=(-10, -10), blue=(-10, 5)),
        grain=(20, 30, 50),
        vignette=-10,
    ),
    Look(
        key="05-classic-neg",
        name="05 Classic Neg",
        description=(
            "Hard, contrasty look inspired by the Classic Neg film simulation: "
            "cyan-green shadows, warm highlights, reds pulled toward magenta, muted "
            "olive greens and dark desaturated blues, like a scanned drugstore print."
        ),
        basic=dict(Contrast=25, Highlights=-20, Shadows=-10, Whites=0, Blacks=-5,
                   Texture=0, Clarity=5, Dehaze=0, Vibrance=-10, Saturation=-18),
        curve=dict(
            rgb=[(0, 10), (40, 30), (128, 128), (200, 210), (255, 250)],
            red=[(0, 0), (128, 132), (255, 252)],
            green=[(0, 6), (128, 128), (255, 250)],
            blue=[(0, 12), (128, 122), (255, 240)],
        ),
        hsl=dict(
            hue=[-8, -5, -5, 10, 5, 5, 0, -5],
            sat=[-5, -12, -25, -25, -15, -20, -20, -10],
            lum=[-10, -5, 0, -10, -5, -20, -10, -5],
        ),
        grading=dict(shadow=(175, 12, 0), midtone=(350, 3, 0), highlight=(40, 8, 0),
                     blending=50, balance=-10, global_=(0, 0, 0)),
        calib=dict(shadow_tint=-5, red=(-10, 5), green=(10, -15), blue=(-5, 15)),
        grain=(25, 25, 60),
        vignette=-15,
    ),
]


# --------------------------------------------------------------------------
# XMP writer
# --------------------------------------------------------------------------
def fmt(v) -> str:
    """Lightroom-style number: explicit '+' on positives, plain 0."""
    if isinstance(v, float):
        return f"{v:+.2f}" if v else "0.00"
    return f"{v:+d}" if v else "0"


def uuid_for(name: str) -> str:
    # Stable UUID per preset so re-running the script never creates duplicates
    return hashlib.md5(f"{GROUP}/{name}".encode("utf-8")).hexdigest().upper()


def alt(tag: str, text: str) -> str:
    text = (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))
    return (f"   <crs:{tag}>\n    <rdf:Alt>\n     <rdf:li xml:lang=\"x-default\">{text}</rdf:li>\n"
            f"    </rdf:Alt>\n   </crs:{tag}>\n")


def seq(tag: str, points) -> str:
    items = "".join(f"     <rdf:li>{x}, {y}</rdf:li>\n" for x, y in points)
    return f"   <crs:{tag}>\n    <rdf:Seq>\n{items}    </rdf:Seq>\n   </crs:{tag}>\n"


def build_xmp(look: Look) -> str:
    b = look.basic
    g = look.grading
    c = look.calib
    attrs = [
        ("PresetType", "Normal"),
        ("Cluster", ""),
        ("UUID", uuid_for(look.name)),
        ("SupportsAmount", "True"),
        ("SupportsColor", "True"),
        ("SupportsMonochrome", "True"),
        ("SupportsHighDynamicRange", "True"),
        ("SupportsNormalDynamicRange", "True"),
        ("SupportsSceneReferred", "True"),
        ("SupportsOutputReferred", "True"),
        ("CameraModelRestriction", ""),
        ("Copyright", "CinemaxMK"),
        ("ContactInfo", ""),
        ("Version", "15.0"),
        # No crs:ProcessVersion on purpose: the preset keeps the photo's own
        # process version instead of forcing an older/newer one.
        ("ConvertToGrayscale", "False"),
        # Basic
        ("Contrast2012", fmt(b["Contrast"])),
        ("Highlights2012", fmt(b["Highlights"])),
        ("Shadows2012", fmt(b["Shadows"])),
        ("Whites2012", fmt(b["Whites"])),
        ("Blacks2012", fmt(b["Blacks"])),
        ("Texture", fmt(b["Texture"])),
        ("Clarity2012", fmt(b["Clarity"])),
        ("Dehaze", fmt(b["Dehaze"])),
        ("Vibrance", fmt(b["Vibrance"])),
        ("Saturation", fmt(b["Saturation"])),
        # Parametric curve neutral, point curve custom
        ("ParametricShadows", "0"),
        ("ParametricDarks", "0"),
        ("ParametricLights", "0"),
        ("ParametricHighlights", "0"),
        ("ParametricShadowSplit", "25"),
        ("ParametricMidtoneSplit", "50"),
        ("ParametricHighlightSplit", "75"),
        ("ToneCurveName2012", "Custom"),
    ]
    # HSL
    for kind, key in (("HueAdjustment", "hue"), ("SaturationAdjustment", "sat"),
                      ("LuminanceAdjustment", "lum")):
        for colour, value in zip(HSL_ORDER, look.hsl[key]):
            attrs.append((f"{kind}{colour}", fmt(value)))
    # Colour grading (shadows/highlights live on the legacy split-toning keys)
    sh, mid, hi, glob = g["shadow"], g["midtone"], g["highlight"], g["global_"]
    attrs += [
        ("SplitToningShadowHue", str(sh[0])),
        ("SplitToningShadowSaturation", str(sh[1])),
        ("SplitToningHighlightHue", str(hi[0])),
        ("SplitToningHighlightSaturation", str(hi[1])),
        ("SplitToningBalance", fmt(g["balance"])),
        ("ColorGradeMidtoneHue", str(mid[0])),
        ("ColorGradeMidtoneSat", str(mid[1])),
        ("ColorGradeShadowLum", fmt(sh[2])),
        ("ColorGradeMidtoneLum", fmt(mid[2])),
        ("ColorGradeHighlightLum", fmt(hi[2])),
        ("ColorGradeBlending", str(g["blending"])),
        ("ColorGradeGlobalHue", str(glob[0])),
        ("ColorGradeGlobalSat", str(glob[1])),
        ("ColorGradeGlobalLum", fmt(glob[2])),
        # Calibration
        ("ShadowTint", fmt(c["shadow_tint"])),
        ("RedHue", fmt(c["red"][0])),
        ("RedSaturation", fmt(c["red"][1])),
        ("GreenHue", fmt(c["green"][0])),
        ("GreenSaturation", fmt(c["green"][1])),
        ("BlueHue", fmt(c["blue"][0])),
        ("BlueSaturation", fmt(c["blue"][1])),
        # Effects
        ("GrainAmount", str(look.grain[0])),
        ("GrainSize", str(look.grain[1])),
        ("GrainFrequency", str(look.grain[2])),
        ("PostCropVignetteAmount", fmt(look.vignette)),
        ("PostCropVignetteMidpoint", "50"),
        ("PostCropVignetteFeather", "60"),
        ("PostCropVignetteRoundness", "0"),
        ("PostCropVignetteStyle", "1"),
        ("PostCropVignetteHighlightContrast", "0"),
        ("HasSettings", "True"),
    ]
    attr_text = "\n".join(f"   crs:{k}=\"{v}\"" for k, v in attrs)
    body = (
        alt("Name", look.name)
        + alt("ShortName", look.name)
        + alt("SortName", look.name)
        + alt("Group", GROUP)
        + alt("Description", look.description)
        + seq("ToneCurvePV2012", look.curve["rgb"])
        + seq("ToneCurvePV2012Red", look.curve["red"])
        + seq("ToneCurvePV2012Green", look.curve["green"])
        + seq("ToneCurvePV2012Blue", look.curve["blue"])
    )
    return (
        '<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 7.0-c000 1.000000, 0000/00/00-00:00:00        ">\n'
        ' <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
        '  <rdf:Description rdf:about=""\n'
        '    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"\n'
        f"{attr_text}>\n"
        f"{body}"
        "  </rdf:Description>\n"
        " </rdf:RDF>\n"
        "</x:xmpmeta>\n"
    )


# --------------------------------------------------------------------------
# Preview renderer (approximation of the sliders, for comparison only)
# --------------------------------------------------------------------------
def srgb_to_linear(c):
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c):
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * np.power(c, 1 / 2.4) - 0.055)


M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929],
               [0.2119034982, 0.6806995451, 0.1073969566],
               [0.0883024619, 0.2817188376, 0.6299787005]])
M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468],
               [1.9779984951, -2.4285922050, 0.4505937099],
               [0.0259040371, 0.7827717662, -0.8086757660]])
M1I = np.linalg.inv(M1)
M2I = np.linalg.inv(M2)


def lin_to_oklab(rgb):
    lms = rgb @ M1.T
    lms = np.cbrt(lms)
    return lms @ M2.T


def oklab_to_lin(lab):
    lms = lab @ M2I.T
    lms = lms ** 3
    return lms @ M1I.T


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def pchip(points):
    """Monotone cubic through 0-255 points; returns a 256-entry lookup in 0..1."""
    xs = np.array([p[0] for p in points], float)
    ys = np.array([p[1] for p in points], float)
    n = len(xs)
    if n == 2:
        return np.interp(np.arange(256), xs, ys) / 255.0
    h = np.diff(xs)
    d = np.diff(ys) / h
    m = np.zeros(n)
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, n - 1):
        if d[i - 1] * d[i] <= 0:
            m[i] = 0.0
        else:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]
            m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    x = np.arange(256, dtype=float)
    idx = np.clip(np.searchsorted(xs, x, side="right") - 1, 0, n - 2)
    t = (x - xs[idx]) / h[idx]
    h00 = 2 * t**3 - 3 * t**2 + 1
    h10 = t**3 - 2 * t**2 + t
    h01 = -2 * t**3 + 3 * t**2
    h11 = t**3 - t**2
    y = h00 * ys[idx] + h10 * h[idx] * m[idx] + h01 * ys[idx + 1] + h11 * h[idx] * m[idx + 1]
    return np.clip(y, 0, 255) / 255.0


def apply_lut1d(x, lut):
    return np.interp(np.clip(x, 0, 1), np.linspace(0, 1, 256), lut)


# Hue conversions: Lightroom's hue wheel (HSV-like) -> OKLCh hue
LR_HUES = np.array([0, 60, 120, 180, 240, 300, 360], float)
OK_HUES = np.array([29, 110, 142, 195, 264, 328, 389], float)


def lr_hue_to_ok(h):
    return np.interp(np.mod(h, 360), LR_HUES, OK_HUES) % 360


HSL_CENTERS_OK = np.array([29, 60, 105, 142, 195, 264, 300, 335], float)


def hsl_interp(hue_ok, values):
    """Piecewise-linear blend of the 8 HSL slider values around the hue circle."""
    centers = np.concatenate([HSL_CENTERS_OK, [HSL_CENTERS_OK[0] + 360]])
    vals = np.concatenate([values, [values[0]]])
    h = np.mod(hue_ok - centers[0], 360) + centers[0]
    return np.interp(h, centers, vals)


def render(rgb_srgb: np.ndarray, look: Look) -> np.ndarray:
    """rgb_srgb: (..., 3) floats in 0..1. Returns the graded sRGB image."""
    lin = srgb_to_linear(rgb_srgb)

    # ---- Calibration: shadow tint + primaries (approximate)
    lab = lin_to_oklab(lin)
    L = lab[..., 0]
    a, b = lab[..., 1], lab[..., 2]
    C = np.hypot(a, b)
    H = np.degrees(np.arctan2(b, a)) % 360
    c = look.calib
    tint = c["shadow_tint"] / 100.0
    a = a + tint * 0.05 * (1 - smoothstep(0.1, 0.6, L))
    for prim_hue, (hue_v, sat_v), sigma in ((29, c["red"], 45), (142, c["green"], 45),
                                            (264, c["blue"], 80)):
        d = np.abs(((H - prim_hue) + 180) % 360 - 180)
        w = np.exp(-(d / sigma) ** 2)
        H = H + hue_v / 100.0 * 20.0 * w
        C = C * (1 + sat_v / 100.0 * 0.5 * w)
    a, b = C * np.cos(np.radians(H)), C * np.sin(np.radians(H))
    lin = np.clip(oklab_to_lin(np.stack([L, a, b], -1)), 0, 1)

    # ---- Basic tone (per channel, in gamma space)
    x = linear_to_srgb(lin)
    bs = look.basic
    ct = 0.6 * bs["Contrast"] / 100.0
    x = x - ct * np.sin(2 * np.pi * x) / (2 * np.pi)
    x = x + bs["Highlights"] / 100.0 * 0.25 * smoothstep(0.3, 0.75, x) * (1 - x) * 2
    x = x + bs["Shadows"] / 100.0 * 0.25 * (1 - smoothstep(0.25, 0.7, x)) * x * 2
    x = x + bs["Whites"] / 100.0 * 0.15 * smoothstep(0.5, 1.0, x)
    x = x + bs["Blacks"] / 100.0 * 0.15 * (1 - smoothstep(0.0, 0.5, x))
    x = np.clip(x, 0, 1)

    # ---- Point curves: master then per channel
    x = apply_lut1d(x, pchip(look.curve["rgb"]))
    for i, ch in enumerate(("red", "green", "blue")):
        x[..., i] = apply_lut1d(x[..., i], pchip(look.curve[ch]))

    # ---- HSL, vibrance, saturation in OKLCh
    lab = lin_to_oklab(srgb_to_linear(x))
    L = lab[..., 0]
    a, b = lab[..., 1], lab[..., 2]
    C = np.hypot(a, b)
    H = np.degrees(np.arctan2(b, a)) % 360
    cw = np.clip(C / 0.08, 0, 1)  # keep neutrals neutral
    hue_adj = hsl_interp(H, np.array(look.hsl["hue"], float))
    sat_adj = hsl_interp(H, np.array(look.hsl["sat"], float))
    lum_adj = hsl_interp(H, np.array(look.hsl["lum"], float))
    H = H + hue_adj * 0.3 * cw
    C = C * (1 + sat_adj / 100.0)
    L = L * (1 + 0.4 * lum_adj / 100.0 * cw)
    vib = bs["Vibrance"] / 100.0
    skin = np.exp(-((((H - 55) + 180) % 360 - 180) / 30.0) ** 2)
    C = C * (1 + vib * 0.8 * (1 - np.clip(C / 0.25, 0, 1)) * (1 - 0.6 * skin))
    C = C * (1 + bs["Saturation"] / 100.0)

    # ---- Colour grading
    g = look.grading
    shift = -g["balance"] / 100.0 * 0.2
    blend = g["blending"] / 100.0
    w_s = 1 - smoothstep(0.05 + shift, 0.45 + shift + blend * 0.3, L)
    w_h = smoothstep(0.55 + shift - blend * 0.3, 0.95 + shift, L)
    w_m = np.clip(1 - w_s - w_h, 0, 1)
    a, b = C * np.cos(np.radians(H)), C * np.sin(np.radians(H))
    for w, (hue, sat, lum) in ((w_s, g["shadow"]), (w_m, g["midtone"]), (w_h, g["highlight"])):
        hk = np.radians(lr_hue_to_ok(hue))
        a = a + w * sat / 100.0 * 0.09 * np.cos(hk)
        b = b + w * sat / 100.0 * 0.09 * np.sin(hk)
        L = L + w * lum / 100.0 * 0.2
    gh, gs, gl = g["global_"]
    hk = np.radians(lr_hue_to_ok(gh))
    a = a + gs / 100.0 * 0.09 * np.cos(hk)
    b = b + gs / 100.0 * 0.09 * np.sin(hk)
    L = L + gl / 100.0 * 0.2

    out = linear_to_srgb(np.clip(oklab_to_lin(np.stack([L, a, b], -1)), 0, 1))
    return np.clip(out, 0, 1)


COLORCHECKER = [
    (115, 82, 68), (194, 150, 130), (98, 122, 157), (87, 108, 67), (133, 128, 177), (103, 189, 170),
    (214, 126, 44), (80, 91, 166), (193, 90, 99), (94, 60, 108), (157, 188, 64), (224, 163, 46),
    (56, 61, 150), (70, 148, 73), (175, 54, 60), (231, 199, 31), (187, 86, 149), (8, 133, 161),
    (243, 243, 242), (200, 200, 200), (160, 160, 160), (122, 122, 121), (85, 85, 85), (52, 52, 52),
]


def test_card(w=600, h=420) -> np.ndarray:
    """A synthetic test image: sky/ground gradients, skin tones, ColorChecker, grey ramp."""
    img = np.zeros((h, w, 3), float)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    # Sky: deep blue at top to pale cyan at horizon, sun glow on the right
    band_h = int(h * 0.30)
    t = (yy[:band_h] / band_h)[..., None]
    sky_top = np.array([0.30, 0.50, 0.85])
    sky_low = np.array([0.72, 0.85, 0.95])
    sky = sky_top * (1 - t) + sky_low * t
    glow = np.exp(-(((xx[:band_h] - w * 0.8) / (w * 0.25)) ** 2 + ((yy[:band_h] - band_h) / (band_h * 0.8)) ** 2))
    sky = sky + glow[..., None] * np.array([0.25, 0.15, 0.0])
    img[:band_h] = sky
    # Ground: foliage green to warm earth
    g0, g1 = band_h, int(h * 0.52)
    t = ((yy[g0:g1] - g0) / (g1 - g0))[..., None]
    u = (xx[g0:g1] / w)[..., None]
    grass = np.array([0.35, 0.52, 0.22]) * (1 - u) + np.array([0.62, 0.55, 0.30]) * u
    img[g0:g1] = grass * (1 - 0.35 * t)
    # Skin tone strip and a few object colours
    s0, s1 = g1, int(h * 0.66)
    skins = [(0.96, 0.84, 0.75), (0.92, 0.74, 0.62), (0.82, 0.60, 0.46), (0.66, 0.45, 0.32),
             (0.48, 0.32, 0.22), (0.32, 0.20, 0.14)]
    objs = [(0.80, 0.12, 0.10), (0.95, 0.55, 0.10), (0.10, 0.35, 0.70), (0.55, 0.20, 0.60)]
    cells = skins + objs
    cw = w / len(cells)
    for i, col in enumerate(cells):
        img[s0:s1, int(i * cw):int((i + 1) * cw)] = col
    # ColorChecker 6x4
    c0, c1 = s1, int(h * 0.90)
    ch = (c1 - c0) / 4
    cw = w / 6
    for i, col in enumerate(COLORCHECKER):
        r, cc = divmod(i, 6)
        y0, y1 = int(c0 + r * ch), int(c0 + (r + 1) * ch)
        x0, x1 = int(cc * cw), int((cc + 1) * cw)
        img[y0 + 2:y1 - 2, x0 + 2:x1 - 2] = np.array(col) / 255.0
    # Grey ramp
    ramp = (xx[c1:] / (w - 1))[..., None]
    img[c1:] = np.repeat(ramp, 3, axis=-1)
    return np.clip(img, 0, 1)


def add_grain(rgb: np.ndarray, amount: int, size: int, seed: int) -> np.ndarray:
    """Cosmetic grain for the previews (Lightroom's grain is its own thing)."""
    if amount <= 0:
        return rgb
    rng = np.random.default_rng(seed)
    h, w = rgb.shape[:2]
    scale = 1 + size / 40.0
    small = rng.normal(0, 1, (int(h / scale) + 1, int(w / scale) + 1))
    noise = np.array(Image.fromarray(np.clip(small * 40 + 128, 0, 255).astype(np.uint8)).resize((w, h), Image.BILINEAR), float)
    noise = (noise - 128) / 40.0
    strength = amount / 100.0 * 0.07
    lum_w = 1 - np.abs(rgb.mean(-1) - 0.5) * 1.2  # less grain in deep blacks/whites
    return np.clip(rgb + (noise * strength * np.clip(lum_w, 0.2, 1))[..., None], 0, 1)


def to_image(arr: np.ndarray) -> Image.Image:
    return Image.fromarray((np.clip(arr, 0, 1) * 255 + 0.5).astype(np.uint8), "RGB")


def label(draw: ImageDraw.ImageDraw, xy, text, font):
    x, y = xy
    draw.rectangle([x - 6, y - 4, x + draw.textlength(text, font=font) + 6, y + 18], fill=(0, 0, 0))
    draw.text((x, y), text, fill=(255, 255, 255), font=font)


def main() -> None:
    os.makedirs(OUT_XMP, exist_ok=True)
    os.makedirs(OUT_PREVIEW, exist_ok=True)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 14)
    except OSError:
        font = ImageFont.load_default()

    card = test_card()
    before = to_image(card)
    written = []
    sheet_rows = []
    for i, look in enumerate(LOOKS):
        fname = f"CinemaxMK Fuji Retro - {look.name}.xmp"
        path = os.path.join(OUT_XMP, fname)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(build_xmp(look))
        written.append(path)

        after = to_image(add_grain(render(card, look), look.grain[0], look.grain[1], seed=i + 1))
        pair = Image.new("RGB", (before.width * 2 + 12, before.height), (18, 18, 18))
        pair.paste(before, (0, 0))
        pair.paste(after, (before.width + 12, 0))
        d = ImageDraw.Draw(pair)
        label(d, (10, 8), "ORIGINAL", font)
        label(d, (before.width + 22, 8), look.name.upper() + "  (approx. preview)", font)
        pair.save(os.path.join(OUT_PREVIEW, f"{look.key}.png"), optimize=True)
        sheet_rows.append((look, after))

    # Contact sheet: original on the left, the five looks to the right (two rows)
    thumb_w, thumb_h = 300, 210
    cols = 3
    rows = 2
    pad = 10
    sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad, rows * (thumb_h + pad + 22) + pad), (18, 18, 18))
    d = ImageDraw.Draw(sheet)
    tiles = [("Original", before)] + [(look.name, img) for look, img in sheet_rows]
    for n, (name, img) in enumerate(tiles):
        r, cc = divmod(n, cols)
        x = pad + cc * (thumb_w + pad)
        y = pad + r * (thumb_h + pad + 22)
        sheet.paste(img.resize((thumb_w, thumb_h), Image.LANCZOS), (x, y + 22))
        d.text((x, y + 3), name, fill=(240, 240, 240), font=font)
    sheet.save(os.path.join(OUT_PREVIEW, "all-presets.png"), optimize=True)

    with zipfile.ZipFile(OUT_ZIP, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in written:
            zf.write(path, os.path.join("CinemaxMK Fuji Retro", os.path.basename(path)))
    print("wrote", len(written), "presets, previews and", os.path.relpath(OUT_ZIP, ROOT))


if __name__ == "__main__":
    main()
