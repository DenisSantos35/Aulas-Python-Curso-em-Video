contagem = ('zero', 'um', 'dois', 'trez', 'quatro','cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze','doze', 'treze', 'quatorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove',
            'vinte')
print(contagem)

while True:
    numero = int(input('Digite um numero entre [0] e [20]: '))
    while numero < 0 or numero > 20:
        numero = int(input('Tente novamente. Digite um numero entre [0] e [20]: '))
    print(f'Voce digitou o numero {contagem[numero]}')
    sair = str(input('Voce quer continuar?[S/N]')).upper().strip()
    if sair == 'N':
        break


