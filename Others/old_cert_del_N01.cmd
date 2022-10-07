@echo off
chcp 65001 > nul

PowerShell -Command "& {Set-Location Cert:;$expired = Get-ChildItem cert:\* ` -recurse -ExpiringInDays 0; $expired | Remove-Item -DeleteKey;Set-Location C:;}"
pause
