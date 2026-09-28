# Desafio 62 - Permite mostrar termos adicionais da PA e continua até o usuário informar 0.

print('=' *25)
print('10 TERMOS DE UMA PA')
print('=' *25)

primeiro = int(input('Digite o termo de início: '))
razao = int(input('Razão da PA: '))

termo = primeiro
contador = 0
total = 0 
mais = 10 

while mais != 0:
    total += mais
    while contador < total:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão com {contador} termos mostrados')
