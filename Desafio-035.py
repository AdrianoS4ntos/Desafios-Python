cores = {'limpa':'\033[m',
         'sublinhado':'\033[4m',
         'negritoverde':'\033[1;32m',
         'negritoroxo':'\033[1;35m'}

print('-=' * 20)
print('{}Analisador de Triângulos{}'.format(cores ['sublinhado'], cores ['limpa']))
print('-=' * 20)

n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))


if  n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima {}PODEM FORMAR{} triângulo'.format(cores ['negritoverde'], cores ['limpa']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} triângulo'.format(cores ['negritoroxo'], cores ['limpa']))
