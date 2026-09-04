# Evolution Mortgage × West Point – step-and-repeat backdrop

Photo-wall artwork for the tailgate: the Evolution Mortgage lockup alternating with the West Point emblem
in a staggered step-and-repeat, on white (primary) or navy.

**The West Point emblem is a placeholder slot in these files.** Drop in the official artwork supplied by
West Point / the Association of Graduates under the sponsorship agreement, then regenerate:

```
cd source && python3 make_backdrop.py 96 96 white /path/to/west-point-emblem.png
```

PNG with a transparent background (2000 px or larger) or SVG. The emblem is fitted into a 12 × 12 in box.

## Sizes

| Size | Files | Notes |
| --- | --- | --- |
| 8 × 8 ft (96 × 96 in) | `…-8x8ft-white-*`, `…-8x8ft-navy-*` | Standard media wall. Fits a 2-3 person photo. |
| 10 × 8 ft (120 × 96 in) | `…-10x8ft-white-*` | Wider wall for groups of 4-6. Same pattern, same logo sizes. |

Each size has: `PRINT-bleed-2in.pdf` (send to printer; trim + 2 in bleed all round), `trim.pdf` (exact size),
`PROOF-guides.pdf` (trim, bleed, eye line, the lower 24 in that people usually hide), editable `.svg` masters,
and a `50ppi.png` raster fallback. `preview-*.png` and `mockup-*.png` are for approvals.

## Pattern

- Evolution lockup 26 in wide (about 7.9 in tall); emblem slot 12 × 12 in.
- Grid pitch 34 in across, 15.5 in down, every other row offset by half a step, centred on the wall so edge cut-offs are symmetric.
- Logos sit at 8-12 in tall, the range that stays readable behind a person in a phone photo.
- White version: full-color lockup, exact brand gradient inside vector edges. Navy version: white lockup on navy `#0B1F3F` with a soft glow. The navy version needs a white / one-color emblem file.

## Ordering notes

- Ask for matte material: tension fabric (pillowcase print on an 8 × 8 ft aluminum frame) or matte vinyl with pole pockets on a telescoping backdrop stand. Glossy vinyl throws flash glare across the logos.
- Fabric photographs better and packs smaller; vinyl is cheaper and tougher outdoors. Either way, request wrinkle-free / steamable fabric or a rigid frame.
- 2 in bleed is included; confirm the printer's pole-pocket or hem allowance before they trim.
- Use the white version outdoors in daylight; navy reads richer under tents and at night events but shows dust.

## Regenerating

`source/make_backdrop.py` imports the logo paths and fonts from the flag generator
(`../evolution-mortgage-tailgate-flag/source/`) and expects Poppins and Inter TTFs in a `fonts/` folder
next to it, so copy those alongside before running. Arguments: width in, height in, `white` or `navy`,
emblem path (or `-` for the placeholder).
