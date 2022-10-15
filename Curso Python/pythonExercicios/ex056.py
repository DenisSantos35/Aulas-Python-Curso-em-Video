media = 0
cont = 0
soma = 0
linha = ''
maior = 0
cont1 = 0
id = 0
for i in range(1, 5):
    nome = str(input('Digite o {}º nome: '.format(i))).upper().strip()
    idade = float(input('Digite a {}ª idade'.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa[m] ou [f]'.format(i))).upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite o sexo da {}ª pessoa[m] ou [f]'.format(i))).upper().strip()
    cont = cont + 1
    soma += idade
    if(sexo == 'M'):
        if(maior < idade):
            maior = idade
            linha = nome

    if(sexo == 'F'):
        if(idade<20):
            cont1 = cont1 + 1
media = soma / cont

print('A media de idade do grupo e igual a: {}'.format(media))
print('O nome da do homem mais velho e {} e tem {} anos'.format(linha, maior))
print('A quantidade de mulheres menor que 20 anos e igual a : {}'.format(cont1))
