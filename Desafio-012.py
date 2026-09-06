prod = float(input('Digite o preço do produto: '))
porc = prod*0.05
valor = prod-porc

print('o valor do desconto de 5 porcento foi de R${:.2f}'.format(valor))