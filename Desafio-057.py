genero  = input('Digite seu gênero [F/M]: ').strip().upper()

while genero not in 'FM':
    print('Gênero inválido. Por favor, digite novamente.')
    genero = input('Digite seu gênero [F/M]: ').strip().upper()


if genero == 'M':
    print('Você é do gênero masculino.')
elif genero == 'F':
    print('Você é do gênero feminino.')
