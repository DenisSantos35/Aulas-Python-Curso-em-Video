from random import randint
from time import sleep
numeros = []

def sorteio(lst):
    print(f'Sorteando 5 valores da lista: ',end="")
    for valor in range(0,5):
        n1 = randint(1,10)
        lst.append(n1)
        print(f'{n1} ',end="")
        sleep(0.3)
    print('Pronto!')




def somapar(lst):
    soma = 0
    print(f'Somando os valores pares de {lst}, temos ',end="")
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(soma ,end="")


sorteio(numeros)
somapar(numeros)






