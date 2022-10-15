from time import sleep
def txt(msg):
    print('-='*20)
    print(msg)


def contador(inicio, fim, passo):
    if inicio < fim:
        for valor in range(inicio, fim, passo):
            print(f'{valor} ', end="")
            sleep(0.5)
        print('FIM!')

    elif fim < inicio:
        for valor in range(inicio, fim, passo):
            print(f'{valor} ', end="")
            sleep(0.5)
        print('FIM!')



txt(f'  Contagem de 1 até 10 de 1 em 1')
contador(inicio=1,fim=11,passo=1)
txt(f'  Contagem de 10 até 0 de 2 em 2 ')
contador(inicio=10, fim=-1, passo=-2)
txt('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
txt(f'   Contagem de {ini} até {fim} de {abs(pas)} em {abs(pas)}')
if pas == 0:
    pas += 1
if ini > fim:
    fim -= 1
    if pas > 0:
        pas = pas * (-1)
if ini < fim:
    fim += 1
    if pas < 0:
        pas = pas * (-1)
contador(inicio = ini, fim = fim , passo = pas)



