@echo off
echo ���ȱ���򿪵�Excel������ʼ���к��ر����е�Excel����...
SET /p TARGET_DIR=������Ҫ���µ�Ŀ¼���ɽ�Ŀ¼ֱ����ק���������ϣ�:
taskkill /f /t /im EXCEL.EXE > nul
python replace_row_data_by_col.py %TARGET_DIR%


pause