'''num = '2', '5', '9', '1'   #tupla imutavel
print(num)
#
num = [2, 5, 9, 1]        #lista mutavel
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 2)
num.remove(2)
num.pop(0)
print(num)
print(f'Essa lista tem {len(num)} elementos')
#
valores = list()
for cont in range(0, 10):
    valores.append(int(input('Digite: ')))
for c, v in enumerate(valores):
    print(f'Na psicao {c+1} encontrei o valor {v}!')
print('Acabou')
#
a = [2, 3, 4, 7]
b = a
b[2] = 8              #qndo iguala 2 listas python cria uma ligacao entre elas
b = a[:]              #esse eh uma copia de A dentro de B
print(f'Lista: {a}')
print(f'Lista: {b}')'''


print('\nEx 078')
valores = list()
mr = 0
mn = 0
print('-='*18)
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {cont}: ')))
    if cont == 0:
        mr = mn = valores[cont]
    else:
        if valores[cont] > mr:
            mr = valores[cont]
        if valores[cont] < mn:
            mn = valores[cont]
print('-='*18)
print(f'Vc digitou os valores:{valores}')
print(f'Onde o maior valor foi {mr} nas posicoes', end=' ')
for i, v in enumerate(valores):
    if v == mr:
        print(f'{i}, ', end='')
print(f'\nE o menor velor foi {mn} nas posicoes', end=' ')
for i, v in enumerate(valores):
    if v == mn:
        print(f'{i}, ', end='')

print('\nEx 079')
import time
lista = list()
print('\33[34m-\33[35m=\33[m'*20)
while True:
    n2 = int(input('\33[33m*\33[m Digite um valor: '))
    if n2 not in lista:
        lista.append(n2)
        print('\33[32mValor adicionado com sucesso...\33[m')
    else:
        print('\33[35mValor duplicado! N posso adiciona-lo...\33[m')
    n1 = str(input('Qr continuar [\33[36mS\33[m/\33[31mN\33[m]? ')).upper().strip()
    if n1 in 'N':
        print('\33[33mEstou carregando seus rsltdos...\33[m')
        time.sleep(1.5)
        break
    if n1 not in 'SN':
        print('\33[31mEsta n eh uma opcao valida! Tente novamente.\33[m')
print('\33[34m-\33[35m=\33[m'*20)
print(f'Vc digitou os valores {lista}')

print('\nEx 080')
lista = list()
for c in range(0, 5):
    n1 = int(input('Número: '))
    if c == 0 or n1 > lista[-1]:
        lista.append(n1)
        print('O número foi adicionado no final da lista.')
    else:
        for i in range(0, 5):
            if n1 <= lista[i]:
                lista.insert(i, n1)
                print(f'O número foi adicionado na posição {i}.')
                break
print(lista)

print('\nEx 081')
import time
lista = list()
print('\33[34m-\33[35m=\33[m' * 20)
while True:
    n2 = lista.append(input('\33[33m*\33[m Digite um valor: '))
    print('\33[32mValor adicionado com sucesso...\33[m')
    n1 = str(input('Qr continuar [\33[36mS\33[m/\33[31mN\33[m]? ')).upper().strip()
    if n1 in 'N':
        print('\33[33mEstou carregando seus rsltdos...\33[m')
        time.sleep(1.5)
        break
    if n1 not in 'SN':
        print('\33[31mEsta n eh uma opcao valida! Tente novamente.\33[m')
print('\33[34m-\33[35m=\33[m' * 20)
print(f'Vc digitou {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Essa eh a lista de forma decrescente: {lista}')
if '5' in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 n foi digitado, consequentemente n esta na lista')

print('\nEx 082')
lista = list()
pairs = list()
odds = list()
print('\33[31m-\33[33m=\33[m' * 20)
while True:
    lista.append(int(input('\33[35m*\33[m Digite um valor: ')))
    print('\33[32mValor adicionado com sucesso...\33[m')
    n1 = str(input('Qr continuar [\33[36mS\33[m/\33[31mN\33[m]? ')).upper().strip()
    if n1 in 'N':
        print('\33[34mEstou carregando seus rsltdos...\33[m')
        time.sleep(1.5)
        break
    if n1 not in 'SN':
        print('\33[36mEsta n eh uma opcao valida! Tente novamente.\33[m')
print('\33[31m-\33[33m=\33[m' * 20)
lista.sort()
print(f'Essa foi a lista original: {lista}')
for x in lista:
    if x % 2 == 0:
        pairs.append(x)
    else:
        odds.append(x)
print(f'Essa eh uma lista apenas dos numeros pares: {pairs}')
print(f'Essa eh uma lista apenas dos numeros impares: {odds}')

print('\nEx 083')
expr = str(input('Digite a expressão: '))
pi = expr.count('(')
pf = expr.count(')')
if expr.index(')') > expr.index('('):
    if pi == pf:
        print('Expressão válida')
    else:
        print('Expressão é inválida')
else:
    print('Expressão inválida')
