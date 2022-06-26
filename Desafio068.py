import random

cont = 0
soma = 0
while True:
    n = int(input('Digite seu número: '))
    escolha = str(input('Par ou Ímpar: [P/I]: ')).upper()
    pc = random.randint(1, 11)
    operacao = (n + pc) % 2
    soma = n + pc
    if operacao == 0 and escolha == 'P':
        print(f'você colcou {n} e o PC {pc}, a soma foi {soma}')
        print('Deu PAR, você ganhou!')
        cont += 1
    if operacao == 0 and escolha == 'I':
        print(f'você colcou {n} e o PC {pc}, a soma foi {soma}')
        print('Deu PAR, você Pedeu!')
        break
    if operacao != 0 and escolha == 'P':
        print(f'você colcou {n} e o PC {pc}, a soma foi {soma}')
        print('Deu ÍMPAR, você perdeu')
        break
    if operacao != 0 and escolha == 'I':
        print(f'você colcou {n} e o PC {pc}, a soma foi {soma}')
        print('Deu ÍMPAR, você ganhou')
        cont += 1
if cont == 0:
    print('Você não ganhou nehuma vez!')
else:
    print(f'Você ganhou {cont} vezes consecutivas')