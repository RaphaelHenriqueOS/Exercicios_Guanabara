primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
cont2 = cont
while cont <= 10:
    print('{} ►'.format(termo), end=' ')
    termo += 1
    cont += 1
menu = str(input('\nVocê gostaria de calcular mais termo? [s/n] ')).upper()
if menu == 'S':
    while menu == 'S':
        novotermo = int(input('\nQuantos termos mais? '))
        if novotermo != 0:
            cont2 = cont
            while cont2 < (cont + novotermo):
                print('{} ►'.format(termo), end=' ')
                termo += 1
                cont2 += 1
        else:
            print(f'Foram calculados {cont2} termos')
            print('Fim')
    else:
        print(f'Foram calculados {cont2} termos')
        print('FIm')

else:
    print(f'Foram calculados {cont} termos')
    print("FIM")