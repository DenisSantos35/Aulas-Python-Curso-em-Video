#fatiamento de frase
frase = 'Curso em Video Python'

print(frase)
print(frase[0])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(frase[2::2])
#analise de string
quantidade = len(frase)
print(quantidade)
contarletra = frase.count('o')
print(contarletra)
contfateado = frase.count('o',0,14)
print(contfateado)
quantasvezes = frase.find('deo')
print(quantasvezes)
quantasvezes = frase.find('android')
print(quantasvezes)
existe = 'Curso'in frase
print(existe)
print(frase.find('y'))
mudar = frase.replace('Python','Android')
print(mudar)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase = '   Aprenda Python  '
print(frase)
print(len(frase))
frase2 = len(frase.rstrip())
print(frase2)
print(frase.strip())
print(len(frase.strip()))

frase3 = 'Curso em Video Python'
print(frase3)
print(frase3.split())
print(len(frase3.split()))
print('/'.join(frase3.split()))
print('-'.join(frase3.split()))

