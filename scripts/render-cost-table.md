# Render economics — measured, not estimated

All figures from Higgsfield `get_cost` preflights on 2026-09-04. One shot = one clip.
A 5:00 video in this pipeline = **30 blocks x 10s**.

| Model | Res | Shot len | Credits/shot | **30 shots (5:00)** |
|---|---|---|---|---|
| `seedance_2_5` | 1080p | 10s | 90 | **2,700** |
| `seedance_2_5` | 720p | 10s | 65 | 1,950 |
| `seedance_2_5` | 1080p | 5s | 45 | 2,700 (60 shots) |
| `minimax_h3` | **2K** | 10s | **20** | **600** |

## The finding
`minimax_h3` at 2K is **4.5x cheaper than Seedance 2.5 at 1080p — and higher resolution.**
It is also the model the `faceless-video` workflow already locks for clips, so it comes with
the automated assembly, QC gates, and burned-subtitle path rather than a hand-built edit.

Seedance's premium buys a different aesthetic and native per-clip audio. This build does not
want per-clip audio — there is one continuous narrator VO over the whole cut, so `generate_audio`
is off either way. That removes most of what the extra 70 credits/shot is paying for.

## Plan sizing (credit packs are unavailable on this workspace; upgrade is the only path)
| Plan | Credits/mo | Full 5:00 on MiniMax H3 (600) | Full 5:00 on Seedance 1080p (2,700) |
|---|---|---|---|
| PLUS $39/yr | 1,000 | yes, ~1.6 videos | **no — short by 1,700** |
| ULTRA $99/yr | 3,000 | yes, ~5 videos | barely one, no retry headroom |

Budget ~15-20% on top of any figure for retries. Blocks 15-20 are the payload shots and are
where retries actually get spent.
