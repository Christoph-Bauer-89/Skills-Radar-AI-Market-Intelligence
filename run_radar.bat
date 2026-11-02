@echo off
REM Wechselt automatisch in das Verzeichnis, in dem die Batch-Datei liegt (Portabel für GitHub)
cd d %~dp0
python ai_job_full_auto.py
pause