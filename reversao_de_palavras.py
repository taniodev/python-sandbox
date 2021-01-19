"""
fonte: https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/
"""


def reverter(frase: str) -> str:
    """
    >>> reverter('the sky is blue')
    'blue is sky the'
    >>> reverter('uma baita frase')
    'frase baita uma'
"""
    lista_de_palavras = frase.split()   # Tempo e memória linear
    palavras_reordenadas = reversed(lista_de_palavras)
    return ' '.join(palavras_reordenadas)

