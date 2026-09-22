# Desafio 17 - Calcula o comprimento da hipotenusa de um triângulo retângulo a partir de seus catetos.

from math import hypot
co = float(input('Digite um número: '))
ca = float(input('Digite outro número: '))
hipo = hypot(co, ca)

print('A hipotenusa de um triangulo retângulo com esses catetos é = {:.2f}'.format(hipo))
