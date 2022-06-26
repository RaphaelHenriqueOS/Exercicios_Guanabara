#Definir se o ano é Bisexto
a = int(input('Digite o ano: '))
b = a % 4
if b == 0:
    print('esse ano é bixesto')
else:
    print('Esse ano não é bixesto')