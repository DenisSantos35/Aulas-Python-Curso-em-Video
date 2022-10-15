import datetime
print('hello world!')
pais = 'Brasil'
print(type(pais))
quantidade = 5
print(type(quantidade))
print('o pais {} ganhou {} titulos'.format(pais,quantidade))
dia = 13
mes = 6
ano = 2022

print(dia,mes,ano, sep ='/')
estados = ['Rio de janeiro', 'São paulo', 'Santa Catarina','Minas gerais']
for x in estados:
    print(x)

# criar funçao
def tabuada(x):
    for cont in range(1,11):
        print('{:2} X {:2} = {:2}'.format(x, cont, x*cont))

num = int(input('Digite um numero: '))
tabuada(num)

