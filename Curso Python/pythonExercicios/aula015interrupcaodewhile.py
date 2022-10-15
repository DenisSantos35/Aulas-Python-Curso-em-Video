'''n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''
nome = 'jose'
anos = 33
salario = 2850.00
print(f'O {nome} tem {anos} anos e ganha um salario de {salario:.10f}') # formatado float 10 casas
print(f'O {nome} tem {anos} anos e ganha um salario de {salario:10f}') # espacado 10 Casas
print(f'O {nome} tem {anos} anos e ganha um salario de {salario:-^10}') # centralizado
print(f'O {nome} tem {anos} anos e ganha um salario de {salario:->10} R$') # alinhado a direita 10 casas
print(f'O {nome} tem {anos} anos e ganha um salario de {salario:-<10} R$') # alinhado a esquerda 10 casas
print(f'O {nome} tem {anos} anos e ganha um salario de {salario:10} R$') # alinhado a esquerda 10 casas



