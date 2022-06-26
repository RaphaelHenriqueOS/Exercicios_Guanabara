resp = 'S'
cont = soma  = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('End')
print(f'Você digitou {cont} números. A sua soma é {soma} e sua média é {media:.1f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')