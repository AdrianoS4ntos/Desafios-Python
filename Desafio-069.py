# Desafio 69 - Cadastra várias pessoas, valida idade e sexo, e mostra a quantidade de pessoas maiores de 18 anos, de homens cadastrados e de mulheres menores de 20 anos.

homens = 0
maior_de_18 = 0
menor_de_20 = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    while True:
        try:
            idade = int(input('Idade: '))
            if idade > 18:
                maior_de_18 += 1
            break
        except ValueError:
            print('Digite uma idade valida.')

    sexo = input('Sexo: [M/F] ').strip().upper()
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menor_de_20 += 1

    continuar = input('Quer continuar a cadastrar? [S/N]: ').strip().upper()
    while continuar not in 'SN':
        continuar = input('Quer continuar a cadastrar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

print('=' * 10,'FIM DO PROGRAMA','=' * 10)
print(f'Total de pessoas com mais de 18 anos: {maior_de_18}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {menor_de_20} mulheres menores de 20 anos.')
