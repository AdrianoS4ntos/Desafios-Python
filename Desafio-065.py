# Desafio 65 - Calcula a média, o maior e o menor valor entre os números digitados pelo usuário.

pergunta = 'S'

soma = 0
contador = 0
maior_num = 0
menor_num = 0

while pergunta == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    media = soma / contador

    if contador == 1:
        maior_num = menor_num = numero

    else:
        if numero > maior_num:
            maior_num = numero
        if numero < menor_num:
            menor_num = numero

    pergunta = input('Quer continuar? [S/N]: ').upper().strip()

print(f'Você digitou {contador} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior_num} e o menor foi {menor_num}')
