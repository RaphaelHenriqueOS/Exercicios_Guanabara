# Desafio 29 - Programa que leia a velocidade de um carro,
v = int(input('Informe a sua velocidade: '))
if v <= 80:
    print('Sua velocidade está ok')
else:
    m = (v-80)*7
    print('Você foi multado! Sua velocidade foi {}, por isso receberá uma multa de: R${}'.format(v, m))
