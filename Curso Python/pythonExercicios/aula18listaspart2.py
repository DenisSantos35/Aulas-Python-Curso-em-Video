'''dados = list()
dados.append('pedro')
dados.append(25)
print(dados)
print(len(dados))
pessoas = list()
pessoas.append(dados[:])
dados[0]= 'maria'
dados[1]= 'joao'
pessoas.append(dados[:])

print(pessoas)
print(len(pessoas))
galera = [['Joao',19], ['Maria', 23], ['joaquim',35], ['ana',63]]
print(galera)
for i in range(0,3):
    for j in range(0,2):
        print(galera[i][j], end=' ')
    print('\n')
galera = [['Joao',19], ['Maria', 23], ['joaquim',35], ['ana',63]]
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')'''
galera = list()
dado = list()
totmai = totmen = 0

for i in range(0,3):
    dado.append(str(input('Digite um nome: ')))
    dado.append(int(input('digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{i[0]} é menor de idade')
        totmen += 1
print(f'Ao todo sao {totmai} maiores de idade e {totmen} menores de idade')



