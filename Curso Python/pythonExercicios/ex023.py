numero = int(input('Digite um numero de 0 a 9999: '))
u = (numero // 1) % 10
d = (numero // 10) % 10
c = (numero // 100) % 10
m = (numero // 1000) % 10
print('unidade: {:.0f}'.format(u))
print('Dezena: {:.0f}'.format(d))
print('Centena: {:.0f}'.format(c))
print('Milhar: {:.0f}'.format(m))




