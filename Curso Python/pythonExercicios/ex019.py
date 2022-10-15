from random import choice
nomea = str(input('Digite o primeiro nome: '))
nomeb = str(input('Digite o segundo nome: '))
nomec = str(input('Digite o terceiro nome: '))
nomed = str(input('Digite o quarto nome: '))
lista = [nomea, nomeb, nomec, nomed]
print(lista)
print(type(lista))
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
