larg = float(input('Digite a largura da parede: '))
altu = float(input('Digite a altura da sua parede: '))
area = larg*altu
calc = area/2

print('A área da sua parede é {}, e a quantidade necessária de tinta seria {:.2f} litros'.format(area, calc))