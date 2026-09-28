# Desafio 58 - Cria um jogo de adivinhação com número aleatório, contabilizando as tentativas e dando dicas.

import random
from time import sleep
computador = random.randint(0,10)

print('-=' * 27)
print('Sou seu computador...')
print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
print('-=' * 27)

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True

    else:
        if jogador > computador:
            print('Menos... tente de novo.')
        elif jogador < computador:
            print('Mais... tente de novo. ')

print('PROCESSANDO...')
sleep(2)
print('Parabéns! Você acertou!')
print(f'Você precisou de {palpites} tentativas para vencer.')
