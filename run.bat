@echo off
REM ---------------------------------------------------------------------------
REM  AI Resume Analyzer - one-click launcher for Windows.
REM
REM  Creates a local virtual environment on first run, installs every
REM  dependency from requirements.txt and starts the Streamlit app.
REM
REM  Usage: double-click run.bat, or run it from a terminal.
REM ---------------------------------------------------------------------------
setlocal

cd /d "%~dp0"

set "VENV_DIR=.venv"
set "PYTHON_CMD=python"

where py >nul 2>&1 && set "PYTHON_CMD=py -3"

echo.
echo ==========================================
echo   AI Resume Analyzer - Setup and Launch
echo ==========================================
echo.

if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo [1/3] Creating virtual environment in %VENV_DIR% ...
    %PYTHON_CMD% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo.
        echo ERROR: could not create the virtual environment.
        echo Install Python 3.10+ from https://www.python.org/downloads/
        echo and make sure "Add Python to PATH" is selected.
        pause
        exit /b 1
    )
) else (
    echo [1/3] Virtual environment already exists, reusing it.
)

echo.
echo [2/3] Installing dependencies ...
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip --quiet
"%VENV_DIR%\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: dependency installation failed. Check your internet connection.
    pause
    exit /b 1
)

echo.
echo [3/3] Starting the AI Resume Analyzer ...
echo Open http://localhost:8501 in your browser when it is ready.
echo Press Ctrl+C in this window to stop the app.
echo.
"%VENV_DIR%\Scripts\python.exe" -m streamlit run app.py

endlocal
