'''for c in range(1,10):
    print(c)
print('fim')'''
c = 0
'''while c < 10 :
    print(c)
    c += 1
print('FIM')'''

'''for c in range(1,5):
    n = int(input('Digite um valor: '))
print('FIM')'''
'''c = str('s').upper().strip()
while(c == 'S'):
    n = int(input('Digite um valor: '))
    c = str(input('Deseja continuar: [s/n]')).upper().strip()
print('FIM')'''
n = 1
contp = 0
conti = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            contp += 1
        else:
            conti += 1
print('Pares {}\nImpares {}'.format(contp, conti))
print('ACABOU')

