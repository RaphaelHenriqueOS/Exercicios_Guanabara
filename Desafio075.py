tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print(tupla)
print(f'O Valor 9 apareceu {tupla.count(9)} vezes') # a) quantas vezes aparece o valor 9

if 3 in tupla:
    print(f'O número três apareceu na posição: {tupla.index(3) + 1}') # b) em que momento o 3 aparece
else:
    print('O número 3 não foi digitado')

for x in tupla:
    if x % 2 == 0:
        print(x, end=', ')

