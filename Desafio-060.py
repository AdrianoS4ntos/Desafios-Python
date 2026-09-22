# Desafio 60 - Calcula o fatorial de um número informado pelo usuário utilizando uma estrutura de repetição.

num = int(input('Digite um número: '))

contador = num
resultado = 1
expressao = ('')

# Reduz o número a cada repetição e acumula o resultado do fatorial.
while contador >= 1:
    resultado *= contador
    expressao += contador

    contador -= 1

print(expressao)