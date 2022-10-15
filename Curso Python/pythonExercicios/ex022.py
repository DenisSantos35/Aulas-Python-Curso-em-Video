nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é ', nome.upper())
print('Seu nome em minúsculas é ', nome.lower())
print('Seu nome tem ao todo {} Letras'.format(len(nome)-nome.count(' ')))
quant = nome.split()
print('Seu primeiro nome é', quant[0], ' e ele tem ', len(quant[0]),'Letras')



