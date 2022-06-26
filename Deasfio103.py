def ficha(nome='<desconhecido>', gols=0):
    print('__'*20)
    print(f'O jogador {nome} marcou {gols} gols.')


# Programa Principal
jogador = str(input('Digite o nome do jogador: '))
if jogador:
    str(jogador)
else:
    jogador = '<desconhecido>'

pontos = str(input('Digite quantos gols ele marcou: '))
if pontos.isnumeric():
   pontos = int(pontos)
else:
    pontos = 0

ficha(jogador, pontos)
