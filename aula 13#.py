import time
import math
import datetime
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Oi')
#print('Fim')
#o de cima eh igual o de baixo  ps: ele n considera o ultimo numero, ent se qr 0,6 = 0,7
#for c in range(1, 7):
#    print('Oi')
#print('Fim')
#for c in range(6, 0, -1):
#    print(c)
#print('Fim')

#s = 0
#for c in range(0, 4):
#    n = int(input('Digite um valor: '))
#    s += n
#print('A soma foi {}'.format(s))

print('\nEx 046')
print('-='*16)
print('\33[31mB\33[32me\33[33mm\33[34m \33[35mv\33[36mi\33[37mn\33[31md\33[32mo\33[33m \33[34ma \33[35mc\33[36mo\33[37mn\33[31mt\33[32ma\33[33mg\33[34me\33[35mm \33[36mr\33[37me\33[31mg\33[32mr\33[33me\33[34ms\33[35ms\33[36mi\33[37mv\33[31m\33[32ma\33[33m!\33[m')
print('-='*16)
n1 = int(input('Digite \33[31m[1]\33[m quando quiser comecar a contagem: '))
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
time.sleep(0.5)
print('BUM! BUM! POOOW!')

print('\nEx 047')
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou')

print('\nEx 048')
soma = 0
cont = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        print(c, end=' ')
        soma = soma + c
        cont = cont + 1
print('\nA soma entre todos os {} valores eh {}'.format(cont, soma))

print('\nEx 049')
n1 = int(input('Digite o valor que deseja saber a tabuada [0- ∞]: '))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n1, c, n1*c))

print('\nEx 050')
soma = 0
cont = 0
for x in range(0, 6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        cont = cont + 1
        soma = soma + n1
print('A soma entre todos os numeros pares eh {}'.format(soma))

print('\nEx 051')
print('-='*15)
print('     10 TERMOS DE UMA PA     ')
print('-='*15)
n1 = int(input('Primeiro Termo: '))
n2 = int(input('Razao: '))
n3 = n1 + (10 - 1) * n2
for x in range(n1, n3 + n2, n2):
    print('{} '.format(x), end='\33[31m➡ \33[m')
print('Acabou')

print('\nEx 052')
n1 = int(input('Digite um numero: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\33[36m', end=' ')
        tot = tot + 1
    else:
        print('\33[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\33[mO numero {} foi dividido {} vezes'.format(n1, tot))
if tot == 2:
    print('E por isso ele eh primo')
else:
    print('E por isso ele n eh primo')

print('\nEx 053')
n1 = str(input('Digite uma frase: ')).strip().upper()
f1 = n1.split()
f2 = ''.join(f1)
vs = ''
for letra in range(len(f2) - 1, -1, -1):
    vs += f2[letra]
if vs == f2:
    print('Temos um palindromo')
else:
    print('A frase n eh um palindromo')
print('O inverso de {} eh {}'.format(f2, vs))

print('\nEx 054')
totmaior = 0
totmenor = 0
atual = datetime.date.today().year
for x in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da pessoa {}: '.format(x)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tbm tivemos {} pessoas menores de idade'.format(totmenor))

print('\nEx 055')
maior = 0
menor = 99999
for p in range(1, 6):
    peso = float(input('Peso da pessoa de numero {}: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} kg'.format(maior))
print('O menor peso foi {} kg'.format(menor))
#or
a = float(input('Peso 1: '))
b = float(input('Peso 2: '))
c = float(input('Peso 3: '))
d = float(input('Peso 4: '))
e = float(input('Peso 5: '))
if a > b and a > c and a > d and a > e:
    print('O maior peso foi {} kg'.format(a))
elif b > a and b > c and b > d and b > e:
    print('O maior peso foi {} kg'.format(b))
elif c > a and c > b and c > d and c > e:
    print('O maior peso foi {} kg'.format(c))
elif d > a and d > b and d > c and d > e:
    print('O maior peso foi {} kg'.format(d))
else:
    print('O maior peso foi {} kg'.format(e))
if a < b and a < c and a < d and a < e:
    print('O menor peso foi {} kg'.format(a))
elif b < a and b < c and b < d and b < e:
    print('O menor peso foi {} kg'.format(b))
elif c < a and c < b and c < d and c < e:
    print('O menor peso foi {} kg'.format(c))
elif d < a and d < b and d < c and d < e:
    print('O menor peso foi {} kg'.format(d))
else:
    print('O menor peso foi {} kg'.format(e))
#or
lista= []
for c in range (1,6):
    lista.append(int(input ('Qual o peso da {}ª pessoa? ' .format (c))))
print ('O maior peso é', max(lista))
print ('O menor peso é', min(lista))

print('\nEx 056')
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- Pessoa de numero {} -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade entre o grupo eh de {} anos'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(totmulher20))