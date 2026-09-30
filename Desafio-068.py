# Desafio 68 - Joga Par ou Ímpar contra o computador e continua até o jogador perder.

import random
contador = 0

print('-=' * 20)
print('Vamos jogar PAR OU ÍMPAR')
print('-=' * 20)

while True:
    num = int(input('Diga um valor: '))
    escolha = input('PAR ou ÍMPAR? [P/I]: ').strip().upper()
    computador = random.randint(1,10)
    soma = num + computador
    
    if soma % 2 == 0:
        resultado = 'PAR'
        letra = 'P'
    else:
        resultado = 'ÍMPAR'
        letra = 'I'

    print('-'*35)
    print(f'Você jogou {num} e o computador {computador}. Total de {soma} DEU {resultado}')
    print('-'*35)

    if letra == escolha:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente... ')
        contador += 1

    else:
        break

print('VOCÊ PERDEU!')
print(f'GAME OVER! Você venceu {contador} vezes...')    
