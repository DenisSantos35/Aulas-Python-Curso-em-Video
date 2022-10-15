ql,qc = list(map(int,input().split()))
lc,cc = list(map(int,input().split()))
print(ql,qc)
lista = []
lista1 = []

for l in range(0,ql):
    for c in range(0,qc):
        lista.append(0)
        if (l > 0 and l < ql -1) and c == (1):
            lista.pop()
            lista.insert(0,3)
        if l == ql-1:
            lista.pop()
            lista.append(2)
        if l > 0 and c == (qc-1):
            lista.pop()
            lista.append(1)
    lista1.append(lista[:])
    lista.clear()
for l in range(0,ql):
    for c in range(0,qc):
        if(l>0 and l<ql-1) and (c>0 and c <qc-1):
            lista1[l][c] = lista1[l-1][c]+lista1[l-1][c-1]+lista1[l][c-1]

for l in range(0,ql):
    for c in range(0,qc):
        print(f'[{lista1[l][c]:^5}]',end='')
    print()
print(lista1[lc-1][cc-1])
'''for i in lista1:
    print('{}'.format(i))'''






