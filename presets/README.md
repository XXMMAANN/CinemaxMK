# CinemaxMK Fuji Retro – Lightroom presets

Five film-style Develop presets inspired by classic Fujifilm colour-negative films and
film simulations. They are standard `.xmp` presets, so they install into Adobe Lightroom
Classic, Lightroom (desktop), Lightroom mobile and Photoshop's Camera Raw, and show up
as one preset group called **CinemaxMK Fuji Retro**.

Download everything at once: [`CinemaxMK-Fuji-Retro-Lightroom-Presets.zip`](CinemaxMK-Fuji-Retro-Lightroom-Presets.zip)
(or grab the individual files from [`lightroom/`](lightroom/)).

![All five looks side by side](previews/all-presets.png)

Previews are a rough simulation of the sliders on a synthetic test card; Lightroom's own
rendering on a real photo is the reference.

## The five looks

| Preset | Character | Try it on |
| --- | --- | --- |
| **01 Superia 400** | Warm consumer negative: green-cyan shadows, yellow-warm highlights, cyan-leaning skies, punchy reds, lifted film base, 400-speed grain. | Everyday snapshots, street, golden hour |
| **02 Classic Chrome** | Muted magazine / documentary feel: steel-cyan blues, deeper reds, hard shadows and soft highlights. | Street, urban scenes, overcast days |
| **03 Pro 400H** | Airy pastel: lifted mint shadows, soft cyan skies, pale peachy skin, low contrast, fine grain. | Portraits, weddings, bright daylight |
| **04 Nostalgic Neg** | 1970s "American New Color": amber highlights, rich warm midtones, quiet greens and blues, light fade. | Interiors, evening light, nostalgic scenes |
| **05 Classic Neg** | Contrasty drugstore print: cyan-green shadows, warm highlights, reds pulled toward magenta, muted olive greens. | Street, harsh light, snapshots |

Per-preset before/after previews live in [`previews/`](previews/).

## Install

### Lightroom Classic (Windows / macOS)

1. Download the zip and unzip it.
2. Open the **Develop** module, click **+** at the top of the **Presets** panel and choose **Import Presets…**
3. Select the five `.xmp` files (recent versions also accept the zip itself) and click **Import**.

Manual alternative: copy the unzipped `CinemaxMK Fuji Retro` folder into the Camera Raw settings folder and restart Lightroom.

- Windows: `%APPDATA%\Adobe\CameraRaw\Settings\`
- macOS: `~/Library/Application Support/Adobe/CameraRaw/Settings/`

### Lightroom (desktop, cloud version)

Open a photo in **Edit**, open **Presets**, click the **…** menu and choose **Import Presets…**, then pick the `.xmp` files or the zip. Imported presets sync to your other devices.

### Lightroom mobile (iOS / Android)

- Easiest: import them on Lightroom desktop or Lightroom Classic while signed in with the same Adobe ID; they sync to the phone automatically.
- Directly on the phone: copy the `.xmp` files to the device (Files / Downloads), open a photo in Lightroom, tap **Presets**, tap the **…** menu, choose **Import Presets** and select the files.

### Photoshop (Camera Raw)

Camera Raw reads the same settings folder as Lightroom Classic, so the manual copy above works. You can also use the **…** menu in Camera Raw's Presets panel and choose **Import Profiles & Presets**.

## Using them

- **Set exposure and white balance first.** The presets deliberately leave Exposure and White Balance untouched, so they stack on top of your basic correction instead of undoing it.
- **Amount slider.** In current Lightroom versions a preset amount slider appears when a preset is selected; 60–80 % gives a subtler version of each look.
- **Profile.** They are tuned for the *Adobe Color* / *Adobe Standard* profiles on raw files and the default *Color* profile on JPEG/HEIC. On Fujifilm raw files, do not stack them on a camera-matching profile such as *Camera CLASSIC CHROME*, or the effect doubles up.
- **Grain and vignette** are part of the look; lower them in the Effects panel if you export small or want a cleaner file.
- **03 Pro 400H** likes an extra +0.3 to +0.7 EV of exposure for the true high-key pastel feel.

## What each preset changes

Included: Basic tone (Contrast, Highlights, Shadows, Whites, Blacks), Presence (Texture, Clarity, Dehaze, Vibrance, Saturation), point curve (RGB plus Red / Green / Blue channels), HSL, Color Grading, Calibration, Grain and Post-Crop Vignette.

Left alone: Exposure, White Balance, profile, crop, lens corrections, sharpening, noise reduction, transform and masks. No process version is written, so the presets never downgrade or upgrade a photo's process version.

## Rebuilding or tweaking

The presets are generated from [`../tools/build_fuji_retro_presets.py`](../tools/build_fuji_retro_presets.py). Edit the slider values in the `LOOKS` list and run:

```bash
pip install numpy pillow
python3 tools/build_fuji_retro_presets.py
```

Each preset keeps a stable UUID, so re-importing a rebuilt version replaces the old one instead of creating duplicates.

## Notes

These presets are independent work inspired by the character of Fujifilm films and film simulations. They are not affiliated with, endorsed by or sponsored by FUJIFILM Corporation, and the film names are used only to describe the inspiration for each look.
