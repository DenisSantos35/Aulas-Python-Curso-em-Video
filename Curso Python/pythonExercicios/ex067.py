from time import sleep
'''cont = 0
val = int(input('Quer ver a tabuada de qual valor? '))
print('-'*30)
while True:
    cont += 1
    print(f'{val} X {cont} = {val * cont}')
    if cont == 10:
        print('-'*30)
        sleep(2)
        val = int(input('Quer ver a tabuada de qual valor? '))
        print('-'*30)
        cont = 0
    if val < 0:
        break
print('PROGRAMA TABOADA ENCERRADO. Volte sempre!')'''
while True:
    val = int(input('Quer ver a tabuada de qual valor? '))
    if val < 0:
        break
    print('-'*30)
    for c in range(1,10):
        print(f'{val} X {c} = {val * c}')
    print('-'*30)
print('PROGRAMA TABOADA ENCERRADO. Volte sempre!')
