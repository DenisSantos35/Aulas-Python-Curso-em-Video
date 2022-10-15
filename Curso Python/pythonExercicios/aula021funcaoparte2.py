#help(print)
#print(input.__doc__)

'''def contador(i,f,p):
    """
    ->faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    funcao criada dia 14/07/2022
    """
    c=i
    while c <= f:
        print(f'{c}',end='..')
        c+=p
    print('fim')


contador(1,10,2)
help(contador)'''
def soma(a=0,b=0,c=0):
    s = a+b+c
    return s

s1 = soma(3,2,5)
s2 = soma(3,2)
s3 = soma(3)
s4 = soma()
print(f' As somas deram {s1}, {s2}, {s3} e {s4}')
'''def test():
    global n
    n = 8
    print(f'Na funcao teste, n vale {n}')
    print(f'Na funcao teste, x vale {n}')
#programa principal
n = 2

print(f'No programa principal, x vale {n}')
test()
print(f'No programa principal, n vale {n}')'''
