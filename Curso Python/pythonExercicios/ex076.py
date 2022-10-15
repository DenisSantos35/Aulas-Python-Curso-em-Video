lista = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
         'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
         'livro', 34.90)
print(lista)
print('-'*30)
print('{:^30}'.format('Listagem de Preço'))
print('-'*30)
for pos in range(0,len(lista),2):
    print(f'{lista[pos]:.<26}R$ {lista[pos + 1]:6.2f}')
    #   pos = pos + 2


