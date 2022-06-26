# Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
# um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois
# lados e menor que a soma dos outros dois lados
"""""| b - c | < a < b + c
     | a - c | < b < a + c
     | a - b | < c < a + b"""""
r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')

