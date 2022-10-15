from datetime import date
ano = date.today().year
print(ano)
dados = dict()
while True:
    dados['nome'] = str(input('Nome: ')).strip()
    nasci = int(input('Ano de nascimento: '))
    dados['idade'] = ano - nasci
    dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if dados['ctps'] == 0:
        break
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: R$ '))
    dados['aposentadoria'] = (dados['contratacao'] - nasci) + 35
    print('-='*30)
    print(dados)
    break
for da, inf in dados.items():
    print(f'{da} tem o valor {inf}')
