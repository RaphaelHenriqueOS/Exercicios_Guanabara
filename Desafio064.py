cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
     soma += n
     cont += 1
    else:
        print('fim')
        print(f'O total de números digitados foi {cont} e a sua soma é {soma}')