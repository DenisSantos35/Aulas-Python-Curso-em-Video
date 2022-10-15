from time import sleep
velocidade = int(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7
print('Caso ultrapasse 80 Km/h a multa é de 7,00 R$ por Km acima de 80 Km')
print('Aguarde os dados ser processados...')
sleep(4)
print('Sua velocidade é de {} Km/h'.format(velocidade))
if velocidade > 80:
    print('Voce foi multado!!! Sua multa e de {:.2f} R$'.format(float(multa)))
else:
    print('Voce está dentro da velocidade permitida!!! Dirija com cuidado')
