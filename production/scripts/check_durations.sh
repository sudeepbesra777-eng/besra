#!/usr/bin/env bash
# Reports the length of every VO file and flags any that overrun their 10s block.
# Needs ffprobe (comes with ffmpeg).  Usage: bash check_durations.sh /path/to/01_vo
OUT="${1:-./01_vo}"
command -v ffprobe >/dev/null || { echo "ffprobe not found. Install ffmpeg."; exit 1; }
total=0; over=0
for f in "$OUT"/block*.mp3; do
  [ -e "$f" ] || continue
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  total=$(awk -v a="$total" -v b="$d" 'BEGIN{print a+b}')
  flag=""
  awk -v d="$d" 'BEGIN{exit !(d>9.5)}' && { flag="  <-- TOO LONG, shorten the words"; over=$((over+1)); }
  printf "%s  %5.2fs%s\n" "$(basename "$f")" "$d" "$flag"
done
echo "-----"
printf "total speech: %.1fs across 30 blocks (target: comfortably under 300s)\n" "$total"
echo "overruns: $over"
