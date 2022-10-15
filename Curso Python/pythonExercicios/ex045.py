import random
escolha = str(input('ESCOLHA: PEDRA, PAPEL OU TESOURA E TENTE GANHAR DO COMPUTADOR')).upper().strip()
lista = ['PEDRA','PAPEL','TESOURA']
computador = random.choice(lista)
print('Voce escolheu {} e o computador escolheu {}'.format(escolha, computador))

if(escolha == computador):
    print('Empate!!! Jogue novamente.')
elif((escolha == 'PEDRA') and (computador == 'TESOURA')):
    print('Parabens!!! Você ganhou')
elif((escolha == 'TESOURA') and (computador == 'PAPEL')):
    print('Parabens!!! Você ganhou')
elif((escolha == 'PAPEL') and (computador == 'PEDRA')):
    print('Parabens!!! Você ganhou')
else:
    print('Você Perdeu!!! tente novamente.')
