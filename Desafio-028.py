import random
from time import sleep
computador = random.randint(0, 5)
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'ciano':'\033[36m'}

print('-=' * 20)
print('{}Vou pensar em um número de 0 a 5. Tente adivinhar...{}'.format(cores ['amarelo'], cores ['limpa']))
print('-=' * 20)

jogador = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('{}Você venceu :){}'.format(cores ['ciano'], cores ['limpa']))
else:
    print('{}Você perdeu :(  eu pensei no número{} {}'.format(cores ['vermelho'], cores ['limpa'], computador))