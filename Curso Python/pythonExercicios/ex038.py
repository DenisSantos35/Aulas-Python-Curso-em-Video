num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print('O numero {} e maior que o numero {}'.format(num1, num2))
elif num1 < num2:
    print('O numero {} e menor que o numero {}'.format(num1, num2))
else:
    print('O numero {} e igual o numero {}'.format(num1, num2))
