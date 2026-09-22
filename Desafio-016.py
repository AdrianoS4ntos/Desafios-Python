# Desafio 16 - Recebe um número real e separa sua parte inteira da parte decimal.

import math
n = float(input('Digite um número real: '))
r = math.trunc(n)
print('A parte inteira de {} é {}'.format(n, r))
