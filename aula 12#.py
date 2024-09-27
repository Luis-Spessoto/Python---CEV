import math
import random
import datetime
import time

"""print('\nEx 036')
n1 = float(input('House value: R$ '))
n2 = float(input('Your monthly income: R$ '))
n3 = int(input('How many years of financing? '))
iv = (n1 / n3) / 12
ip = (0.3 * n2)
print('To buy a R$ {:.2f} house in {} years, the instalment will be R$ {:.2f}'.format(n1, n3, iv))
if iv <= ip:
    print('\33[36mThe loan can be approved!\33[m')
else:
    print('\33[31mThe loan can not be approved!\33[m')

print('\nEx 037')
n1 = int(input('Type a number: '))
print('Escolha uma das bases para converter: [1] para Binario, [2] para Octal [3] para Hexadecimal')
op = int(input('Sua escolha: '))
if op == 1:
    print('{} convertido para Binario equivale a {}'.format(n1, bin(n1)))
elif op == 2:
    print('{} converitdo para Octal equivale a {}'.format(n1, oct(n1)))
elif op == 3:
    print('{} convertido para Hexadecimal equivale a {}'.format(n1, hex(n1)))
else:
    print('\33[31mEssa n eh uma opcao valida\33[m')

print('\nEx 038')
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('O primeiro valor eh maior')
elif n1 < n2:
    print('O segundo valor eh maior')
elif n1 == n2:
    print('N existe valor maior, os dois sao iguais')

print('\nEx 039')
print('-='*20)
print('\33[32mBem vindo ao calculo para o alistamento\33[m')
print('-='*20)
sx = str(input('Digite seu sexo [a primeira letra deve ser maiuscula]: '))
if sx == 'Feminino':
    print('Seu alistamento no exercito eh facultativo!')
elif sx == 'Masculino':
    n1 = int(input('Digite seu ano de nascimento: '))
    atual = datetime.date.today().year
    idade = atual - n1
    s1 = 18 - idade
    s2 = idade - 19
    if idade == 18:
        print('\33[32mEsta na hora de vc se alistar!\33[m')
    elif idade < 18:
        print('\33[34mVc ainda n tem idade para o alistamento. Faltam {} anos para que vc possa se alistar!'.format(s1))
    elif idade > 18:
        print('\33[31mJa se passaram {} anos desde que vc deveria ter se alistado!\33[m'.format(s2))\

else:
    print('\33[31mEssa n eh uma opcao valida!\33[m')

print('\33[m\nEx 040')
print('\33[35mBem vindo a calculadora de medias!\33[m')
pn = float(input('Digite sua primeira nota: '))
sn = float(input('Digite sua segunda nota: '))
m = (pn + sn) / 2
print('A media entre {} e {} eh {:.1f}'.format(pn, sn, m))
if m < 5:
    print('\33[31mReprovado!\33[m')
elif 5 <= m < 7:
    print('\33[33mRecuperacao!\33[m')
elif m > 7:
    print('\33[32mAprovado!\33[m')


print('\nEx 041')
print('-='*22)
print('\33[34mBem vindo a Confederacao Nacional de Natacao\33[m')
print('-='*22)
ano = int(input('Digite seu ano de nascimento: '))
n1 = datetime.date.today().year
ida = n1 - ano
if ida <= 9:
    print('Vc tem {} anos, classificando vc na categoria \33[32mMirim\33[m'.format(ida))
elif ida <= 14:
    print('Vc tem {} anos, classificando vc na categoria \33[34mInfantil\33[m'.format(ida))
elif ida <= 19:
    print('Vc tem {} anos, classificando vc na categoria \33[36mJunior\33[m'.format(ida))
elif ida <= 25:
    print('Vc tem {} anos, classificando vc na categoria \33[35mSenior\33[m'.format(ida))
else:
    print('Vc tem {} anos, classificando vc na categoria \33[31mMaster\33[m'.format(ida))

print('\nEx 042')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo', end='')
    if r1 == r2 and r2 == r3:
        print(' Equilatero!')
    elif r1 != r2 != r3 != r1:
        print(' Escaleno!')
    else:
        print(' Isosceles!')
else:
    print('Os segmentos acima n podem formar um triangulo!')

print('\nEx 043')
p = float(input('Digite seu peso em kg: '))
h = float(input('Digite sua altura em m: '))
imc = p / (h ** 2)
print('O IMC dessa pessoa eh de {:.1f}'.format(imc))
if imc < 18.5:
    print('Este eh um peso classificado como magreza')
elif 18.5 < imc < 24.9:
    print('Este eh um peso classificado como normal')
elif 25.0 < imc < 29.9:
    print('Este eh um peso classificado como sobrepeso')
elif 30.0 < imc < 39.9:
    print('Este eh um peso classificado como obesidade')
elif imc > 40.0:
    print('Este eh um peso classificado como obesidade grave')

print('\nEx 044')
print('========== \33[36mLojas Poseidon\33[m ==========')
pp = float(input('Digite o valor das compras: R$ '))
print('\33[35mFormas de Pagamento')
print('\33[31m[1]\33[m à vista no dinheiro/cheque')
print('\33[31m[2]\33[m à vista no cartao')
print('\33[31m[3]\33[m 2x no cartao')
print('\33[31m[4]\33[m 3x ou mais no cartao')
oc = int(input('Ql a forma de pagamento desejada? '))
dc = pp - (pp * 0.10)
ac = pp - (pp * 0.05)
c3 = pp + (pp * 0.20)
if oc == 1:
    print('Sua compra de R$ {} vai custar R$ {:.2f} no checkout.'.format(pp, dc))
elif oc == 2:
    print('Sua compra de R$ {} vai custar R$ {:.2f} no checkout.'.format(pp, ac))
elif oc == 3:
    print('Sua compra de R$ {} vai custar R$ {} no checkout.'.format(pp, pp))
elif oc == 4:
    n1 = int(input('Quantas parcelas vc deseja? '))
    vp = c3 / n1
    print('Sua compra sera parcelada em {} vezes de R$ {} Com Juros no checkout.'.format(n1, vp))
    print('Custando assim: R$ {:.2f} no final'.format(c3))
else:
    print('\33[31mEssa n eh uma forma de pagamento valida!\33[m Tente Novamente')"""

print('\nEx 045')
print('-='*15)
print('     \33[35mVamos jogar Jokenpo\33[m')
print('-='*15)
lista = ('Pedra', 'Papel','Tesoura')
choice = random.randint(0, 2)
print('Suas opcoes:')
print('\33[33m[0]\33[m PEDRA')
print('\33[33m[1]\33[m PAPEL')
print('\33[33m[2]\33[m TESOURA')
n1 = int(input('Digite sua escolha: '))
print('\33[36mJO\33[m')
time.sleep(1)
print('\33[36mKEN\33[m')
time.sleep(1)
print('\33[36mPO\33[m')
print('-='*11)
print('Computador jogou {}'.format(lista[choice]))
print('Jogador jogou {}'.format(lista[n1]))
print('-='*11)
if choice == 0:
    if n1 == 0:
        print('\33[33mEmpate!\33[m')
    elif n1 == 1:
        print('\33[32mJogador Venceu!\33[m')
    elif n1 == 2:
        print('\33[31mO computador venceu!\33[m')
    else:
        print('\33[31mJogada Invalida\33[m')
elif choice == 1:
    if n1 == 0:
        print('\33[31mO computador venceu!\33[m')
    elif n1 == 1:
        print('\33[33mEmpate!\33[m')
    elif n1 == 2:
        print('\33[32mJogador Venceu!\33[m')
    else:
        print('\33[31Jogada Invalida\33[m')
elif choice == 2:
    if n1 == 0:
        print('\33[32mJogador Venceu!\33[m')
    elif n1 == 1:
        print('\33[31mO computador venceu!\33[m')
    elif n1 == 2:
        print('\33[33mEmpate!\33[m')
    else:
        print('\33[31mJogada Invalida\33[m')