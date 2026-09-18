# Desafio 59 - Criar um menu de operações matemáticas que permita
# ao usuário realizar diferentes operações com dois números,
# trocar os números ou encerrar o programa.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

roxo = '\033[1;34m'
vermelho = '\033[1;31m'
limpar = '\033[m'

while True:
    print(f'{roxo}Escolha uma das opções abaixo:{limpar}\n')

    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa\n')

    opcao = int(input(f'{roxo}Digite a opção desejada: {limpar}'))

#SOMA
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é ={soma}')

#MULTIPLICAÇÃO
    if opcao == 2:
        mult= num1 * num2
        print(f' A multiplicação entre {num1} e {num2} é = {mult}')

#MAIOR NÚMERO
    if opcao == 3:
        if num1 > num2:
            print(f'O maior número é {num1}')
        elif num2 > num1:
            print(f'O maior número é {num2}')
        else:
            print('Os números são iguais.')

#NOVOS NÚMEROS
    if opcao == 4:
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))

#SAIR DO PROGRAMA
    if opcao == 5:
        print('Finalizando o programa...')
        break

#OPCÃO INVÁLIDA
    if opcao < 1 or opcao > 5:
        print(f'{vermelho}Opção invalida! Tente novamente.{limpar}')
