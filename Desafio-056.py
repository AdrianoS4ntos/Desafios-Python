somaidade = 0
médiaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0

for pess in range(1,5):
    print(f'---- {pess}º PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    Sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade

    if pess == 1 and Sexo in 'Mm':
        maioridadehomen = idade
        nomevelho= nome
    if Sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if Sexo in 'Ff' and idade < 20:
        totmulher20 += 1

médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomen} anos')
print(f'Ao todo são {totmulher20} mulheres com mais de 20 anos')
