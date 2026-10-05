# Desafio 68 - Joga Par ou Ímpar contra o computador e continua até o jogador perder.

import random
vitorias = 0

print('-=' * 20)
print('Vamos jogar PAR OU ÍMPAR')
print('-=' * 20)

while True:
    jogador = int(input('Diga um valor: '))
    computador = random.randint(1,10)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('PAR ou ÍMPAR? [P/I]: ').strip().upper()

    print('-'*35)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}.', end=' ')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-'*35)

    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            break
    elif escolha == 'I' :
        if soma % 2 != 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            break
    print('Vamos jogar novamente... ')
print('VOCÊ PERDEU!')
print(f'GAME OVER! Você venceu {vitorias} vezes...')    
