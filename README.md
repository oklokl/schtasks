# schtasks
taskschd.msc schtasks Windows Task Scheduler 예약작접 스케줄러

https://cafe.daum.net/candan/BLQD/72 오래된 인증서 삭제 방법

https://cafe.daum.net/candan/I45j/71 예약 작업 등록 방법

`schtasks /create /tn "old_cert_del" /tr "cmd /c d:\old_cert_del.cmd" /sc onlogon`

등록방법

.

`Get-ChildItem cert:\LocalMachine\root|Where {$_.NotAfter -lt  (Get-Date).AddDays(60)}|select NotAfter, Subject`

파워쉘 오래된 인증서 검색 방법
