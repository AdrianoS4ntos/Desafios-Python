# Desafio 23 - Separa um número de quatro dígitos em unidade, dezena, centena e milhar.

n = input('Digite um número de 0 a 9999: ')
 
unidade = n[3]
dezena = n[2]
centena = n[1]
milhar = n[0]

print('unidade:{}'.format(unidade))
print('dezena:{}'.format(dezena))
print('centena:{}'.format(centena))
print('milhar:{}'.format(milhar))
