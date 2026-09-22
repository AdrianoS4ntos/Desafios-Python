# Desafio 55 - Lê os pesos de cinco pessoas e identifica o maior e o menor peso informado.

maiorpeso = 0
menorpeso = 0
for p in range (1,6):
    peso = float(input(f'Peso da {p}º pessoa: '))

    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print(f'O MAIOR peso lido foi de {maiorpeso}kg')
print(f"O MENOR peso lido foi de {menorpeso}kg")
