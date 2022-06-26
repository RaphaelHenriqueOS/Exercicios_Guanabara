n = int(input('Digite um número: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', c, end=' ')
        tot += 1
    else:
        print('\033[34m', c, end=' ')
if tot == 2:
    print('\033[m')
    print('O número {} é PRIMO'.format(n))
else:
    print('\033[m')
    print('O número {} NÃO é primo.'.format(n))