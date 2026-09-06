print('-='*15)
print('VERIFICADOR DE PALÍNDROMO')
print('-='*15)

frase = input('digite uma frase: ').strip()
frase = frase.replace(' ','').lower()
invertida = frase[::-1]

if frase == invertida:
    print('Esta frase É UM PALÍNDROMO')
else:
    print('Esta frase NÃO É UM PALÍNDROMO')
