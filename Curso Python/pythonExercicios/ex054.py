from datetime import date
ano = date.today().year
print('Ano atual, {}'.format(ano))
cont = 0
cont1 = 0
for i in range(1,8):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano - nasc
    print('Pessoa n {}, idade {}'.format(i, idade))
    if(idade >= 18):
        cont = cont + 1
    else:
        cont1 = cont1 + 1
print('A quantidade de pessoas com 18 ou mais anos de idade e de: {}'.format(cont))
print('A quantidade de pessoas menor de 18 anos de idade e igual a: {}'.format(cont1))
