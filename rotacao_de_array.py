"""
Fonte: https://www.programcreek.com/2015/03/rotate-array-in-java/
"""


def rotacionar(lista: list, k: int) -> list:
    """
>>> rotacionar([1, 2, 3, 4, 5, 6, 7], 3)
[5, 6, 7, 1, 2, 3, 4]
    """
    resultado = []
    cursor = len(lista)-k

    for _ in lista:
        resultado.append(lista[cursor])
        cursor += 1

        if cursor == len(lista):
            cursor = 0

    return resultado
