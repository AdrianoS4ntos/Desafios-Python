# Desafio 46 - Realiza uma contagem regressiva de 10 até 0 com uma pausa entre os números.

from time import sleep
cores = {'limpa':'\033[m',
         'negritovermelho':'\033[1;31m'}

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(f'{cores ["negritovermelho"]}BOMMMMMM!{cores ["limpa"]}')
