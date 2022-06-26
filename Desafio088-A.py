#Jogo da Megasena
#Segunda forma que fiz esse programa. Essa foi a melhor, porém não consigui descobrir como colocar os números em ordem
#sem dar erro

from random import sample
from time import sleep
import emoji

jogo = []
aposta = []
quantidade = int(input('Quantos jogos você quer fazer? '))

for p in range(1, quantidade + 1):
    jogo.append(sample(range(1, 60), 6))

print('-=' * 15)
print('         JOGO MEGASENA', end=' ')
print(emoji.emojize(':four_leaf_clover:'))
print('-=' * 15)
print()
for p, j in enumerate(jogo):
    sleep(1)
    print(f'Jogo {p + 1}: {j}')
print('-=' * 15)
sleep(1)
print('         Boa Sorte!!!')