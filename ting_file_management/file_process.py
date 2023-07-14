from .file_management import txt_importer


def process(path_file, instance):
    for item in instance._data:
        if item['nome_do_arquivo'] == path_file:
            print(f"Arquivo {path_file} já existente na fila. Ignorando...")
            return None

    lines = txt_importer(path_file)
    new_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines,
    }

    instance.enqueue(new_dict)

    print(new_dict)


def remove(instance):
    if not len(instance) >= 1:
        print('Não há elementos')
        return None
    removed_instance = instance.dequeue()
    path_file = removed_instance['nome_do_arquivo']
    print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
