n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Esta em letra MAIUSCULA? {}'.format(n.isupper()))
print('É um Alfanuerico? {}'.format(n.isalnum()))
print('É alfabético? {} '.format(n.isalpha()))
print('Esta em letra minuscula {}'.format(n.islower()))
print('É um numero? {}'.format(n.isnumeric()))
print('Só tem espaços? {}'.format(n.isspace()))
print('Esta capitalizada? {}'.format(n.istitle()))
