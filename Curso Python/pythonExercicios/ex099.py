from time import sleep
def maior(* num):
    print('-='* 30)
    print('Analisando valores passados...')
    maior = cont = 0
    for valor in num:
        if cont == 0:
            maior = valor
        else:
            if maior < valor:
                maior = valor
        cont += 1
        print(f'{valor} ', end="")
        sleep(0.2)

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
