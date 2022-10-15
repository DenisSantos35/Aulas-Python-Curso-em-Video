lista = list()
listapares = list()
listaimpares = list()

while True:
    lista.append(int(input('Digite um numero: ')))
    msg = ' '
    while msg not in 'SsNn':
        msg = str(input('Quer continuar? [S/N]')).strip().upper()
    if msg == 'N':
        break
for num in lista:
    if num % 2 == 0:
        listapares.append(num)
    else:
        listaimpares.append(num)
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapares}')
print(f'A lista de ímpares é {listaimpares}')
