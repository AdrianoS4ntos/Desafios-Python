# Desafio 67 - Mostra a tabuada de vários números e encerra quando um número negativo é informado.

while True:
    num = int(input('Quer ver a tabuada de que valor? '))
    print('-' * 35)
    if num < 0:
        break
    
    for multiplicador in range(1, 11): 
        print(f'{num} x {multiplicador} = {num * multiplicador}')
    print('-' * 35)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
