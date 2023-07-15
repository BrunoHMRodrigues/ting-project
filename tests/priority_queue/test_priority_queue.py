import pytest

from ting_file_management.priority_queue import PriorityQueue

queue_high_priority_item_1 = {
    "nome_do_arquivo": "arquivo_high_priority_item_1.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [
        'teste high item 1',
        'dos testes high item 1',
        'vqv high item 1'
    ]
}

queue_high_priority_item_2 = {
    "nome_do_arquivo": "arquivo_high_priority_item_2.txt",
    "qtd_linhas": 2,
    "linhas_do_arquivo": [
        'teste high item 2',
        'dos testes high item 2'
    ]
}

queue_high_priority_item_3 = {
    "nome_do_arquivo": "arquivo_high_priority_item_3.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": [
        'teste high item 3',
        'dos testes high item 3',
        'vqv high item 3',
        'testando high item 3'
    ]
}

queue_regular_priority_item_1 = {
    "nome_do_arquivo": "arquivo_regular_priority_item_1.txt",
    "qtd_linhas": 5,
    "linhas_do_arquivo": [
        'teste regular item 1',
        'dos testes regular item 1',
        'vqv regular item 1',
        'testando regular item 1',
        'mais uma linha regular item 1'
    ]
}

queue_regular_priority_item_2 = {
    "nome_do_arquivo": "arquivo_regular_priority_item_2.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": [
        'teste regular item 2',
        'dos testes regular item 2',
        'vqv regular item 2',
        'testando regular item 2',
        'mais uma linha regular item 2',
        'ultima linha regular item 2'
    ]
}

queue_regular_priority_item_3 = {
    "nome_do_arquivo": "arquivo_regular_priority_item_3.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": [
        'teste regular item 3',
        'dos testes regular item 3',
        'vqv regular item 3',
        'testando regular item 3',
        'último item regular item 3',
        'último item mesmo regular item 3'
    ]
}


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue(queue_regular_priority_item_1)
    pq.enqueue(queue_high_priority_item_2)
    pq.enqueue(queue_regular_priority_item_3)
    pq.enqueue(queue_high_priority_item_3)

    assert len(pq.high_priority) == 2
    assert len(pq.regular_priority) == 2

    pq.dequeue()

    assert len(pq.high_priority) == 1
    assert len(pq.regular_priority) == 2

    assert pq.search(0) == queue_high_priority_item_3
    assert pq.search(2) == queue_regular_priority_item_3

    pq.dequeue()

    assert len(pq.high_priority) == 0
    assert len(pq.regular_priority) == 2

    pq.dequeue()

    assert len(pq.high_priority) == 0
    assert len(pq.regular_priority) == 1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(999)


# Verificar por que abaixo não funciona
# def test_basic_priority_queueing():
#     test_high_priority_queueing()
#     test_regular_priority_queueing()
#     test_dequeue_high_priority()
#     test_dequeue_regular_priority()
#     test_dequeue_general()
#     test_search_high_priority()
#     test_search_regular_priority()


# def test_high_priority_queueing():
#     pq = PriorityQueue()

#     pq.enqueue(queue_high_priority_item_2)
#     pq.enqueue(queue_high_priority_item_3)
#     pq.enqueue(queue_high_priority_item_1)

#     assert len(pq.high_priority) == 3
#     assert len(pq.regular_priority) == 0
#     assert pq.high_priority[2] == queue_high_priority_item_1


# def test_regular_priority_queueing():
#     pq = PriorityQueue()

#     pq.enqueue(queue_regular_priority_item_1)
#     pq.enqueue(queue_regular_priority_item_3)
#     pq.enqueue(queue_regular_priority_item_2)

#     assert len(pq.high_priority) == 0
#     assert len(pq.regular_priority) == 3
#     assert pq.regular_priority[2] == queue_regular_priority_item_2


# def test_dequeue_high_priority():
#     pq = PriorityQueue()

#     pq.enqueue(queue_high_priority_item_3)
#     pq.enqueue(queue_high_priority_item_2)

#     assert len(pq.high_priority) == 2
#     assert len(pq.regular_priority) == 0

#     item = pq.dequeue()

#     assert item == queue_high_priority_item_3
#     assert len(pq.high_priority) == 1
#     assert len(pq.regular_priority) == 0


# def test_dequeue_regular_priority():
#     pq = PriorityQueue()

#     pq.enqueue(queue_regular_priority_item_3)
#     pq.enqueue(queue_regular_priority_item_2)

#     assert len(pq.high_priority) == 0
#     assert len(pq.regular_priority) == 2

#     item = pq.dequeue()

#     assert item == queue_regular_priority_item_3
#     assert len(pq.high_priority) == 0
#     assert len(pq.regular_priority) == 1

# def test_dequeue_general():
#     pq = PriorityQueue()

#     pq.enqueue(queue_regular_priority_item_3)
#     pq.enqueue(queue_high_priority_item_2)
#     pq.enqueue(queue_regular_priority_item_2)
#     pq.enqueue(queue_high_priority_item_1)
#     pq.enqueue(queue_regular_priority_item_1)

#     assert len(pq.high_priority) == 2
#     assert len(pq.regular_priority) == 3

#     item = pq.dequeue()

#     assert item == queue_high_priority_item_2
#     assert len(pq.high_priority) == 1
#     assert len(pq.regular_priority) == 3

#     item = pq.dequeue()

#     assert item == queue_high_priority_item_1
#     assert len(pq.high_priority) == 0
#     assert len(pq.regular_priority) == 3


# def test_search_high_priority():
#     # Testa a busca por índice nos arquivos prioritários
#     pq = PriorityQueue()

#     pq.enqueue(queue_high_priority_item_2)
#     pq.enqueue(queue_high_priority_item_1)

#     item = pq.search(0)

#     assert item == queue_high_priority_item_2


# def test_search_regular_priority():
#     # Testa a busca por índice nos arquivos prioritários
#     pq = PriorityQueue()

#     pq.enqueue(queue_regular_priority_item_2)
#     pq.enqueue(queue_high_priority_item_2)
#     pq.enqueue(queue_high_priority_item_1)

#     item1 = pq.search(0)

#     assert item1 == queue_high_priority_item_2

#     item2 = pq.search(1)

#     assert item2 == queue_high_priority_item_1

#     item3 = pq.search(2)

#     assert item3 == queue_regular_priority_item_2

# def test_search_inexistent():
#     # Testa a busca por índice nos arquivos prioritários
#     pq = PriorityQueue()

#     pq.enqueue(queue_regular_priority_item_2)
#     pq.enqueue(queue_high_priority_item_2)
#     pq.enqueue(queue_high_priority_item_1)

#     with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
#         item = pq.search(999)
