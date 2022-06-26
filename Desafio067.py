cont = total = 0
while True:
    n = int(input('Informe qual valor você que ver a tabuada: '))
    if n >= 0:
        print('=-='*3)
        for cont in range (0, 11):
            total = n * cont
            print(f'{n} x {cont} = {total}')
            cont += 1
        print('=-=' * 3)
    else:
        break
print('Fim')