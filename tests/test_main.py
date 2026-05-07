"""Testes automatizados para os utilitários do projeto."""

import os
import sys
import json
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from utils.file_utils import ensure_dir, list_files


def test_ensure_dir_creates_directory():
    with tempfile.TemporaryDirectory() as tmp:
        new_dir = os.path.join(tmp, 'novo', 'subdir')
        ensure_dir(new_dir)
        assert os.path.isdir(new_dir)


def test_list_files_filters_by_extension():
    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, 'a.txt'), 'w').close()
        open(os.path.join(tmp, 'b.py'), 'w').close()
        open(os.path.join(tmp, 'c.txt'), 'w').close()
        result = list_files(tmp, '.txt')
        assert len(result) == 2


def test_config_is_valid_json():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    assert 'project' in config
    assert 'version' in config['project']


if __name__ == '__main__':
    test_ensure_dir_creates_directory()
    test_list_files_filters_by_extension()
    test_config_is_valid_json()
    print("Todos os testes passaram!")
