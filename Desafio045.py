import random
voce = str(input('Jogue: '))
PC = ['Pedra', 'Papel', 'Tesoura']
PC2 = random.choice(PC)
if voce == PC2:
    print(voce, PC2, 'DEU EMPATE!')
elif voce == 'Pedra' and PC2 == 'Papel':
    print(voce, PC2, 'VOCÊ PERDEU!')
elif voce == 'Pedra' and PC2 == 'Tesoura':
    print(voce, PC2, 'VOCÊ GANHOU!')
elif voce == 'Papel' and PC2 == 'Pedra':
    print(voce, PC2, 'VOCÊ PERDEU!')
elif voce == 'Papel' and PC2 == 'Tesoura':
    print(voce, PC2, 'VOCÊ PERDEU')
elif voce == 'Tesoura' and PC2 == 'Pedra':
    print(voce, PC2, 'VOCÊ PERDEU')
elif voce == 'Tesoura' and PC2 == 'Papel':
    print(voce, PC2, 'VOCÊ GANHOU!')