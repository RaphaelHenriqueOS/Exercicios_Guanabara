peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso / (pow(altura, 2)))
if imc < 18.5:
    print('Você está ABAIXO DO PESO. Seu IMC é de {:.1f}'.format(imc))
elif imc < 25:
    print('Você está com seu PESO IDEAL. Seu IMC é de {:.1f}'.format(imc))
elif imc < 30:
    print('Você está com SOBREPESO. Seu IMC é de {:.1f}'.format(imc))
elif imc < 40:
    print('Você está com OBESIDADE. Seu IMC é de {:.1f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA. Seu IMC é de {:.1f}'.format(imc))