termo = int(input('Digite o primeiro: '))
razao = int(input('Digite a razão: '))
print('O valor da Pogreçao Aritimetica: (', end=" ")
#decimo = termo + (10 ) * razao
decimo = 9
print(termo,',', end=' ')
cont = 1
while(decimo != 0):
    termo = termo + razao
    print('{}, '.format(termo), end=" ")
    decimo -= 1
    if decimo == 0:
        decimo = int(input('\nQuantos termos quer mostrar?'))
    cont = cont + 1
print('Progreçao aritimetica finalizada com {} termos mostrados'.format(cont))
