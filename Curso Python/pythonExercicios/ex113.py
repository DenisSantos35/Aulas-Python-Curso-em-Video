def leiaint(num):
    while True:
        try:
            numero = int(input(num))
        except (ValueError, TypeError):
            print(f'\033[0;031mERRO! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
            continue
        else:
            return numero
def leiareal(num):
    while True:
        try:
            valor = float(input(num))
        except:
            print(f'\033[0;031mERRO! DIGITE UM NUMERO REAL VALIDO.\033[m')
            continue
        else:
            return valor


inteiro = leiaint('Digite um numero')
real = leiareal('Digite um Real')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real} ')
