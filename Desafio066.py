soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f'Foram digitados \033[31m{cont}\033[m e a soma entre eles é: \033[34m{soma}\033[m')

