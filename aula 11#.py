'''#\033[0;30;41m
#\033[4;33;44m
#\033[1;35;43m
#\033[0;30;42m
#\033[m                 #padrao do terminal
#\033[7;30m             #pra fazer letra preta

print('\033[1;36mSup girl?\033[m ')
print('\33[0;30mHow u doing?\33[m ')
m = (' Love u')
print('Exemplo de frase:\33[32m{}\33[m'.format(m))


print('\n')
print('-=-=' * 11)
print('\33[35mWelcome to my currency converter! USD to R$\33[m')
print('-=-=' * 11)
n1 = float(input('- Amount of dollars (if u do not know type 0): USD '))
n2 = float(input('- Amount of real (if u do not know type 0): R$ '))
cc = int(input('Type \33[36m[1]\33[m if u wanna do USD to R$ or \33[36m[2]\33[m if u wanna do R$ to USD: '))
rd = 0.18 * n1
dr = 5.50 * n2
if cc == 1:
    print(f'{n1} USD equals to {dr} R$')
elif cc == 2:
    print(f'{n2} R$ equals to {rd} USD')
else:
    print('\33[31mThat\'s not an option\33[m')'''

from random import randint
lista = list()
cont = 0
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
    if cont >= 6:
        break
lista.sort()
print(f'Os nmros sorteados foram {num}')