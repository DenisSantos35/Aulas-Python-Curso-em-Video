'''#importa biblioteca especifica raiz quadrada e potencia
from math import sqrt, pow
#calculo teorema de pitagoras a² = b² + c²
# a = raizq(a² + b²)
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adj = float(input('Digite o valor do cateto adjascente: '))
hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adj, 2))
#saida mostra o valor da hipotenusa
print('O valor da hipotenusa e igual a {:.2f}: '.format(hipotenusa))'''

import math
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjascente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa e igual a {:.2f}'.format(hi))
