# Desafio 64 - Permite somar e contar vários números até o usuário informar 999.

num = int(input('Digite um número [999 para parar]: '))

soma = 0
contador = 0

while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite outro número [999 para parar]: '))


print(f'A soma dos números digitados é {soma}')
print(f'Você digitou {contador} números')
