numero = int(input('Digite um numero: '))
cont = 0
for i in range(1, numero + 1):
    if(numero % i == 0):
        cont = cont + 1
if(cont == 2):
    print('O numero {} e um Numero primo'.format(numero))
else:
    print('O numero {} e um  nao é um Numero primo'.format(numero))
