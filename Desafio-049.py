# Desafio 49 - Exibe a tabuada de um número escolhido pelo usuário utilizando uma estrutura de repetição.

num = int(input('Qual número você quer ver a tabuada?: '))

for c in range(1,11):
    print(f'{num} x {c} = {num*c}')
