import random
#time = int(input('How old is your car?'))
#if time <= 3:
#    print('New car')
#else:
#    print('Old car')
#print('--End--')
# ou
#time = int(input('How old are u?'))
#print('You are young' if time <= 18 else 'You are old')
#print('-' * 10)
#print('End')

#n1 = float(input('\nDigite sua primeira nota: '))
#n2 = float(input('Digite sua segunda nota: '))
#m = (n1 + n2) / 2
#print('Sua média é {}, parabéns!'.format(m) if m >= 8 else 'Sua média é {}, estude mais um pouco!'.format(m))
#print('-'*31)
#print('Tenha um bom final de bimestre!')

import random
import time
print('\nEx 028')
print('\33[30m-=-\33[m'*20)
print('   Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('\33[30m-=-\33[m'*20)
n1 = int(input('Em que numero pensei? '))
lista = random.randint(0, 5)
print('Processando...')
time.sleep(1)
print('\033[0;36mParabéns! Vc conseguiu me vencer!\33[m' if n1 == lista else
      '\33[31mGanhei! Eu pensei no {} e n no {}!\33[m'.format(lista, n1))

print('\nEx 029')
n1 = int(input('Qual é a velocidade atual do veiculo? '))
m = (n1-80)*7
if n1 <= 80:
    print('\33[36mTenha um bom dia! Drive safely!\33[m')
else:
    print('\33[31mMultado! Vc excedeu o limite permitido que é de 80Km/h\33[m')
    print('Vc deve pagar uma multa de R${}!'.format(m))

print('\nEx 030')
n1 = int(input('Diigte um nmro qlqr: '))
r = n1 % 2
if r == 0:
    print('O nmro {} é PAR'.format(n1))
else:
    print('O nmro {} é IMPAR'.format(n1))
print('-=-'*9)
print('That is IT')
print('-=-'*9)

print('\nEx 031')
n1 = float(input('Qual a distancia da sua viagem? '))
menos2 = 0.5*n1
mais2 = 0.45*n1
if n1 >= 200:
    print('Vc esta prestes a cmcr sua viagem de {} km. O valor de sua passagem sera de {}'.format(n1, mais2))
else:
    print('Vc esta prestes a cmcr sua viagem de {} km. O valor de sua passagem sera de {}'.format(n1, menos2))

print('\nEx 032')
print('Bissexto ou nn?')
n1 = int(input('Digite o ano que vc qr saber: '))
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('O ano {} é bissexto'.format(n1))
else:
    print('O ano {} n é bissexto'.format(n1))

print('\nEx 033')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))

print('\nEx 034')
n1 = float(input('Qual o valor do salario do funcionario? R$ '))
ss = (n1 * 0.1) + n1
si = (n1 * 0.15) + n1
if n1 >= 1250:
    print('Quem ganahava R${} passa a ganhar R${} agora.'.format(n1, ss))
else:
    print('Quem ganhava R${} passa a ganhar R${} agora.'.format(n1, si))

print('\nEx 035')
print('-=-='*10)
print('Analisador de Triangulos')
print('-=-='*10)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima nao podem formar um triangulo.')



