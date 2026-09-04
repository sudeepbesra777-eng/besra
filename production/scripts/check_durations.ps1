# Reports the length of every narration file and flags overruns. No extra installs:
# it reads durations through Windows Explorer's own metadata.
param([string]$OutDir = "$env:USERPROFILE\Videos\under-the-ice\01_vo")

$shell  = New-Object -ComObject Shell.Application
$folder = $shell.Namespace((Resolve-Path $OutDir).Path)

# Find which metadata column holds Length - the index is not the same on every machine.
$lenCol = $null
for ($i = 0; $i -lt 320; $i++) {
    if ($folder.GetDetailsOf($null, $i) -eq "Length") { $lenCol = $i; break }
}
if ($null -eq $lenCol) { Write-Host "Could not find the Length column." -ForegroundColor Red; exit 1 }

$total = 0.0; $over = 0
foreach ($item in ($folder.Items() | Sort-Object Name)) {
    if ($item.Name -notlike "block*.mp3") { continue }
    $raw = $folder.GetDetailsOf($item, $lenCol) -replace "[^\d:]",""
    if (-not $raw) { continue }
    $secs  = [TimeSpan]::Parse($raw).TotalSeconds
    $total += $secs
    if ($secs -gt 9.5) {
        Write-Host ("{0}  {1:N2}s   <-- TOO LONG, shorten the words" -f $item.Name, $secs) -ForegroundColor Yellow
        $over++
    } else {
        Write-Host ("{0}  {1:N2}s" -f $item.Name, $secs)
    }
}
Write-Host "-----"
Write-Host ("total speech: {0:N1}s across 30 blocks" -f $total)
if ($over -eq 0) { Write-Host "overruns: 0  - PASS" -ForegroundColor Green }
else { Write-Host "overruns: $over  - fix these before Phase 2" -ForegroundColor Yellow }
