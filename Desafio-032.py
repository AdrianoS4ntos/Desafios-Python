from datetime import date
cores = {'limpa':'\033[m',
         'negritovermelho':'\033[1;31m',
         'negritoverde':'\033[1;32m'}

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: 
    print('O ano {} {}é BISSEXTO.{}'.format(ano, cores ['negritoverde'], cores['limpa']))
else:
    print('O ano {} {}NÃO é BISSEXTO{}'.format(ano, cores ['negritovermelho'], cores ['limpa']))
