# Desafio 08 - Converte uma distância informada em metros para outras unidades de medida.

metros = float(input('Digite um valor na uni. de medida metros: '))
cm = metros*100
mm = metros*1000

print('convertendo para cm fica ={}cm. e para mm fica = {}mm'.format(cm, mm))
