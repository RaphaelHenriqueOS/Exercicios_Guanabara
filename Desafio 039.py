#Desafio 039 - ano de alistamento
ano = int(input('Iforme seu ano de nascimento: '))
idade = (2022 - ano)
#print(idade)
if idade < 18:
    print('Você nasceu em {} e tem {} anos'.format(ano, idade))
    print('Você ainda não precisa se alistar. Faltam {} anos. Você se alistará no ano de {}'.format((18 - idade), (2022 + idade)))
elif idade > 18:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('Você já deveria ter se alistado. Já se passaram {} anos. Você deveria ter se alistado em {}'.format((idade - 18), (ano + 18)))
else:
    print('Você nasceu em {} e tem {} anos.'.format(ano, idade))
    print('Você já tem {} anos. Está na hora guerreiro!'.format(idade))
