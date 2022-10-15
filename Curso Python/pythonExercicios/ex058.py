from random import randint
computador = randint(0,10)
usuario = int(input('Tente vencer o computador digite um numero: '))
print('Voce jogou {} e o computador jogou {}'.format(usuario, computador))
cont = 0
while(usuario != computador):
    cont += 1
    usuario = int(input('Tente vencer o computador digite um numero: '))
    print('Voce jogou {} e o computador jogou {}\n'.format(usuario, computador))
print('Parabens!!! Voce conseguiu')
print('Voce precisou de {} tentativas para vencer o computador'.format(cont+1))

