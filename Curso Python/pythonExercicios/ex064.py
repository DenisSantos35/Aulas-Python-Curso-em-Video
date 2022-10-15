senha = cont = soma = 0
while senha != 999:
    numero = int(input('Digite um numero ou [999] Para finalizar:'))
    senha = numero
    if senha != 999:
        soma += numero
        cont += 1




print('Foram digitados {} numero(s)'.format(cont))
print('A soma dos numeros desconsiderando a senha foi igual a {}'.format(soma))

