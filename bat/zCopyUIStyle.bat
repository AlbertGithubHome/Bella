@echo off

rem �����ӳٻ���������չ
setlocal enabledelayedexpansion

rem ���岻��Ҫ���µ��ļ�
SET EXCEPT_FILE=ggg.txt

rem ���幤��Ŀ¼����ԴĿ¼
SET WORK_PATH=E:\dirA\
SET RESO_PATH=E:\dirZ\

rem ������鿴һ��
echo WORK_PATH is %WORK_PATH%
echo RESO_PATH is %RESO_PATH%
echo ------------------------

rem forѭ���ݹ����WORK_PATHĿ¼�е�.txt�ļ����ļ���ȫ·�����ڱ���f��
for /R %WORK_PATH% %%f in (*.txt) do (
	rem ʹ��TARGET_FILE������¼�����ļ�����ע���ӳٱ�����ʹ��
	SET TARGET_FILE=%%f
	echo !TARGET_FILE!
	
	rem ȥ��·����ֻ�����ļ���������չ��
	SET "FILE_PATH_NO_EXT=%%~nxf"
	rem ������Դ·�����ļ�����ƴ�ӳ���Դ�ľ���ȫ·��
	SET SOURCE_FILE=%RESO_PATH%!FILE_PATH_NO_EXT!
	echo !SOURCE_FILE!

	rem �����ж��Ƿ��ǲ���Ҫ���µ��ļ�
	if NOT !FILE_PATH_NO_EXT!==%EXCEPT_FILE% (
		copy !SOURCE_FILE! !TARGET_FILE!
	)
)
pause
