casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quanto tempo pretende pagar? '))
tempo = tempo * 12 #tempo em meses
#calcule o valor da prestação mensal sabendo que ela não
#exceder 30% do salário ou então o empréstimo será negado.
salario30 = salario - (salario*(30/100))
prestacao = casa // tempo
print('Sua prestação ficou em: R${} pagas em {} meses'.format(prestacao, tempo))
if prestacao > salario30:
    print('A prestação excede 30% do seu salário. Empréstimo negado')
else:
    print('Parabéns! Seu empréstimo foi aprovado')
