## Calculando a área da parede e quanto ele gastaria de tinta ##
c = float(input('Qual o comprimento da sua parede: '))
l = float(input('Qual a largura da sua parede: '))
a = ((c*l))
print('Sua parede tem {:.2f}m x {:.2f}m, com uma área de {:.2f}m². Serão necessários {:.3f}l de tinta para pinta-la.'.format(c, l, a, (a/2)))