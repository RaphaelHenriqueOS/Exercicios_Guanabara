from datetime import date
atual = date.today().year
totalmenor = 0
totalmaior = 0
for ano in range(1, 8):
    pessoa = int(input('Em que ano a {}ª nasceu? '.format(ano)))
    idade = atual - pessoa
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade < 21:
        totalmenor += + 1
    else:
        totalmaior += +1
print('O total de maiores foi de: {}'.format(totalmaior))
print('O total de menores foi de: {}'.format(totalmenor))