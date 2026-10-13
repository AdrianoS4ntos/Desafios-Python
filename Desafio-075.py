n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

numeros = (n1, n2, n3, n4)
pares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    if num == 3:
        print(f'O número 3 está na posição {numeros.index(3)}')
    else:
        print('O valor 3 não foi digitado em nenhuma posição')

print(numeros)
print(f'Os valores pares digitados foram {num}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')