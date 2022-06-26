valores = []
pares = []
impares = []

for c in range(0, 7):
    valores.append(int(input('Digite um valor: ')))
    if valores[c] % 2 == 0:
        pares.append(valores[c])
        pares.sort()
    else:
        impares.append(valores[c])
        impares.sort()

valores.clear()
valores.append(pares)
valores.append(impares)

print('-=' * 30)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
