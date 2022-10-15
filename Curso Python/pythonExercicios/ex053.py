frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('{}'.format(junto))
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada nao e um palindromo!')





