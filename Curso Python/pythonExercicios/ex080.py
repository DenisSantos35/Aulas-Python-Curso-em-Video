
'''for pos, i in enumerate(range(0,5)):
    lista.append(int(input('Digite um valor: ')))
    if pos == 0 or  lista[pos] > lista[pos-1]:
            print('Adicionado ao final da lista...')
    elif lista[pos]<lista[pos-pos]:
            n1 = lista.pop()
            lista.insert(0,n1)
            print(f'Adicionado na posicao {pos - pos} ')
    if pos == 2:
        if lista[pos-1] > lista [pos] > lista[pos - pos]:
            n1 = lista.pop()
            lista.insert(1,n1)
            print(f'Adicionado na posição {pos-1} ')
    if pos == 3:
        if lista[pos-pos] < lista[pos] < lista[pos-2]:
            n1 = lista.pop()
            lista.insert(1,n1)
            print(f'Adicionado na posição {pos - 2}')
        elif lista[pos-2] < lista[pos] < lista[pos - 1]:
            n1 = lista.pop()
            lista.insert(2,n1)
            print(f'Adicionado na posição {pos - 1}')
    if pos == 4:
        if lista[pos-pos] < lista[pos] < lista[pos-3]:
            n1 = lista.pop()
            lista.insert(1,n1)
            print(f'Adicionado na posição {pos - 3}')
        elif lista[pos-3] < lista[pos] < lista[pos - 2]:
            n1 = lista.pop()
            lista.insert(2,n1)
            print(f'Adicionado na posição {pos - 2}')
        elif lista[pos-2] < lista[pos] < lista[pos - 1]:
            n1 = lista.pop()
            lista.insert(3,n1)
            print(f'Adicionado na posição {pos - 1}')
print(lista)'''
lista = list()
for c in range(0,5):
    n = int(input('Digite um valor'))
    if c==0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1
print('=-'*30)
print(f'Os valores digitados em ordem foram{lista}')

