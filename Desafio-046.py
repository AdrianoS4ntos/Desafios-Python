from time import sleep
cores = {'limpa':'\033[m',
         'negritovermelho':'\033[1;31m'}

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(f'{cores ["negritovermelho"]}BOMMMMMM!{cores ["limpa"]}')
