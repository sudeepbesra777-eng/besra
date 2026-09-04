# Seedance 2.5 — 3-Shot Style Test

**Purpose:** prove the visual system on the three hardest registers before committing to 30 blocks.
**Pipeline:** Claude (research/script/storyboard/direction/prompts) → Seedance 2.5 (clips only) →
CapCut/DaVinci (VO, music, subtitles, labels, assembly).
**Global settings:** `model: seedance_2_5` · `16:9` · **`generate_audio: false`**

## Test tier (REVISED — cost-optimised)
Run the test at **480p**. Production stays 1080p.

| Shot | Res | Dur | Credits | Why this length |
|---|---|---|---|---|
| A establishing | 480p | 4s | 10 | Simple slow push-in; palette is judged in the first second |
| B hero reveal | 480p | **10s** | 25 | The one shot where temporal stability must be proven at full block length |
| C diagram | 480p | 4s | 10 | Static geometry, locked truck; legibility is judged instantly |
| | | | **45 total** | |

**Absolute floor** if you want it cheaper: all three at 4s = **30 credits**. The extra 15 credits on
Shot B buy the single most valuable piece of information in the test — see "Why B stays at 10s".

### Measured price curve (get_cost, audio off, 16:9)
Cost is **purely per second of output** — shot length is not a lever, only resolution is.

| Res | Credits/sec | 4s | 10s | **Full 5:00 (300s)** |
|---|---|---|---|---|
| 480p | 2.5 | 10 | 25 | 750 |
| 720p | 6.5 | 26 | 65 | 1,950 |
| 1080p | 9.0 | 36 | 90 | 2,700 |

Splitting a 10s block into two 5s shots costs exactly the same as one 10s shot. Cut as often as
the edit wants — more cuts are free, and better for retention.

### Why B stays at 10s
Camera drift, geometry morphing and detail decay all **grow with duration**. A prompt that looks
perfect at 4s can fall apart at second 7. Shots A and C are slow single-axis moves over simple
subjects and will behave. Shot B is the hero: complex carved geometry, one hard moving light, a
crane-and-tilt. If it holds for 10s it holds anywhere, and that is the finding that de-risks the
other 27 blocks. Testing it at 4s would leave the project's biggest unknown untested.

---

## The STYLE LOCK

This exact string is appended **verbatim** to all 30 prompts. It is the consistency mechanism —
the single most important artifact in this system. Never edit it mid-project; if it changes,
every prior shot is off-model.

```
STYLE LOCK v1:
Stylized 3D scientific visualization, deliberately not photorealistic and not archival
documentary footage. Cold desaturated palette limited to bone white, glacial teal, and deep
navy black. Volumetric light, soft atmospheric haze, fine film grain. Cinematic widescreen
framing, shallow depth of field. No people, no faces, no hands, no text, no letters, no
numbers, no logos, no watermarks, no UI overlays.
```

### Three deliberate decisions inside it

**1. Non-photoreal, on purpose.** The Icefin/Thwaites survey is a real expedition. Photoreal output
would be fabricated documentary footage of a real scientific event — dishonest, and it invites
"is this real?" comments that poison a science channel's credibility. A stylized visualization
register is truthful, reads as intentional art direction, and is *far* more consistent shot-to-shot
because the model isn't chasing photographic realism it can't hold.

**2. No generated text, ever.** Video models render letterforms badly and differently every run.
All labels, arrows, callouts and numbers are added in DaVinci over clean plates. This is faster,
looks better, and is the single biggest repeatability win in the whole system.

**3. No people.** Cheaper, avoids the hardest failure mode in AI video, and keeps the channel
visually faceless as well as vocally.

### Consistency chain (order matters)
Shot A renders **first and alone** in `t2v`. A frame from its output then becomes the
`image_references` input for B and C in `omni_reference` mode, carrying palette, grain and
light quality forward. This is not a parallel batch of three.

---

# SHOT A — the cold open

| | |
|---|---|
| **2. Duration** | 10s |
| **3. Camera** | Slow continuous forward push-in (dolly). Hole stays centred and grows. Horizon stays level. No cuts, no rotation, no handheld. |
| **4. Subject/action** | A narrow dark borehole in a vast empty ice plain. Dry snow streams across the surface in low wind-driven ribbons. Nothing else moves. |
| **5. Style & lighting** | Flat overcast polar daylight, no visible sun, high-key and near-shadowless. Cold, bright, empty. Establishes the palette. |
| **6. Reference images** | **None** — pure `t2v`. This shot *creates* the look. Everything downstream references it. |
| **7. Narration line** | "There's a hole in Antarctica. Two feet wide. It drops through six hundred metres of ice into water no light has ever touched." |
| **8. Connects to** | Match cut on the dark circle — Shot B begins inside that same hole, below the ice. Surface → subsurface. |

**1. Exact prompt:**
```
A narrow dark vertical borehole, roughly half a metre wide, at the centre of a vast empty ice
plain stretching to a flat horizon. Fine dry snow streams in low ribbons across the surface,
driven by steady wind. The camera pushes slowly and continuously forward toward the opening;
the hole remains centred in frame and grows larger; the horizon line stays level throughout.
Flat overcast polar daylight, no visible sun, high-key and shadowless.

[STYLE LOCK v1]
```

---

# SHOT B — the hero reveal

This is the payload shot of the entire video. If the test fails anywhere, it fails here.

| | |
|---|---|
| **2. Duration** | 10s |
| **3. Camera** | Slow upward crane with a gentle tilt up, revealing more ceiling as it rises. Steady, no roll. |
| **4. Subject/action** | The underside of a glacier seen from within dark water: wide shallow terraces like a staircase, broken by deep vertical fissures and steeply sloped walls. Sediment drifts through the light. |
| **5. Style & lighting** | A single hard lamp from below frame rakes across the ice, hard falloff into pure black at the edges. High-contrast, one source. The opposite of Shot A's flat daylight — that contrast is the point. |
| **6. Reference images** | **Yes.** `mode: omni_reference`, a frame from Shot A as `image_references`, to hold palette, grain and haze across a total lighting change. |
| **7. Narration line** | "Terraces, like a staircase. Deep vertical cracks. Sloped walls. An entire hidden landscape, hanging upside down above the water." |
| **8. Connects to** | Cuts to Shot C, which explains the geometry just revealed. Spectacle → mechanism; the standard explainer beat. |

**1. Exact prompt:**
```
Looking upward at the underside of a glacier from within dark, still seawater. The ice ceiling
is carved into wide shallow terraces resembling a staircase, broken by deep vertical fissures
and steeply sloped walls. A single hard lamp below the frame rakes slowly across the ice,
picking out texture and edges, falling off sharply into black at the corners. Fine sediment
particles drift slowly through the beam. The camera cranes slowly upward and tilts up,
revealing more of the carved ceiling as it rises.

[STYLE LOCK v1]
```

---

# SHOT C — the diagram register

The register most likely to break, and the one a science channel cannot do without.

| | |
|---|---|
| **2. Duration** | 10s |
| **3. Camera** | Slow steady lateral truck, left to right, parallel to the section. No rotation, no zoom, no perspective drift. |
| **4. Subject/action** | A clean cross-section model of a glacier system: dark bedrock sloping downward left to right, thick pale ice above it, a wedge of deep water intruding from the right along the contact between them. Static geometry; only the camera moves. |
| **5. Style & lighting** | Even, self-illuminated, matte — a physical museum diorama, not a screen graphic. Dark empty background so DaVinci labels have clean space to sit in. |
| **6. Reference images** | **Yes.** Same Shot A frame as `image_references`, so the diagram belongs to the same world as the photoreal-adjacent shots rather than looking like a pasted-in graphic. |
| **7. Narration line** | "Now add the ground. The bedrock slopes inland and downward, so every retreat carries the glacier into deeper water." |
| **8. Connects to** | Block 25 reuses this exact setup with the grounding line one step further back — the feedback loop shown as a repeat, not explained as a sentence. Regenerating the same prompt with a shifted water wedge is why the locked camera move matters. |

**1. Exact prompt:**
```
A clean cross-section diorama of a glacier system viewed directly from the side against a dark
empty background. The layers read clearly and separately: dark bedrock at the base sloping
downward from left to right, a thick pale ice mass resting above it, and a wedge of deep water
intruding from the right along the contact surface between ice and rock. Surfaces are matte and
softly self-illuminated, like a physical museum model under even light. The camera trucks slowly
and steadily from left to right, parallel to the cross-section, without rotating.

[STYLE LOCK v1]
```

---

## Exact call sequence

```
STEP 1 — alone, t2v  (10 credits):
generate_video { model:"seedance_2_5", mode:"t2v", prompt:"<SHOT A + STYLE LOCK>",
                 resolution:"480p", aspect_ratio:"16:9", duration:4, generate_audio:false }

STEP 2 — pull a clean frame from Shot A, then B and C via generate_video_batch (35 credits):
  B { model:"seedance_2_5", mode:"omni_reference", resolution:"480p", aspect_ratio:"16:9",
      duration:10, generate_audio:false,
      medias:[{ role:"image_references", value:"<shot A frame media_id>" }] }
  C { ...same, duration:4 }
```
`omni_reference` at 480p/4s prices at 10 credits — **identical to t2v**. Reference chaining is free.

## What to judge on delivery
1. **A → B → C palette drift.** Same world, or three different videos? This is the whole test.
2. **Shot B ice geometry.** Terraces readable as terraces, or mush?
3. **Shot C layer separation.** Are bedrock / ice / water distinct enough to label in DaVinci?
4. **Camera obedience.** Seedance holds slow single-axis moves well; if any shot drifts or adds
   a move, that's a prompt fix, not a model limit.
5. **Any leaked text or people** — if the negative clauses aren't holding, STYLE LOCK needs v2
   before block 4 onward.

## If the test passes
The remaining 27 blocks reuse this exact structure: STYLE LOCK verbatim, Shot A's frame as the
standing reference, one register per shot from the three proven here. Shot list is in
`thwaites-5min-block-script.md`, already written to the 10s grid.
