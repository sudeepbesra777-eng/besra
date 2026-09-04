# Creates the project folder tree on Windows. Run in PowerShell.
#   powershell -ExecutionPolicy Bypass -File setup_project.ps1
param([string]$Parent = "$env:USERPROFILE\Videos")

$Root = Join-Path $Parent "under-the-ice"
$folders = @("01_vo","02_img","02_img\_rejects","03_vid","03_vid\_rejects",
             "04_stock","05_gfx","06_music","07_project","08_export")
foreach ($f in $folders) {
    New-Item -ItemType Directory -Force -Path (Join-Path $Root $f) | Out-Null
}

@"
under-the-ice/
  01_vo/      30 narration files, block01.mp3 ... block30.mp3   <- make these FIRST
  02_img/     7 AI still images: img02, img04, img07, img10, img11, img12, img20
  03_vid/     5 AI video clips: vid01, vid14, vid15, vid16, vid30
  04_stock/   public-domain downloads: stock09, stock23, nasa03, nasa06, nasa29
  05_gfx/     graphics you build in Fusion
  06_music/   music bed + wind ambience + underwater ambience
  07_project/ the DaVinci Resolve project file
  08_export/  final render + thumbnail

RULE: every file carries its shot number. With 47 clips in a bin, the number is
the only thing that saves you.
"@ | Out-File -FilePath (Join-Path $Root "README.txt") -Encoding utf8

Write-Host ""
Write-Host "Created: $Root" -ForegroundColor Green
Get-ChildItem -Path $Root -Directory -Recurse | Select-Object -ExpandProperty FullName
