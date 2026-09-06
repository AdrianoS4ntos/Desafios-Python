from datetime import date
nas = int(input('Qual ano você nasceu?: '))
ano_atual = date.today().year

idade = ano_atual - nas

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SÉNIOR')
else:
    print('Sua categoria é MASTER')
    