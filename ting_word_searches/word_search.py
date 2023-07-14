def get_occurrences(lines, word, is_function_exists):
    occurrences = []
    for index, line in enumerate(lines, 1):
        if line.lower().find(word.lower()) != -1:
            if is_function_exists:
                occurrences.append({'linha': index})
            else:
                occurrences.append({
                    'linha': index,
                    'conteudo': line,
                })
    return occurrences


def build_output(occurrences, result, word, name):
    if len(occurrences) > 0:
        result.append({
            'palavra': word,
            'arquivo': name,
            'ocorrencias': occurrences,
        })

    return result


def exists_word(word, instance):
    result = []
    is_function_exists = True

    for item in instance._data:
        lines = item['linhas_do_arquivo']

        occurrences = get_occurrences(lines, word, is_function_exists)

        # ocorrencias = []
        # for index, line in enumerate(item['linhas_do_arquivo'], 1):
        #     if line.lower().find(word.lower()) != -1:
        #         ocorrencias.append({'linha': index})

        name = item['nome_do_arquivo']
        result = build_output(occurrences, result, word, name)
        # if len(occurrences) > 0:
        #     result.append({
        #         'palavra': word,
        #         'arquivo': item['nome_do_arquivo'],
        #         'ocorrencias': occurrences,
        #     })
    return result


def search_by_word(word, instance):
    result = []
    is_function_exists = False

    for item in instance._data:
        lines = item['linhas_do_arquivo']

        occurrences = get_occurrences(lines, word, is_function_exists)

        name = item['nome_do_arquivo']
        result = build_output(occurrences, result, word, name)

    return result
