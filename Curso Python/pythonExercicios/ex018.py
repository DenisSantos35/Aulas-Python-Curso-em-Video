import math
angulo = float(input('Digite o angulo'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo e igual a {:.2f}, \nO seno e igual a {:.4f}'.format(angulo, seno))
print('O cosseno e igual a {:.4f}, \nA tangente e igual a {:.4f}'.format(cosseno, tangente))
