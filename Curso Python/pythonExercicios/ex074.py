from random import randint
'''n1 = randint(0,9)
n2 = randint(0,9)
n3 = randint(0,9)
n4 = randint(0,9)
n5 = randint(0,9)
tupla = (n1, n2, n3, n4, n5)'''
tupla = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
cont = 0
maior = 0
menor = 0
'''for i in tupla:
    if maior < i:
        maior = i
    if cont == 0 or menor > i:
        menor = i
        cont = 1'''
print(f'Os valores sorteados são {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')



