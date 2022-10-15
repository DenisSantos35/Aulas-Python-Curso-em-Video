salario = float(input('Qual o valor do seu salario: '))

if (salario > 1250.00):
    aumento = 0.10
else:
    aumento = 0.15
aumento = ( salario * aumento)
print('O valor do seu amento é de {:.2f}R$'.format(aumento))
print('Seu novo salario e de {:.2f} R$'.format(salario + aumento))

