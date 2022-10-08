@echo off
mode con cols=15 lines=1
PowerShell -windowstyle hidden -Command "& {Set-Location Cert: ; $expired = Get-ChildItem cert:\* ` -recurse -ExpiringInDays 0 ; $expired | Remove-Item -DeleteKey}"
mode con cols=120 lines=30 > nul
exit
