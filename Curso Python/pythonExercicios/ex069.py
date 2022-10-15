quant18 = homem = menor20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).upper().strip()
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if idade >= 18:
        quant18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <= 20:
        menor20 += 1
    if continuar == 'N':
        break
print('='*6,'FIM PROGRAMA','='*7)
print(f'Total de pessoa(s) com mais de 18 anos: {quant18}')
print(f'Ao todo temos {homem} homem(s) cadastrados.')
print(f'Temos {menor20} mulher(s) com menos se 20 anos.')

