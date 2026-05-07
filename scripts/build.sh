#!/usr/bin/env bash
set -euo pipefail

echo "=== Build: Conversor PDF -> PNG ==="

echo "[1/4] Verificando Python..."
python3 --version

echo "[2/4] Instalando dependencias..."
pip install -r requirements.txt --quiet

echo "[3/4] Executando testes..."
python3 -m pytest tests/ -v

echo "[4/4] Validando estrutura..."
python3 src/main.py

echo "Build concluido com sucesso!"
