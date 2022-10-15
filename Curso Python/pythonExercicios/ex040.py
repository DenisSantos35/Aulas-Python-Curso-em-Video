n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media < 5.0:
     print('Sua media foi de {}.Voce foi Reprovado. Estude mais'.format(media))
elif ((media >= 5.0) and (media <= 6.9)):
    print('Sua media foi de {}.Voce esta de Recuperação'.format(media))
else:
    print('Parabens!!!Sua media foi de {}. Voce foi aprovado'.format(media))
