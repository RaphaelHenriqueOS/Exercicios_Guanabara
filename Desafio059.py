v1 = int(input('Informe o primeiro valor: '))
v2 = int(input('Informe o segundo valor: '))
menu = 0
soma = 0
multiplicacao = 0
while menu != 5:
    print('++++ MENU ++++')
    menu = int(input('''Aperte [1] = Para Somar:
Aperte [2] = Para Multiplicar:
Aperte [3] = Para saber qual o maior valor: 
Aperte [4] = Para Digitar Novos Valores: 
Aperte [5] = Para Sair.
++++ FIM ++++'''))
    if menu != 1 or 2 or 3 or 4 or 5:
        print('Opção inválida. Tente novamente!')
    if menu == 1:
        soma = v1 + v2
        print('A soma de {} e {} é: {}'.format(v1, v2, soma))
    if menu == 2:
        multiplicacao = v1 * v2
        print('A multiplicação entre {} e {} é: {}'.format(v1, v2, multiplicacao))
    if menu == 3:
        if v1 < v2:
            print('O maior valor é {}'.format(v2))
        else:
            print('O maior valor é {}'.format(v1))
    if menu == 4:
        v1 = int(input('Digite um novo valor para v1: '))
        v2 = int(input('Digite um novo valor para v2: '))

print('fim')