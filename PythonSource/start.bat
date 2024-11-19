@echo off
setlocal

REM Define a log file
set LOGFILE=install_log.txt

REM Check if Python is installed
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Please install Python and add it to your PATH.
    pause
    exit /b
)

REM Check if pip is installed
pip --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo pip is not installed. Please install pip.
    pause
    exit /b
)

REM Check if requirements.txt exists
IF NOT EXIST requirements.txt (
    echo requirements.txt not found. Please make sure it is in the current directory.
    pause
    exit /b
)

REM Install the requirements and log output
echo Installing packages from requirements.txt...
pip install -r requirements.txt > %LOGFILE% 2>&1

IF ERRORLEVEL 1 (
    echo Failed to install some packages. Please check the output below for details:
    type %LOGFILE%
    pause
    exit /b
) ELSE (
    echo All packages installed successfully.
)

REM Check if main.py exists
IF NOT EXIST main.py (
    echo main.py not found. Please make sure it is in the current directory.
    pause
    exit /b
)

REM Run main.py and log output
echo Running main.py...
python main.py >> %LOGFILE% 2>&1

IF ERRORLEVEL 1 (
    echo main.py encountered an error. Please check the output below for details:
    type %LOGFILE%
    pause
    exit /b
)

pause
