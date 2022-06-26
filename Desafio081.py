lista = list()
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    print(lista)
    pergunta = ''
    pergunta = str(input('Deseja continuar? [S/N] :')).upper()
    if pergunta != 'S':
        break
print(f'Foram digitados {len(lista)} itens.')
lista.sort(reverse=True)
print(f'A lista de trás para frente fica: {lista}')

print(f'Existe o número 5 na variável Lista? {5 in lista}')


