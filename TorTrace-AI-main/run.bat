@echo off
title BIMBO - Network Attribution System
color 0B

echo ======================================================================
echo    BIMBO - Multi-Layer Tor Network Attribution System
echo ======================================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python found
echo.

:: Install dependencies if needed
echo Checking dependencies...
pip show flask >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install flask scapy networkx folium scikit-learn xgboost joblib pandas numpy
)
echo [OK] Dependencies ready
echo.

:: Create required directories
if not exist "data\pcap_files" mkdir "data\pcap_files"
if not exist "data\batch_results" mkdir "data\batch_results"

echo ======================================================================
echo    Starting BIMBO Dashboard on http://localhost:5000
echo    Press Ctrl+C to stop
echo ======================================================================
echo.

:: Set encoding for Unicode support
set PYTHONIOENCODING=utf-8

:: Launch the unified dashboard
python unified_dashboard.py

pause
