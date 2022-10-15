from datetime import date
nascimento = int(input('Qual o ano de seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - nascimento
while ((nascimento < 1932 )or (nascimento > ano_atual)):
    nascimento = int(input('Qual o ano de seu nascimento? '))
if idade < 18:
    result = 18 - idade
    ano = ano_atual + result
    print('Voce ainda não tem idade para se alistar,falta {} anos para se alistar'.format(result))
    print('Seu alistamento vai ser em {}'.format(ano))
elif idade == 18:
    print('Voce ja esta na idade de se alistar')
elif idade > 18:
    result = idade - 18
    ano = ano_atual - result
    print('Voce ja passou {} anos da idade de se alistar'.format(result))
    print('seu alistamento foi em {}'.format(ano))

