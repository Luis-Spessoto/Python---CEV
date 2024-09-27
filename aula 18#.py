import time
import random
"""teste = list()
teste.append('Luis')
teste.append(15)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
#
pessoas = [['Pedro', 25], ['Maria', 19], ['Jao', 32]]
print(pessoas[0][0])
print(pessoas[1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')
#
galera = list()
dado = list()
totmai = 0
totmen = 0
for x in range(0, 3):
    dado.append(str(input('Seu nome: ')))
    dado.append(int(input('Sua idade: ')))
    print('-'*24)
    galera.append(dado[:])
    dado.clear()
for s in galera:
    if s[1] >= 21:
        print(f'{s[0]} eh maior de idade')
        totmai += 1
    else:
        print(f'{s[0]} eh menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores de idade \nE {totmen} menores de idade')
print('-='*12)
print(f'{galera[0][0]} tem {galera[0][1]} anos de idade')
print(f'{galera[1][0]} tem {galera[1][1]} anos de idade')
print(f'{galera[2][0]} tem {galera[2][1]} anos de idade')"""

print('\nEx 084')
print('\33[35m-\33[36m==\33[35m-\33[m'*7)
print('          Weighing')
print('\33[35m-\33[36m==\33[35m-\33[m'*7)
lista = list()
cont = list()
maior = 0
menor = 0
while True:
    cont.append(str(input('Tell me your name: ')))
    cont.append(float(input('Your weight: ')))
    print('\33[31m-\33[34m==\33[31m-\33[m'*7)
    n1 = str(input('Do u wanna keep going [\33[32mY\33[m/\33[31mN\33[m]?')).upper()
    print('\33[31m-\33[34m==\33[31m-\33[m'*7)
    if not lista:
        maior = menor = cont[1]
    for valor in lista:
        if valor[1] > maior:
            maior = valor[1]
        elif valor[1] < menor:
            menor = valor[1]
    lista.append(cont[:])
    cont.clear()
    if n1 not in 'YN':
        print('Try again...')
        n1 = str(input('Do u wanna keep going [\33[32mY\33[m/\33[31mN\33[m]?')).upper()
        print('\33[31m-\33[34m==\33[31m-\33[m' * 7)
    elif n1 in 'N':
        print('Ok..Loading your info...')
        print('\33[37m*\33[m')
        break
print(f'{len(lista)} people were registred!')
print(f'O maior peso foi de {maior}Kg, pertencente a ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' - ')
print(f'\nE o menor peso foi de {menor}Kg, pertencente a ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=' - ')

print('\nEx 085')
lista = [[], []]
for s in range(0, 7):
    n1 = int(input(f'Digite o {s+1}º valor: '))
    if n1 % 2 == 0:
        lista[0].append(n1)
    else:
        lista[1].append(n1)
lista[0].sort()
lista[1].sort()
print(f'Essa eh uma lista apenas dos numeros pares: {lista[1]}')
print(f'Essa eh uma lista apenas dos numeros impares: {lista[0]}')

print('\nEx 086') #matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('\33[35m-=\33[m'*15)
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = int(input(f'Digite um valor para [{x}, {c}]: '))
print('\33[35m-=\33[m'*15)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^5}]', end='')
    print()
print('\33[36m-=\33[m'*15)

print('\nEx 087')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
print('\33[31m-=\33[m' * 15)
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = int(input(f'\33[32m*\33[mDigite um valor para [{x}, {c}]: '))
print('\33[35m-=\33[m' * 15)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'\33[35m[\33[m{matriz[x][c]:^5}\33[36m]\33[m', end='')
        if matriz[x][c] % 2 == 0:
            spar += matriz[x][c]
    print()
print('\33[36m-=\33[m' * 15)
print(f'A soma dos valores pares eh {spar}')
for x in range(0, 3):
    scol += matriz[x][2]
print(f'A soma dos valores da terceira coluna eh {scol}')
print(f'O maior valor da segunda linha eh {max(matriz[1])}')

print('\nEx 088')
num = list()
jgs = list()
print('\33[32m-\33[m\33[33m=\33[m' * 15)
print('          MEGA SENA')
print('\33[32m-\33[m\33[33m=\33[m' * 15)
n1 = int(input('Qntos jogos qr q eu sorteie? '))
print('\33[34m-\33[33m=\33[m' * 3, end='')
print(f' Sorteando {n1} jogos', end='')
print('\33[34m-\33[32m=\33[m' * 3)
tot = 1
time.sleep(1)
while tot <= n1:
    con = 0
    while True:
        n2 = random.randint(1, 60)
        if n2 not in num:
            num.append(n2)
            con += 1
        if con >= 6:
            break
    num.sort()
    jgs.append(num[:])
    num.clear()
    tot += 1
for x in range(0, n1):
    print(f'Jogo \33[35m[\33[m{x+1}\33[36m]\33[m: {jgs[x]}')
    time.sleep(1.1)
print('\nBoa Sorte! \33[33m👍\33[m :)')

print('\nEx 089')
ficha = list()
print('\33[35m-\33[36m=\33[m'*12)
print('        Boletim')
print('\33[35m-\33[36m=\33[m'*12)
while True:
    nome = str(input('Nome: '))
    not1 = float(input('Nota 1: '))
    not2 = float(input('Nota 2: '))
    print('\33[33m-\33[32m=\33[m' * 12)
    mdia = (not1 + not2) / 2
    ficha.append([nome, [not1, not2], mdia])
    resp = str(input('Qr continuar [S/N]? ')).upper()
    if resp not in 'SN':
        print('\33[31mEsta n eh uma opcao valida! Tente novamente.\33[m')
    print('\33[33m-\33[32m=\33[m' * 12)
    if resp in 'N':
        print('Carregando suas informacoes...')
        time.sleep(1.5)
        break
print('-='*12)
print(f'{"No.":<4}{"Nome":<10}{"Mdia":>8}')
print('-='*12)
for x, a in enumerate(ficha):
    print(f'{x:<4}{a[0]:<10}{a[2]:>8}')