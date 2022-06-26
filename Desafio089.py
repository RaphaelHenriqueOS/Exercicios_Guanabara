geral = []
alunos = []
notas = []
nome = ''
media = 0
cont = 0

while True:
    nome = str(input('Nome do Aluno: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2

    alunos.append(nome)
    alunos.append(notas[:])
    alunos.append(media)

    geral.append(alunos[:])
    media = 0
    alunos.clear()
    notas.clear()

    per = ''
    per = str(input('Quer Continuar? '))
    if per in 'Nn':
        break
print()
print()
print('-=' * 15)
print(f"{'No' : <5}", end='')
print(f"{'Nome': ^10}", end='')
print(f"{'Média': >15}")
print('__' * 15)

while cont < (len(geral)):
    print(f"{cont : <8}", end='')
    print(f"{geral[cont][0] : <12}", end='')
    print(f"{geral[cont][2] : >10}")
    cont += 1
print('__' * 15)

while True:
    perg = 0
    perg = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if perg == 999:
        print('Muito obrigado por usar nosso programa! Volte sempre!')
        break
    else:
        print('__' * 15)
        print(f'O aluno \033[1;32m{geral[perg][0]}\033[m tirou as notas \033[1;34m{geral[perg][1][0]}\033[m e \033[1;34m{geral[perg][1][1]}\033[m')
        print('__' * 15)