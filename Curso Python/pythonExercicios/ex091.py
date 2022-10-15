from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
cont = 0
while True:
    jogo['Jogador1'] = randint(1,6)
    jogo['Jogador2'] = randint(1,6)
    jogo['Jogador3'] = randint(1,6)
    jogo['Jogador4'] = randint(1,6)
    break
print(jogo)
for dado, status in jogo.items():
    print(f'O {dado} tirou {status}')
    sleep(1)
print(f'Ranking dos jogadores: ')
cont = 0

for vencedor in sorted(jogo, key = jogo.get, reverse = True):
    cont += 1
    print(f'{cont}º lugar: {vencedor} com {jogo[vencedor]}')
    sleep(1)
'''
ou
ranking = list()
ranking = sorted(jogo.items, key = jogo.itemgetter, reverse = Tru
devolve resultado como lista e tuplas dentro
for i, v in enumerate(ranking):
    print(f'{i} lugar: {v[0]} com {v[1]}
    sleep(1)'''




