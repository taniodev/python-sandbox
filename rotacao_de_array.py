"""
Fonte: https://www.programcreek.com/2015/03/rotate-array-in-java/
"""

from itertools import chain


def rotacionar_1(lista: list, k: int) -> list:
    """
    >>> lista = [1, 2, 3, 4, 5, 6, 7]
    >>> rotacionar_1(lista, 3)
    [5, 6, 7, 1, 2, 3, 4]
    >>> rotacionar_1(lista, 5)
    [3, 4, 5, 6, 7, 1, 2]
    """
    tamanho = len(lista)
    parte_1 = lista[tamanho-k:]
    parte_2 = lista[:tamanho-k]
    return parte_1 + parte_2


def rotacionar_2(lista: list, k: int):
    """
    >>> lista = [1, 2, 3, 4, 5, 6, 7]
    >>> list(rotacionar_2(lista, 3))
    [5, 6, 7, 1, 2, 3, 4]
    >>> list(rotacionar_2(lista, 5))
    [3, 4, 5, 6, 7, 1, 2]
    >>> next(rotacionar_2(lista, 3))   # O(1) em tempo e memória
    5
    """
    tamanho = len(lista)
    parte_1 = range(tamanho-k, tamanho)
    parte_2 = range(tamanho-k)
    sequencia = chain(parte_1, parte_2)

    for i in sequencia:
        yield lista[i]
