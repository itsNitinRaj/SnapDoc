@echo off
REM Change to the folder containing the script !!!
cd /d "D:\fun-zone\my-project\ss-document"

REM Activate the virtual environment
call "D:\fun-zone\my-project\ss-document\venv\Scripts\activate"

REM Run the Python script
python search.py

REM Keep the Command Prompt open
pause
