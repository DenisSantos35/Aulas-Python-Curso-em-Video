lista = list() #criaçao de lista vazia
#maior = 0 # atribuiçao de maior
m = list()# atribuiçao de posicao menor
p = list() # atribuicao para posicao maior
for pos, val in enumerate(range(0,5)):
    lista.append(int(input(f'Digite um valor para posicao {pos} ')))
for pos, val in enumerate(lista):
    if min(lista) == val:
        m.append(pos)
    if max(lista) == val:
        p.append(pos)

print(f'Voce digitou os valores {lista}')
print(f'O maior valor da lista e {max(lista)} e sua posicao é',end=' ')
for v in p:
    print(v,'... ',end='')
print(f'\nO menor valor da lista e {min(lista)} e sua posiçao é',end='')
for x in m:
    print(x,'... ',end='')

