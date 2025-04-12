@echo off
REM Change to the folder containing the script
cd /d "%~dp0"

REM Activate the virtual environment
call "venv\Scripts\activate"

REM Run the Python script
python main.py

REM Keep the Command Prompt open
pause
