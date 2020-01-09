"""
Exercício Torre de Hanoi Recursivo
"""


def hanoi(n: int, orig='A', aux='B', dest='C') -> None:
    if n >= 1:
        hanoi(n-1, orig, dest, aux)
        print(f'De {orig} para {dest}: {n}')
        hanoi(n-1, aux, orig, dest)
