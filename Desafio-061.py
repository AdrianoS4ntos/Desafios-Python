# Desafio 61 - Refaz a PA do desafio 51 utilizando while para mostrar os 10 primeiros termos.

print('=' *25)
print('10 TERMOS DE UMA PA')
print('=' *25)

termo1 = int(input('Digite um número de início: '))
razao = int(input('Digite qual vai ser o número de progressão: '))

termo = termo1
contador = 0

while contador < 10:
        print(termo)
        termo += razao
        contador += 1
print('FIM')
    
