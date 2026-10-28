# Evolution Mortgage – navy tablecloth (72 × 54 in)

Flat rectangular tablecloth, 72 × 54 in, navy field with a soft centre glow and the white Evolution Mortgage lockup.
Same navy as the navy tailgate flag: `#0B1F3F` at the edges to `#163D72` at the centre.

![proof](proof.png)

## Layout

On a standard 6 ft table (72 × 30 in top) the 54 in width hangs 12 in over the front and the back, with no side drop.
The main file puts the lockup on the **front drop**, 22 in wide, centred in the 12 in band, so it stays visible when the
table top is covered with food and coolers. `alternates/logo-centered/` has the lockup 34 in wide in the middle of the
cloth, for a table that will stay clear or for a different table size.

## Files

| File | Use |
| --- | --- |
| `…-PRINT-bleed-1in.pdf` | **Send this.** 74 × 56 in page = 72 × 54 in finished + 1 in bleed all round. Vector. |
| `…-trim.pdf` | Exact 72 × 54 in, for printers that add their own hem or bleed. |
| `…-PROOF-guides.pdf`, `proof.png` | Proof only: trim, the 6 ft table top and the front drop. |
| `….svg` | Editable vector master. |

## Ordering notes

- Ask for dye-sublimated polyester (twill or poplin), hemmed on all four sides. It is machine washable and wrinkle resistant.
- Confirm the printer's hem allowance. If their template is a different size, the layout regenerates in seconds.
- Regenerate with `python3 source/make_tablecloth.py` next to the flag generator (`../evolution-mortgage-tailgate-flag/source/make_flag.py`).
