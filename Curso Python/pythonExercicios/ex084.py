dados = list()
analise = list()
tot = menor = cont = 0
result = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    analise.append(dados[:])
    dados.clear()
    msg = str(input('Quer continuar? [S/N]')).upper().strip()
    #tot += 1
    if msg in 'N':
        break
print(f'Ao todo, você cadastrou {len(analise)} pessoas')
maior = 0
nome = list()
for peso in analise:
    if peso[1] >= maior:
        maior = peso[1]
print(f'O maior peso foi de {maior}Kg.Peso de ', end='')
for nome in analise:
    if nome[1] == maior:
        print(f'[{nome[0]}]', end=' ')
menor = analise[0][1]
for peso in analise:
    if peso[1] < menor:
        menor = peso[1]
print(f'\nO menor peso é {menor}. E a pessoa(s) e(são): ', end='')
for nome in analise:
    if nome[1] == menor:
        print(f'{nome[0]} ', end='')







