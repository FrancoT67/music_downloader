@echo off
REM Cambiar al directorio donde está tu programa
cd /d "C:\Users\Hogar\Desktop\tutorial\prueba"

REM Activar el entorno virtual (si usas uno)
call venv\Scripts\activate

REM Ejecutar el servidor Flask
start cmd /k "python app.py"

REM Esperar unos segundos para que Flask arranque
timeout /t 3 >nul

REM Abrir la página en Chrome
start brave http://127.0.0.1:5000/static/index.html
