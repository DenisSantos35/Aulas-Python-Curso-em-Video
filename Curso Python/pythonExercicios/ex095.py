jogador = dict()
gol = list()
dados = []
soma = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?' ))
    for part in range(0,partidas):
        gols = int(input(f'Quantos gols na partida {part}? '))
        gol.append(gols)

    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    dados.append(jogador.copy())
    gol.clear()
    while True:
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()
        if sair in 'SN':
            break
        print('ERRO! RESPONDA S OU N')
    if sair == 'N':
        break
# armazenamento de dados ate aqui

#apartir daqui analize de dados

print('-='*30)
print(f' cod     nome         gols       total')
print('-='*30)
for num, dad in enumerate(dados):
    print('{:<8} '.format(num + 1), end='')
    for valor in dad.values():
        print('{:<13}'.format(str(valor)), end='')
    print()
print('-='*30)
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    print('-='*30)
    if opcao == 999:
        break
    if opcao >= len(dados):
        print(f'ERRO! NAO EXISTE JOGADOR COM CODIGO {opcao}')
    else:
        print(f'---LEVANTAMENTO DO JOGADOR {dados[opcao]["nome"]}')
        for pos, v in enumerate(dados[opcao]["gols"]):
            print(f'      No jogo {pos + 1} fez {v} gols.')
    print('-='*30)
print('<<VOLTE SEMPRE>>')


'''for dado, status in jogador.items():
    print(f'O campo {dado} tem o valor {status}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for part in range(0,partidas):
    print(f'    => Na partida {part}, fez {gol[part]} gols.')
print(f'Foi um total de {soma} gols.')'''
