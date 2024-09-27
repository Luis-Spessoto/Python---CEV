# while True:
#     n1 = str(input('I love _ ')).upper().strip()
#     if n1 not in 'Uu':
#         print('No that\'s wrong')
#     else:
#         print('Yeah that\'s true!')
#         break

"""lanche = 'Burguer', 'Suco', 'Pizza', 'Pudim'
for c in lanche:
    print(f'Eu vou comer {c}')

a = 2, 5, 4
b = 5, 8, 1, 2
c = b + a
print(c)           #duas tuplas juntas
print(len(c))      #tamanho
print(c.count(5))  #conta qntas vezes aparece
print(c.index(4))  #posicao do desejado da primeira aparicao"""

print('\nEx 072')
tl = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um valor [0-20]: '))
x = tl[n1]
while n1 > 20 or n1 < 0:
    n1 = int(input('Tente novamente. Digite um valor [0-20]: '))
print(f'Vc digitou o nmro \33[35m{x}\33[m!')

print('\nEx 073')
p20 = ('Sao Paulo', 'Internacional', 'Atletico-MG', 'Flamengo', 'Gremio', 'Palmeiras', 'Fluminense', 'Santos', 'Ceara', 'Corinthians', 'Athletico-PR', 'Atletico-GO', 'Bragantino', 'Sport Recife', 'Vasco da Gama', 'Fortaleza', 'Bahia', 'Goias', 'Botafogo', 'Coritiba')
pr5 = p20[0:5]
ul4 = p20[16:21]
oal = sorted(p20)
cha = p20.index("Flamengo") + 1
print('-='*22)
print(f'Lista de times do Brasileirao: {p20}')
print('-='*22)
print(f'Os 5 primeiros sao {pr5}')
print('-='*22)
print(f'Os 4 ultimos sao {ul4}')
print('-='*22)
print(f'Times em ordem alfabetica: {oal}')
print('-='*22)
print(f'O Flamengo esta na posicao de numero {cha}')

print('\nEx 074')
from random import randint

a = tuple(randint(1, 10) for i in range(5))
print(f'Os valores sorteados foram: {a}')
print(f'O maior valor sorteado foi {max(a)}')
print(f'O menor valor sorteado foi {min(a)}')

print('\nEx 075')
resul = par = ()
n1 = int(input('Digite um nmro: '))
n2 = int(input('Digite outro nmro: '))
n3 = int(input('Digite mais um: '))
n4 = int(input('Digite o ultimo nmro: '))
a = n1, n2, n3, n4
v9 = a.count(9)
print(f'Vc digitou os valores {a}')
print(f'O valor 9 apareceu {v9} vezes')
if 3 in a:
    v3 = a.index(3) + 1
    print(f'O valor 3 apareceu na posicao de numero {v3}')
else:
    print('O valor 3 n foi digitado')
print(f'Os valores pares digitados foram', end=' ')
for n in a:
    if n % 2 == 0:
        print(n, end=', ')

print('\nEx 076')
lista = ('Burguer', 19.90, 'Coca Cola', 5.00, 'Batata Frita', 7.50, 'Chocolate', 6.50, 'Pizza Grande', 49.90)
print('\33[31m-\33[33m=\33[m'*17)
print('\33[36m        Tabela de Valores')
print('\33[31m-\33[33m=\33[m'*17)
print(f'\33[35m{lista[0]}', end='')
print('\33[m.'*17, end='')
print(f'R$ {lista[1]}', end='')
print(f'\33[34m\n{lista[2]}', end='')
print('\33[m.'*15, end='')
print(f'R$  {lista[3]}', end='')
print(f'\33[35m\n{lista[4]}', end='')
print('\33[m.'*12, end='')
print(f'R$  {lista[5]}', end='')
print(f'\33[34m\n{lista[6]}', end='')
print('\33[m.'*15, end='')
print(f'R$  {lista[7]}', end='')
print(f'\33[35m\n{lista[8]}', end='')
print('\33[m.'*12, end='')
print(f'R$ {lista[9]}', end='\n')
print('\33[31m-\33[33m=\33[m'*17)
# or a maneira correta e mais facil
listagem = ('Burguer', 19.90, 'Coca Cola', 5.00, 'Batata Frita', 7.50, 'Chocolate', 6.50, 'Pizza Grande', 49.90)
for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)

print('\nEx 077')
palavras = ('aprender', 'curso', 'falar', 'linguagem', 'python', 'programar', 'futuro', 'programador')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'Vogais da palavra \33[35m{p.upper()}\33[m: ', end='')
    for l in p:
        if l in vogais:
            print(f'\033[31m{l.upper()}\033[m', end=', ')
    print()



