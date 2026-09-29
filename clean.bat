@echo off
echo ==========================================
echo      KeyVault - Limpeza de Ambiente      
echo ==========================================

if exist "venv" (
    echo [1/2] Removendo a pasta 'venv'...
    rmdir /s /q venv
) else (
    echo [1/2] Nenhuma pasta 'venv' encontrada.
)

echo [2/2] Limpando caches do Python...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"

echo ==========================================
echo Limpeza concluida! O projeto esta 100%% limpo.
echo ==========================================
pause