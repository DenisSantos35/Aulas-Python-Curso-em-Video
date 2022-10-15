from time import sleep
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
opcao = 0
while(opcao != 5):
    print('''======MENU DO OPÇAO======
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')
    opcao = int(input('Digite uma opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('{} X {} = {}'.format(n1, n2 ,mult))
    elif opcao == 3:
        if(n1 > n2):
            print('O numero {} e maior que o numero {}'.format(n1, n2))
        else:
            print('O numero {} e maior que o numero {}'.format(n2, n1))
    elif opcao == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite um valor: '))
    else:
        print('opcao invalida tente novamente')
    print('=========================')
    sleep(3)

