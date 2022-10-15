termo = int(input('Digite o primeiro: '))
razao = int(input('Digite a razão: '))
print('O valor da Pogreçao Aritimetica: (', end=" ")
#decimo = termo + (10 ) * razao
decimo = 9
print(termo,',', end=' ')
while(decimo != 0):
    termo = termo + razao
    print('{}, '.format(termo), end=" ")
    decimo -= 1
print('FIM)')

