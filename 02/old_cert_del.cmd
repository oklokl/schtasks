@echo off
mode con cols=15 lines=1
REM 20221009 "https://www.codeproject.com/Questions/599352/Howplustoplusremovepluscertificateplususingpluspow"
PowerShell -windowstyle hidden -Command "& {Get-ChildItem -Path Cert:\LocalMachine\Root | Where-Object {$_.NotAfter -lt (Get-Date).AddDays(40)} | ForEach-Object {Remove-Item -Path "Cert:\LocalMachine\Root\$($_.Thumbprint)" -Recurse -Verbose}}"
REM PowerShell -windowstyle hidden -Command "& {Set-Location Cert: ; $expired = Get-ChildItem cert:\* ` -recurse -ExpiringInDays 0 ; $expired | Remove-Item -DeleteKey}"
powershell -windowstyle hidden -Command "& {Get-ChildItem """$env:temp""" | Remove-Item -recurse; Stop-Process -name CMD}"
mode con cols=120 lines=30 > nul
exit
