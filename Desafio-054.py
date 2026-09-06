from datetime import date
atual = date.today().year
cores = {'limpa':'\033[m',
         'negritoverde':'\033[1;32m',
         'negritovermelho':'\033[1;31m'}

maiores = 0
menores = 0
for pess in range(1,8):
    nascimento = int(input(f'Em que ano a {pess}º pessoa nasceu? '))

    idade = atual - nascimento
    if idade < 21:
        menores = menores + 1
        print(f'você {cores ["negritovermelho"]}NÃO ATINGIU{cores["limpa"]} a maioridade, acesso negado')
    else:
        maiores = maiores +1
        print(f'acesso {cores ["negritoverde"]}LIBERADO{cores ["limpa"]}')

print(f'{maiores} Pessoas são maiores de 18 e {menores} são menores')