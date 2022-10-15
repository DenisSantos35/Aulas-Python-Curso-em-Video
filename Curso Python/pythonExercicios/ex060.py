'''from math import factorial
n = int(input('digite um numero'))
n = factorial(n)
print(n)'''

numero = int(input('Digite um numero: '))
cont = numero - 1
print('{}'.format(numero), end=" ")
while cont != 0:
    numero = numero * cont
    print(' X {}'.format(cont), end=" ")
    cont -= 1
print(' = {}'.format(numero))

