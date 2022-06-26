from time import sleep

def contador(ini, fim, passo):
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    print('-=' * 30)
    for c in range(ini, fim, passo):
        print(c, end=' ')
        sleep(0.2)
    print(' FIM!')

#contador(1, 10, 2)
#contador(10, 0, -2)

#personalizavel
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if passo < 0:
    passo = passo *(-1)
if passo == 0:
    passo = 1

contador(inicio, fim, passo)


