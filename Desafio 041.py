from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
dataatual = date.today().year
idade = dataatual - ano
if idade <= 9:
    print('Você tem {} anos e sua categoria é: \033[0;34mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria é: \033[0;34mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print("Você tem {} anos e sua categoria é: \033[0;34mJUNIOR\033[m".format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é: \033[0;34mSÊNIOR\033[m'.format(idade))
elif idade > 25:
    print('Você tem {} anos e sua categoria é: \033[0;34mMASTER\033[m'.format(idade))