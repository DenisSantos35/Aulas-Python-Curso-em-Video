viagem = float(input('Digite a Distancia da Viagem: '))

if viagem < 200:
    viagem = viagem * 0.50
else:
    viagem = viagem * 0.45
print('O valor da sua viagem é de {:.2f} R$'.format(viagem))
