nu = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão:\n [ 1 ] converter para BINÁRIO\n [ 2 ] converter para OCTAL\n [ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(nu, bin(nu)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(nu, oct(nu)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(nu, hex(nu)[2:]))
else:
    print('Opção inválida')
