## Calcular o valor a pagar pelo aluguel do carro sendo: 60 reias a diária e 0,15 o KM##
d = float(input('Quantos dias alugados: '))
k = float(input('Quantos km rodados: '))
td = d*60
tk = (k*float(0.15))
s = td + tk
print(f'Sua diária ficou em R${td:.2f}, seu km ficou em R${tk:.2f}. Total a pagar de R${s:.2f}')