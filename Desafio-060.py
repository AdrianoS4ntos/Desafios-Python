# Desafio 60 - Calcula o fatorial de um número informado pelo usuário utilizando uma estrutura de repetição.

from math import factorial

num = int(input('Digite um número para calcular seu fatorial: '))

f = factorial(num)

print(f'O fatorial de {num} é {f}.')

#==========
#   OU
#==========

from math import factorial

n = int(input('Digite  um número para calcular seu Fatorial: '))

contador = n
f = factorial(n)

print(f'Calculando {n}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1
print(f)