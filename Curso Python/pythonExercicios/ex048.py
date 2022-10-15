soma = 0
cont = 0
for i in range(1, 501, 2):
    #if(i % 2 == 1):
        if(i % 3 == 0):
            soma = soma + i
            cont = cont + 1
            print(' {}, '.format(i))
print('A quantidade de numeros impares e divisiveis por 3 e igual a: {}'.format(cont))
print('A soma dos numeros impares de 1 a 500 e divisiveis por 3 e de: {}'.format(soma))
