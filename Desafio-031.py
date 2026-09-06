cores = {'limpa':'\033[m',
         'sublinhado':'\033[4m',
         'negritoverde':'\033[1;32m'}

distancia = float(input('{}Digite o valor da distância da viagem:{} '.format(cores ['sublinhado'], cores ['limpa'])))

duzentos = distancia * 0.50
maisduzen = distancia * 0.45

if distancia <= 200:
    print('Sua viagem custou R${}{:.2f}{}'.format(cores ['negritoverde'], duzentos, cores ['limpa']))
else:
    print('Sua viagem custou R${}{:.2f}{}'.format(cores ['negritoverde'], maisduzen, cores ['limpa']))

dis = int(input('Digite o valor da distância da viagem: '))

if dis <= 200:
    preco = dis * 0.50

else: 
    preco = dis * 0.45

print('Sua viagem custo R${}{:.2f}{}'.format(cores ['negritoverde'], preco, cores['limpa']))
