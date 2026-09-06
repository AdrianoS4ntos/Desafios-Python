salario = float(input('Qual o salário do funcionario? R$'))
cores = {'limpa':'\033[m',
         'negritoroxo':'\033[1;35m',
         'negritoverde':'\033[1;32m'}

if salario > 1250:
    aumento = salario * 0.10 + salario
else:
    aumento = salario * 0.15 + salario

print('O seu salario foi de R${}{:.2f}{} para R${}{:.2f}{}'.format(cores ['negritoroxo'], salario, cores ['limpa'], cores ['negritoverde'],aumento, cores ['limpa']))
