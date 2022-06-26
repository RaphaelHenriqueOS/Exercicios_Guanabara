soma = 0
contador = 0
for c in range(1, 501):
    if (c % 2) == 1: #teste se é ímpar
        if (c % 3) == 0: #teste se é multuplo de 3
            print(c)
            contador = contador + 1
            soma = (soma +  c) #somando os valore na variável c
print('Foram somados {} valores, totalizando: {}'.format(contador, soma))