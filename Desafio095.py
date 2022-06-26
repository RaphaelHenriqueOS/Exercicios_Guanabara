jogador = dict()
partidas = list()
soma = 0

jogador['nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input('Quantas partidas ele fez? '))
for c in range(0, qtd_partidas):
    partidas.append(int(input(f'Quantas gols ele fez na partida {c}? ')))
    soma += partidas[c]

jogador['gols'] = partidas
jogador['total'] = soma
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {qtd_partidas} partidas')
for k, v in enumerate(partidas):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {soma} gols.')