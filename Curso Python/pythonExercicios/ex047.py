n = int(input('digite um numero: '))
for i in range(1,n+1):
    if(i % 2 == 0):
        print('{}, '.format(i), end=' ')
