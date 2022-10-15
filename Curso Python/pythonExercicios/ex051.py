termo = int(input('Digite o primeiro: '))
razao = int(input('Digite a razão: '))
print('O valor da Pogreçao Aritimetica: (', end=" ")
decimo = termo + (10 ) * razao
for i in range(termo, decimo, razao):
    print('{}, '.format(i), end=" ")
print(')')

