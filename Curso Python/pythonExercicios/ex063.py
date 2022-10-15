numero = int(input('Digite quantas sequencias de fibonatti deseja ver:'))
a = 0
b = 0
res = 1
while(numero > 0):
    a = a + b
    b = res
    res = a
    print(a, ',', end = '')
    numero -= 1
