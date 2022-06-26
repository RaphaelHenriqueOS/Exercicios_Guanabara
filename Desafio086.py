numero = 0
conta = 0
linha1 = []
linha2 = []
linha3 = []

for p in range (0, 3):
    numero = int(input(f'Digite um valor para [{0, conta}]: '))
    conta += 1
    linha1.append(numero)
conta = 0
for p in range(4, 7):
    numero = int(input(f'Digite um valor para [{1, conta}]: '))
    conta += 1
    linha2.append(numero)
conta = 0

for p in range (5, 8):
    numero = int(input(f'Digite um valor para [{2, conta}]: '))
    conta += 1
    linha3.append(numero)
conta = 0

print('-='*30)

for p in range(0, len(linha1)):
    print(f'[ {linha1[p]:^5} ]', end='')
print('\n')
for p in range(0, len(linha2)):
    print(f'[ {linha2[p]:^5} ]', end='')
print('\n')
for p in range(0, len(linha3)):
    print(f'[ {linha3[p]:^5} ]', end='')
