@echo off
echo 请先保存打开的Excel，程序开始运行后会关闭所有的Excel程序...
SET /p TARGET_DIR=输入需要更新的目录（可将目录直接拖拽到命令行上）:
taskkill /f /t /im EXCEL.EXE > nul
python replace_row_data_by_col.py %TARGET_DIR%


pause