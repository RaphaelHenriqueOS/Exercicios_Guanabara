s = float(input('Qual o seu salário? R$ '))
if s > 1250:
    print('Seu aumento será de 10%, totalizando: R${}'.format(s + (s * (10/100))))
else:
    print('Seu aumento será de 15%, totalizando: R${}'.format(s + (s * (15/100))))