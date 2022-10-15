dados = dict()
lista = list()
soma = 0
while True:
    dados['nome'] = str(input('Nome: ')).upper().strip()
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if dados['sexo'] not in 'MF':
            print(f'Por favor digite apenas M ou F...')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())

    sair = ' '
    while sair not in 'SN':
        sair = str(input('Deseja continuar? ')).upper().strip()
        if sair not in 'SN':
            print(f'Digite apenas S ou N...')
    if sair == 'N':
        break
print(lista)
# ate aqui leitura de dados

#daqui para baixo analise de dados
media = soma / len(lista)
print(f'O grupo tem {len(lista)} pessoas.')
print(f'A média de idade é de {media} anos.')
print(f'As mulheres cadastradas foram: ', end=' ')
for pos, mulheres in enumerate(lista):
    if lista[pos]['sexo'] == 'F':
        print(lista[pos]['nome'], end=' ')
print()
print(f'A lista das pessoas que estão acima da média: ')
for pos,med in enumerate(lista):
    if lista[pos]['idade'] >= media:
        for dad,stat in med.items():
            print(f'{dad} = {stat}; ', end=' ')
        print()
print(f'<<ENCERRADO>>')


