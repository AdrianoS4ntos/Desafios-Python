a = input('Digite algo:' )
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())

#OU#

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))        
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('A soma vale {} a multiplicação é {} e a divisão é {:.2f}'.format (s, m, d))
print('Dicisão inteira {} e potência {}'.format(di, e))