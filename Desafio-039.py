from datetime import date
jovem = int(input('Qual é seu ano de nascimento?: '))
anoatual = date.today().year
cores = {'limpa': '\033[m',
        'negritoverde':'\033[1;32m',
        'negritovermelho': '\033[1;31m',
        'negritoroxo': '\033[1;35m'}

idade = anoatual - jovem
vai = 18 - idade
tinha = idade - 18

if idade <= 17:
    
    print('{}Você tem que se alistar daqui á {} anos{} no caso em {}'.format(cores ['negritoverde'], vai, cores ['limpa']))
elif idade == 18:
    print('{}VOCÊ TEM QUE SE ALISTAR ESSE ANO DE {} {}'.format(cores ['negritoroxo'], anoatual, cores ['limpa']))
else:
    print('{}VOCÊ TINHA QUE TER SE ALISTADO A {} ANOS ATRÁS{}'.format(cores ['negritovermelho'],tinha, cores ['limpa']))