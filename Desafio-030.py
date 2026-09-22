# Desafio 30 - Verifica se um número inteiro informado pelo usuário é par ou ímpar.

nu = int(input('Digite um número: '))

if nu % 2 == 0:
    print('{} é um número par'.format(nu))
else:
    print('{} é um número ímpar'.format(nu))
    