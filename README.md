# schtasks
taskschd.msc schtasks Windows Task Scheduler 예약작접 스케줄러

https://cafe.daum.net/candan/BLQD/72 오래된 인증서 삭제 방법

https://cafe.daum.net/candan/I45j/71 예약 작업 등록 방법

https://cafe.daum.net/candan/BLQD/85 본문 내용과 같은 내용 

`schtasks /create /ru administrators /tn "old_cert_del" /tr "cmd /c d:\old_cert_del.cmd" /sc onlogon /RL HIGHEST`

등록방법 숨기기 /RL HIGHEST 를 꼭 적어 주어야 하네요 안되면 실행 안됨 ㅎㅎ /ru "NT Authority\System" 쓰면 숨긴다고 하는대 문제는 이렇게 하면 실행이 안되네요.

.

만약 필요 없다면 삭제 방법

schtasks /Delete /tn "old_cert_del" /f

del d:\old_cert_del.cmd

.

`Get-ChildItem cert:\LocalMachine\root|Where {$_.NotAfter -lt  (Get-Date).AddDays(60)}|select NotAfter, Subject`

파워쉘 오래된 인증서 검색 방법

.

기타 수상한 자격증명이 있는 것 같으면 바이러스 포털에 검사.

https://docs.microsoft.com/ko-kr/sysinternals/downloads/sigcheck 파일 받는곳   

`sigcheck.exe –tv`

`.\sigcheck.exe -tv`


삭제 방법 Thumbprint: 부분을 적으면 된다.

파워쉘에서 해야 하네요 c:로 이동 이걸 꼭 적으세요 ㅎ 

`c:`

`Get-ChildItem Cert:\LocalMachine\Root\c843721cbc3ad29910e1f31c99361eedceb6ddds | Remove-Item`

`Get-ChildItem Cert:\LocalMachine\Root\??? | Remove-Item`

무름표 부분을 지우고 의심 가는 키를 넣으면 되네요.

.

자격증명을 보려면 (이거 머냐? 하면 컴퓨터에서 열쇠 같은건대요? 해커가 이 열쇠 훔쳐서.. 나쁜 짓을 하기도 해요 결론) 잘 관리 해야함. ㅎㅎ 한대 업데이트 잘 안해주네요.

윈도우 + R

`netplwiz`

`certmgr.msc`

`certlm.msc`
