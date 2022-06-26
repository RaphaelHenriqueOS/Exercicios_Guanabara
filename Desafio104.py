def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro\033[m\033[31m! Digite um número válido\033[m')
        if ok:
            break
    return valor


#Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o núemro {n}')