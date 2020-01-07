"""
Funções para calcular o máximo e o mínimo de uma lista
"""


def max_min_1(lst: list) -> tuple:
    """
    Retorne o máximo e o mínimo de uma lista

    Se a lista estiver vazia, deve lançar uma exception.
    A lista em lst está ordenada em ordem crescente.
    >>> max_min_1([2, 3, 6, 8, 9])
    (9, 2)

    """
    if len(lst) == 0:
        raise ValueError('A lista está vazia')

    return (lst[-1], lst[0],)


def max_min_2(lst: list) -> tuple:
    """
    Retorne o máximo e o mínimo de uma lista

    Se a lista estiver vazia, deve lançar uma exception.
    A lista em lst pode estar ordenada ou embaralhada, não sabemos a ordem.
    >>> max_min_2([2, 3, 6, 8, 9])
    (9, 2)
    >>> max_min_2([5, 7, 2, 16, 8, 9])
    (16, 2)

    """
    if len(lst) == 0:
        raise ValueError('A lista está vazia')

    return (max(lst), min(lst),)


def max_min_3(lst: list) -> tuple:
    """
    Retorne o máximo e o mínimo de uma lista

    Se a lista estiver vazia, deve lançar uma exception.
    A lista em lst pode estar ordenada ou embaralhada, não sabemos a ordem.
    >>> max_min_3([2, 3, 6, 8, 9])
    (9, 2)
    >>> max_min_3([5, 7, 2, 16, 8, 9])
    (16, 2)

    """
    if len(lst) == 0:
        raise ValueError('A lista está vazia')

    maximo = lst[0]
    minimo = lst[0]

    for valor in lst:
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor

    return (maximo, minimo,)
