primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = (primeiro + (11 - 1) * razao) #fórmula matemática para se achar o 10º termo. an = a1 + (n – 1)r
for c in range(primeiro, decimo, razao):
    print(c, end=' → ')
print('ACABOU')