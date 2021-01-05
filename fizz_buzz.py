"""
Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:
- Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
- Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
- Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.

Fonte: https://dojopuzzles.com/problems/fizzbuzz/
"""

def fb(n: int) -> None:
    for numero in range(1, n+1):
        resultado = ''

        if numero % 3 == 0:
            resultado = 'Fizz'

        if numero % 5 == 0:
            resultado += 'Buzz'

        if not resultado:
            resultado = numero

        print(resultado)
