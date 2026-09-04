#!/usr/bin/env bash
# Generates all 30 narration files with edge-tts. Free, no account, no API key.
#
# One-time setup:   pip install edge-tts
# Usage:            bash generate_vo.sh /path/to/under-the-ice/01_vo
#
# Audition voices first:  edge-tts --list-voices | grep en-GB
# Then change VOICE below if you prefer a different one.

set -e
OUT="${1:-./01_vo}"
BLOCKS="$(dirname "$0")/../narration/blocks.txt"
VOICE="en-GB-RyanNeural"     # documentary-style male. Swap after auditioning.
RATE="-5%"                   # slightly slower than default; suits this material.

command -v edge-tts >/dev/null || { echo "edge-tts not found. Run: pip install edge-tts"; exit 1; }
[ -f "$BLOCKS" ] || { echo "Cannot find $BLOCKS"; exit 1; }
mkdir -p "$OUT"

n=0
while IFS= read -r line; do
  [ -z "$line" ] && continue
  n=$((n+1))
  f=$(printf "%s/block%02d.mp3" "$OUT" "$n")
  echo "[$n/30] $f"
  edge-tts --voice "$VOICE" --rate="$RATE" --text "$line" --write-media "$f"
done < "$BLOCKS"

echo
echo "Done: $n files in $OUT"
echo "Now check durations - anything over 9.5s needs its LINE shortened, not its speed changed:"
echo "  bash $(dirname "$0")/check_durations.sh \"$OUT\""
