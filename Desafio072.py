cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    # _______________________________________________________
    while True:
        num = (int(input('digite um numero de zero a vinte: ')))
        if 0 <= num <= 20:
            break
        print('tente novamente. ', end=' ')

    print(f'você digitou o número {cont[num]}')
    # _______________________________________________________

    resp = " "
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':
        break

print('Fim')
