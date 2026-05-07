"""
main.py - Ponto de entrada para utilitários de build e validação do projeto.
"""

import os
import json
import sys

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')


def load_config():
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_structure():
    root = os.path.join(os.path.dirname(__file__), '..')
    required = [
        'docs/requisitos.md', 'docs/arquitetura.md',
        'src/main.py', 'tests/test_main.py',
        'scripts/build.sh', 'config/settings.json',
        'index.html', 'README.md', 'CHANGELOG.md', 'requirements.txt',
    ]
    missing = [p for p in required if not os.path.exists(os.path.join(root, p))]
    if missing:
        print("Arquivos ausentes:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    else:
        print("Estrutura do projeto validada com sucesso!")


def main():
    config = load_config()
    print(f"Projeto: {config['project']['name']} v{config['project']['version']}")
    check_structure()


if __name__ == '__main__':
    main()
