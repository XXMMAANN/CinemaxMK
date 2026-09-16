# Evolution Mortgage × Army West Point – step-and-repeat backdrop

Black photo wall for the tailgate: the Evolution Mortgage lockup and the Army West Point shield in a diamond
step-and-repeat, both in Army gold, so the wall matches the black / gold flag.

## Sizes and colorways

| Files | Size | Notes |
| --- | --- | --- |
| `…-8x8ft-black-*` | 96 × 96 in | **Primary.** Standard media wall, fits a 2-3 person photo. |
| `…-10x8ft-black-*` | 120 × 96 in | Wider wall for groups of 4-6. Same pattern and logo sizes. |
| `…-8x8ft-white-*` | 96 × 96 in | Alternate: full-color Evolution lockup and the two-color (black + gold) shield on white. |

Each set has: `PRINT-bleed-2in.pdf` (send to the printer; trim + 2 in bleed all round), `trim.pdf` (exact size),
`PROOF-guides.pdf` (trim, bleed, eye line and the lower 24 in people usually hide), editable `.svg` masters and a
`50ppi.png` raster fallback. `preview-*.png`, `mockup-*.png` and `proof-*.png` are for approvals.

## Fabric pop-up straight display, 10 × 8 ft (printer template)

Built on the printer's template for the fabric pop-up (file `147.51 × 89.51 in` = 2 in bleed + 12.96 in end cap + 117.60 × 89.50 in visible front + end cap + 2 in bleed; the template has no top or bottom bleed). The pattern sits on the front face only and the end caps carry nothing but the black field, so the sides of the display are plain.

- Every mark is whole and inside the front safe area (103.64 × 75.52 in): 16 lockups at 15.97 in wide and 15 shields at 7.99 in tall on a 23 in diamond pitch, 7 rows. Nothing straddles the rounded corner where the front wraps into the caps.
- The black field and centre glow run edge to edge, caps and bleed included, so there is no seam at the cap.
- Files: `…-popup-10x8ft-black-PRINT-147.51x89.51in.pdf` (**send this**, vector, exact template size), `…-PROOF-guides.pdf` (template zones drawn over the art, proof only), `…-popup-10x8ft-black.svg`, `…-50ppi.png`, `preview-popup-10x8ft-black.png`, `proof-popup-10x8ft-black.png`.
- Canva copy, editable: <https://www.canva.com/design/DAHVY8KbsfA/edit> (6194 × 3758 px, 42 px per inch, every mark its own element; sources in `canva-layers/popup-10x8ft-black-*`).
- For the printer's **online design tool** (canvas 144 × 90 in, fold lines 13 in from each edge, 118 in front): `…-DESIGNTOOL-144x90in-21600x13500px-150ppi.jpg` (150 px per inch of the finished size) or the smaller `…-14400x9000px-100ppi.jpg`. Same layout, proportioned to the tool's canvas so it fills it exactly once dragged to the corners; `proof-popup-10x8ft-black-designtool-canvas.png` shows the zones. Generated with `python3 source/make_popup.py 23 42 canvas` and `source/render_big.js` (tiled render, no browser size cap).
- Regenerate with `python3 source/make_popup.py [pitch in] [canva px per in]`; the template dimensions are constants at the top of the script.

## Art

- Evolution lockup: 16.7 in wide, vector, filled with Army gold `#D3BC8D` on black (full-color on white).
- Army West Point shield: 8.3 in tall (about 7.2 in wide), traced to vector from the supplied logo file (`source/army-west-point-gold.svg`, `source/army-west-point-2color.svg`). On black it is the gold-only, one-color reproduction; on white it is black + gold.
- Gold `#D3BC8D` is sampled from the supplied logo and equals the published Army gold, RGB 211 / 188 / 141, Pantone 467 C. Ask the printer to match 467 C.
- Black field `#0A0A0A` with a soft lift to `#262626` at the centre.

## Pattern (diamond)

- Rows alternate: a row of lockups, then a row of shields, and every row shifts half a step. Marks repeat every 24 in along a row, rows are 12 in apart, so the half-step equals the row pitch and each mark sits inside a true 45° diamond of the other mark. On the 8 ft wall that is 4 columns and 8 rows.
- The lattice is centred on the wall so edge cut-offs are symmetric, and a shield row lands at eye line on the 8 ft wall.
- Logos sit at about 8 in tall, the low end of the range that stays readable behind a person in a phone photo. Pass a larger pitch (sixth argument, e.g. `36`) for fewer, bigger marks.
- The earlier in-row stagger is still available: pass `stagger` as the fifth argument to the generator.

## Ordering notes

- Matte only: tension fabric (pillowcase print on an 8 × 8 ft aluminum frame) or matte vinyl with pole pockets on a telescoping stand. Glossy vinyl throws flash glare across the gold.
- Black fabric shows lint and dust in flash photos; bring a lint roller and steam it before the event.
- 2 in bleed is included; confirm the printer's pole-pocket or hem allowance before they trim.
- Confirm with West Point / the Association of Graduates that the shield may be used on sponsor material under the sponsorship agreement.

## Regenerating

`source/make_backdrop.py` imports the logo paths and fonts from the flag generator
(`../evolution-mortgage-tailgate-flag/source/`) and expects Poppins and Inter TTFs in a `fonts/` folder next to it.
Arguments: width in, height in, `black` / `white` / `navy`, emblem SVG or PNG path:

```
python3 make_backdrop.py 96 96 black army-west-point-gold.svg
```

## Canva

Editable copies in the Evolution Mortgage Canva account, imported from the trim-size PDFs. The lockups and shields came in as vector shapes.

| Size | Canva design |
| --- | --- |
| 8 × 8 ft, black | <https://www.canva.com/design/DAHVYn_9P38/edit> |
| 10 × 8 ft, black | <https://www.canva.com/design/DAHVYufpLoA/edit> |
| 8 × 8 ft, white | <https://www.canva.com/design/DAHVYmldRXA/edit> |

- Canva caps a page at 8000 px, so the walls are scaled (the 8 ft wall is 4995 px square, about 52 px per inch). Everything on the page is vector, so the printer simply scales the export to the finished size.
- To print from Canva: Share → Download → PDF Print, and tell the printer the finished size (96 × 96 in or 120 × 96 in) and that the file has no bleed. The `PRINT-bleed-2in.pdf` files in this folder remain the reference print files.

### Editable 8 × 10 ft (native Canva elements)

<https://www.canva.com/design/DAHVY9LnOu4/edit> is the 8 ft tall × 10 ft wide wall (120 × 96 in) rebuilt from native Canva elements instead of a PDF import: a glow background image, then 20 gold lockups and 24 gold shields, each its own image element at the exact lattice position of the print file (24 in pitch, 12 in rows, half-step offset). Any mark can be moved, resized, deleted or swapped for another upload in the editor, and the background image can be replaced or removed to change the field.

- Page 5520 × 4416 px, 46 px per inch. Canva caps a page at about 25 million pixels, so the wall cannot be laid out at 96 px per inch; the printer scales the export to 120 × 96 in.
- Sources in `canva-layers/`: `8x10ft-black-canva.html` (the file Canva imports), `8x10ft-black-elements.json` (element positions), `8x10ft-black-background.png` (glow field) and `army-west-point-gold.png` (shield, transparent). The gold lockup is `../evolution-mortgage-tailgate-flag/canva-layers/black-logo.png`.
- To rebuild at another size or pitch: `python3 source/canva_backdrop.py <width in> <height in> <px per in> [pitch in]`, then `python3 source/make_canva_html.py <elements.json> <out.html> <raw GitHub base url> <background png> <lockup png> <shield png>`, commit, and import the HTML into Canva from a commit-pinned raw URL (the branch URL is cached for several minutes and can hand Canva a stale file).
- Two earlier imports titled "zz TEST COPY … safe to delete" in the Canva account are clipped by that page cap and can be deleted.
