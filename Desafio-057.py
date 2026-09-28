# Desafio 57 - Solicita um gênero ao usuário e repete a entrada enquanto o valor informado for inválido.

genero  = input('Digite seu gênero [F/M]: ').strip().upper()[0]

while genero not in 'FM':
    genero = input('Gênero inválido. Por favor, digite novamente: ').strip().upper()[0]
print(f'Genero {genero} registrado com sucesso!')
    