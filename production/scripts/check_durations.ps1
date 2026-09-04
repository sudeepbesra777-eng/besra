# Reports the length of every narration file and flags overruns.
# No extra installs - it reads durations through Windows Explorer's own metadata.
#   powershell -ExecutionPolicy Bypass -File check_durations.ps1
param([string]$OutDir = "$env:USERPROFILE\Videos\under-the-ice\01_vo")

if (-not (Test-Path $OutDir)) { Write-Host "Folder not found: $OutDir" -ForegroundColor Red; exit 1 }

$shell  = New-Object -ComObject Shell.Application
$folder = $shell.Namespace((Resolve-Path $OutDir).Path)

# The metadata column index for Length is not the same on every machine, so find it by name.
$lenCol = $null
for ($i = 0; $i -lt 320; $i++) {
    if ($folder.GetDetailsOf($null, $i) -eq "Length") { $lenCol = $i; break }
}
if ($null -eq $lenCol) {
    Write-Host "Could not find the 'Length' column (non-English Windows?)." -ForegroundColor Red
    Write-Host "Fallback: right-click any block file > Properties > Details tab > read Length." -ForegroundColor Yellow
    exit 1
}

# Parse h:m:s or m:s explicitly. [TimeSpan]::Parse would read "0:04" as 4 MINUTES.
function ConvertTo-Seconds([string]$t) {
    $p = $t -split ":"
    switch ($p.Count) {
        3 { return [double]$p[0]*3600 + [double]$p[1]*60 + [double]$p[2] }
        2 { return [double]$p[0]*60 + [double]$p[1] }
        1 { return [double]$p[0] }
    }
    return 0
}

$total = 0.0; $over = 0; $count = 0
foreach ($item in ($folder.Items() | Sort-Object Name)) {
    if ($item.Name -notlike "block*.mp3") { continue }
    $raw = ($folder.GetDetailsOf($item, $lenCol)) -replace "[^\d:]", ""
    if (-not $raw) { Write-Host ("{0}  (no duration reported)" -f $item.Name) -ForegroundColor Yellow; continue }
    $secs = ConvertTo-Seconds $raw
    $total += $secs; $count++
    if ($secs -gt 9.5) {
        Write-Host ("{0}  {1,5:N2}s   <-- TOO LONG, shorten the words in blocks.txt" -f $item.Name, $secs) -ForegroundColor Yellow
        $over++
    } elseif ($secs -lt 3) {
        Write-Host ("{0}  {1,5:N2}s   <-- suspiciously short, check this one" -f $item.Name, $secs) -ForegroundColor Yellow
    } else {
        Write-Host ("{0}  {1,5:N2}s" -f $item.Name, $secs)
    }
}

Write-Host "-----"
Write-Host ("files found:  {0}  (expected 30)" -f $count)
Write-Host ("total speech: {0:N1}s  (expected roughly 200-280s)" -f $total)
if ($count -eq 30 -and $over -eq 0) {
    Write-Host "overruns: 0  -  PASS, ready for the timeline" -ForegroundColor Green
} else {
    Write-Host ("overruns: {0}  -  fix these before moving on" -f $over) -ForegroundColor Yellow
}
