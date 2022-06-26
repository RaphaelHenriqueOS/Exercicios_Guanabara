from math import factorial


def fatorial(num, show=False):
    """Função Fatorial
cálculo de fatorial"""
    print(f'O Fatorial de {num}! é: {factorial(num)}')
    print(end=' => ')
    if show == True:

        cont = num
        if cont >= 0:
            for c in range(1, num):
                print(cont, end=' x ')
                cont -= 1
        if cont == 1:
            print('1', end='')


número = int(input('Digite um numero: '))
pergunta = str(input('Gostaria de exibir a conta? [S/N] ')).upper()
if pergunta in 'S':
    exibir = True
    fatorial(número, exibir)
else:
    exibir = False
    fatorial(número, exibir)