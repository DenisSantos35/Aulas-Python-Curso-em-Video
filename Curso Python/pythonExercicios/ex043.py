from math import pow
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (pow(altura, 2))
print('Seu imc e {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc < 25:
    print('Você esta no peso ideal')
elif imc < 30:
    print('Você esta no Sobrepeso')
elif imc < 40:
    print('Você esta na obesidade')
else:
    print('Voce esta na obesidade morbida')
