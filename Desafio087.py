numero = 0
linha1 = []
linha2 = []
linha3 = []
maiorValorSegundaLinha = []
soma = 0
cont2 = cont3 = 0
soma_3coluna = 0


for p in range (0, 3):
    numero = int(input(f'Digite um valor para [{0, p}]: '))
    linha1.append(numero)
    if linha1[p] % 2 == 0:
        soma += linha1[p]

for p in range(0, 3):
    numero = int(input(f'Digite um valor para [{1, cont2}]: '))
    linha2.append(numero)
    if linha2[cont2] % 2 == 0:
        soma += linha2[cont2]
    cont2 += 1

for p in range (0, 3):
    numero = int(input(f'Digite um valor para [{2, cont3}]: '))
    linha3.append(numero)
    if linha3[cont3] % 2 == 0:
        soma += linha3[cont3]
    cont3 += 1

soma_3coluna = linha1[2] + linha2[2] + linha3[2]


print('-='*15)

for p in range(0, len(linha1)):
    print(f'[ {linha1[p]:^5} ]', end='')
print('\n')
for p in range(0, len(linha2)):
    print(f'[ {linha2[p]:^5} ]', end='')
print('\n')
for p in range(0, len(linha3)):
    print(f'[ {linha3[p]:^5} ]', end='')
print()
print('-='*15)

print(f'\nA soma dos valores pares é: {soma}')

print(f'A soma da terceira coluna é: {soma_3coluna}')

print(f'O maior valor da Segunda Linha é: {max(linha2)}')
