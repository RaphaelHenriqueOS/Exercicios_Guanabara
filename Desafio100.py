from random import randint
from time import sleep
numeros = list()


def sorteia(num):
    n = 0
    print(f'Os valores sorteados são: ', end=' ')
    for c in range(0, 5):
        n = randint(1, 20)
        print(f'\033[0;34m{n}\033[m', end=' ')
        sleep(0.5)
        num.append(n)


def somaPar(soma):
    outro = 0
    for c in soma:
        if c % 2 == 0:
            outro += c
    print(f'\nA soma dos valores pares é \033[4;36m{outro}\033[m')


sorteia(numeros)
somaPar(numeros)


