def leiaopcao(msg):
    cores = {'amarelo': '\033[0;33m',
             'azul': '\033[0;34m',
             'vermelho': '\033[0;31m',
             'verde': '\033[0;32m',
             'fechar': '\033[m'
             }
    while True:
        print('-'*30)
        print(f'{msg:>4}'.center(30))
        print('-'*30)
        print(f'{cores["amarelo"]}1{cores["fechar"]} - {cores["azul"]}Ver pessoas cadastradas{cores["fechar"]}\n'
              f'{cores["amarelo"]}2{cores["fechar"]} - {cores["azul"]}Cadastrar nova pessoa{cores["fechar"]}\n'
              f'{cores["amarelo"]}3{cores["fechar"]} - {cores["azul"]}Sair{cores["fechar"]}')
        print('-'*30)
        try:
            opc = int(input(f'{cores["amarelo"]}{msg}{cores["fechar"]}'))
            if opc < 0 or opc > 3:
                print(f'{cores["vermelho"]}Erro: Digite uma opção válida.{cores["fechar"]}')
                continue
        except ValueError:
            print(f'{cores["vermelho"]}Erro: Por favor, digite um numero inteiro válido.{cores["fechar"]}')
            continue
        else:

            if opc == 1:
                print('-'*30)
                print('OPCAO 1'.center(30))
                print('-'*30)
                continue
            elif opc == 2:
                print('-'*30)
                print('OPCAO 2'.center(30))
                print('-'*30)
            else:
                print('Saindo do sistema... Até logo!')
                break



