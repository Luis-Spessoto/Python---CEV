import math
#n1 = int(input('Type a number: '))
#rq = math.sqrt(n1)
#print('The square root of {} is {}'.format(n1, rq))

#n1 = random.randint(1, 9)
#print(n1)

print('\nEx 014')
n1 = float(input('Digite a temperatura em Celsius: '))
tf = ((9*n1)/5)+32
print('{} graus Celsius é igual a {} graus Farenheit'.format(n1, tf))

print('\nEx 015')
km = float(input('Quantos Km vc andou? '))
dias = int(input('Ha quantos dias vc esta com o carro? '))
valor = (dias*60)+(km*0.15)
print('Vc devera pagar {} reais pelo carro.'.format(valor))

print('\nEx 016')
real = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua aprte inteira é {}'.format(real, math.trunc(real)))

print('\nEx 017')
oposto = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
h = math.sqrt(oposto**2 + adj**2)
print('Sua hipotenusa mede {:.3f}'.format(h))

print('\nEx 018')
ang = float(input('Digite o valor de tal angulo: '))
sen = math.sin(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
tang = math.tan(math.radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))

import random
print('\nEx 019')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

print('\nEx 020')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentacao dos trabalhos sera')
print(lista)

print('\nEx 021')

