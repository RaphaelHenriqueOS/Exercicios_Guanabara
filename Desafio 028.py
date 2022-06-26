import random
n = int(input('Escreva um número de 0 a 5: '))
m = random.randint(0,5)
if n == m:
    print('parabéns! Você acertou! seu número foi: {} e o do PC foi: {}'.format(n, m))
else:
    print('Que pena, você erro! Seu número foi: {} e o do PC foi: {}'.format(n, m))
