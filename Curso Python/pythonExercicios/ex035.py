r1, r2, r3 = list(map(float,input('Digite o seguimento 1, 2 e 3: ').split()))
if((r1 + r2)> r3) and ((r1+r3)>r2) and ((r2+r3)>r1):
    print('As tres retas pode formar um triangulo')
else:
    print('As tres retas não pode formar um triângulo')
