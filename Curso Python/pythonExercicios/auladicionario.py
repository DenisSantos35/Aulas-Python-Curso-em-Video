'''dados = {'nome':'pedro', 'idade': 25}
n1 = [5,7,10]
print(n1.index(7))
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)

del dados['idade']
print(dados, n1)'''

'''print(filme.values())
print(filme.keys())
print(filme.items())'''

'''for k,v in filme.items():
    print(f'O {k.upper()} é {v}')'''
'''filme1 = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

filme2 = {
    'titulo':'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}
filme3 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowsky'
}
locadora = list()
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(locadora)
print(locadora[1]['titulo'])'''
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado ['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v}',end = ' - ')
    print()
