lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    msg = ' '
    while msg not in 'SsNn':
        msg = str(input('Quer continuar? [S/N]')).strip().upper()
    if msg == 'N':
        break
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print('Os valores em ordem decrescente sao{}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encotrado na lista!')

