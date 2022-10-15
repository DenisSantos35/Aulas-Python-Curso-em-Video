def leiaint(num):
    while True:
        num = str(input(num))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f'\033[0;031mERRO! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')


n = leiaint('Digite um numero')
print(f'Voce acabou de digitar o numero {n}')
