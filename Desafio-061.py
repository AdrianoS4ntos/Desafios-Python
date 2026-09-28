# Desafio 61 - Refaz a PA do desafio 51 utilizando while para mostrar os 10 primeiros termos.

print('=' *25)
print('10 TERMOS DE UMA PA')
print('=' *25)

primeiro = int(input('Digite o termo de início: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 0

while contador < 10:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
print('FIM')
