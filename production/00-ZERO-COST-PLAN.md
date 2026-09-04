# "Under the Ice" — Zero-Additional-Cost Production Plan

**Budget: $0 beyond an existing Claude Pro subscription.**
No Higgsfield. No paid credits. Nothing in this plan requires a purchase.

> **Verify before relying on any free tier.** Free-tier limits change constantly and my
> information has a cutoff. Every third-party allowance below is marked with a confidence
> level. The **UNLIMITED / LOCAL** and **PUBLIC DOMAIN** rows are the ones that cannot be
> withdrawn from you — the plan is built so those carry the video even if every hosted free
> tier disappeared tomorrow.

---

## The core decision: stop trying to AI-generate 5 minutes of video

Generating 300 seconds of AI video is the single most expensive way to build this, and it is
also **not how most successful faceless channels actually work.** They are mostly *stills with
motion*, cut fast, over a strong voice.

That is lucky, because free AI **image** generation is far more abundant than free AI **video**,
and free **public-domain footage** of exactly this subject already exists — NASA and NOAA have
enormous archives of Antarctic, glacier, ice-sheet and satellite material in the public domain.

### The 4-way media split

| Type | Shots | Share | Cost |
|---|---|---|---|
| **Motion graphics** built in DaVinci Resolve | 13 | 43% | $0, unlimited |
| **AI stills** + Ken Burns / 2.5D parallax | 8 | 27% | $0, free daily tiers or local |
| **Public-domain footage** (NASA/NOAA/Pexels) | 4 | 13% | $0, unlimited |
| **AI video** — hero moments only | 5 | 17% | $0, free daily tiers, gathered over ~3 days |

Only **5 shots** actually need AI video. That is comfortably inside free daily allowances,
and if every free video tier failed you, all 5 degrade gracefully to AI stills with motion.

---

# 1. FINAL 5-MINUTE SCRIPT

30 blocks x 10s = **5:00**. One narration line per block, 20-24 words, ~9s spoken at 150wpm.
Total ~640 words.

| # | Narration |
|---|---|
| 01 | There's a hole in Antarctica. Two feet wide. It drops through six hundred metres of ice into water no light has ever touched. |
| 02 | In 2020, scientists lowered a robot down that hole. They wanted to measure melting. They found out they'd been measuring the wrong thing. |
| 03 | The glacier is called Thwaites. Researchers have another name for it. They call it the Doomsday Glacier. That is not marketing. |
| 04 | Antarctica is not land with snow on top. It is rock, buried under an ice sheet up to four kilometres thick. |
| 05 | Stand on that surface, and the real ground sits further below you than a passenger jet flies above you. |
| 06 | Thwaites itself is roughly the size of Great Britain. One glacier. Larger than most countries on Earth. And it is moving. |
| 07 | Here is what makes it dangerous. The rock beneath Thwaites sits below sea level, and it slopes downward as you travel inland. |
| 08 | That means the ocean can reach underneath it. Warm water slides in from the sea and eats the glacier from below. |
| 09 | From above, nothing looks wrong. The surface is white, solid, still. For decades, that surface was all we could actually see. |
| 10 | So a British and American team flew onto the ice with a hot water drill, and started melting a hole straight down. |
| 11 | It took days. The borehole had to be kept warm the whole time, or it would freeze shut and swallow the equipment. |
| 12 | The robot is called Icefin. Three and a half metres long, thin enough to fit down a shaft barely wider than a dinner plate. |
| 13 | It carries cameras, sonar, and sensors for temperature and salt. A cable feeds power down, and sends data back up. |
| 14 | Icefin reached the bottom, swam sideways into the cavity, and became the first machine to see where Thwaites meets the sea. |
| 15 | And the ceiling above it was not flat. Not smooth. Not anything the models had drawn. It was carved into shapes. |
| 16 | Terraces, like a staircase. Deep vertical cracks. Sloped walls. An entire hidden landscape, hanging upside down above the water. |
| 17 | Then the team compared melt rates across that landscape, and the result did not match the predictions. Not even close. |
| 18 | Across the flat stretches, the ice was melting more slowly than expected. Slower. That was better news than anyone had hoped for. |
| 19 | But inside the cracks, and along the sloped walls, the melting was fast. In places, several times faster than the flat ice. |
| 20 | So the glacier was not dissolving evenly, like an ice cube in a glass. It was being unpicked, along its weak points. |
| 21 | That distinction matters far more than the raw numbers. Here is exactly why it changes every forecast we had. |
| 22 | Ice that melts evenly shrinks. Slowly. Predictably. You can model that, and project a century ahead with some confidence. |
| 23 | Ice that fails along its cracks does not shrink. It fractures. And fracturing holds, and holds, and then goes all at once. |
| 24 | Now add the ground. The bedrock slopes inland and downward, so every retreat carries the glacier into deeper water. |
| 25 | Deeper water means more warm ocean touching more ice, which pushes the grip point back further, into deeper water again. |
| 26 | That is a feedback loop. A system that, once it truly starts, helps itself along without needing any more push. |
| 27 | And I want to be straight with you, because this part gets exaggerated constantly. We do not know Thwaites has crossed that line. |
| 28 | Scientists genuinely disagree on how close it is. Some models say centuries. Anyone giving you a firm date is selling something. |
| 29 | Thwaites alone holds enough ice to raise global sea level by half a metre. It also acts as a cork, holding back far more. |
| 30 | We built a robot to discover our own planet wasn't shaped the way we thought. What would you send a camera into? Subscribe. |

---

# 2 + 3 + 4 + 5. 30-SHOT STORYBOARD, PROMPTS, MEDIA TYPE, TOOL

**Legend:** `GFX` = motion graphic built in DaVinci · `IMG` = AI still + camera move ·
`STOCK` = public-domain footage · `VID` = AI video (hero only)

## The STYLE LOCK
Append **verbatim** to every AI image and video prompt. This is what makes 30 shots look like
one video. Never edit it mid-project.

```
STYLE LOCK v2:
Stylized 3D scientific visualization, deliberately not photorealistic and not archival
documentary footage. Cold desaturated palette limited to bone white, glacial teal, and deep
navy black. Volumetric light, soft atmospheric haze, fine film grain. Cinematic widescreen
16:9 framing, shallow depth of field. No people, no faces, no hands, no text, no letters,
no numbers, no logos, no watermarks.
```

**Why non-photoreal:** the Icefin/Thwaites survey is a real expedition. Photoreal AI output
would be fabricated documentary footage of a real scientific event — dishonest, and it invites
"is this even real?" comments that kill a science channel's credibility. A stylized register is
truthful, reads as deliberate art direction, and holds together far better across 30 shots.

**Why no generated text:** AI renders letterforms badly and differently every time. Every label,
arrow, number and callout is added in DaVinci over clean plates. Cheaper, better, repeatable.

---

### ACT 1 — THE HOOK (01-09)

| # | Type | Tool | Prompt / build note |
|---|---|---|---|
| 01 | **VID** | Kling / Hailuo free daily | `A narrow dark vertical borehole, roughly half a metre wide, at the centre of a vast empty ice plain stretching to a flat horizon. Fine dry snow streams in low ribbons across the surface. The camera pushes slowly and continuously forward toward the opening; the hole stays centred and grows; the horizon stays level. Flat overcast polar daylight, no visible sun, shadowless.` + STYLE LOCK |
| 02 | IMG | Free image gen | `A slender yellow torpedo-shaped underwater robot suspended on a cable, descending into a narrow dark shaft cut through pale blue ice, seen from slightly above.` + STYLE LOCK — **DaVinci: slow push-in + slight downward drift** |
| 03 | GFX | DaVinci + NASA | NASA Blue Marble Antarctica still, slow zoom to West Antarctic coast, animated pin drop. Title card typed in DaVinci. |
| 04 | IMG | Free image gen | `A cross-section of the Antarctic ice sheet against a dark background: dark bedrock at the base, a vast pale ice mass above it, thin ocean layer to one side. Matte museum-diorama surfaces, even lighting.` + STYLE LOCK — **labels in DaVinci** |
| 05 | GFX | DaVinci | Vertical scale bar: tiny figure silhouette on ice surface, bedrock far below, jet far above. Pure vector, built in Fusion. |
| 06 | GFX | DaVinci + NASA | NASA Antarctic satellite base, Thwaites outline animated on, Great Britain silhouette scaled and overlaid for comparison. |
| 07 | IMG | Free image gen | `A clean side-view cross-section diorama: dark bedrock sloping downward from left to right, thick pale ice resting above it, dark water to the right. Matte self-illuminated surfaces, dark empty background.` + STYLE LOCK |
| 08 | GFX | DaVinci | Reuse shot 07 plate. Animate warm-current arrows pushing under the ice base. Arrows drawn in Fusion. |
| 09 | **STOCK** | Pexels / NASA | Aerial drift over featureless Antarctic ice plain. Search: "Antarctica aerial", "ice sheet drone", "polar plateau". |

### ACT 2 — THE EXPEDITION (10-14)

| # | Type | Tool | Prompt / build note |
|---|---|---|---|
| 10 | IMG | Free image gen | `A small remote polar field camp on a flat ice plain: a drilling rig, coiled hoses, equipment crates, low tents. Overcast flat daylight, no people visible.` + STYLE LOCK — **slow lateral drift** |
| 11 | IMG | Free image gen | `A thick insulated hose descending into a narrow hole in thick ice, faint steam rising from the opening into cold air, equipment in soft focus behind.` + STYLE LOCK — **slow push-in** |
| 12 | IMG | Free image gen | `A slender yellow cylindrical underwater robot in profile against a dark neutral background, thrusters and lamp housings visible, engineering-model presentation.` + STYLE LOCK — **slow lateral truck** |
| 13 | GFX | DaVinci | Reuse shot 12 plate. Animate component callout lines and labels in Fusion. |
| 14 | **VID** | Kling / Hailuo free daily | `A slender yellow underwater robot emerges from a narrow vertical ice shaft into a vast dark open water cavity, its lamps switching on and cutting two beams into the blackness. The camera follows behind it and slowly widens out.` + STYLE LOCK |

### ACT 3 — THE DISCOVERY (15-20) — the payload

| # | Type | Tool | Prompt / build note |
|---|---|---|---|
| 15 | **VID** | Kling / Hailuo free daily | `Looking upward at the underside of a glacier from within dark still seawater. A single hard lamp below frame rakes slowly across the ice, revealing an uneven carved ceiling, falling off sharply into black. Fine sediment drifts through the beam. The camera cranes slowly upward.` + STYLE LOCK |
| 16 | **VID** | Kling / Hailuo free daily | `The underside of a glacier carved into wide shallow terraces like an inverted staircase, broken by deep vertical fissures and steeply sloped walls, lit by one hard moving lamp from below. The camera tilts up and tracks slowly along the ceiling.` + STYLE LOCK |
| 17 | GFX | DaVinci | Split screen: shot 15 plate (flat) vs shot 16 plate (crevassed). Animated melt arrows, differing rates. |
| 18 | GFX | DaVinci | Flat-ice panel isolated, slow melt arrows, a downward-trending line drawn on. |
| 19 | GFX | DaVinci | Crevasse panel isolated, rapid melt arrows cutting into the walls. Deliberately faster animation than 18 — the contrast *is* the point. |
| 20 | IMG | Free image gen | `Two ice blocks side by side against a dark background: the left one smooth and evenly rounded, the right one split along sharp internal seams. Matte diorama surfaces.` + STYLE LOCK — **DaVinci: slow reveal L to R** |

### ACT 4 — THE MECHANISM (21-26)

| # | Type | Tool | Prompt / build note |
|---|---|---|---|
| 21 | GFX | DaVinci | Text beat over a darkened, slowly drifting shot-16 plate. Kinetic type. |
| 22 | GFX | DaVinci | Smooth shrinking-volume animation with a steady, confident projection curve. |
| 23 | **STOCK** | Pexels / NOAA | Real glacier calving footage — abundant, free, and more visceral than anything AI will give you. Search: "glacier calving", "ice collapse". |
| 24 | GFX | DaVinci | Reuse shot 07 plate. Animate the grounding line retreating down the reverse slope. |
| 25 | GFX | DaVinci | **Identical to 24, one step further back.** The repeat *is* the argument — the loop is shown, not narrated. |
| 26 | GFX | DaVinci | Circular loop diagram: retreat → warm water → retreat. Fusion vectors. |

### ACT 5 — HONESTY + STAKES (27-30)

| # | Type | Tool | Prompt / build note |
|---|---|---|---|
| 27 | GFX | DaVinci | Clean two-column type: "What we know / What we don't." Plain, calm, high contrast. |
| 28 | GFX | DaVinci | Divergent projection curves fanning out from today into a wide uncertainty cone. |
| 29 | GFX | DaVinci + NASA | NASA satellite base. Thwaites highlights, then the wider West Antarctic sheet lights up behind it. |
| 30 | **VID** | Kling / Hailuo free daily | `Looking up a narrow vertical ice shaft from deep below toward a small distant circle of pale daylight at the top, robot lamps receding downward away from the opening, particles drifting in the beam. The camera slowly falls away from the light.` + STYLE LOCK |

**Tally: 13 GFX · 8 IMG · 4 STOCK · 5 VID.**

---

# 5. FREE TOOLS

### AI video — only 5 shots needed (01, 14, 15, 16, 30)
| Tool | Free allowance | Confidence |
|---|---|---|
| **Kling AI** | Daily free credits, refreshes every 24h | Medium — was the most generous free video tier |
| **Hailuo / MiniMax** | Daily free generations | Medium |
| **Vidu** | Daily free credits | Medium |
| **Pixverse** | Daily free credits | Medium |
| **Krea** | Daily free tier | Medium |
| **ComfyUI + Wan 2.2 / LTX-Video / HunyuanVideo, local** | **UNLIMITED** | **High — open weights, cannot be revoked** |

**Strategy:** 5 clips over ~3 days on daily free tiers, rotating services. If you have a GPU
(8GB+ VRAM), run Wan 2.2 locally instead and the constraint disappears entirely. Google Colab's
free tier can also host ComfyUI, with session limits.

### AI images — 8 shots
| Tool | Free allowance | Confidence |
|---|---|---|
| **Stable Diffusion / Flux, local via ComfyUI or A1111** | **UNLIMITED** | **High — open weights** |
| Microsoft Designer / Bing Image Creator | Generous daily DALL·E boosts | Medium |
| Google ImageFX | Free with a Google account | Medium |
| Leonardo.ai | ~150 tokens/day | Medium |
| Ideogram | Free daily | Medium |
| Krea | Free daily | Medium |

### Public-domain footage — 4 shots, plus map plates
| Source | Licence | Confidence |
|---|---|---|
| **NASA Scientific Visualization Studio** | **Public domain** — superb ice-sheet visualisations, exactly on topic | **High** |
| **NASA Earth Observatory / Worldview** | Public domain satellite imagery | **High** |
| **NOAA** | Public domain | **High** |
| Pexels / Pixabay / Videvo / Coverr | Free, no attribution required | High |

NASA SVS is the standout here. It has purpose-built Antarctic ice-sheet and grounding-line
visualisations that are both free and more scientifically accurate than anything you could
generate. Check each asset's page for credit requirements.

---

# 6. VOICEOVER — $0

The script is ~640 words / ~3,500 characters. Options, best first:

| Option | Cost | Quality | Confidence |
|---|---|---|---|
| **edge-tts** (Python: `pip install edge-tts`) | **Free, unlimited** | Very good neural voices | **High — no account, no key** |
| **Kokoro TTS** (local, open weights) | **Free, unlimited** | Excellent, very natural | **High** |
| **Piper TTS** (local, open) | Free, unlimited | Good | High |
| ElevenLabs free tier | ~10k chars/month | Best-in-class | Medium — 3,500 chars fits, so ~1 video/month |
| **Your own voice** + a phone mic | Free | Depends on you | — |

**Recommendation: `edge-tts`.** It is genuinely free, needs no account, has no monthly cap,
and gives you neural voices. Generate each of the 30 lines as a separate file — that keeps them
aligned to blocks and lets you re-render one line without redoing the whole track.

```bash
pip install edge-tts
edge-tts --list-voices | grep en-GB      # audition; en-GB-RyanNeural is a good documentary read
edge-tts --voice en-GB-RyanNeural --rate=-5% \
         --text "There's a hole in Antarctica..." --write-media block01.mp3
```

**Lock one voice for the whole video and never change it mid-project.** Rate `-5%` to `-10%`
suits this material — the default is slightly fast for a wonder-driven read.

### Music and SFX — $0
YouTube Audio Library (cleared for YouTube), Pixabay Music, Freesound (check each CC licence),
Incompetech (CC-BY, credit in description). Wind and underwater ambience from Freesound will do
more for this video's atmosphere than any extra visual polish.

---

# 7. FREE EDITING WORKFLOW

**DaVinci Resolve (free version)** is the whole post pipeline. The free version is not a demo —
it is a professional grade tool, and critically it includes **Fusion**, which is where your 13
motion-graphic shots get built. Nothing else is needed.

| Page | Job here |
|---|---|
| **Media** | Import 30 VO files, all plates, stock, music |
| **Cut / Edit** | Lay VO first as the spine, then hang visuals on it |
| **Fusion** | Build all 13 GFX shots; animate arrows, labels, curves, maps |
| **Color** | The consistency saviour — see below |
| **Fairlight** | VO levelling, ducking music under narration |
| **Deliver** | YouTube 1080p preset, H.264 |

### The trick that makes mixed sources look like one video
Your footage comes from 4 different origins and *will* mismatch. Fix it in Color, not in the
generators:

1. Grade every clip to the same palette — cold, desaturated, teal-and-bone.
2. Put **one shared adjustment clip across the entire timeline**: a subtle film grain, a slight
   vignette, and a unifying cool tint.
3. That single layer is what makes AI stills, AI video, NASA footage and Fusion graphics read as
   one production. It matters more than any individual asset's quality.

### Subtitles — free, and worth it
Resolve free can auto-transcribe on recent versions; otherwise generate an SRT with **Whisper**
(`pip install openai-whisper`, runs locally, free, unlimited) from your VO track, import it,
style it, and burn it in. Alternatively CapCut's free auto-captions.

### Ken Burns on the 8 AI stills
Generate stills at the **largest size the free tool allows** — you need headroom to move within
the frame. In Resolve, keyframe Zoom from 1.00 to ~1.12 across the shot, with a small Position
drift, and ease both ends. Never let a still sit motionless; it reads as a broken video.
For 2 or 3 hero stills, cut the subject onto its own layer and offset its move slightly against
the background for a cheap 2.5D parallax that looks far more expensive than it is.

---

# 8. STEP-BY-STEP PRODUCTION WORKFLOW

### Phase 0 — Setup (once)
1. Install DaVinci Resolve (free), Python, `edge-tts`, and Whisper.
2. Optional but transformative: install ComfyUI + a local image model, and Wan 2.2 if your GPU
   allows. This converts every "free daily limit" into "unlimited".
3. Create folders: `/vo /img /vid /stock /gfx /music /project`.

### Phase 1 — Voice first (30-60 min) — **do this before any visuals**
4. Generate all 30 VO lines with `edge-tts`, named `block01.mp3` … `block30.mp3`.
5. Check each line's duration. Any line over ~9.5s: shorten the words, do not slow the read.
6. Lay all 30 into Resolve on a 5:00 timeline. **This is now your spine.** Every visual gets cut
   to it. Building visuals before the voice is the classic faceless-channel mistake — you end up
   with beautiful shots that don't fit.

### Phase 2 — Free assets, no generation (1-2 hrs)
7. Pull the 4 stock shots (09, 23) and NASA map plates (03, 06, 29) from NASA SVS / Pexels.
8. Drop them into the timeline as blocking. Half your Act-1 and Act-4 visuals now exist for $0
   and zero generation.

### Phase 3 — AI stills (1-2 hrs)
9. Generate the 8 IMG shots. **STYLE LOCK verbatim on every prompt.**
10. Generate shot 07 first — it is reused as the plate for 08, 24 and 25. One good render covers
    four shots.
11. Regenerate anything off-palette *now*, before it is buried in the edit.

### Phase 4 — AI video, hero shots only (spread over ~3 days)
12. Five clips: **01, 14, 15, 16, 30**. Free daily tiers refresh every 24h, so take 2 on day one,
    2 on day two, 1 on day three, rotating between Kling / Hailuo / Vidu as limits allow.
13. Generate **01 first**. It defines the look. Where a service accepts an image reference, feed
    a frame from 01 into 14/15/16/30 to hold palette across them.
14. **If a clip won't come out right after 2 or 3 attempts, drop to an AI still with a strong
    camera move.** Do not burn three days of free allowance on one shot. In a finished edit,
    under narration and grain, a well-moved still is nearly indistinguishable.

### Phase 5 — Motion graphics (3-5 hrs, the biggest block of real work)
15. Build the 13 GFX shots in Fusion. Do them in this order — each reuses the last:
    - 07 plate → 08 (arrows) → 24 (retreat) → 25 (retreat repeated)
    - 17 → 18 → 19 (the melt-rate trio)
    - 05, 21, 22, 26, 27, 28 as standalone
16. Keep every label on its own layer so text can be fixed without re-rendering the animation.

### Phase 6 — Assembly
17. Cut all visuals to the VO spine. Trim to the frame where each line lands.
18. Add music at roughly −22 dB under the voice, ducking further beneath narration.
19. Add wind ambience across Acts 1-2, underwater ambience across Act 3.

### Phase 7 — The unification pass (do not skip)
20. Grade every clip toward the same cold palette in the Color page.
21. Add the **single shared adjustment layer** — grain, vignette, cool tint — over the whole
    timeline. This is the step that makes it look like one video.
22. Whisper → SRT → import → style → burn in.

### Phase 8 — Deliver
23. Export YouTube 1080p H.264.
24. Thumbnail: build it in Resolve or GIMP (free) from your best shot-16 frame. Three words
    maximum, heavy sans, high contrast.
25. Publish chapters in the description — this format's segment independence means chapters
    *raise* average view duration rather than lowering it.

---

## Realistic time budget
| Phase | Time |
|---|---|
| Voice | 1 hr |
| Free assets | 1.5 hrs |
| AI stills | 1.5 hrs |
| AI video | 3 days elapsed, ~1 hr hands-on |
| Motion graphics | 4 hrs |
| Assembly + grade + subs | 3 hrs |
| **Total** | **~12 hrs work, ~4 days elapsed, $0** |

Videos 2 and 3 drop to roughly 6-7 hours: the STYLE LOCK, the Fusion graphic templates, the
voice setting and the grade layer all carry over. **That reuse is the actual system** — the
first video is where you build the templates, not just the video.

## What this plan gives up, honestly
- **Motion variety.** 13 graphics and 8 moved stills means fewer moving photographic shots than
  a fully-generated video. Mitigated by fast cutting and a strong voice — and this is genuinely
  what most successful channels in this format already do.
- **Free-tier friction.** Daily caps mean AI video is spread over days. Local models remove this
  entirely if you have the GPU.
- **Time instead of money.** ~12 hours of your work replaces the spend. That is the trade, and
  for learning the workflow it is the better side of it.
