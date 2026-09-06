import random
from time import sleep
cores = {'limpa':'\033[m',
         'negritovermelho':'\033[1;31m',}

print('-='*20)
print('Desafio, vamos jogar {}JOKENPÔ...{}'.format(cores ['negritovermelho'], cores ['limpa']))
print('-='*20)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0,2)
print('''SUAS OPÇÕES:
[0] = pedra
[1] = papel
[2] = tesoura''')
jogador = int(input('Qual você escolhe: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-='*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*20)

#EMPATE
if jogador == computador:
    print('DEU EMPATE, MAS VALEU A TENTATIVA!!')
#VENCEU
elif jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('JOGADOR VENCEU')
#PERDEU
else:
    print('COMPUTADOR VENCEU')
