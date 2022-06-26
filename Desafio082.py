valores = list()
valorespares = list()
valoreimpares = list()

while True:
    n = (int(input('Digite o valor: ')))
    valores.append(n)

    pergunta = ''
    pergunta = str(input('Você quer continuar? [S/N]? ')).upper()
    if pergunta != 'S':
        break

cont = 0
for c in valores:
    if valores[cont] % 2 == 0:
        valorespares.append(valores[cont])
    else:
        valoreimpares.append(valores[cont])
    cont += 1

valores.sort()
valorespares.sort()
valorespares.sort()
print('-='* 30)
print(f'A lista com todos os itens informados foi: {valores}')
print(f'A lista com todos os valores pares foi: {valorespares}')
print(f'A lista com todos os valores ímpares foi: {valoreimpares}')
