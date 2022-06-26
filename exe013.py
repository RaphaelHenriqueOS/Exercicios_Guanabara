## acréscimo do salário##
n = float(input('Qual o salário:  R$'))
s = n+(n*(15/100))
print(f'O salario de R${n}, com o acréscimo de 15% passa a ser: R${s:.2f}')

## calculando valor a vista com 10% desconto e 8% aumento se for parcelado.##

p = float(input('Digite o valor do produto: R$'))
avista = (p-(p*(10/100)))
parcelado = (p+(p*(8/100)))
print(f'Pagando a vista, o valor de R${p} terá desconto de 10% e será{avista}. Se pagar parcelado, terá aumento de 8% que será {parcelado}')