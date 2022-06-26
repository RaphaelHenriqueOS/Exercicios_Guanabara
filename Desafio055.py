maiorpeso = 0
menorpeso = 0
for p in range(1, 5):
    peso = float(input('Digite o pesoa da {}ª pessoa: '.format(p)))
    if p == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('O maior peso foi: {}kg'.format(maiorpeso))
print('O menor peso foi: {}kg'.format(menorpeso))