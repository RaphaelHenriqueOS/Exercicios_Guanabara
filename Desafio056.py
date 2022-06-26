soma = 0
media = 0
maioridade = 0
mulher20anos = 0
pessoamaisvelha = ''
for p in range(1, 6):
    print('++++ {}ª PESSOA ++++'.format(p))
    pessoa = str(input('Informe o nome: '.format(p)))
    idade = int(input('Informe a idade: '.format(p)))
    genero = str(input('Iforme o sexo: '.format(p))).upper()
    print('')
    soma += idade
    if p == 1:
        maioridade = idade
        pessoamaisvelha = pessoa
    else:
        if genero == 'M' and idade > maioridade:
            pessoamaisvelha = pessoa
            maioridade = idade
        if genero == 'F' and idade < 20:
            mulher20anos += 1
media = soma / 5
print('A média do grupo é de \033[31m{}\033[m anos '.format(media))
print('Existem \033[31m{}\033[m mulheres com menos de 20 anos'.format(mulher20anos))
print('O homem mais velho é o \033[31m{}\033[m e ele tem {}'.format(pessoamaisvelha, maioridade))
