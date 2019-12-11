@ECHO OFF

REM ping 100 hosts from 10.0.0.1 to 10.0.0.100 and write alive hosts to iplist.txt

:START

FOR /L %%N IN (1,1,100) DO (
	ping -n 1 10.0.0.%%N 2>NUL | findstr "TTL"
	IF NOT ERRORLEVEL 1 (
		ECHO 10.0.0.%%N >> iplist.txt
		)
)
