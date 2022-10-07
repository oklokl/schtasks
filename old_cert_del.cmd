@echo off
PowerShell -windowstyle hidden -Command "& {Set-Location Cert: ; $expired = Get-ChildItem cert:\* ` -recurse -ExpiringInDays 0 ; $expired | Remove-Item -DeleteKey}"
exit