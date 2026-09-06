peso = int(input('digite seu peso em (Kg): '))
alt = float(input('Digite sua altura em (m): '))
cores = {'limpa':'\033[m',
         'negritovermelho':'\033[1;31m'}

imc = peso / (alt**2)

if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal')
elif imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está  em {}OBESIDADE!{}'.format(cores ['negritovermelho'], cores ['limpa']))
else:
    print('Você está em {}OBSIDADE MÓRBIDA, cuidado!{}'.format(cores ['negritovermelho'], cores ['limpa']))
print('E seu IMC é {:.1f}'.format(imc))
