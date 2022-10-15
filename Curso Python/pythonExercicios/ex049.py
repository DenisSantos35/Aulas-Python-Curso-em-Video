num = int(input('Digite o numero que desejar ver a tabuada: '))
for i in range(0, 11):
    print('{} X {} = {:3}'.format(num, i, (num*i)))
