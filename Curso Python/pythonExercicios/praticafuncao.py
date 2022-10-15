'''def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f *= c
    return f
n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O fatorial e igual a {f1}, {f2}, e {f3}')'''

def parOuImpar(n=0):
    if n % 2 ==0:
        return True
    else:
        return False
n1 = int(input('Digite um valor: '))
print(f'O valor {n1} é par? {parOuImpar(n1)}')
