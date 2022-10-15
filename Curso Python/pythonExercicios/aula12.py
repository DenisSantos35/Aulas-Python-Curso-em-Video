nome = str(input('Qual e o seu nome: ')).strip().upper()
if nome == 'DENIS':
    print('Que nome bonito!!!')
elif nome == 'MARIA' or nome == 'PEDRO' or nome == 'JOAO':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ANA CLAUDIA JESSICA JULIA':

        print('Que belo nome feminino')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia, {}!!!'.format(nome))
