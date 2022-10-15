def txt(msg):
    print(msg)
    print('-'*20)


def area(l, c):
    ar = l * c
    print(f'A área de um terreno {l} X {c} é de {ar} m²')


txt('CONTROLE DE TERRENO')
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
area(larg, compr)
