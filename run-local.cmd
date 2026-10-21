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
powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/api/health -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"
if errorlevel 1 start "Luma API" cmd /k "cd /d ""%PROJECT_DIR%"" && uv run uvicorn backend.main:app --host 127.0.0.1 --port 8000"

powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing http://127.0.0.1:5173/ -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"
if errorlevel 1 start "Luma website" cmd /k "cd /d ""%PROJECT_DIR%"" && uv run python -m http.server 5173 --bind 127.0.0.1 --directory frontend/dist"

echo Waiting for the local website...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ready = $false; for ($i = 0; $i -lt 30; $i++) { try { $r = Invoke-WebRequest -UseBasicParsing http://127.0.0.1:5173/ -TimeoutSec 2; if ($r.StatusCode -eq 200) { $ready = $true; break } } catch {}; Start-Sleep -Seconds 1 }; if (-not $ready) { exit 1 }"
if errorlevel 1 (
    echo The website did not start. Check the Luma website window for an error.
    pause
    exit /b 1
)

start "" "http://127.0.0.1:5173/"
echo The website is open. Keep both Luma windows running while you use it.
