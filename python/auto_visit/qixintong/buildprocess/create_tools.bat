copy ..\\auto_qixintong_visitor.py .\\visit_qixintong.py
pyinstaller -i black.ico -F .\\visit_qixintong.py ..\..\..\tools\network\agentpool.py ..\..\..\tools\network\proxypool.py
REM del /Q visit_qixintong.py