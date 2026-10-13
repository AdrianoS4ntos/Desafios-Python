# Desafio 73 - Exibe os times do Brasileirão, mostra os 5 primeiros e os 4 últimos colocados, ordena os times em ordem alfabética e informa a posição da Chapecoense.

brasileirao = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Cruzeiro', 'Bahia', 'Bragantino', 'Coritiba', 'Atlético-MG', 'Corinthians', 'Botafogo', 'Vitória', 'São Paulo', 'Santos', 'Grêmio', 'Mirassol', 'Remo', 'Vasco', 'Internacional', 'Chapecoense')

print('-='*20)
print(f'Lista dos times Brasileirão 2026: {brasileirao}')
print('-='*20)


print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-='*20)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*20)
print(f'O Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição.')
