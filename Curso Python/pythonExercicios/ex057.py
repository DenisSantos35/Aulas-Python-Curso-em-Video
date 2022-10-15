sexo = str(input('Digite o sexo [F/M]')).strip().upper()

while(sexo != 'F' and sexo != 'M'):
    sexo = str(input('Digite o sexo [F/M]')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
