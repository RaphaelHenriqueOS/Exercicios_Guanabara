s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite seu sexo: ')).upper()
    if s != 'M' and s != 'F':
        print('Você digitou errado, tente outra vez!')
print('Fechou!')
