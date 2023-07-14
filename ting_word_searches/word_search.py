def exists_word(word, instance):
    result = []
    for item in instance._data:
        ocorrencias = []
        # for index in range(0, len(item['linhas_do_arquivo']), 1)
        #     if line.find(word) != -1:
        for index, line in enumerate(item['linhas_do_arquivo'], 1):
            if line.lower().find(word.lower()) != -1:
                ocorrencias.append({'linha': index})

        if len(ocorrencias) > 0:
            result.append({
                'palavra': word,
                'arquivo': item['nome_do_arquivo'],
                'ocorrencias': ocorrencias,
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
