cores = {'limpa':'\033[m',
         'sublinhadociano':'\033[4;36m',
         'negritovermelho':'\033[1;31m',
         'negritoverde':'\033[1;32m'}

velo = int(input('{}Qual foi a velocidade do carro? :{} '.format(cores ['sublinhadociano'], cores ['limpa'])))
valor = (velo - 80) * 7


if velo > 80:
    print('{}MULTADO{}, você excedeu o limite permitido de 80km/h Você deve pagar uma muta de  R${:.2f}'.format(cores ['negritovermelho'], cores ['limpa'], valor))
else:
    print('{}Você está dentro da velocidade permitida :){}'.format(cores ['negritoverde'], cores ['limpa']))
