@ECHO OFF
FOR %%a IN (loops_multiple_file.bat ToDo.txt file_test.tmp) DO (
	IF EXIST %%a (echo File Found: %%a) ELSE (echo File NOT Found: %%a)
)
