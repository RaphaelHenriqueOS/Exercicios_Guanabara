altura = float(input('Digite sua altura: '))
peso = int(input('Digite o seu peso: '))
imc = peso // pow(altura, 2)
print('Seu IMC é: ', imc)
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc <= 25:
    print('Você está no PESO IDEAL')
elif imc <= 30:
    print('Você está com SOBREPESO')
elif imc <= 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')
