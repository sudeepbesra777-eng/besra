#!/usr/bin/env bash
# Creates the project folder tree. Run once, from wherever you keep your video projects.
# Usage:  bash setup_folders.sh  [optional-parent-path]
set -e
ROOT="${1:-.}/under-the-ice"
mkdir -p "$ROOT"/{01_vo,02_img/_rejects,03_vid/_rejects,04_stock,05_gfx,06_music,07_project,08_export}
cat > "$ROOT/README.txt" <<'TXT'
under-the-ice/
  01_vo/      30 narration files, block01.mp3 ... block30.mp3   <- make these FIRST
  02_img/     8 AI still images, named img02.png, img04.png ... (number = shot number)
    _rejects/ failed generations you might revisit. Keeps the main folder clean.
  03_vid/     5 AI video clips, vid01.mp4, vid14.mp4, vid15.mp4, vid16.mp4, vid30.mp4
    _rejects/
  04_stock/   public-domain downloads. Name them stock09.mp4, stock23.mp4, nasa03.png ...
  05_gfx/     graphics you build or export out of Fusion
  06_music/   music bed + wind ambience + underwater ambience
  07_project/ the DaVinci Resolve project file lives here
  08_export/  final renders and the thumbnail

RULE: name every file with the shot number it belongs to. When you have 47 files open
in a bin, the number is the only thing that saves you.
TXT
echo "Created: $ROOT"
find "$ROOT" -type d | sort
