# Desafio 15 - Calcula o valor do aluguel de um carro com base nos dias utilizados e na distância percorrida.

dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
resul = dias*60 + km*0.15

print('O total a pagar é de R${:.2f}'.format(resul))
