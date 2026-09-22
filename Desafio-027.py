
# Desafio 27 - Separa e exibe o primeiro e o último nome de uma pessoa.
nome = str(input('Digite seu nome completo: ')).strip()

partes = nome.split()

print('Primeiro nome: ', partes[0])
print('Último nome: ', partes[-1])
