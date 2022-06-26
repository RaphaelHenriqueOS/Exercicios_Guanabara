trabalhador = {}
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nascimento'] = int(input('Ano de Nasciemnto: '))
trabalhador['ctps'] = int(input('CTPS: '))
trabalhador['idade'] = 2022 - trabalhador['nascimento']



if trabalhador['ctps'] != 0:

    trabalhador['ano_contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['tempo para aposentar'] = 35 - (2022 - trabalhador['ano_contratacao'])
    if trabalhador['tempo para aposentar'] <= -1:
        trabalhador['tempo para aposentar'] * (-1)
        print('Você já pode se aposentar.')
print('-='*15)
print(trabalhador)
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')

