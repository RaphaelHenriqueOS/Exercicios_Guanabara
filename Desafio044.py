preconormal = float(input('Valor do produto: R$'))
condicao = int(input('Qual a forma de pagamento? \n1: à vista;\n2: à vista no cartão: \n3: Parcelado:\nQual a sua opção? '))
if condicao == 1:
    print('à vista no dinheiro/cheque, você tem 10% de desconto. R${}'.format(preconormal - (preconormal * (10 / 100))))
elif condicao == 2:
    print('à vista no cartão, você tem 5% de desconto: R${}'.format(preconormal - (preconormal * (5 / 100))))
elif condicao == 3:
    parcelado: int = int(input('Quantas vezes? '))
    if parcelado == 2:
        print('Você não terá acrescimo no valor. Ficará {}x de R${} = R${}'.format(parcelado, parcelado, (preconormal / parcelado)))
    else:
        parcelado >= 3
        print(f'Parcelando em {parcelado}x, seu produto sairá 20% mais caro. Será {parcelado}x de R${((preconormal + (preconormal * 0.2)) / parcelado):.2f} = R${(preconormal + (preconormal * 0.2)):.2f}')