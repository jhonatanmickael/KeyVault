echo "=========================================="
echo "    KeyVault - Instalador Automático     "
echo "=========================================="

if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python3 não foi encontrado."
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "[1/3] Criando ambiente virtual (venv)..."
    python3 -m venv venv
else
    echo "[1/3] Ambiente virtual (venv) já existe."
fi

echo "[2/3] Atualizando o pip..."
source venv/bin/activate
pip install --upgrade pip

echo "[3/3] Instalação concluída com sucesso!"
echo "=========================================="