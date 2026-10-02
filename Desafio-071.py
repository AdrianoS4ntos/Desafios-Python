print('=' * 30)
print('CAIXA ELETRÔNICO')
print('=' * 30)

cedulas_de_100 = 0
cedulas_de_50 = 0
cedulas_de_20 = 0
cedulas_de_10 = 0
moedas_de_1 = 0

valor = int(input('Qual valor você quer sacar? R$'))

while True:
    if valor >= 100:
        cedulas_de_100 += 1
        valor -= 100
    elif valor >= 50:
        cedulas_de_50 += 1
        valor -= 50
    elif valor >= 20:
        cedulas_de_20 += 1
        valor -= 20
    elif valor >= 10:
        cedulas_de_10 += 1
        valor -= 10
    elif valor >= 1:
        moedas_de_1 += 1
        valor -=1
    if valor == 0:
        break

print(f'Total de {cedulas_de_100} cédulas de R$100')
print(f'Total de {cedulas_de_50} cédulas de R$50')
print(f'Total de {cedulas_de_20} cédulas de R$20')
print(f'Total de {cedulas_de_10} cédulas de R$10')
print(f'Total de {moedas_de_1} moedas de R$1')
print('=' * 30)
print('Volte sempre ao nosso caixa eletrônico!')