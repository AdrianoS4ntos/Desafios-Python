import random
aluno1 = input('Aluno 1: ')
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

nomes = [aluno1, aluno2, aluno3, aluno4]
aleatorio = random.choice(nomes)

print('O sortudo foi {}!!!!'.format(aleatorio))
