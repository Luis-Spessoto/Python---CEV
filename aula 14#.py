import math
import random
import time

'''for x in range(1, 11):
    print(x)
print('Fim')
x = 1
while x < 11:
    print(x)
    x = x + 1
print('Fim')
x = 1
par = impar = 0
while x != 0:
    x = int(input('Digite um valor: '))
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
print('Vc digitou {} numeros pares e {} numeros impares\n'.format(par, impar))
print('Fim')'''

print('\nEx 057')
print('\33[33m-=\33[m'*23)
x = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
if x in 'MmFf':
    print('Sexo \33[36m{}\33[m registrado com sucesso.'.format(x))
else:
    while x not in 'MmFf':
        x = str(input('\33[31mDados invalidos!\33[mPor favor, informe seu sexo: '))
    print('Sexo \33[36m{}\33[m registrado com sucesso.'.format(x))
print('\33[33m-=\33[m'*23)

print('\nEx 058')
print('\33[31mI\'m your computer...\33[m')
time.sleep(1)
print('\33[31mI\33[m just thought of a number between \33[35m0 - 10\33[m.')
time.sleep(0.5)
print('Can u guess what number was \33[31mI\33[m thinking?')
time.sleep(1)
lista = random.randint(0, 10)
palpite = 0
acertou = False
while not acertou:
    n1 = int(input('What\'s your guess? '))
    palpite = palpite + 1
    if n1 == lista:
        acertou = True
    else:
        if n1 < lista:
            print('More... Try again')
        elif n1 > lista:
            print('Less... Try again')
print('U got it :)')
print('It took u {} attempts to guess it right :)'.format(palpite))

print('\nEx 059')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digit outro valor: '))
re = 0
time.sleep(0.8)
while re != 5:
    print('-=' * 22)
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] para saber qual o maior')
    print('[4] para digitar novos numeros')
    print('[5] para sair do programa')
    print('-=' * 22)
    re = int(input('Ql sua opcao? '))
    if re == 1:
        sm = n1 + n2
        print('{} + {} = {}'.format(n1, n2, sm))
    elif re == 2:
        mt = n1 * n2
        print('{} x {} = {}'.format(n1, n2, mt))
    elif re == 3:
        if n1 > n2:
            print('{} eh maior que {}'.format(n1, n2))
        elif n2 > n1:
           print('{} eh maior que {}'.format(n2, n1))
    elif re == 4:
        print('Informe os numeros novamente:')
        n3 = int(input('Primeiro valor: '))
        n4 = int(input('Segundo valor: '))
        while re != 5:
            print('-=' * 22)
            print('[1] para somar')
            print('[2] para multiplicar')
            print('[3] para saber qual o maior')
            print('[4] para digitar novos numeros')
            print('[5] para sair do programa')
            print('-=' * 22)
            re = int(input('Ql sua opcao? '))
            if re == 1:
                sm1 = n3 + n4
                print('{} + {} = {}'.format(n3, n4, sm1))
            elif re == 2:
                mt1 = n3 * n4
                print('{} x {} = {}'.format(n3, n4, mt1))
            elif re == 3:
                if n1 > n2:
                    print('{} eh maior que {}'.format(n3, n4))
                elif n2 > n1:
                    print('{} eh maior que {}'.format(n3, n4))
            elif re == 5:
                print('Finalizando...')
                time.sleep(0.8)
                print('-=' * 22)
                print('Volte Sempre! :)')
            else:
                print('Essa n eh uma opcao valida. Tente novamente')
    elif re == 5:
        print('Finalizando...')
        time.sleep(0.8)
        print('-='*22)
        print('Volte Sempre! :)')
    else:
        print('Essa n eh uma opcao valida. Tente novamente')

print('\nEx 060')
n1 = int(input('Digite um numero para calcular seu Fatorial [!]: '))
re = n1
f = math.factorial(n1)
print('Calculando {}! = '.format(n1), end='')
time.sleep(0.8)
while re > 0:
    print('{} '.format(re), end='')
    print(' x ' if re > 1 else '= ', end='')
    re = re - 1
print('{}'.format(f))

print('\nEx 061')
print('Gerador de PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
rz = int(input('Razao da PA: '))
cont = 1
tm = n1
while cont <= 10:
    print('{} - '.format(tm), end='')
    tm = tm + rz
    cont = cont + 1
print('Fim')

print('\nEx 062')
print('Gerador de PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
rz = int(input('Razao da PA: '))
cont = 1
tm = n1
tl = 0
ms = 10
while ms != 0:
    tl = tl + ms
    while cont <= tl:
        print('{} - '.format(tm), end='')
        tm = tm + rz
        cont = cont + 1
    print('Pausa')
    ms = int(input('Qntos termos vc qr mostrar mais? '))
print('Fim')


print('\nEx 063')
print('-'*26)
print('Seqncia de Fibonacci')
print('-'*26)
n1 = int(input('Qntos termos vc qr mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('→ Fim')

print('\nEx 064')
n1 = 0
cont = 0
soma = 0
n1 = int(input('Digite um nmro [999 pr parar]: '))
while n1 != 999:
    cont = cont + 1
    soma = soma + n1
    n1 = int(input('Digite um nmro [999 pr parar]: '))
print('Vc digitou {} nmros e a soma entre eles foi {}'.format(cont, soma))

print('\nEx 065')
resp = 'S'
soma = 0
quant = 0
mdia = 0
mr = 0
mn = 0
while resp in 'Ss':
    n1 = int(input('Digite um nmro: '))
    soma = soma + n1
    quant = quant + 1
    if quant == 1:
        mr = mn = n1
    else:
        if n1 > mr:
            mr = n1
        if n1 < mn:
            mn = n1
    resp = str(input('Qr continuar [S/N]? ')).upper().strip()[0]
mdia = soma / quant
print('Vc digiotu {} nmros e a mdia foi de {}'.format(quant, mdia))
print('O maior valor foi {} e o menor foi {}'.format(mr, mn))
