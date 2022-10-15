from random import randint
from time import sleep
print('-'*30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-'*30)
jogos = int(input('Quantos jogos quer que sorteie? '))
sorteio = list()
megasena = list()
for cont in range(0, jogos):
    for j in range(0,6):
        num = randint(1, 60)
        while num in sorteio:
            num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
    megasena.append(sorteio[:])
    sorteio.clear()
print('-='*4, end='')
print('SORTEANDO {} JOGOS'.format(jogos), end='')
print('-='*4,)
for pos, imprecao in enumerate(megasena):
    print(f'Jogo {pos + 1}: {sorted(megasena[pos])}')
    sleep(1)
print('-='*6, end='')
print('< BOA SORTE > ', end='')
print('-='*6)

