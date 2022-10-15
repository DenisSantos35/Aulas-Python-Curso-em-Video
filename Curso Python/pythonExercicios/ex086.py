'''matriz = list()
num = list()
for l in range(0,3):
    for c in range(0,3):
        matriz.append(int(input(f'Digite um valor para [{l, c}]: ')))
        num.append(matriz[:])
        matriz.clear()
for l in range(0,9,3):
    for c in range(0,3):
        print(num[c+l], end='')
    print('\n')'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
