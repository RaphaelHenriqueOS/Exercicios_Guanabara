## Usando o módulo math
import math
co = float(input('\033[1;33;40mCateto Oposto:\33[m '))
ca = float(input('\033[1;33;40mCateto Adjacente:\33[m '))
hi = math.hypot(co,ca)
print('A hipotenusa é: {:.2f}'.format(hi))