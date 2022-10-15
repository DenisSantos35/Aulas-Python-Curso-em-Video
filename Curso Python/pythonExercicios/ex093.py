jogador = dict()
gol = list()
soma = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?' ))
    for part in range(0,partidas):
        gols = int(input(f'Quantos gols na partida {part}? '))
        gol.append(gols)
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    break
print('-='*30)
print(jogador)
print('-='*30)
for dado, status in jogador.items():
    print(f'O campo {dado} tem o valor {status}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for part in range(0,partidas):
    print(f'    => Na partida {part}, fez {gol[part]} gols.')
print(f'Foi um total de {sum(gol)} gols.')

