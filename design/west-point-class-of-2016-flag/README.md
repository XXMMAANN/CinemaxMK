# West Point Class of 2016 – flag (3 × 5 ft)

Black flag with a gold frame, arched "WEST POINT" in the Army West Point stencil lettering, the full-color USMA
crest in the middle and "CLASS OF 2016" beneath. Gold matches the tailgate flag and backdrop.

## Lettering, honestly

The Army West Point stencil face is a proprietary typeface with no public font file. So:

- **"WEST POINT"** uses the actual letters from the supplied wordmark, traced to vector at 4× and set on the arch. Exact letterforms.
- **"CLASS OF 2016"** is set in Big Shoulders Stencil Black (open licence), the closest match in structure and cuts, stretched 10 % horizontally to the official letter proportions.
- If the athletics brand team can supply the real font file (OTF/TTF), swap it in `source/make_class_flag2.py` and both lines become exact.

## Files

| File | Use |
| --- | --- |
| `…-PRINT-bleed-1in.pdf` | **Send this to the printer.** 62 × 38 in page = 60 × 36 in trim + 1 in bleed. Lettering is vector; the crest is embedded at 3600 px (about 170 px per inch at size). |
| `…-trim.pdf` | Same art at exact trim size. |
| `…-PROOF-guides.pdf` | Proof only: trim and bleed marks. |
| `….svg`, `…-BLEED-1in.svg` | Editable vector masters (crest embedded as an image). |
| `…-6000x3600.png` | Raster fallback, 100 px per inch. |
| `preview.png`, `mockup.png` | For approvals. |
| `alternates/shield-serif/` | Earlier version: Army West Point shield with slab-serif lettering. |
| `source/` | Generator, traced letters, trimmed crest and the stencil font. `python3 make_class_flag2.py 2016` (change the year for other classes). |

## Specs

- Trim 60 × 36 in, bleed 1 in. Gold frame 0.8 in thick, inset 2 in.
- "WEST POINT" 40 in wide (6.5 in caps) on a 50 in radius arch; crest 13.5 in tall; "CLASS OF 2016" 36 in wide (4.8 in caps).
- Colors: gold `#D3BC8D` (Army gold, RGB 211 / 188 / 141, Pantone 467 C); field black `#0A0A0A` with a soft lift to `#1F1F1F`. Crest in its own colors.

## Ordering notes

- This flag carries text: order **double-sided (2-ply with blockout)** if it flies on a pole and is seen from both sides; on a single-reverse flag the lettering reads backwards from the back.
- Hung on the tent or a fence like the reference banner, single-sided with brass grommets at the corners is fine. The frame is inset enough for corner grommets.
- Matte polyester, dye-sublimation; match Pantone 467 C for the gold. The crest's red, blue and gold print as-is.
- Confirm the crest and wordmark may be used under the class or sponsorship guidelines.

## Canva

Editable copy: <https://www.canva.com/design/DAHVYjwNYPA/edit>. The page is 5760 × 3456 px, which Canva treats as 60 × 36 in (96 px per inch), trim size with no bleed. Imported from the trim PDF: the lettering and frame are vector shapes, the crest is an image.

To print from Canva: Share → Download → PDF Print, finished size 60 × 36 in, no bleed in the file. The `PRINT-bleed-1in.pdf` here remains the reference print file.

## Canva fonts for this lettering

`canva-font-matches.png` sets "WEST POINT / CLASS OF 2030" in the Canva fonts closest to the reference banner's heavy slab serif. Closest first: **Alfa Slab One**, **Bevan** (heavier, a little more condensed), then Rokkitt Black and Kameron Bold (Rockwell-style geometry but lighter), Ultra and Holtwood One SC (heavier and wider). If the account's font list includes Rockwell, Rockwell Extra Bold is the genuine article. Arch the top line with Text → Effects → Curve.
