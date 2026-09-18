# Desafio 60 - Calcular o fatorial de um número informado pelo usuário,
# mostrando o processo das multiplicações e o resultado final.

num = int(input('Digite um número: '))

original = num
fatorial = num
expressao = str(num)

# Reduz o número a cada repetição e acumula o resultado do fatorial.
while fatorial > 1:
    fatorial -= 1
    num *= fatorial
    expressao = expressao + ' x ' + str(fatorial)

print(f'O fatorial de {expressao} = {num}')
print(f'{original}! = {num}')