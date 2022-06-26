#Desafio 040 - média de nota
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = float((n1 + n2) / 2)
if media < 5.0:
    print('Você tirou {:.2f}! Está \033[;31mreprovado\033[m'.format(media))
elif 5.0 <= media <= 6.9:
    print('Você tirou {:.2f}! Está de \033[0;31mrecuperação!\033[m')
else:
    print('Você tirou {:.2f}! Está \033[;34maprovado\033[m!'.format(media))
