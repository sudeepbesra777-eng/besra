# "Under the Ice" — Complete Workflow in Shotcut (Windows, ₹0)

**Editor: Shotcut.** Replaces DaVinci Resolve throughout this project.

## Why Shotcut

| Requirement | Shotcut |
|---|---|
| Free | Yes — GPL-3.0 open source, no account, no sign-up |
| Commercial / monetised YouTube use | **Permitted.** GPL licence, no restriction on output |
| Watermark | None. "The only watermarks are the ones you add" |
| Export limit | None. Up to 8K; you need 1080p |
| Windows | Yes — Windows 10 and 11 |
| Runs on modest hardware | Yes — far lighter than Resolve |

Version 26.8.1 as of August 2026.

**Why not the alternatives:** Clipchamp is built into Windows 11 and is the gentlest starting
point, but it needs a Microsoft account and is weaker at the two things this project actually
needs — shape masks and precise keyframing. CapCut is fast to learn but its licensing around
built-in assets is murkier for a monetised channel. Shotcut's GPL licence is the cleanest
possible answer to "can I monetise this?"

---

## What this project needs, and the Shotcut feature that does it

| Job | Shotcut tool |
|---|---|
| 30 narration files at exact 10s marks | Playhead timecode + **B** (overwrite) |
| Slow push-in (Ken Burns) | Filter: **Size, Position & Rotate** with keyframes |
| The dark borehole | Filter: **Mask: Simple Shape** (ellipse) |
| Cool cinematic grade | Filters: **White Balance** + **Saturation** |
| Vignette | Filter: **Vignette** |
| Applying the grade to everything at once | **Timeline → Output** master filters *(fallback: build the filter stack on one clip, then Copy Filters → Paste Filters onto the rest)* |
| Titles and labels | Filter: **Text: Rich** |
| Subtitles | Built-in **Subtitles** panel, or import an SRT |
| Export | **Export** panel → YouTube preset |

---

## THE COMPLETE WORKFLOW

### PHASE A — Setup
1. Install Shotcut from **shotcut.org/download** (take the installer, not the portable zip)
2. **Settings → Video Mode → HD 1080p 30 fps** — do this **before** adding any clip
3. Save the project into `07_project\` as `under-the-ice.mlt`

### PHASE B — Voiceover (may already be done)
4. 30 narration files from `edge-tts`, `block01.mp3` … `block30.mp3`, in `01_vo\`
5. Verify: 30 files, none longer than 9.5 seconds

### PHASE C — The spine
6. Add one audio track (**Ctrl+U**) and two video tracks (**Ctrl+I** twice)
7. Place each `blockNN.mp3` at its 10-second mark using the timecode + **B** method
8. Result: a 5:00 timeline, narration only, no pictures. **This is the backbone** — every
   visual afterwards is cut to a slot that already exists.

### PHASE D — Visuals, shot by shot
9. Follow `PHASE-2-SOURCING.md`. Per shot: place the clip on the video track at its
   10-second mark, trim to 10 seconds, add its motion filter.
10. Order of work: free downloads first, then the reusable plates, then AI shots last.

### PHASE E — The unifying grade
11. Build the grade once, apply it to the whole timeline via **Output** master filters.
12. This is what makes stock footage, NASA imagery and your own graphics read as one film.

### PHASE F — Sound
13. Music bed at roughly −22 dB under the narration
14. Wind ambience across Acts 1–2, underwater ambience across Act 3

### PHASE G — Subtitles and export
15. Generate subtitles, style them, burn them in
16. **Export → YouTube 1080p** into `08_export\`

---

## Honest caveat
I can't run Shotcut to verify each click, so some menu names may differ slightly in your
version. If a step doesn't match what you see on screen, tell me what *is* there and I'll
correct it rather than guess again.
