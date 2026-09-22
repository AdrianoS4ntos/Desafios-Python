# Desafio 62 - Permite mostrar termos adicionais da PA e continua até o usuário informar 0.

print('=' *25)
print('10 TERMOS DE UMA PA')
print('=' *25)

termo1 = int(input('Digite um número de início: '))
razao = int(input('Digite qual vai ser o número de progressão: '))

termo = termo1

for c in range (10):
    print(termo) # Mostra o termo primeiro antes de realizar a conta
    termo += razao

mais = int(input('Quantos termos você quer a mais? '))

while mais != 0:
    for c in range(mais):
        print(termo)
        termo += razao

    mais = int(input('Quantos termos você quer a mais? '))
    
print('FIM')
