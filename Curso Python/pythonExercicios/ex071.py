from time import sleep
nome = 'Denis Diogo dos Santos'
senha = 123456
loguin = int(input('Digite a senha para ter acesso ao caixa eletronico'))
if loguin != senha:
    cont = 1
    while loguin != senha:
        senha = 123456
        if cont == 3:
            print('CARTAO BLOQUEADO!!! PROCURE SUA AGENCIA PARA DESBLOQUEAR!!!')
            break
        print('Senha incorreta!\n{}ª TENTATIVA\nApós a terceira tentativa o cartao sera BLOQUEADO'.format(cont + 1))
        loguin = int(input('Digite a senha para ter acesso ao caixa eletronico'))
        cont += 1

        if loguin == senha:
            print('Acessando a conta')
            sleep(3)
if loguin == senha:
    print('Seja bem vindo {}'.format(nome))
    sleep(3)
    if loguin == senha:
        banco = 'BANCO SEM DINHEIRO'
        print('='*30)
        print('      ',banco,'      ')
        print('='*30)

        while True:
            valor = float(input('Qual valor quer sacar? R$ '))
            print('Aguarde contando Cédulas')
            sleep(4)
            cin = (valor // 50)
            vin = (valor % 50) // 20
            res = (valor % 50)-vin * 20
            dez = (res // 10)
            um = (valor % 10)
            if cin > 0:
                print('Total de {} cédulas de R$ 50,00'.format(int(cin)))
            if vin > 0:
                print('Total de {} cédulas de R$ 20,00'.format(int(vin)))
            if dez > 0:
                print('Total de {} cédulas de R$ 10,00'.format(int(dez)))
            if um > 0:
                print('Total de {} cédula de R$ 1,00'.format(int(um)))
            print('='*30)
            print('Volte sempre ao banco {}! Tenha um bom dia!'.format(banco))
            break







