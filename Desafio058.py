import random
voce = 50
pc = 0
palpites = 0
while pc != voce:
    voce = int(input('Digite um número de 1 a 10: '))
    pc = random.randint(1, 10)
    if voce != pc:
        palpites += 1
        print('Você digitou {} e o PC escolheu {}. Você perdeu. Tente outra vez!'.format(voce, pc))
print('Você digitou {} e o PC escolheu {}.'.format(voce, pc))
print('Finalmente você acertou, mas foram necessárias {} tentativas.'.format(palpites + 1))