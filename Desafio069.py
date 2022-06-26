totalentrevistado = cont_maior_18 = cont_M = cont_mulher_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()
    totalentrevistado += 1
    if idade > 18:
        cont_maior_18 += 1
    if sexo == 'M':
        cont_M += 1
    if idade < 20 and sexo == 'F':
        cont_mulher_20 += 1

    pergunta = str(input('Deseja continuar? [S/N] ')).upper()
    if pergunta == 'N':
        break
print(f'Total de pessoas entrevistadas: {totalentrevistado}')
print(f'Total de pessoas com mais de 18 anos: {cont_maior_18}')
print(f'Total de homens cadastrados: {cont_M}')
print(f'Total de mulheres com menos de 20 anos: {cont_mulher_20}')