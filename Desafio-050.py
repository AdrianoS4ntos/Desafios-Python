soma = 0
cont = 0 
for num in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'A soma de todos os {cont} números PARES são: {soma}')
