import time
import random

#
var = ''


def lin(msg):
    print('\33[36m-\33[35m=\33[m' * 12)
    print(msg)
    print('\33[36m-\33[35m=\33[m' * 12)


# lin()
# print(f'{var:<2}Function System Test')
# lin()

lin(f'{var:<2}Function System Test')
#
while True:
    a = float(input('Number 1: '))
    b = float(input('Number 2: '))


    def soma():
        s = a + b
        print('-='*10)
        print(f'{a:.2f} + {b:.2f} = {s:.2f}')
        print('-='*10)
    soma()

    c = str(input('Do u want to keep going [Y/N]: ')).upper()[0]
    if c not in 'YN':
        print('\33[31mErRo\33[mr\33[35m! \33[36mTR\33[my \33[33mAgA\33[31mI\33[mn:')
    if c == 'N':
        break
#


def cont(*n1):
    for v in n1:
        print(f'{v} ', end='')
    print()


cont(2, 1, 7)
cont(8, 0)
cont(4, 4, 7, 6, 2)
#


def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


values = [6, 3, 9, 1, 0, 2]
double(values)
print(values)

print('\nEx 096')
var = ''


def lin(msg):
    print('\33[36m-\33[35m=\33[m' * 12)
    print(msg)
    print('\33[36m-\33[35m=\33[m' * 12)


lin(f'{var:<2}Controle de Terrenos')
length = float(input('Largura [m]: '))
width = float(input('Comprimento [m]: '))


def area():
    a1 = length * width
    print(f'A area de um terreno {length:.2f} x {width:.2f} eh de {a1:.2f}m²')


area()
print('\nEx 097')


def phrase(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)


phrase('Oi')
phrase('Testando o teste do teste testado')
print('\nEx 098')


def l():
    print('\33[35m-\33[36m=\33[m' * 15)


def lin(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    l()
    print(f'Contagem de {i} ate {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            time.sleep(0.5)
            print(f'{cont} ', end='')
            cont += p
        print('!')
    else:
        cont = i
        while cont >= f:
            time.sleep(0.5)
            print(f'{cont} ', end='')
            cont -= p
        print('!')


lin(1, 10, 1)
lin(10, 0, 2)
l()
print('Agr eh sua vez de personalizar a contagem!')
n1 = int(input('Inicio: '))
n2 = int(input('Fim: '))
n3 = int(input('Passo: '))
lin(n1, n2, n3)
print('\nEx 099')


def maior(* num):
    cont = maior = 0
    l()
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ', end='')
        time.sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
print('\nEx 100')


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        time.sleep(0.3)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
