from random import randint
soma = cont = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-'*15)
    usuario = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    print('-'*30)
    computador = randint(0,10)
    soma = usuario + computador
    cont += 1
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'ÍMPAR'
    print('-'*30)
    print(f'Voce jogou {usuario} e o computador {computador}. Total de {soma} DEU {result}')
    print('-'*30)
    if escolha == 'P' and result == 'PAR':
        print('Voce VENCEU!\nVamos jogar novamente...')
    elif escolha == 'I' and result == 'ÍMPAR':
        print('Voce VENCEU!\nVamos jogar novamente...')
    elif escolha == 'P' and result == 'ÍMPAR':
        print('Você PERDEU!')
        print('=-'*15)
        break
    elif escolha == 'I' and result == 'PAR':
        print('Você PERDEU!')
        print('=-'*15)
        break
print(f'GAME OVER! Você venceu {cont} Vezes')






