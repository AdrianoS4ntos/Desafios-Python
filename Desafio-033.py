
a = int(input('Primeiro número: '))
b  = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

#verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c 

print('O menor número digitado é {}'.format(menor))
print('O maior número digitado é {}'.format(maior))