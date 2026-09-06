print('=' * 15)
print('LOJAS ADRIANO')
print('=' * 15)

produto = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO: 
[1] à vista Dinheiro ou Cheque  
[2] à vista Cartão à vista 
[3] 2x no cartão 
[4] 3x ou mais''')
pagamento = int(input('Qual a opção de pagamento?: '))

if pagamento == 1:
   total = produto - produto * 0.10
elif pagamento == 2:
    total = produto - produto * 0.05
elif pagamento == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif pagamento == 4:
    total = produto + produto * 0.20
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela ))
else:
    total = produto
    print('OPÇÃO INVALIDA')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, produto))
