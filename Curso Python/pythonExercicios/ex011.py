largura = float(input())
altura = float(input())
area = altura * largura
litro = 2
pintura = area / litro
print('Largura = {}m, \nAltura = {}m, \nArea = {:.2f}m²'.format(largura, altura, area))
print('Quantidade de tinta {:.2f} litros '.format(pintura))
