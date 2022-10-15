
numero = int(input('Digite um numero:'))
print('-=-'*6)
escolha = int(input('[1] Binario\n[2] octal\n[3] hexadecimal:\n'))
print('-=-'*6)
while((escolha <= 0) or (escolha > 3)):
    print('-=-'*6)
    escolha = int(input('[1] Binario\n[2] octal\n[3] hexadecimal:\n'))
    print('-=-'*6)

if(escolha == 1):
    binario = format(numero, "b")
    print('Numero {}, Conversao para binario = {}'.format(numero,binario))
elif(escolha == 2):
    octal = format(numero, "o")
    print('Numero {}, Conversao para Octal = {}'.format(numero,octal))
elif(escolha == 3):
    hexa = format(numero,"x")
    print('Numero {}, Conversao para HexaDecimal = {}'.format(numero,hexa.upper()))






