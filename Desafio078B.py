valores = []
cont1 = 1
cont = maior = menor = 0
while cont1 <= 5:
    valores.append(int(input(f'Informe o {cont1}º valor: ')))
    cont1 += 1
    if cont == 0:
        maior = menor = valores[0]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
           menor = valores[cont]
    cont += 1

print('=-' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print()


