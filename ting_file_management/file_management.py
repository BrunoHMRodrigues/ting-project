import os
import sys


def txt_importer(path_file):

    # Verificar se arquivo existe
    if not os.path.exists(path_file):
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
        return []

    # Verificar se o formato é .txt

    if not path_file.lower().endswith('.txt'):
        sys.stderr.write("Formato inválido")
        return []

    # retorna uma lista contendo as linhas do arquivo

    with open(path_file, 'r') as file:
        lines = file.read().splitlines()

    return lines
