@echo off

REM Run Flet app with hot reload and ignore cache directories
flet run -p=50125 --name=animge -d -r -w --ignore-dirs=components/__pycache__,components/ui/__pycache__,constants/__pycache__,contexts/__pycache__,utils/__pycache__

pause
