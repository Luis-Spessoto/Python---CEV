import datetime

"""# docstring
def cont(i, f, p):
    -Faz uma contagem
    i: inicio
    f: fim
    p: passo
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')


cont(1, 10, 2)


# parametros opicionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    print(f'A soma vale {s}')


n1 = somar(3, 2, 5)
n2 = somar(2, 2)
n3 = somar(6)
print(f'Os resultados foram {n1}, {n2} e {n3}')


# escopo de variaveis
def test():
    x = 8
    print(f'Na funcao teste, n vale {n}')
    print(f'Na funcao teste, x vale {x}')


#     x so funciona aq dentro sendo assim um escopo local
#     ja y eh um escopo global, pois funciona em um td


n = 2
print(f'No programa principal, n vale {n}')
test()


# print(f'No programa principal, x vale {x}')


# outro teste da mesma materia
def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)


# Exercicio pratico
def fat(n1=1):
    f = 1
    for x in range(n1, 0, -1):
        f *= x
    return f


n = int(input('Digigite um nmro: '))
print(f'O fatorial de {n} eh igual a {fat(n)}')"""

print('\nEx 101')
print('\33[35m-\33[36m_\33[m' * 11)
"""Para checar votos
    :x: ano de nascimento
    :y: ano vigente
    :return:
    """


def vote(ano):
    o = datetime.date.today().year
    z = o - ano
    if z < 16:
        return f'Com {z} anos: VOTO NEGADO'
    if 16 <= z < 18:
        return f'Com {z} anos: VOTO OPCIONAL'
    if 18 <= z < 65:
        return f'Com {z} anos: VOTO OBRIGATORIO'
    if z >= 65:
        return f'Com {z} anos: VOTO OPICIONAL'


x = int(input('Em que ano vc nasceu? '))
print(vote(x))
print('\33[36m-\33[35m_\33[m' * 11)