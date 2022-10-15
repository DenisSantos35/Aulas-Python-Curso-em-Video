times = ('Palmeiras', 'Corinthians', 'Atletico-Pr', 'Atletico-Mg', 'Internacional',
         'Fluminense', 'Botafogo', 'Santos', 'Sao Paulo', 'Bragantino', 'Avai',
         'Atletico-go', 'Ceará SC', 'Flamengo', 'Coritiba', 'America-Mg',
         'Goias', 'Cuiaba', 'Fortaleza', 'Juventude')
print('-='*30)
print(times)
print('-='*30)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*30)
print(f'Os 4 ultimos são {times[16:]}')
print('-='*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*30)
posicao = times.index('Flamengo') + 1
print(f'O Flamengo esta na {posicao}ª posição: ')



