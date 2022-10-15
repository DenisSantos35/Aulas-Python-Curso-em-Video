'''matriz = list()
num = list()
soma = 0
soma2 = 0
maior = 0

for l in range(0,3):
    for c in range(0,3):
        n1 = int(input(f'Digite um valor para [{l, c}]: '))
        if n1 % 2 == 0:
            soma += n1
        if c == 2:
            soma2 += n1
        if l == 1:
            if maior < n1:
                maior = n1

        matriz.append(n1)
        num.append(matriz[:])
        matriz.clear()
for l in range(0,9,3):
    for c in range(0,3):
        print(num[c+l], end='')


    print('\n')
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {maior}')'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
for l in range(0,3):
    scol += matriz[l][2]
for c in range(0,3):
    if c == 0 or mai < matriz[1][c]:
        mai = matriz[1][c]


print('-='*30)
print(f'A soma dos valores pares e {spar}')
print(f'A soma da terceira coluna é {scol}')
print(f'O maior valor da segunda linha e {mai}')







