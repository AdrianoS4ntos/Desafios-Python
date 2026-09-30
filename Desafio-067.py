# Desafio 67 - Mostra a tabuada de vários números e encerra quando um número negativo é informado.

while True:
    num = int(input('Quer ver a tabuada de que valor? '))

    if num < 0:
            print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
            break
    
    print('-' * 35)   
    for multiplicador in range(1, 11): 
        resultado = num * multiplicador
        print(f'{num} x {multiplicador} = {resultado}')
    print('-' * 35)
    