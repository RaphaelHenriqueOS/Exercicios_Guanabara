## conversão de real para dolar ##
n = float(input('Quanto dinheiro você tem na carteira: '))
print('Os seus R${:.2f} valem US${:.2f}'.format(n, (n/4.70)))
## sem usar o .format e editando a quantidade de valores reais a serem exibidos ##
print(f'Os sues R${n:.2f} valem US${(n/4.70):.2f}')
