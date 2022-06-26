# Jogos da Megasena
import time
from random import randint

jogos = []
quant_jogos = int(input('Quantos Jogos você deseja fazer? '))

for p in range(0, quant_jogos):
    jogos.append([randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)])
    jogos[p].sort()

    result = []
    while jogos[p] != 4:
        r = randint(0, 100)
        if randint(1, 60) not in jogos[p]:
            jogos.append(randint(1, 60))

print('-' * 30)
print('       JOGO DA MEGASENA')
print('-' * 30)
print(f'Quantos números você que que eu sorteie? {quant_jogos}')
time.sleep(1)
for c, v in enumerate(jogos):
    time.sleep(1)
    print(f'Jogo {c + 1}: {v}')
print('-' * 30)
print('Boa Sorte!!!')