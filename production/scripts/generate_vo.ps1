# Generates all 30 narration files with edge-tts (free, no account, no key).
# Setup once:  pip install edge-tts
# Run:         powershell -ExecutionPolicy Bypass -File generate_vo.ps1
param(
  [string]$OutDir     = "$env:USERPROFILE\Videos\under-the-ice\01_vo",
  [string]$BlocksFile = "$env:USERPROFILE\Videos\under-the-ice\blocks.txt",
  [string]$Voice      = "en-GB-RyanNeural",
  [string]$Rate       = "-5%"
)

if (-not (Test-Path $BlocksFile)) { Write-Host "Cannot find $BlocksFile" -ForegroundColor Red; exit 1 }
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

# 'python -m edge_tts' is used instead of the bare 'edge-tts' command because it
# works even when Windows has not put the script folder on PATH.
$lines = Get-Content $BlocksFile | Where-Object { $_.Trim() -ne "" }
if ($lines.Count -ne 30) { Write-Host "Expected 30 lines, found $($lines.Count)" -ForegroundColor Yellow }

$n = 0
foreach ($line in $lines) {
    $n++
    $file = Join-Path $OutDir ("block{0:D2}.mp3" -f $n)
    Write-Host ("[{0}/{1}] block{2:D2}.mp3" -f $n, $lines.Count, $n)
    python -m edge_tts --voice $Voice --rate=$Rate --text "$line" --write-media "$file"
}
Write-Host ""
Write-Host "Done: $n files in $OutDir" -ForegroundColor Green
