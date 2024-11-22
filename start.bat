@echo off
SETLOCAL

REM Set the paths for requirements.txt and the executable
SET "REQUIREMENTS_FILE=requirements.txt"
SET "EXECUTABLE_FILE=verse.exe"

REM Change to the directory where this batch file is located
cd /d "%~dp0"

REM Check if requirements.txt exists
IF NOT EXIST "%REQUIREMENTS_FILE%" (
    echo Error: %REQUIREMENTS_FILE% not found!
    exit /b 1
)

REM Install the required Python packages
echo Installing packages from %REQUIREMENTS_FILE%...
pip install -r "%REQUIREMENTS_FILE%"

REM Check if the installation was successful
if %ERRORLEVEL% neq 0 (
    echo Failed to install packages. Exiting...
    exit /b %ERRORLEVEL%
)

REM Check if the executable file exists
IF NOT EXIST "%EXECUTABLE_FILE%" (
    echo Error: %EXECUTABLE_FILE% not found!
    exit /b 1
)

REM Run the executable file
echo Running %EXECUTABLE_FILE%...
start "" "%EXECUTABLE_FILE%"

REM Optional: Wait for user input before closing the command window
pause
ENDLOCAL
