'''def mostraLinha():
    print('-'*30)
mostraLinha()
print('ola')
mostraLinha()
def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem('CURSO EM VIDEO')
mensagem('APRENDENDO PYTHON')
mensagem('PRIMEIROS PASSOS')
a = 4
b = 5
s = a + b
print(s)
def soma(a=0, b=0):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
# programa principal
soma(b=4, a=5)
soma(8, 9)
soma(10,12)
soma(4)
def contador(*  num):
    for v in num:
        print(v, end="")
    print('fim')
    tam = len(num)
    print(f'tamanho = {tam}')
#programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
def dobra(lis):
    pos = 0
    while pos < len(lis):
        lis[pos] *= 2
        pos += 1
    print(lis)
valores = [7, 2, 5, 0, 4]
print(valores)
dobra(valores)'''
def soma(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'A soma dos valores {valores} = {soma}')


soma(5, 6)
soma(10, 8, 3, 7, 8, 11)
