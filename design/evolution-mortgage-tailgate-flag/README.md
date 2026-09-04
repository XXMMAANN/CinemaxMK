# Evolution Mortgage – tailgate sponsor flag (3 × 5 ft)

Print-ready artwork for a 3 ft × 5 ft (36 × 60 in) landscape sponsor flag in two colorways,
built from the approved logo files in the brand kit and the rules in the Design & Template HQ.

- **Navy** (recommended for a tailgate): white logo lockup on a deep navy field. Reads from across a lot, hides dust and handling.
- **White**: the full-color logo (blue gradient, red helix) on a white field, navy type.

Same layout in both: logo only, 47 in wide and centred, with the helix mark repeated as a faint watermark on the fly edge.
A version with the tagline "Home loans made simple." and the NMLS / Equal Housing footer is kept in `alternates/with-tagline/` in case compliance wants it on the flag.

## Files

| File | Use |
| --- | --- |
| `…-navy-PRINT-bleed-1in.pdf` / `…-white-PRINT-bleed-1in.pdf` | **Send this to the printer.** 62 × 38 in page = 60 × 36 in trim + 1 in bleed on every side. All text outlined, no fonts needed. Navy is pure vector; white embeds the brand's color logo as a clipped fill inside vector edges. |
| `…-trim.pdf` | Same art at exact trim size (60 × 36 in), for printers that add their own bleed. |
| `…-PROOF-guides.pdf` | Proof only. Shows trim, 1 in bleed, safe area and hoist side. Do not print this one. |
| `…-navy.svg`, `…-navy-BLEED-1in.svg` (and white) | Editable vector masters (Illustrator, Inkscape, Affinity). |
| `…-6000x3600.png` | Raster fallback, 100 px per inch at full size. |
| `preview-*.png`, `mockup-*.png` | For approvals and sharing. |
| `source/` | Generator scripts, traced logo paths and the color-logo fill, so the art can be regenerated or edited in code (`python3 make_flag.py A navy`). |

## Specs

- Trim size 60 × 36 in, landscape. Hoist (pole side) is the left edge.
- Bleed 1 in. Safe area 3 in on all sides, 4 in on the hoist (room for a pole sleeve or grommet header).
- Colors (RGB masters, printer converts): navy `#0B1F3F`, glow centre `#163D72`, deep blue `#1456AA`, cyan `#21A0DE`, white.
- Type (alternate version only): Poppins SemiBold (tagline) and Inter Medium (footer), converted to outlines. The main files carry no text besides the logo.
- Logos: approved white lockup (vectorized from the brand PNG) on navy; approved full-color lockup on white. Helix mark repeated at 6–7 % as a fly-edge watermark.

## Ordering notes

- Material: 200D / 110 gsm knitted polyester, dye-sublimation print.
- Single-reverse (standard, cheapest) prints one side and shows through mirrored on the back; the logo still reads, the small text reverses. Order double-sided (2-ply with blockout liner) if the flag will be read from both sides.
- Finish: pole sleeve for a telescoping tailgate pole, or canvas header with brass grommets. Ask for double-stitched hems and a 4-row fly-end hem for wind.
- White polyester shows dirt quickly outdoors; navy is the safer pick for repeated tailgates.

## Brand compliance

- The main files are logo only: no claims, no rates, no officer names.
- If the flag needs the company NMLS #2432729 and the Equal Housing Opportunity mark, use the files in `alternates/with-tagline/` or regenerate with `python3 make_flag.py A navy full`; a loan officer line ("Name · NMLS #xxxxxx") can be added to that footer.
