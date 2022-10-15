import random
from time import sleep
n1 = random.randint(0,5)
n2 = int(input('Adivinhe o numero escolhido pelo computador: '))
print('Processando...')
sleep(3)
print('O numero que o computador escolheu foi {} e o numero que voce escolheu foi {}'.format(n1,n2))
if n1 == n2:
    print('Parabens, Voce acertou o numero')
else:
    print('Nao foi desta vez, Tente novamente: ')
print('-----------------end-------------------')

