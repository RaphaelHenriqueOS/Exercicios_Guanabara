n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f, end='')

'''
#Tentando fazer com FOR
n = int(input('Informe qual número você quer calcular seu Fatorial: '))
f =  n
fatorial = 1
c = 0
for c in range(-n, 0):
    print(f, end=' x ')
    f -= 1
    c += 1
    fatorial *= c
print(f' = {fatorial}')'''
