from random import randint
from time import sleep
import datetime
"""movies = {'title': 'Star Wars',
          'year': 1977,
          'director': 'George Lucas'}
print(movies.values())
print(movies.keys())
print(movies.items())
for k, v in movies.items():
    print(f'The {k} is {v}')
#
locadora = {'title': 'Star Wars', 'year': 1977, 'director': 'George Lucas'}, \
           {'title': 'Avengers', 'year': 2012, 'director': 'Joss Whedon'}, \
           {'title': 'Matrix', 'year': 1999, 'director': 'Wachowski'}
print(locadora[0]['year'])
print(locadora[2]['title'])
print(locadora)
#
Brazil = []
state1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
state2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
Brazil.append(state1)
Brazil.append(state2)
print(Brazil[1]['uf'])
#
state0 = dict()
Brazil = list()
for x in range(0, 3):
    state0['uf'] = str(input('Unidade Federativa: '))
    state0['sigla'] = str(input('Sigla Estadual: '))
    Brazil.append(state0.copy())
for s in Brazil:
    for k, v in s.items():
        print(v, end='- ')
print(Brazil)"""

print('\nEx 090')
pc = dict()
pc['nome'] = str(input('Nome: '))
pc['mdia'] = float(input(f'Mdia de {pc["nome"]}: '))
if pc['mdia'] >= 7:
    situation = 'Aprovado'
    pc['Situacao'] = situation
else:
    situation = 'Reprovado'
    pc['Situacao'] = situation
print(f'Seu nome eh {pc["nome"]} e sua mdia foi de {pc["mdia"]}, consequentemente sua situacao eh de {pc["Situacao"]}')

print('\nEx 091')
print('\33[35m-\33[36m=\33[m' * 12)
print('\33[32m     Dice Simulator\33[m')
print('\33[35m-\33[36m=\33[m' * 12)
total = dict()
list0 = list()
press = int(input('Press \33[35m[\33[m1\33[36m]\33[m to start: '))
print()
if press == 1:
    for x in range(0, 4):
        n = randint(1, 6)
        total['player' + str(x + 1)] = n
        list0.append(n)
        sleep(0.5)
        print(f'\33[32m*\33[mThe player number {x + 1} rolled a \33[31m{n}\33[m.')
        sleep(0.5)
list0.sort(reverse=True)
play = 'p'
print('Ranking:')
for s in range(0, 4):
    print(f'\33[33m{s + 1}º\33[m place: ', end='')
    for k, v in total.items():
        if v == list0[s] and play != k:
            sleep(0.5)
            print(k)
            play = k
            break

print('\nEx 092')
data = dict()
print('\33[34m-\33[m'*20)
print('    Aposentadoria')
print('\33[34m-\33[m'*20)
data['Nome'] = str(input('Nome: '))
data['Year'] = int(input('Ano de Nascimento: '))
data['CTSP'] = int(input('Carteira de Trabalho [(0) caso n tenha]: '))
if data['CTSP'] == 0:
    print('\33[35m-\33[m\33[36m-\33[m' * 10)
    print('Vc ainda n tem uma Carteira de Trabalho!')
    print('\33[35m-\33[m\33[36m-\33[m' * 10)
else:
    data['JobYear'] = int(input('Ano de contratação: '))
    data['Salary'] = float(input('Salary: R$ '))
    year = datetime.date.today().year
    age = year - data['Year']
    retire0 = year - data['JobYear']
    retire1 = 35 - retire0
    retire2 = retire1 + age
    print('\33[35m-\33[m\33[36m-\33[m' * 10)
    sleep(1)
    print(f'Nome: {data["Nome"]}')
    sleep(1)
    print(f'Idade: {age}')
    sleep(1)
    print(f'CTSP: {data["CTSP"]}')
    sleep(1)
    print(f'Salary: R$ {data["Salary"]}')
    sleep(1)
    print(f'Aposentadoria: {retire2} anos')
    print('\33[35m-\33[m\33[36m-\33[m' * 10)
print('...THE END...')
# or
data = dict()
print('\33[34m-\33[m'*20)
print('    Aposentadoria')
print('\33[34m-\33[m'*20)
data['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
data['Age'] = datetime.date.today().year - nasc
data['CTSP'] = int(input('Carteira de Trabalho [(0) caso n tenha]: '))
if data['CTSP'] == 0:
    print('\33[35m-\33[m\33[36m-\33[m' * 10)
    print('Vc ainda n tem uma Carteira de Trabalho!')
    print('\33[35m-\33[m\33[36m-\33[m' * 10)
else:
    data['JobYear'] = int(input('Ano de contratação: '))
    data['Salary'] = float(input('Salary: R$ '))
    data['Aposentadoria'] = data['Age'] + ((data['JobYear'] + 35) - datetime.date.today().year)
print('-=')
for k, v in data.items():
    print(f' - {k} tem o valor {v}')

print('\nEx 093')
data = dict()
goal = list()
data['Nome'] = str(input('Nome jogador: '))
tot = int(input(f'Qntas partidas {data["Nome"]} jogou? '))
for c in range(0, tot):
    goal.append(int(input(f'Qntos gols na partida {c+1}? ')))
data['gols'] = goal[:]
data['total'] = sum(goal)
print('-='*30)
print(data)
print('-='*30)
for k, v in data.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jgdor {data["Nome"]} jogou {len(data["gols"])} partidas')
for i, v in enumerate(data['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f' Foi um total de {data["total"]} gols')

print('\nEx 094')
galera = list()
pessoa = dict()
soma = mdia = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('\33[31mError\33[m!Digite apenas [M/F]')
    pessoa['Age'] = int(input('Idade: '))
    soma += pessoa['Age']
    galera.append(pessoa.copy())
    while True:
        press = str(input('Qr continuar [S/N]? ')).upper()[0]
        if press in 'SN':
            break
        print('Essa n eh uma alternativa valida')
    if press == 'N':
        break
print('-=' * 12)
print(f'Ao td temos {len(galera)} pessoas cadastradas')
mdia = soma / len(galera)
print(f'A mdia de idade eh de {mdia:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=',')
print()
print('Lista das pessoas acima da mdia: ', end='')
for p in galera:
    if p['Age'] >= mdia:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')

print('Fim')

print('\nEx 095')
time = list()
player = dict()
match = list()
while True:
    player.clear()
    player['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Qntas partidas {player["nome"]} jogou? '))
    for c in range(0, tot):
        match.append(int(input(f'Qntos gols na partida {c}? ')))
    player['gols'] = match[:]
    player['total'] = sum(match)
    time.append(player.copy())
    while True:
        press = str(input('Qr continuar [S/N]? ')).upper()[0]
        if press in 'SN':
            break
        print('Essa n eh uma alternativa valida')
    if press == 'N':
        break
print('-='*20)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)
print(f'O jgdor {player["nome"]} jogou {len(player["gols"])} partidas.')
for i, v in enumerate(player['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {player["total"]} gols')
# INACABADO