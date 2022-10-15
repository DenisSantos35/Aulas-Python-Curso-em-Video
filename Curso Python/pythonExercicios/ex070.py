print('-'*30)
loja = 'LOJA SUPER BARATAO'
print('      LOJA SUPER BARATAO      ')
print('-'*30)
soma = cont = barato = flag = 0
p = ''
while True:
    prod = str(input('Nome do produto: ')).upper().strip()
    preco = float(input('Preco: R$ '))
    soma += preco
    if preco > 1000:
        cont += 1
    if flag == 0 or barato > preco:
        barato = preco
        p = prod
        flag = 1
    resposta = ' '
    while resposta not in 'NS':
        resposta = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de {soma:.2f}R$')
print(f'Temos {cont} produtos custando mais de 1000,00 R$')
print(f'O produto mais barato foi {p} que custa {barato:.2f} R$')
