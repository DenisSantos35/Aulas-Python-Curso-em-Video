impar = list()
par = list()
lista = list()
'''ou pode declarar a lista assim:
lista = [[],[]]'''

for valores in range(0,7):
    numero = int(input(f'Digite o valor {valores + 1}º valor: '))
    if numero % 2 == 0:
        par.append(numero)
        #posso adicionar assim:
        #lista[0].append(numero)
    else:
        impar.append(numero)
        #posso adicionar assim:
        #lista[1].append(numero)
lista.append(impar[:])
lista.append(par[:])
'''ou posso ordenar assim:
lista[0].sort()
lista[1].sort()'''
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram:{lista[1]}')
print(f'Os valores impares digitados foram: {lista[0]}')




