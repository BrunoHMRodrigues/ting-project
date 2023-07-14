from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    # Inserção
    def enqueue(self, value):
        self._data.append(value)

    # Remoção
    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    # Busca
    def search(self, index):
        if index < 0 or index >= len(self):
            raise IndexError('Índice Inválido ou Inexistente')
        return self._data[index]
