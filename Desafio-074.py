# Desafio 74 - Sorteia cinco números aleatórios, armazena-os em uma tupla e mostra os valores sorteados, o maior e o menor número.

import random

n1 = random.randint(0,10)
n2 = random.randint(0,10)
n3 = random.randint(0,10)
n4 = random.randint(0,10)
n5 = random.randint(0,10)

numeros = (n1, n2, n3, n4, n5)

print(f'Os valores sorteados foram {numeros}')
print(f'O maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')
    