'''n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 > n3:
    print('O numero maior é {}'.format(n1))
    print('O numero menor é {}'.format(n3))
if n1 > n3 > n2:
    print('O numero maior é {}'.format(n1))
    print('O numero menor é {}'.format(n2))
if n2 > n3 > n1:
    print('O numero maior é {}'.format(n2))
    print('O numero menor é {}'.format(n1))
if n2 > n1 > n3:
    print('O numero maior é {}'.format(n2))
    print('O numero menor é {}'.format(n3))
if n3 > n1 > n2:
    print('O numero maior é {}'.format(n3))
    print('O numero menor é {}'.format(n2))
if n3 > n2 > n1:
    print('O numero maior é {}'.format(n3))
    print('O numero menor é {}'.format(n1))'''
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O menor valor digitado foi {}'.format(maior))
