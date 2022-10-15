num = list() #cria lista vazia
cont = 0 #variavel de manipulação
while True:
    if cont == 0:  #condiçao para primeiro numero a ser adicionado
        n1 = (int(input('Digite um valor: ')))
        num.append(n1)
        print('Numero adicionado com sucesso')
        print(num)
    cont += 1 #condição para que o laço nao entre dentro deste if
    condicao = str(input('Quer continuar? [S/N]')).upper().strip() #pergunta para usuario
    if condicao == 'N': #usuario responder não sai do programa
        break
    else: #caso contrario executa os comandos abaixo
        n1 = (int(input('Digite um valor: ')))
        num.append(n1)
        print(num)
    while n1 in num[:-1]: #condição se o valor estiver em n1 do 0 ate o ultimo excluindo ele fica em loop
        num.pop() #exclui o numero repetido
        print('Valor duplicado! Não vou adicionar:')
        condicao = str(input('Quer continuar? [S/N]')).upper().strip()
        if condicao == 'N':
            break
        else:
            n1 = (int(input('Digite um valor: ' )))
            num.append(n1) #inclui novo numero e verifica se esta repetido
    print('Numero adicionado com sucesso')
print('-='*30)
print('Voce digitou os valores {}'.format(sorted(num)))






