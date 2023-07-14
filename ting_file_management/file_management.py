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

    # length_path_file = len(path_file)

    # correction_to_last_index = 1

    # last_index = length_path_file - correction_to_last_index
    # start_index = last_index - length_format

    # path_format = ''

    # length_format = 4

    # Verificar se formato do arquivo é .txt
    # for i in range(start_index, last_index, 1 ):
    #     path_format[i] = path_file[i]
    # if path_format != '.txt':
    #     raise IndexError('Formato inválido na stderr')

    # retorna uma lista contendo as linhas do arquivo

    with open(path_file, 'r') as file:
        lines = file.read().splitlines()

    return lines
