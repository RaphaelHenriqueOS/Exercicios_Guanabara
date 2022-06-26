valores = list()
lista = list()
cont = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    cont += 1
    lista = valores[:]
lista.sort()

print(lista)
print('*'*15)
print(f'O maior valor digitado foi {lista[4]} na posição {lista.index(lista[4])} e o menor valor foi {lista[0]} na posição {lista.index(lista[0])}')
print('Fim')
