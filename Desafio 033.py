# Desafio 33 - dizer quem é maior e quem é menor

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
lista = sorted([n1, n2, n3]) #sorted coloca a lista em ordem crescente
print('O maior número é {} e o menor é {}'.format(lista[2], lista[0]))