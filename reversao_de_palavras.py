"""
fonte: https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/
"""


def reverter_1(frase: str) -> str:
    """
    >>> reverter_1('the sky is blue')
    'blue is sky the'
    >>> reverter_1('uma baita frase')
    'frase baita uma'
    """
    lista_de_palavras = frase.split()   # Tempo e memória linear
    palavras_reordenadas = reversed(lista_de_palavras)
    return ' '.join(palavras_reordenadas)


def reverter_palavra(frase: list, inicio: int, fim: int) -> None:
    while inicio < fim:
        frase[inicio], frase[fim] = frase[fim], frase[inicio]
        inicio += 1
        fim -= 1


def reverter_2(frase: list) -> list:
    """
    >>> reverter_2(['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'])
    ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
    >>> reverter_2(['u', 'm', 'a', ' ', 'b', 'a', 'i', 't', 'a', ' ', 'f', 'r', 'a', 's', 'e'])
    ['f', 'r', 'a', 's', 'e', ' ', 'b', 'a', 'i', 't', 'a', ' ', 'u', 'm', 'a']
    """
    # Algoritmo com memória constante e tempo linear
    inicio = 0

    for indice, letra in enumerate(frase):
        if letra == ' ':
            reverter_palavra(frase, inicio, indice-1)
            inicio = indice+1

    reverter_palavra(frase, inicio, len(frase)-1)
    frase.reverse()   # Tempo O(n), e memória O(1)

    return frase

