saida = str('s').upper().strip()
cont = soma = media = maior = menor = 0
while saida == 'S':
    numero = int(input('Digite o {}º numero: '.format(cont+1)))
    soma = soma + numero
    cont += 1
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if maior < numero:
            maior = numero
        if menor > numero:
            menor = numero
    saida = str(input('Voce quer continuar digitando? [s/n]')).upper().strip()
media = soma / cont
print('Voce digitou {} numeros'.format(cont))
print('A soma dos numeros foi {}'.format(soma))
print('A media dos {} valores digitados foi de {}'.format(cont, media))
print('O numero {} foi o menor valor'.format(menor))
print('O numero {} foi o maior valor'.format(maior))

