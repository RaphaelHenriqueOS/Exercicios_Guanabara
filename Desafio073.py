clubes = ('Bragantino', 'Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians', 'América-MG', 'Internacional',
          'Avaí', 'Palmeiras', 'Flamengo', 'Curitiba', 'São Paulo', 'Botafogo', 'Fluminense', 'Ceará',
          'Atlético-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
print(f'Os 5 primeiros colocados são: {clubes[0:5]}')
print(f'Os últimos 4 colocados são: {clubes[-4:]}')
print(f'Os times em ordem alfabética: {sorted(clubes)}')
print('Curitiba está na posição: {}ª'.format(clubes.index('Curitiba')))


