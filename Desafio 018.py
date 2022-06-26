import math
a = int(input('\33[32mInforme o ângulo:\33[m '))
graus = math.radians(a)  ## passando de radianos para graus ##
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(graus), math.cos(graus), math.tan(graus)))
