'''lista = []

for i in range(0,10):
    lista.append(i)
print(lista)
lista.pop()
lista.remove(4)
del lista[7]
print(lista)'''
'''valores = [2,4,6,2,3,1,8,3,4,5]
if 7 in valores:
    valores.remove(2)
    print(valores)
else:
    print('valor nao encontrado')
valores.sort()
print(valores)
valores.sort(reverse=True)
valores.insert(1,10)
valores.pop(8)
print(valores)
print(len(valores))
val = []
val.append(5)
val.append(9)
val.append(4)
val.sort()
print(val)
for c,i in enumerate(val):
    print(f'posiçao', c,'valor ', i)
print('Cheguei ao final da lista')
value = list()
for cont in range(1,10):
    value.append(int(input('Digite um valor')))
print(value)'''
# neste caso b = a recebe faz com que os a e b faca ligaçao entre a e b
a = [2, 3, 4, 5]
b = a
print(a)
print(b)
b[2] = 8
print(a)
print(b)
#desta maneira faz se copia
a = [2, 3, 4, 5]
b = a[:]
print(a)
print(b)
b[2] = 7
print(a)
print(b)
c = a + b
print(c)


