# Desafio 66 - Lê valores inteiros até o usuário informar 999 e mostra a quantidade e a soma dos números digitados.

valor = 0
soma = 0
contador = 0

while True:
    valor = int(input('Digite um valor, [999] para parar: '))

    if valor == 999:
        break
    
    soma += valor
    contador += 1
    

print(f'Você digitou {contador} valores e a soma é {soma}')
