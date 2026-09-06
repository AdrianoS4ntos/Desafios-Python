casa = float(input('Qual é o valor da casa?: '))
salario = float(input('Qual é o seu salário?: '))
anos = int(input('Em quantos anos de financiamento?: '))
cores = {'limpa': '\033[m',
         'negritoverde': '\033[1;32m',
         'negritovermelho': '\033[1;31m'}

prestacao = casa / (anos * 12)
limite = salario * 0.30

if prestacao > limite:
    print('Emprestimo {}negado{}, o valor da prestação mesal {:.2f} excede à 30% do seu salário'.format(cores ['negritovermelho'], cores ['limpa'], prestacao))
else:
    print('Emprestimo {}aprovado{} o valor da prestação é {:.2f}'.format(cores ['negritoverde'],  cores ['limpa'], prestacao))
