# Desafio 58 - Cria um jogo de adivinhação com número aleatório, contabilizando as tentativas e dando dicas.

import random
from time import sleep
computador = random.randint(0,10)

print('-=' * 27)
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print('-=' * 27)

jogador = int(input('Digite um número: '))
palpites = 1
while jogador != computador:
    jogador = int(input('Tente novamente: '))
    palpites += 1
    if jogador > computador:
        print('Escolhi um número menor.')
    elif jogador < computador:
        print('Escolhi um número maior.')

print('PROCESSANDO...')
sleep(2)
print('Parabéns! Você acertou!')
print(f'Você precisou de {palpites} palpites para vencer.')
