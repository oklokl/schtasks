@echo off
cd /d "%~dp0"
setlocal

REM "모꼬모지님께서 만들어 주셨네요"
REM "https://kin.naver.com/qna/detail.naver?d1id=1&dirId=104&docId=433076909"
for /f "tokens=2* delims= " %%f in (
'schtasks /query /fo list /v ^|find /i "onedrive"'
) do (
for %%p in (
"OneDrive Standalone Update Task",
"OneDrive Reporting Task"
) do (
echo "%%~g"|find /i "%%~p" 2>nul>nul&&(
echo schtasks /change /tn "%%~g" /disable 
call schtasks /change /tn "%%~g" /disable 
)))

:end
endlocal
pause
