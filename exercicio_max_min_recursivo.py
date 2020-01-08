"""
Calcular o máximo e o mínimo de uma lista de forma recursiva
"""


def max_min(lst: list) -> tuple:
    """
    Retorne o máximo e o mínimo de uma lista

    Se a lista estiver vazia, deve lançar uma exception.
    A lista em lst pode estar ordenada ou embaralhada, não sabemos a ordem.
    >>> max_min([4])
    (4, 4)
    >>> max_min([2, 3, 6, 8, 9])
    (9, 2)
    >>> max_min([5, 7, 2, 16, 8, 9])
    (16, 2)

    """
    if len(lst) == 0:
        raise ValueError('A lista está vazia')

    maximo = lst[-1]
    minimo = lst[-1]
    cursor = len(lst)-1

    def max_min_rec(cursor):
        nonlocal maximo
        nonlocal minimo

        if cursor < 0:
            return (maximo, minimo,)

        if lst[cursor] > maximo:
            maximo = lst[cursor]
        if lst[cursor] < minimo:
            minimo = lst[cursor]
        return max_min_rec(cursor-1)

    return max_min_rec(cursor)
