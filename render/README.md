# Scene renderer — "Under the Ice"

Procedural renderer for the 30 documentary scenes. Pure Python + Pillow, no paid
services and no external assets.

- `style.py`  — the shared visual system: palette, gradients, haze, grain, vignette.
  Every scene ends by passing through `finish()`, which is what makes 30 separate
  images read as one film.
- `scenes.py` — 30 scene functions, one per narration block, matched to the script.
- `encode.py` — camera-move + encode pass. **Does not run in this container**: the
  only ffmpeg available here is a Playwright screen-recorder build with no H.264,
  no scale/crop/zoompan filters and no PNG decoder. Kept for use on a machine with
  a normal ffmpeg.

## Rebuild the stills
```bash
python3 -m pip install Pillow
python3 -c "import sys; sys.path.insert(0,'.'); import scenes, os; \
os.makedirs('stills', exist_ok=True); \
[f().save(f'stills/s{i:02d}.png') for i,f in enumerate(scenes.SCENES,1)]"
```
Outputs 30 PNGs at 2560x1440 — oversized on purpose, so a pan or zoom in the editor
has pixels to work with at a 1080p delivery.

Generated images are gitignored; the code is the source of truth.
