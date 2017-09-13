@echo off

SET MAIN_ABS_PATH=%~dp0
SET PREMAKE_EXE=%MAIN_ABS_PATH%premake4.exe
SET PREMAKE_LUA=%MAIN_ABS_PATH%premake.lua

%PREMAKE_EXE% --file=%PREMAKE_LUA% vs2008
set VS2008=%VS09COMNTOOLS%..\IDE\devenv
set SERVERDIR=%MAIN_ABS_PATH%\..\..\code\encoding.sln
"%VS2008%" "%SERVERDIR%" /Rebuild "Debug%|Win32"
pause