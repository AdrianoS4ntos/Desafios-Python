# Desafio 51 - Lê o primeiro termo e a razão de uma PA e exibe seus 10 primeiros termos.

print('=' *25)
print('10 TERMOS DE UMA PA')
print('=' *25)

termo1 = int(input('digite um número de inicio: '))
razão = int(input('Digite qual vai ser o número de progressão: '))

termo = termo1

for c in range(10):
    print(termo)
    termo += razão
