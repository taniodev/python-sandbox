"""
Torre de Hanoi iterativo
"""


def hanoi(n: int, orig='A', aux='B', dest='C') -> None:
    pilha = [(False, n, orig, aux, dest)]

    while pilha:
        print_flag, n, orig, aux, dest = pilha.pop()

        if n < 1:
            continue

        if not print_flag:
            pilha.append((True, n, orig, aux, dest))
            pilha.append((False, n-1, orig, dest, aux))
        else:
            print(f'De {orig} para {dest}: {n}')
            pilha.append((False, n-1, aux, orig, dest))
