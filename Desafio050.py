soma = 0
contador = 1
for n in range(0, 6):
    n = int(input('Digite um valor: '))
    if (n % 2) == 0:
        soma += n
        contador += 1
print('foram somados {} números pares e a soma foi: {}'.format(contador, soma))
