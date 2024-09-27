frase = str('Curso em video Python')
#print(frase[9])                    #para pegar caracter unico
#print(frase[9:14])                 #separacao palavra (range)
#print(frase[9:21:2])               #comeca no 9, para no 21 e pula de 2 em 2
#print(frase[:5])                   #qndo omiti onde cmc, ele apns trmnara no 4 (ja q omiti o ultimo), cmcnd do 0
#print(frase[15:])                  #oposto do de cima |
#print(frase[9::3])                 #comeca no 9, vai ate o final pois n tem nd no meio, e pula de 3 em 3
#len(frase)                         #mostrar comprimento
#frase.count('o')                   #contar qntas vezes aparece letra
#frase.count('o', 0, 13)            #contara qntas letras e do 0 ate o 13 so
#frase.find('deo')                  #se encontra oq vc quer
#'Curso'in frase                    #dira se tem ou nn
#print(frase.replace('Python','Android'))  #trocar palavras
#frase.upper()                            #maisculo
#frase.strip()                            #retirar espacos
#print(frase.strip())
#print(len(frase.strip()))
#frase.split
#print(frase.split())                #divisao de palavras por seus espacos
#print(frase.upper().count('O'))
#print(len(frase))

print('\nEx 022')
n1 = str(input('Type your name: ')).strip()
print('Analyzing your name...')
print('Your name in uppercase is {}'.format(n1.upper()))
print('Your name in lowercase is {}'.format(n1.lower()))
print('Your name has {} letters'.format(len(n1)-n1.count(' ')))
print('Your first name has {} letters'.format(n1.find(' ')))

print('\nEx 023')
n1 = int(input('Type a number between 0 and 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

print('\nEx 024')
cid = str(input('Digite o nome da sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')

print('\nEx 025')
nome = str(input('Digite seu nome inteiro: ')).strip()
divisao = nome.upper().split()
print('SILVA' in divisao)

print('\nEx 026')
n = str(input('Digite uma frase: ')).strip()
print('A letra A apareceu {} vezes na frase'.format(n.upper().count('A')))
print('A primeira letra A apareceu na posicao {}'.format(n.upper().find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(n.upper().rfind('A')+1))

print('\nEx 027')
n = str(input('Type your full name: ')).strip()
print('first name: {}'.format(n.split(' ')[0]))
print('last name: {}'.format(n.split(' ')[len(n.split())-1]))
print('Muito prazer em te conhecer {}, e obrigado por testar meu programa :)'.format(n.split(' ')[0]))
