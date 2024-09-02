@echo off
set EXE_NAME=r5apex.exe 
set EXE_PATH=C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Apex Legends.url

rem Check if the process is running
tasklist /FI "IMAGENAME eq %EXE_NAME%" 2>NUL | find /I "%EXE_NAME%" >NUL

if %ERRORLEVEL% NEQ 0 (
    echo %EXE_NAME% is not running. Starting %EXE_NAME%.
    start "" "%EXE_PATH%"
) else (
    echo %EXE_NAME% is already running.
)
start "DMT" "C:\Program Files (x86)\Dual Monitor Tools\DMT.exe"
start "program_wor" "C:\Users\User\Documents\GitHub\inGameSelection\apex\apex legends.py"

