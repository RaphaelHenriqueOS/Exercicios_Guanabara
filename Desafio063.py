numero = int(input('Digite quantos termos: '))
anterior = 0
proximo = 1
lista = []
fibonacci = 2
while fibonacci < numero:
    lista += [anterior, proximo]
    anterior += proximo
    proximo += anterior
    fibonacci += 1
print(lista)
print('Fim')