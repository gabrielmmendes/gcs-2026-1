"""Utilitários para manipulação de arquivos."""

import os


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def list_files(directory: str, extension: str = '') -> list:
    files = []
    for fname in os.listdir(directory):
        if extension and not fname.endswith(extension):
            continue
        files.append(os.path.join(directory, fname))
    return sorted(files)
