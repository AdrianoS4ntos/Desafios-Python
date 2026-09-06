n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

if n1 > n2:
    print('O valor {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O valor {} é maior  que {}'.format(n2, n1))
else:
    print('Os valores {} e {} são iguais'.format(n1, n2))
