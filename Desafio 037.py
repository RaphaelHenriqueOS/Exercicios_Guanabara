numero = int(input('Escreva um número qualquer: '))
opcao = int(input('Em que base você deseja converter?\n1 - binário'
                  '\n2 - octal'
                  '\n3 - hexadecimal'
                  '\n'))
if opcao == 1:
    print('O valor de {} em Binário é: {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O valor de {} em Octal é: {}'.format(numero, oct(numero)[2:]))
else:
    print('O valor de {} em Hexadecimal é: {}'.format(numero, hex(numero)[2:]))
# o [2:] significa que ele vai exibir da segunda casa até o final. Fatiamento de String
