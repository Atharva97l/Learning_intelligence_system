@echo off
setlocal
set "PROJECT_DIR=%~dp0"

where uv >nul 2>nul
if errorlevel 1 (
    echo Could not find uv. Install uv, then double-click this file again.
    pause
    exit /b 1
)

if not exist "%PROJECT_DIR%frontend\dist\index.html" (
    echo The built website was not found at frontend\dist\index.html.
    echo Restore the frontend source and build it before launching the project.
    pause
    exit /b 1
)

echo Starting the Luma API and website...
netstat -ano | findstr "127.0.0.1:8000" | findstr "LISTENING" >nul
if errorlevel 1 start "Luma API" cmd /k "cd /d ""%PROJECT_DIR%"" && uv run uvicorn backend.main:app --host 127.0.0.1 --port 8000"

netstat -ano | findstr "127.0.0.1:5173" | findstr "LISTENING" >nul
if errorlevel 1 start "Luma website" cmd /k "cd /d ""%PROJECT_DIR%"" && uv run python -m http.server 5173 --bind 127.0.0.1 --directory frontend/dist"

echo Waiting for the local website...
for /L %%I in (1,1,30) do (
    netstat -ano | findstr "127.0.0.1:5173" | findstr "LISTENING" >nul
    if not errorlevel 1 goto website_ready
    timeout /t 1 /nobreak >nul
)

echo The website did not start. Check the Luma website window for an error.
pause
exit /b 1

:website_ready
start "" "http://127.0.0.1:5173/"
echo The website is open. Keep both Luma windows running while you use it.
