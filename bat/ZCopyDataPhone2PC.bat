SET LOG_FILE_NAME=ZLog.%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%.log
adb pull storage/emulated/0/Game/game.log ./%LOG_FILE_NAME%

@echo off
echo running result:
if %errorlevel%==0 goto endsuccess
:endFail
echo Copydata from phone to pc falied!!!
pause
exit /b 1

:endsuccess
echo Copydata from phone to pc success!!!
ping -n 5 127.0.0.1 >nul
exit /b 0