from math import sin, cos, tan, radians
angu = float(input('Digite o valor do  ângulo: '))
rad = radians(angu)
se = sin(rad)
co = cos(rad)
ta = tan(rad)

print('O SENO é {:.2f} o COSSENO é {:.2f} e a TANGENTE é {:.2f}'.format(se, co, ta))
