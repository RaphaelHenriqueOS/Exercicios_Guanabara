aluno = {}

nome = str(input('Digite o nome do Aluno: '))
media = float(input('Informe a média desse aluno: '))
if media <= 5:
    aluno['Situação'] = (f'\033[31m{"Reprovado"}\033[m')
else:
    aluno['Situação'] = f'\033[34m{"Aprovado"}\033[m'

aluno['Aluno'] = nome
aluno['Média'] = media

print(f'O aluno {aluno["Aluno"]} foi {aluno["Situação"]}!')

