usuario = int(input())
numeros = []
for i in range(0,usuario):
    crianca = int(input())
    numeros.append(crianca)
print(sorted(numeros))
cont = 0
for j in range(min(numeros), max(numeros)):
    if j not in numeros:
        print(j)
