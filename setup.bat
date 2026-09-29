@echo off
echo ==========================================
echo     KeyVault - Instalador Automatico     
echo ==========================================

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! Instale o Python 3.
    pause
    exit /b
)

if not exist "venv" (
    echo [1/3] Criando ambiente virtual (venv)...
    python -m venv venv
) else (
    echo [1/3] Ambiente virtual (venv) ja existe.
)

echo [2/3] Atualizando o pip...
call venv\Scripts\activate
python -m pip install --upgrade pip

echo [3/3] Instalacao concluida com sucesso!
echo ==========================================
pause