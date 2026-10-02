# Desafio 70 - Cadastra vários produtos, calcula o total da compra, conta quantos produtos custam mais de R$1000 e identifica o produto mais barato.

print('-' * 30)
print('LOJA SUPER BARATÃO')
print('-' * 30)

total = 0
produtos_mais_de_1000 = 0
nome_produto_mais_barato = ''
preco_produto_mais_barato = 0

while True:
    nome_produto = input('Nome do produto: ')
    preco_produto = float(input('Preço: R$'))
    total += preco_produto

    if preco_produto > 1000:
        produtos_mais_de_1000 += 1

    if preco_produto_mais_barato == 0:
        preco_produto_mais_barato = preco_produto
        nome_produto_mais_barato = nome_produto

    else:
        if preco_produto < preco_produto_mais_barato:
            preco_produto_mais_barato = preco_produto
            nome_produto_mais_barato = nome_produto

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtos_mais_de_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_produto_mais_barato} que custa R${preco_produto_mais_barato:.2f}')
    