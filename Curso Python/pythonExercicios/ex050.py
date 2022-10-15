soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º Numero: '.format(i)))
    #n = numero
    #for s in range(n, n+1):
    if numero % 2 == 0:
        soma += numero
        cont = cont + 1
print('Voce digitou {} numeros pares'.format(cont))
print('A soma dos numero pares e igual a: {}'.format(soma))
