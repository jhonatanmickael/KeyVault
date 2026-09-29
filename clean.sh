#!/usr/bin/env bash

echo "=========================================="
echo "      KeyVault - Limpeza de Ambiente      "
echo "=========================================="

if [ -n "$VIRTUAL_ENV" ]; then
    echo "[1/3] Desativando ambiente virtual..."
    unset VIRTUAL_ENV
    unset PYTHONHOME
    export PATH=$(echo "$PATH" | sed -e 's|[^:]*/venv/bin:||g')
    hash -r 2>/dev/null
fi

if [ -d "venv" ]; then
    echo "[2/3] Removendo a pasta 'venv'..."
    rm -rf venv
else
    echo "[2/3] Nenhuma pasta 'venv' encontrada."
fi

echo "[3/3] Limpando caches do Python (__pycache__, *.pyc)..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null

echo "=========================================="
echo "Limpeza concluída! O projeto está 100% limpo."
echo "=========================================="