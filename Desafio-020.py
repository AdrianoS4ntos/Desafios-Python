# Desafio 20 - Recebe os nomes de quatro alunos e sorteia a ordem de apresentação dos trabalhos.

import random
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

nomes = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(nomes)

print('A ordem será: {}'.format(nomes))
