lista = []
copia = []
maior = menor = 0

while True:
    lista.append(str(input('Digite seu nome: ')))
    lista.append(int(input('Digite seu peso: ')))

    if len(copia) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    copia.append(lista[:])
    lista.clear()

    p = ''
    p = (str(input('Quer Continuar? ')))
    if p in 'Nn':
        break

print()
print('-=' * 30)
print(f'Foram cadastrados {len(copia)} pessoas.')
print(f'O maioir peso cadastrado foi {maior}kg e pertence a: ', end='')
for p in copia:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso cadastrado foi {menor}kg e pertence a: ', end='')
for p in copia:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')