from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = date.today().year
idade = ano - nascimento
print('sua idade e {} ano(s)'.format(ano - nascimento))
print('De acordo com a idade do atleta a sua categoria é: ')
if (idade <= 9):
    print('MIRIM')
elif (idade <= 14):
    print('INFANTIL')
elif (idade <= 19):
    print('JUNIOR')
elif (idade <= 25):
    print('SENIOR')
else:
    print('MASTER')

