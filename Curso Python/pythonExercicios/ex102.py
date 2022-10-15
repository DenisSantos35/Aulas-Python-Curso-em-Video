#programa principal
def fatorial(num=1, show=False):
    """
    -> calcula o fatorial de um numero.
    :param num: O numero a ser calculado
    :param show: (opcional) mostrar ou nao a conta.
    :return: o valor do fatorial de um numero
    """
    f = 1
    for c in range(num,0,-1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(f'X', end=" ")
            else:
                print(f'=', end=" ")
        f *= c
    return f


num = int(input('Digite um numero: '))
print(fatorial(num, show=True))
