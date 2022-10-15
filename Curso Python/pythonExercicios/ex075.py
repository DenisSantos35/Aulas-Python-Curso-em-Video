'''val1 = int(input('Digite um numero: '))
val2 = int(input('Digite um outro numero: '))
val3 = int(input('Digite mais um numero: '))
val4 = int(input('digite o ultimo numero: '))
tupla = (val1, val2, val3, val4)'''
tupla = (int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')),
         int(input('Digite um numero: ')))
print(f'Voce digitou os valores {tupla}')
print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))
p = 0
if 3 in tupla:
    print('O valor 3 apareceu na {}ª posição'.format(tupla.index(3)+1))
else:
    print('O valor 3 não foi digitado em nehuma posição')


print('Os valores pares digitados foram ', end='')
for p in tupla:
    if p % 2 == 0:
        pares = p
        print( pares ,',' , end='')



