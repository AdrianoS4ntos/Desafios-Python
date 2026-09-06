print('=' *25)
print('10 TERMOS DDE UMA PA')
print('=' *25)

termo1 = int(input('digite um número de inicio: '))
razão = int(input('Digite qual vai ser o número de progressão: '))

termo = termo1

for c in range(10):
    print(termo)
    termo += razão
