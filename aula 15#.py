'''cont = 1
while True:
    print(cont, '- ', end='')
    cont = cont + 1
print('Fim') #infinito
n1 = 0
s = 0
while n1 != 999:
    n1 = int(input('nmro: '))
    s += n1
print('A sm eh {}'.format(s))
n = s = 0
while True:
    n = int(input(': '))
    if n == 999:
        break
    s += n
print('= {}'.format(s))
#or f.str now
n = s = 0
while True:
    n = int(input(': '))
    if n == 999:
        break
    s += n
print(f'= {s}'.)'''

print('\nEx 066')
n1 = 0
cont = 0
soma = 0
while True:
    n1 = int(input('Digite um nmro [999 pr parar]: '))
    if n1 == 999:
        break
    cont = cont + 1
    soma = soma + n1
print(f'A soma dos {cont} valores foi {soma}!')

print('\nEx 067')
while True:
    n1 = int(input('Qr ver a tabuada de ql vlr? '))
    if n1 < 0:
        print('\33[31mI can\'t do the multiplication table of negative numbers\33[m')
        break
    print('-'*15)
    for c in range(0, 11):
        print(f'{n1} x {c:2} = {n1 * c}')
    print('-'*15)
    break
print('Tabuada encerrada!')

print('\nEx 068')
import random
v = 0
print('=-'*12)
print('\33[35mVamos jgr par ou impar\33[m')
print('=-'*12)
while True:
    n1 = int(input('Diga um valor [0-10]: '))
    pc = random.randint(0, 10)
    tt = pc + n1
    pi = ' '
    while pi not in 'PI':
        pi = str(input('\33[33mPAR\33[m ou \33[36mIMPAR\33[m [P/I]? ')).strip().upper()[0]
    print(f'Vc jgou {n1} e o computador jgou {pc}. Total de {tt}.')
    if pi == 'P':
        if tt % 2 == 0:
            print('\33[33mVc venceu!\33[m')
            v = v + 1
        else:
            print('\33[31mVc perdeu!\33[m')
            break
    elif pi == 'I':
        if tt % 2 == 1:
            print('\33[33mVc venceu!\33[m')
            v = v + 1
        else:
            print('\33[31mVc perdeu!\33[m')
            break
    print('Vmos mais uma...')
print(f'All done. Vc venceu {v} vezes seguidas')

print('\nEx 069')
tothomem = 0
totm = 0
tot18 = 0
n1 = 0
while True:
    print('----- Cadastre uma pessoa -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-'*31)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomem += 1
    if sexo == 'F':
        totm += 1
    n1 = ' '
    while n1 not in 'SN':
        n1 = str(input('Qr continuar [S/N]: ')).strip().upper()[0]
    if n1 == 'N':
        print('\n--------Fim do Programa--------')
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao td temos {tothomem} homens cadastrados')
print(f'E temos {totm} mulheres com menos de 20 anos')

print('\nEx 070')
cont = 0
total = 0
totalmil = 0
menor = 0
n2 = ''
barato = n2
print('\33[35m-=\33[m' * 10)
print('   \33[36mPoseidon Store\33[m')
while True:
    print('\33[35m-=\33[m' * 10)
    n2 = str(input('Nome do produto: '))
    v2 = float(input('Valor: R$ '))
    barato = n2
    cont += 1
    total = total + v2
    if v2 > 1000:
        totalmil = totalmil + 1
    if cont == 1:
        menor = v2
    else:
        if v2 < menor:
            menor = v2
            barato = n2
    n1 = ' '
    while n1 not in 'SN':
        n1 = str(input('Qr continuar [S/N]? ')).upper()[0]
    if n1 == 'N':
        print('\33[35m-=-\33[31mFim do Programa\33[35m-=-\33[m')
        break
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totalmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato custa R${menor:.2f}, sendo ele a/o {barato}')

print('\nEx 071')
print('='*30)
print('          \33[36mOcean Bank\33[m')
print('='*30)
n1 = int(input('Ql valor vc qr sacar? R$ '))
total = n1
nt = 50
totnt = 0
while True:
    if total >= nt:
        total -= nt
        totnt += 1
    else:
        if totnt > 0:
            print(f'Total de {totnt} cedulas de R${nt}')
        if nt == 50:
            nt = 20
        elif nt == 20:
            nt = 10
        elif nt == 10:
            nt = 1
        totnt = 0
        if total == 0:
            break
print('='*30)
print('Volte Sempre! :)')