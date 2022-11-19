@echo off
chcp 65001 > nul

REM "전승환님께서 만들어 주셨네요"
REM "https://kin.naver.com/qna/detail.naver?d1id=1&dirId=104&docId=433043796"
for /f "delims=" %%a in ('schtasks /query /fo LIST /v ^| findstr /c:"OneDrive Standalone Update Task"') do set "ServiceName=%%a"
set "ServiceName=%ServiceName:TaskName:                             =%"
echo "%ServiceName%"
schtasks /change /tn "%ServiceName%" /disable
pause
