a = float(input('Digite o seguimento da reta A: '))
b = float(input('Digite o seguimento da reta B: '))
c = float(input('Digite o seguimento da reta C: '))

if (((a+b)>c) and ((a+c)>b) and ((c+b)>a)):
    print('Os seguimentos a, b e c formam um triangulo do tipo', end = ' ')
    if ( a == b == c):
        print('Equilatero')
    elif ((a != b != c !=a)):
        print('Escaleno')
    elif ((a==b) or (a==c) or (b==c)):
        print('Isosceles')

else:
    print('Nao Forma triangulo')
