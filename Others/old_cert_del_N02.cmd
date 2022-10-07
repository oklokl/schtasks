@echo off
chcp 65001 > nul
BCDEDIT > nul 

if "%ERRORLEVEL%" EQU "1" Powershell.exe -Command "& {Start-Process """%0""" -Verb RunAs}" & exit
title 관리자 권한이 시작 되었습니다.
PowerShell -Command "& {Set-Location Cert:;$expired = Get-ChildItem cert:\* ` -recurse -ExpiringInDays 0; $expired | Remove-Item -DeleteKey;Set-Location C:;}"
pause
