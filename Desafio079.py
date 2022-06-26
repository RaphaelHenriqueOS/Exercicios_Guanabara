valores = list()
n = 0
pergunta = 'S'
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        pergunta = str(input('Quer contiunuar? [S/N] ')).upper()
        if pergunta == 'N':
            break
    else:
        print('Esse valor já consta na lista. Tente outro valor')

valores.sort()
print(valores)


