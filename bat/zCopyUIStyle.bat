@echo off

rem 启用延迟环境变量扩展
setlocal enabledelayedexpansion

rem 定义不需要更新的文件
SET EXCEPT_FILE=ggg.txt

rem 定义工作目录和资源目录
SET WORK_PATH=E:\dirA\
SET RESO_PATH=E:\dirZ\

rem 简单输出查看一下
echo WORK_PATH is %WORK_PATH%
echo RESO_PATH is %RESO_PATH%
echo ------------------------

rem for循环递归遍历WORK_PATH目录中的.txt文件，文件的全路径放在变量f中
for /R %WORK_PATH% %%f in (*.txt) do (
	rem 使用TARGET_FILE变量记录绝对文件名，注意延迟变量的使用
	SET TARGET_FILE=%%f
	echo !TARGET_FILE!
	
	rem 去掉路径，只保留文件的名及扩展名
	SET "FILE_PATH_NO_EXT=%%~nxf"
	rem 利用资源路径和文件名，拼接出资源的绝对全路径
	SET SOURCE_FILE=%RESO_PATH%!FILE_PATH_NO_EXT!
	echo !SOURCE_FILE!

	rem 条件判断是否是不需要更新的文件
	if NOT !FILE_PATH_NO_EXT!==%EXCEPT_FILE% (
		copy !SOURCE_FILE! !TARGET_FILE!
	)
)
pause
