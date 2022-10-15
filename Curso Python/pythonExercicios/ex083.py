lista = list()
lista.append(str(input('Digite a expreção')))
for i in lista:
    e1 = i.count('(')
    e2 = i.count(')')
if e1 == e2:
    print('Sua expreçao esta valida!')
else:
    print('Sua exprecao esta errada!')
