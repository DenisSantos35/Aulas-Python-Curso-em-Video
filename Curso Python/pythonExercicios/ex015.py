km = float(input('Qual a quantidade de Km percorrido? '))
dias = int(input('Qual a quantidade de Dias alugados? '))
custo = (60*dias)+(0.15*km)
print('O total a pagar pelo aluguel do carro é de {:.2f} R$'.format(custo))
