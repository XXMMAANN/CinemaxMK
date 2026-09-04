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

## Art

- Evolution lockup: 25 in wide, vector, filled with Army gold `#D3BC8D` on black (full-color on white).
- Army West Point shield: 12.5 in tall (about 10.7 in wide), traced to vector from the supplied logo file (`source/army-west-point-gold.svg`, `source/army-west-point-2color.svg`). On black it is the gold-only, one-color reproduction; on white it is black + gold.
- Gold `#D3BC8D` is sampled from the supplied logo and equals the published Army gold, RGB 211 / 188 / 141, Pantone 467 C. Ask the printer to match 467 C.
- Black field `#0A0A0A` with a soft lift to `#262626` at the centre.

## Pattern (diamond)

- Rows alternate: a row of lockups, then a row of shields, and every row shifts half a step. Lockups repeat every 36 in along a row, rows are 18 in apart, so the half-step equals the row pitch and each mark sits inside a true 45° diamond of the other mark.
- The lattice is centred on the wall so edge cut-offs are symmetric, and a shield row lands at eye line on the 8 ft wall.
- Logos sit at 8-12.5 in tall, the range that stays readable behind a person in a phone photo.
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
