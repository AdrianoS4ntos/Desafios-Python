n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
cores = {'limpa':'\033[m',
         'negritoverde':'\033[1;32m',
         'negritovermelho':'\033[1;31m',
         'negritoroxo':'\033[1;35m'}

media = (n1 + n2) / 2

if media < 5:
    print('{}REPROVADO COM A MÉDIA DE {:.1f}{}'.format(cores ['negritovermelho'],media, cores ['limpa']))
elif media >= 5 and media < 7:
    print('{}RECUPERAÇÃO SUA MÉDIA FOI {:.2f}{}'.format(cores ['negritoroxo'],media, cores ['limpa']))
else:
    print('{}APROVADO COM A MÉDIA DE {:.1f}{}'.format(cores ['negritoverde'],media, cores ['limpa']))
