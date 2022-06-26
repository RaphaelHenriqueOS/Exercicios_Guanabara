dicionario = dict()
lista = list()
cont = soma = mulheres = 0
cont_idade = cont_m = media = cont_media = idade_maior_media =0

while True:
    dicionario['nome'] = str(input('Nome: '))
    dicionario['idade'] = int(input('Idade: '))

    while True:
        dicionario['sexo'] = str(input('Sexo [M/F] ')).upper()
        if dicionario['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F')

    lista.append(dicionario.copy())
    dicionario.clear()
    cont += 1


    pergunta = str(input('Quer Continuar? [S/N] ')).upper()
    if pergunta in 'N':
        break

for c in lista:
    soma += c['idade']
    cont_idade += 1

print(f'Foram Cadastradas {cont} pessoas.')
print()
print(f'A média das idades é {(soma / cont):.2f} anos.')
print()
print(f'As mulheres cadastradas são:',end=' ')
for d in lista:
    if d['sexo'] == 'F':
        print(f'{d["nome"]} ', end='')
        mulheres += 1
        cont_m += 1
    else:
        cont_m += 1
print(f' totalizando {mulheres} cadastros.', end='')
print()
media = soma / cont
for c in lista:
    if c['idade'] > media:
        print('   ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO!')