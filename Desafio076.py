produtos = ('Lápis', 0.15, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90, 'Caneca', 17.50)
cont = 0
print('=-' * 19)
print(f'{"LISTA DE PREÇOS":^40}')
for n in produtos:
    print(f'{(produtos[cont]):.<30}' f'R$ {(produtos[cont + 1]):.2f}') # :.<30 significa alinhado a esquerda
    cont += 2
print('=-' * 19)