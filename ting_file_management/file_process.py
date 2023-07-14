from .file_management import txt_importer
# import sys
# sys.path.append('ting_file_management/file_management.py/diretorio')


def process(path_file, instance):
    # path_file_is_in_instamce = False
    for item in instance._data:
        if item['nome_do_arquivo'] == path_file:
            # path_file_is_in_instamce = True
            print(f"Arquivo {path_file} já existente na fila. Ignorando...")
            return None

    # if path_file_is_in_instamce == False:
    lines = txt_importer(path_file)
    new_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines,
    }

    instance.enqueue(new_dict)

    print(new_dict)

    # return new_dict


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
