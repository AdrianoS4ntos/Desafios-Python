frase = input('Digite uma frase: ').strip()

minus = frase.lower()

print('A letra A aparece {} vezes na frase'.format(minus.count('a')))

print('A primeira letra A apareceu na posição {}'.format(minus.find('a')+1))

print('A última letra A apareceu na posição {}'.format(minus.rfind('a')+1))
