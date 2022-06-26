d = int(input('Qual a distância: '))
if d <= 200:
    print('Sua passagem custará: R${}'.format(d * 0.50))
else:
    print('Sua passagem custará: R${}'.format(d * 0.45))