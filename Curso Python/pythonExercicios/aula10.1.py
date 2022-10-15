'''nome = str(input('Qual o seu nome: ')).strip().upper()
if nome == 'DENIS':
    print('Que nome lindo voce tem')
else:
    print('Seu nome é tao normal')
print('Bom dia {}'.format(nome))'''

n1 = float(input('Digite a primeira Nota: '))
n2 = float(input('Digite a segunda Nota: '))
media = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(media))
if media >= 6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')

